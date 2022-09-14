from pathlib import Path

cache_dir = Path(__file__).parent.parent.parent.joinpath("cache")
cache_dir.exists() or cache_dir.mkdir()
