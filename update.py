import os
import subprocess
import shutil
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

# GitHub repository URL
GITHUB_REPO = "https://github.com/zooxinirll/BuCaG.git"
CURRENT_DIR = os.getcwd()  # Get the current working directory

def clean_directory(directory):
    """Remove all files and subdirectories in the given directory."""
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.unlink(item_path)  # Remove file or link
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)  # Remove directory

def run_update():
    try:
        # Display spinner animation and progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold yellow]{task.description}"),
            transient=True
        ) as progress:

            # Step 1: Clean up the current directory
            clean_task = progress.add_task("Cleaning up current directory...", total=None)
            clean_directory(CURRENT_DIR)
            progress.update(clean_task, description="[bold green]Directory cleaned![/bold green]")
            
            # Step 2: Clone the updated repository into the current directory
            update_task = progress.add_task("Cloning updated repository...", total=None)
            subprocess.run(["git", "clone", GITHUB_REPO, "."], check=True)
            progress.update(update_task, description="[bold green]Repository cloned successfully![/bold green]")
            
            console.print("[bold green]Update completed successfully![/bold green]")

    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Error during update: {e}[/bold red]")
    
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")

if __name__ == "__main__":
    run_update()
