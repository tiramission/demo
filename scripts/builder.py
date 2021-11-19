import os
import shutil
from subprocess import check_call
from pathlib import Path
from sys import argv


def clean():
    dist_dir = Path(__file__).parent.parent.joinpath('dist')
    build_dir = Path(__file__).parent.parent.joinpath('build')
    spec_file = Path(__file__).parent.parent.joinpath('hello.spec')
    dist_dir.exists() and shutil.rmtree(dist_dir)
    build_dir.exists() and shutil.rmtree(build_dir)
    spec_file.exists() and os.remove(spec_file)


def build():
    clean()
    if "clean" in argv or "--clean" in argv:
        return
    entry_py = Path(__file__).parent.parent.joinpath('main.py').relative_to(Path.cwd())
    build_cmd = f"pyinstaller {entry_py} -F --name hello"
    check_call(build_cmd, shell=True)


if __name__ == '__main__':
    build()
