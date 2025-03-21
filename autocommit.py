import os
import subprocess
import google.generativeai as genai
import click
from git import Repo
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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
    """Uses Google Gemini API to generate a commit message."""
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(
            f"Write a clear and concise Git commit message for the following changes:\n{diff_text}"
        )
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini API Error: {e}")
        exit(1)

def commit_changes():
    """Commits staged changes with a Gemini-generated commit message."""
    diff_text = get_git_diff()
    commit_message = generate_commit_message(diff_text)
    
    repo = Repo(".")
    repo.git.commit('-m', commit_message)
    print(f"✅ Committed Successfully: {commit_message}")

@click.command()
@click.option('--analyze', is_flag=True, help="Analyze Git changes and suggest a commit message")
@click.option('--commit', is_flag=True, help="Commit with AI-generated message")
def cli(analyze, commit):
    """CLI tool for AI-powered Git commit messages using Google Gemini."""
    if analyze:
        diff_text = get_git_diff()
        commit_message = generate_commit_message(diff_text)
        print(f"💡 Suggested Commit Message:\n\n{commit_message}")
    
    if commit:
        commit_changes()

if __name__ == '__main__':
    cli()
