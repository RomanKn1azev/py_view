import pandas as pd


from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union, Dict
from utils import get_filename_type_from_path, read_csv_from_path, check_columns_in_dataframe, apply_dtype_to_col, unique_values_col


class Data(ABC):
    def __init__(self, path: Union[Path, str]) -> None:
        self._path = path
        self._name, self._data_type = get_filename_type_from_path(self.path)

    @property
    def path(self):
        return self._path
    
    @property
    def name(self):
        return self._name
    
    @property
    def data_type(self):
        return self._data_type

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def check_data(self, data: pd.DataFrame):
        pass

    @abstractmethod
    def process_data(self, data: pd.DataFrame):
        pass


class LoadingData(Data):
    def __init__(self, path: Union[Path, str], loading_params: dict) -> None:
        super().__init__(path)
        self.loading_params: dict = loading_params
        self.opportunity_tasks: set = set()
        self.data: pd.DataFrame = None
        self.labels: set = {}
        self.read_data()

    def read_data(self):
        data = read_csv_from_path(self.path)
        self.check_data(data)
        self.process_data(data)

    def check_data(self, data: pd.DataFrame):
        for task_name, params in self.loading_params["tasks"].items():
            if check_columns_in_dataframe(data, params) == True:
                self.opportunity_tasks.add(task_name)

    def process_data(self, data: pd.DataFrame):
        result_data = pd.DataFrame()

        for task in self.opportunity_tasks:
            col_dtypes: dict = self.loading_params["tasks"][task]["dtypes"] # dtype каждого стоблца

            for col, dtype in col_dtypes.items():
                if col not in result_data.columns:
                    result_data[col] = apply_dtype_to_col(data[col].copy(), dtype)

        self.data = result_data               
        self.labels = unique_values_col(result_data["y_true"])

class MetricsData(Data):
    def __init__(self, path: Union[Path, str], metrics_params: dict) -> None:
        super().__init__(path)
        self.metrics_params: dict = metrics_params        
    
    def read_data(self):
        ...

    def check_data(self, data: pd.DataFrame):
        ...

    def process_data(self, data: pd.DataFrame):
        ...


class LabelsData(Data):
    def __init__(self, path: Union[Path, str]) -> None:
        super().__init__(path)
    
    def read_data(self):
        ...

    def check_data(self, data: pd.DataFrame):
        ...

    def process_data(self, data: pd.DataFrame):
        ...


class ResulsData(Data):
    def __init__(self, path: Union[Path, str]) -> None:
        super().__init__(path)
    
    def read_data(self):
        ...

    def check_data(self, data: pd.DataFrame):
        ...

    def process_data(self, data: pd.DataFrame):
        ...