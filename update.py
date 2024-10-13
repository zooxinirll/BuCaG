#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys
import time

GIT_REPO = "https://github.com/zooxinirll/BuCaG.git"

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"


def clear_directory():
    for item in os.listdir("."):
        item_path = os.path.join(".", item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
    
    # Remove the .git folder if it exists
    if os.path.exists(".git"):
        shutil.rmtree(".git")


def clone_repository():
    try:
        subprocess.run(["git", "clone", GIT_REPO, "."], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{RED}Error during git clone: {e}{RESET}")
        sys.exit(1)


def show_spinner(message, duration=5):
    spinner = ['⠋', '⠙', '⠸', '⠴', '⠦', '⠇']
    sys.stdout.write(f"{CYAN}{message}{RESET}")
    sys.stdout.flush()
    for i in range(duration * 10):
        time.sleep(0.1)
        sys.stdout.write(f"\r{CYAN}{spinner[i % len(spinner)]} {message}{RESET}")
        sys.stdout.flush()
    sys.stdout.write("\r")


def main():
    user_input = input(f"Type {CYAN}Update/update{RESET} to update: ").strip().lower()

    print()

    if user_input not in ["update", "Update"]:
        print(f"{RED}Invalid input. Exiting.{RESET}")
        return

    show_spinner("Updating ....", duration=3)

    clear_directory()

    try:
        clone_repository()
        print(f"\n{GREEN}BuCaG Updated ✓{RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{RED}Error during update: {e}{RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()
