"""
Constants to be used throughout the project these include:
 - string constants (such as dates), common phrases, dates
 - numeric constants such as factors and single inputs
 - all file paths (data, figures etc)
 """
from pathlib import Path

# paths
ROOT = Path(__file__).parent.parent
DATA = ROOT / 'data'
EXTERNAL = DATA / 'external'
INTERIM = DATA / 'interim'
PROCESSED = DATA / 'processed'
RAW = DATA / 'raw'

MODELS = ROOT / 'models'

FIGURES = ROOT / 'reports' / 'figures'

# dates


# string constants



# numeric constants
MIL: int = 1_000_000

