"""Module of global constants"""
from pathlib import Path


class Paths:
    """Global constants for directory/file paths"""
    ROOT = Path(__file__).parent.parent
    DATA = ROOT / 'data'
    INTERIM = DATA / 'interim'
    RAW = DATA / 'raw'

    MODELS = ROOT / 'models'

    OUTPUT = ROOT / 'output'

    SQL = ROOT / 'src' / 'data'
