import os
import google.generativeai as genai
import click
from git import Repo
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# This comment is for testing auto-commit CLI
# Get the API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("❌ Error: GEMINI_API_KEY is not set. Please add it to your .env file.")
    exit(1)

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def get_git_diff():
    """Fetches staged Git changes."""
    repo = Repo(".")
    diff = repo.git.diff('--staged')
    if not diff:
        print("❌ No staged changes found. Use `git add .` to stage files.")
        exit(1)
    return diff

def generate_commit_message(diff_text):
    """Uses Google Gemini API to generate a commit message automatically."""
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")

        # Limit input size to 1000 characters
        diff_text = diff_text[:1000]

        response = model.generate_content(
            f"Write a clear and concise Git commit message for the following changes and no extra text:\n{diff_text}"
        )
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini API Error: {e}")
        exit(1)

def commit_changes():
    """Commits staged changes with an AI-generated commit message."""
    diff_text = get_git_diff()
    commit_message = generate_commit_message(diff_text)
    
    repo = Repo(".")
    repo.git.commit('-m', commit_message)
    print(f"✅ Changes committed: {commit_message}")
    try:
        print("🚀 Pushing changes to remote repository...")
        origin = repo.remotes.origin
        origin.push()
        print("✅ Changes pushed successfully!")
    except Exception as e:
        print(f"❌ Error pushing to remote: {e}")
        exit(1)

    return commit_message
    

@click.command()
@click.option('--analyze', is_flag=True, help="Analyze Git changes and suggest a commit message")
@click.option('--commit', is_flag=True, help="Commits and pushs with AI-generated message")
# @click.option('--push', is_flag=True, help="Push committed changes to remote")
def cli(analyze, commit):
    """CLI tool for AI-powered Git commit messages using Google Gemini."""
    if analyze:
        diff_text = get_git_diff()
        commit_message = generate_commit_message(diff_text)
        print(f"\n💡 Suggested Commit Message:\n\n{commit_message}\n")

    if commit:
        commit_message = commit_changes()

if __name__ == '__main__':
    cli()
