import os
import pandas as pd

from pathlib import Path
from typing import Union, Tuple


def get_filename_from_path(path: Union[Path, str]) -> str:
    return os.path.basename(path).split(".")[0]


def get_filename_type_from_path(path: Union[Path, str]) -> Tuple[str]:
    filename = os.path.basename(path)
    name, ext = os.path.splitext(filename)
    return name, ext


def read_csv_from_path(path: Union[Path, str]):
    return pd.read_csv(path, sep=" ")