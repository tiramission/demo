from python_project.cli import cli
from python_project.commands.golang import golang

if __name__ == '__main__':
    cli.add_command(golang)
    cli()
