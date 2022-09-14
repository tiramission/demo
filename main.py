"""
Program Entry Point
"""

from app.cli import cli
from app.commands.golang import golang

if __name__ == '__main__':
    cli.add_command(golang)
    cli()
