import json
import logging
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from typing import Any, Dict, List, Optional, Union

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
    A reusable GitHub client to fetch directories and JSON data.
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

    def list_directory(self, relative_path: str) -> List[str]:
        """
        Returns a list of filenames inside a GitHub directory using the Contents API.
        """
        api_url = GitHubConfig.get_api_contents_url(relative_path)
        try:
            logger.info(f"Listing directory from: {api_url}")
            headers = {"Accept": "application/vnd.github.v3+json"}
            response = self.session.get(api_url, headers=headers, timeout=10)
            
            if response.status_code == 404:
                logger.error(f"Directory not found (404) at: {api_url}")
                return []
            
            if response.status_code == 403:
                logger.error(f"GitHub API Rate Limit exceeded: {response.text}")
                return []
                
            response.raise_for_status()
            contents = response.json()
            
            if isinstance(contents, list):
                # Return only file names
                return [item['name'] for item in contents if item['type'] == 'file']
            else:
                logger.error(f"Path is not a directory: {api_url}")
                return []
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Network failure while listing {api_url}: {str(e)}")
            return []

    def build_raw_url(self, relative_path: str) -> str:
        """
        Constructs the full raw GitHub URL for a given relative path.
        """
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
