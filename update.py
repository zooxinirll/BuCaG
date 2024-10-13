import os
import subprocess
import shutil
from rich.console import Console

console = Console()

# GitHub repository URL
GITHUB_REPO = "https://github.com/zooxinirll/BuCaG.git"
BUCAG_DIR = "BuCaG"

def run_Update():
    try:
        # Check if the BuCaG directory exists and remove it before updating
        if os.path.exists(BUCAG_DIR):
            console.print(f"[bold yellow]Removing existing '{BUCAG_DIR}' directory...[/bold yellow]")
            shutil.rmtree(BUCAG_DIR)

        # Clone the public GitHub repository
        console.print("[bold yellow]Updating tool from GitHub repository...[/bold yellow]")
        subprocess.run(["git", "clone", GITHUB_REPO], check=True)

        console.print("[bold green]Tool successfully updated![/bold green]")

    except subprocess.CalledProcessError as e:
        # If there's an error (e.g., the repo is private), print the error and remove the BuCaG directory
        console.print(f"[bold red]Error during update: {e}[/bold red]")
        
        if os.path.exists(BUCAG_DIR):
            console.print("[bold yellow]Removing BuCaG directory as the repo is private or inaccessible.[/bold yellow]")
            shutil.rmtree(BUCAG_DIR)

if __name__ == "__main__":
    run_Update()
