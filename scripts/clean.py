import shutil
import os

from pathlib import Path


def clean():
    dist_dir = Path(__file__).parent.parent.joinpath('dist')
    build_dir = Path(__file__).parent.parent.joinpath('build')
    spec_file = Path(__file__).parent.parent.joinpath('hello.spec')
    cache_dir = Path(__file__).parent.parent.joinpath('cache')
    dist_dir.exists() and shutil.rmtree(dist_dir)
    build_dir.exists() and shutil.rmtree(build_dir)
    spec_file.exists() and os.remove(spec_file)
    cache_dir.exists() and shutil.rmtree(cache_dir)


if __name__ == '__main__':
    clean()
