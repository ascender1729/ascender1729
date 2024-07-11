from .exceptions import ReadmeUpdateError

class ReadmeUpdater:
    def __init__(self, readme_path: str):
        self.readme_path = readme_path

    def update(self, stats: dict) -> None:
        try:
            with open(self.readme_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            stats_text = f"""<!-- GITHUB_STATS_START -->
Joined GitHub {stats['ACCOUNT_AGE']} years ago. Since then, I've pushed {stats['COMMITS']} commits, opened {stats['ISSUES']} issues, submitted {stats['PULL_REQUESTS']} pull requests, and received {stats['STARS']} stars across {stats['REPOSITORIES']} personal projects. Contributed to {stats['REPOSITORIES_CONTRIBUTED_TO']} public repositories.
<!-- GITHUB_STATS_END -->"""
            
            if '<!-- GITHUB_STATS -->' in content:
                # Handle old placeholder format
                updated_content = content.replace('<!-- GITHUB_STATS -->', stats_text)
            elif '<!-- GITHUB_STATS_START -->' in content and '<!-- GITHUB_STATS_END -->' in content:
                # Handle new placeholder format
                start = content.index('<!-- GITHUB_STATS_START -->')
                end = content.index('<!-- GITHUB_STATS_END -->') + len('<!-- GITHUB_STATS_END -->')
                updated_content = content[:start] + stats_text + content[end:]
            else:
                # If neither placeholder exists, append stats to the end
                updated_content = content + '\n\n' + stats_text
            
            with open(self.readme_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
        except IOError as e:
            raise ReadmeUpdateError(f"Error updating README: {str(e)}") from e
