from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union
from utils import get_filename_type_from_path, read_csv_from_path


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
    def check_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass


class LoadingData(Data):
    def __init__(self, path: Union[Path, str]) -> None:
        super().__init__(path)
        self.read_data()

    def read_data(self):
        data = read_csv_from_path(self.path)
        

    def check_data(self):
        ...

    def process_data(self):
        ...


class MetricsData(Data):
    def __init__(self, path: Union[Path, str]) -> None:
        super().__init__(path)
    
    def read_data(self):
        ...

    def check_data(self):
        ...

    def process_data(self):
        ...


class ResulsData(Data):
    def __init__(self, path: Union[Path, str]) -> None:
        super().__init__(path)
    
    def read_data(self):
        ...

    def check_data(self):
        ...

    def process_data(self):
        ...