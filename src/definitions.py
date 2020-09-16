"""Module of global constants"""
from pathlib import Path


class Paths:
    """Global constants for directory/file paths"""
    ROOT = Path(__file__).parent.parent
    DATA = ROOT / 'data'
    CACHES = DATA / 'caches'
    INTERIM = DATA / 'interim'
    RAW = DATA / 'raw'

    MODELS = ROOT / 'models'

    OUTPUT = ROOT / 'output'

    def version(self, i: int):
        dir_ = self.OUTPUT / f'version_{i}'
        dir_.mkdir(exist_ok=True)
        return dir_

    SRC_DATA = ROOT / 'src' / 'data'
