from pathlib import Path
from subprocess import check_call


def black():
    source_dir = Path(__file__).parent.parent.joinpath("python_project")
    scripts_dir = Path(__file__).parent
    check_call(f"black {str(source_dir)}", shell=True)
    check_call(f"black {str(scripts_dir)}", shell=True)


def isort():
    source_dir = Path(__file__).parent.parent.joinpath("python_project")
    scripts_dir = Path(__file__).parent
    check_call(f"isort {str(source_dir)}", shell=True)
    check_call(f"isort {str(scripts_dir)}", shell=True)


if __name__ == "__main__":
    black()
    isort()
