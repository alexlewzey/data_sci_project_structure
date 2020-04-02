"""
Constants to be used throughout the project these include:
 - string constants (such as dates), common phrases, dates
 - numeric constants such as factors and single inputs
 - all file paths (data, figures etc)
 """
from pathlib import Path


class Dirs:
    """namespace for directory paths"""
    ROOT = Path(__file__).parent.parent
    DATA = ROOT / 'data'  # store for intermediate analysis
    OUTPUT = ROOT / 'output'
    CHARTS = OUTPUT / 'charts'
    EXTERNAL = DATA / 'external'
    INTERIM = DATA / 'interim'
    PROCESSED = DATA / 'processed'
    RAW = DATA / 'raw'

    MODELS = ROOT / 'models'

    FIGURES = ROOT / 'reports' / 'figures'


class External:
    """namespace for external data file paths"""
    pass


class Interim:
    """namespace for interim data file paths"""
    pass


class Processed:
    """namespace for processed data file paths"""
    pass


class Raw:
    """namespace for raw data file paths"""
    pass


class Models:
    """namespace for serialised model paths"""
    pass


class Charts:
    """namespace for chart file paths"""
    pass


# dates


# string constants


# numeric constants
MIL: int = 1_000_000
