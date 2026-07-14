class GitHubConfig:
    OWNER = "Satyam4755"
    REPO = "AMFI_Fetcher"
    BRANCH = "main"
    BASE_PATH = "data/sif"

    @classmethod
    def get_base_raw_url(cls) -> str:
        """
        Dynamically constructs the base Raw GitHub URL.
        """
        return f"https://raw.githubusercontent.com/{cls.OWNER}/{cls.REPO}/{cls.BRANCH}/{cls.BASE_PATH}"

    @classmethod
    def get_api_contents_url(cls, path: str) -> str:
        """
        Dynamically constructs the GitHub API URL for a repository path.
        """
        clean_path = path.lstrip('/')
        full_path = f"{cls.BASE_PATH}/{clean_path}" if cls.BASE_PATH else clean_path
        full_path = full_path.strip('/')
        return f"https://api.github.com/repos/{cls.OWNER}/{cls.REPO}/contents/{full_path}?ref={cls.BRANCH}"
