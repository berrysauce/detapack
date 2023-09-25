import os
import json
import typer
from rich.progress import Progress, SpinnerColumn, TextColumn, track
from deta import Deta


# app configuration
app = typer.Typer(help="detapack: Import/Export data from/to Deta Bases")
APP_NAME = "detapack"
APP_VERSION = "0.1.3"


@app.command(name="version")
def version_command():
    """
    Displays detapack's version
    """

    typer.secho(f"""
    ╭――――――――――――――――――╮
    │     {APP_NAME}     │
    │      v{APP_VERSION}      │
    ╰――――――――――――――――――╯
    """,
    fg=typer.colors.BRIGHT_MAGENTA)

    typer.secho("""    more info:
    github.com/berrysauce/detapack\n""",
    fg=typer.colors.BRIGHT_BLACK)


@app.command(name="export")
def export_command(
    basename: str,
):
    """
    Export Deta Base to a local .json file
    """
    
    key = typer.prompt("Enter your project key", hide_input=True, type=str)
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True
    ) as progress:
        progress.add_task("Connecting to Deta...")
    
        try:
            deta = Deta(key)
            base = deta.Base(basename)
        except AssertionError:
            typer.secho("ERROR! Bad project key provided", fg=typer.colors.BRIGHT_RED)
            return
        
        progress.add_task("Receiving data...")

        res = base.fetch().items
        
        progress.add_task("Writing data...")
        
        target = "export.json"
        destination = str(os.getcwd()) + "/" + target

        with open(destination, "w") as f:
            f.write(json.dumps(res, indent=4))

    typer.secho(f"DONE! Saved as {target} in {str(os.getcwd())}", fg=typer.colors.BRIGHT_GREEN)


@app.command(name="import")
def import_command(
    basename: str,
    path: str
):
    """
    Import local .json file to Deta Base
    """
    
    key = typer.prompt("Enter your project key", hide_input=True, type=str)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True
    ) as progress:
        progress.add_task("Connecting to Deta...")
        
        try:
            deta = Deta(key)
            base = deta.Base(basename)
        except AssertionError:
            typer.secho("ERROR! Bad project key provided", fg=typer.colors.BRIGHT_RED)
            return

        progress.add_task(f"Reading data from {path}...")
        
        data = ""
        try:
            with open(path, "r") as f:
                data = f.read()
        except FileNotFoundError:
            typer.secho("ERROR! File to import doesn't exist", fg=typer.colors.BRIGHT_RED)
            return
        
    data = json.loads(data)
    for item in track(iter(data), description="Importing..."):
        base.put(item)

    typer.secho(f"DONE! Imported data to {basename}", fg=typer.colors.BRIGHT_GREEN)