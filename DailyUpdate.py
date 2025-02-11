import os
import datetime
import subprocess

github_repo = "https://github.com/bdicicco88/DailyUpdatePy.git"
file_to_modify = "data.txt"
commit_message = "Automated daily update"

def modify_file():
    with open(file_to_modify, "a") as file:
        file.write(f"Updated on {datetime.datetime.now()}\n")

def git_commit_and_push():
    try:
        subprocess.run(["git", "add", file_to_modify], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Changes pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Git operation failed: {e}")

if __name__ == "__main__":
    modify_file()
    git_commit_and_push()