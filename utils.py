import os
import pandas as pd
import yaml

from pathlib import Path
from typing import Union, Tuple


STANDART_DTYPE = {'int', 'str', 'float'}


def get_filename_from_path(path: Union[Path, str]) -> str:
    return os.path.basename(path).split(".")[0]


def get_filename_type_from_path(path: Union[Path, str]) -> Tuple[str]:
    filename = os.path.basename(path)
    name, ext = os.path.splitext(filename)
    return name, ext


def read_csv_from_path(path: Union[Path, str]):
    return pd.read_csv(path, sep=";")


def read_yaml_from_path(path: Union[Path, str]):
    with open(path, 'r') as file:
        data = yaml.safe_load(file)

    return data


def check_columns_in_dataframe(df: pd.DataFrame, columns_dict: dict) -> bool:
    for col in columns_dict['required_columns']:
        if col not in df.columns:
            return False

    return True


def apply_dtype_to_col(data_col, dtype: str):
    if dtype in STANDART_DTYPE:
        return data_col.astype(dtype)
    else:
        if "list" in dtype:
            elem_dtype = str_to_dtype(dtype[4:].strip("[]"))
            return data_col.apply(
                lambda x: [elem_dtype(i) for i in x.strip('[]').split(',')]
            )
        
    return data_col


def str_to_dtype(str_dtype: str):
    match str_dtype:
        case "int":
            return int
        case "float":
            return float
        case "str":
            return str
        case _:
            return str


# Удаление NaN и извлечение уникальных значений в порядке их появления
def unique_values(labels_cols, dtype=None):
    return labels_cols.dropna().astype(dtype).unique().tolist()


# Уникальные значения в стоблце в виде set
def unique_values_col(col_data) -> set:
    return set(col_data.unique())