import sys
import pandas as pd
import yaml


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, QFileDialog, qApp
from functools import partial
from typing import Dict
from data import LoadingData, MetricsData, ResulsData


class ViewMetrics(QMainWindow):
    def __init__(self):
        super().__init__()        

        self.loading_data : Dict[pd.DataFrame] = {}
        self.metrics_data: Dict[pd.DataFrame] = {}
        self.resuls_data: Dict[pd.DataFrame] = {}

        self.initUi()
    
    def initUi(self):
        # Параметры окна
        self.setWindowTitle("Метрики")
        self.setGeometry(100, 100, 800, 600)

        # Меню
        menubar = self.menuBar()
        
        # Файл меню
        file_menu = menubar.addMenu("Файл")

        # Новое окно
        new_window_action = QAction("Новое", self)
        new_window_action.triggered.connect(self.create_new_window)
        file_menu.addAction(new_window_action)

        # Загрузить данные
        load_data_action = QAction("Загрузить данные", self)
        load_data_action.triggered.connect(self.load_data)
        file_menu.addAction(load_data_action)

        # Очистить данные
        clear_data_action = QAction("Очистить", self)
        clear_data_action.triggered.connect(self.clear_data)
        file_menu.addAction(clear_data_action)

        # Очистить все данные
        clear_all_data_action = QAction("Очистить все", self)
        clear_all_data_action.triggered.connect(self.clear_all_data)
        file_menu.addAction(clear_all_data_action)

        # Выход
        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(qApp.quit)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # Метрики меню
        metrics_menu = menubar.addMenu("Метрики")

        # Редактировать метрики
        edit_metrics_action = QAction("Редактировать", self)
        edit_metrics_action.triggered.connect(self.edit_metrics)
        metrics_menu.addAction(edit_metrics_action)

        # Загрузка параметров метрик
        load_metrics_action = QAction("Загрузить", self)
        load_metrics_action.triggered.connect(self.load_metrics)
        metrics_menu.addAction(load_metrics_action)

        # Сохранение параметров метрик
        save_metrics_action = QAction("Сохранить", self)
        save_metrics_action.triggered.connect(self.save_metrics)
        metrics_menu.addAction(save_metrics_action)

        # Меню результатов
        results_menu = menubar.addMenu("Результаты")

        # Подсчет результатов метрик
        calc_results_action = QAction("Подсчет", self)
        calc_results_action.triggered.connect(self.calc_results_metrics)
        results_menu.addAction(calc_results_action)

        # Сохранение результатов метрик
        save_results_metrics_action = QAction("Сохранение результатов", self)
        save_results_metrics_action.triggered.connect(self.save_resuls_metrics)
        results_menu.addAction(save_results_metrics_action)

        # Загрузка результатов метрик
        load_results_metrics_action = QAction("Загрузка результатов", self)
        load_results_metrics_action.triggered.connect(self.load_results_metrics)
        results_menu.addAction(load_results_metrics_action)

        # Очистка результатов метрик
        clear_results_metrics_action = QAction("Очистка результатов", self)
        clear_results_metrics_action.triggered.connect(self.clear_results)
        results_menu.addAction(clear_results_metrics_action)

        # Отображение результатов метрик
        view_results_metrics_action = QAction("Отображение", self)
        view_results_metrics_action.triggered.connect(self.view_resuls_metrics)
        results_menu.addAction(view_results_metrics_action)

        # Сохранение отображения результатов метрик
        save_view_results_action = QAction("Сохранение отображения", self)
        save_view_results_action.triggered.connect(self.save_view_results_metrics)
        results_menu.addAction(save_view_results_action)

        # Очистка отображения результатов метрик
        clear_view_results_action = QAction("Очистка отображения", self)
        clear_view_results_action.triggered.connect(self.clear_view_results)
        results_menu.addAction(clear_view_results_action)


    # Ф-я создания нового окна
    def create_new_window(self):
        ...

    # Ф-я загрузки данных (csv)
    def load_data(self):
        ...

    # Ф-я выборочной очистки данных
    def clear_data(self):
        ...

    # Ф-я очистки всех данных
    def clear_all_data(self):
        ...

    # Ф-я редактирования метрик
    def edit_metrics(self):
        ...

    # Ф-я загрузки параметров метрик
    def load_metrics(self):
        ...

    # Ф-я сохранения параметров метрик
    def save_metrics(self):
        ...

    # Ф-я подсчета результатов метрик
    def calc_results_metrics(self):
        ...

    # Ф-я сохранения результатов подсчета
    def save_resuls_metrics(self):
        ...

    # Ф-я загрузки результатов метрик
    def load_results_metrics(self):
        ...

    # Ф-я отображения резульатов
    def view_resuls_metrics(self):
        ...

    # Ф-я сохранения отображения результатов
    def save_view_results_metrics(self):
        ...
    
    # Ф-я очистка результатов
    def clear_results(self):
        ...

    # Ф-я очистка отображения результатов
    def clear_view_results(self):
        ...

def main():
    app = QApplication(sys.argv)
    main_window = ViewMetrics()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()