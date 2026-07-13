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
