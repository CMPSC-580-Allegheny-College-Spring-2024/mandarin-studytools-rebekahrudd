"""Run the picture evaluation."""

import typer
from rich.console import Console
from a_readin import functions

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()

# Add comments to explain the steps in the main function
@cli.command()
def main(image_name: str):
    """Edit a picture"""
