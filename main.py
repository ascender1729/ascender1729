import os
import logging
from dotenv import load_dotenv
from src import GitHubStats, ReadmeUpdater, GitHubStatsError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    load_dotenv()

    token = os.getenv('GITHUB_TOKEN')
    username = 'ascender1729'
    readme_path = 'README.md'

    if not token:
        logger.error("GITHUB_TOKEN not found in environment variables")
        return

    try:
        github_stats = GitHubStats(token, username)
        stats = github_stats.get_stats()
        logger.info("Successfully fetched GitHub stats")

        updater = ReadmeUpdater(readme_path)
        updater.update(stats)
        logger.info("Successfully updated README")

    except GitHubStatsError as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()