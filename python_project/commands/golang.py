import shutil
import tempfile
from pathlib import Path

import click

import python_project.tools.golang as golang_tools


@click.command("golang")
@click.option("--list", "-l", is_flag=True)
def golang(**kwargs):
    show_list: bool = kwargs.pop("list")
    if show_list:
        versions = golang_tools.get_all_versions()
        for version in versions:
            click.echo(f" * {version}")
