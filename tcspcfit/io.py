import logging

import pandas as pd

from .error import UnknownBrand

logger = logging.getLogger(__name__)

def _read_edinburgh(path, model=None):
    configs = {
        'header': None,
        'names': ['time', 'counts'],
        'skiprows': 1
    }
    if model == 'F980':
        configs['delimiter'] = '\s+'
    elif model == 'F900':
        configs['delimiter'] = ','
    else:
        raise UnknownBrand

    return pd.read_csv(path, **configs)

def read_file(path, brand=None, **kwargs):
    try: 
        return {
            'Edinburgh': _read_edinburgh
        }[brand](path, **kwargs)
    except KeyError:
        raise UnknownBrand("unsupported brand \"{}\"".format(brand))