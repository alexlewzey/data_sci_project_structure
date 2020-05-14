"""Module of global constants"""
from pathlib import Path

from src.helpers import slibtk


class Paths:
    """Global constants for directory/file paths"""
    ROOT = Path(__file__).parent.parent
    DATA = ROOT / 'data'
    INTERIM = DATA / 'interim'
    RAW = DATA / 'raw'

    MODELS = ROOT / 'models'

    OUTPUT = ROOT / 'output'
    TODAY = slibtk.date_versioned_dir(OUTPUT)
    TODAY.mkdir(exist_ok=True)

    SQL = ROOT / 'src' / 'data'
