import os
import json
import typer
from deta import Deta
from progress.bar import ChargingBar


# app configuration
app = typer.Typer(help="detapack: Import/Export data from/to Deta Bases")
APP_NAME = "detapack"
APP_VERSION = "0.1.1"


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
def export_command(key: str, basename: str):
    """
    Export Deta Base to a local .json file
    """

    typer.echo("Connecting to Deta...")
    try:
        deta = Deta(key)
        base = deta.Base(basename)
    except AssertionError:
        typer.secho("ERROR! Bad project key provided", fg=typer.colors.BRIGHT_RED)
        return

    typer.echo("Receiving data...")
    res = base.fetch().items

    typer.echo("Writing data...")
    target = "export.json"
    destination = str(os.getcwd()) + "/" + target

    with open(destination, "w") as f:
        f.write(json.dumps(res))

    typer.secho(f"DONE! Saved as {target} in {str(os.getcwd())}", fg=typer.colors.BRIGHT_GREEN)

@app.command(name="import")
def import_command(key: str, basename: str, path: str):
    """
    Import local .json file to Deta Base
    """

    typer.echo("Connecting to Deta...")
    try:
        deta = Deta(key)
        base = deta.Base(basename)
    except AssertionError:
        typer.secho("ERROR! Bad project key provided", fg=typer.colors.BRIGHT_RED)
        return

    typer.echo(f"Reading data from {path}...")
    data = ""
    with open(path, "r") as f:
        data = f.read()

    typer.echo(f"Importing to Deta Base...")
    data = json.loads(data)
    for item in ChargingBar("Importing").iter(data):
        base.put(item)

    typer.secho(f"DONE! Imported data to {basename}", fg=typer.colors.BRIGHT_GREEN)