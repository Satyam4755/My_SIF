import csv
import json
import logging
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from typing import Any, Dict, List, Optional, Union
from io import StringIO

from sif_app.my_sif.config.github_config import GitHubConfig

# Configure standard logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


class GitHubService:
    """
    A reusable GitHub client to fetch raw JSON and CSV data.
    """
    
    def __init__(self):
        self.session = self._create_retry_session()
        self.base_url = GitHubConfig.get_base_raw_url()

    def _create_retry_session(self, retries: int = 3, backoff_factor: float = 0.5) -> requests.Session:
        """
        Creates a requests Session with built-in retry logic.
        """
        session = requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=(500, 502, 503, 504)
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def build_raw_url(self, relative_path: str) -> str:
        """
        Constructs the full raw GitHub URL for a given relative path.
        """
        # Ensure there are no double slashes if relative_path starts with '/'
        clean_path = relative_path.lstrip('/')
        return f"{self.base_url}/{clean_path}"

    def _fetch_content(self, url: str) -> Optional[str]:
        """
        Fetches text content from the given URL with timeout and error handling.
        """
        try:
            logger.info(f"Fetching data from: {url}")
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 404:
                logger.error(f"File not found (404) at: {url}")
                return None
                
            response.raise_for_status()
            return response.text
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Network failure while fetching {url}: {str(e)}")
            return None

    def get_json(self, relative_path: str) -> Optional[Union[Dict[str, Any], List[Any]]]:
        """
        Downloads and parses a JSON file from GitHub.
        """
        url = self.build_raw_url(relative_path)
        content = self._fetch_content(url)
        
        if not content:
            return None
            
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON received from {url}: {str(e)}")
            return None

    def get_csv(self, relative_path: str) -> Optional[List[Dict[str, str]]]:
        """
        Downloads and parses a CSV file from GitHub into a list of dictionaries.
        """
        url = self.build_raw_url(relative_path)
        content = self._fetch_content(url)
        
        if not content:
            return None
            
        try:
            # Parse CSV content using DictReader
            f = StringIO(content)
            reader = csv.DictReader(f)
            return list(reader)
        except Exception as e:
            logger.error(f"Failed to parse CSV from {url}: {str(e)}")
            return None
