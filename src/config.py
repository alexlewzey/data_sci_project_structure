"""Project configurations such as logger, color scheme etc"""

import logging
from itertools import cycle

# logger configuration
logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.INFO,
    # filename='logs.txt'
)

# color schemes
rgba = {
    'green main': 'rgba(112, 182, 88, 0.6)',
    'green dark': 'rgba(33, 84, 37, 0.6)',
    'grey dark': 'rgba(49, 45, 49, 0.6)',
    'dog': 'rgba(191, 209, 67, 0.6)',
    'cat': 'rgba(232, 132, 65, 0.6)',
    'small pet': 'rgba(212, 153, 59, 0.6)',
    'fish': 'rgba(40, 58, 140, 0.6)',
    'bird': 'rgba(109, 173, 218, 0.6)',
    'reptile': 'rgba(101, 38, 57, 0.6)',
}
rgba_vals = list(rgba.values())
rgba_inf = cycle(rgba.values())

rgb = {
    'green_main': (112, 182, 88),
    'green_dark': (33, 84, 37),
    'grey_dark': (49, 45, 49),
    'dog': (191, 209, 67),
    'cat': (232, 132, 65),
    'small_pet': (212, 153, 59),
    'fish': (40, 58, 140),
    'bird': (109, 173, 218),
    'reptile': (101, 38, 57),
    'black': (0, 0, 0),
    'white': (255, 255, 255),
}
