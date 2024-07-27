from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union
from utils import get_filename_type_from_path


class Data(ABC):
    def __init__(self, path: Union[Path, str]) -> None:
        self.path = path
        self.name, self.type = get_filename_type_from_path(self.path)

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

    def read_data(self):
        ...

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