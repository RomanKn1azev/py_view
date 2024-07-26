import sys
import pandas as pd


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, QFileDialog, qApp
from functools import partial
from typing import Dict


class ViewMetrics(QMainWindow):
    def __init__(self):
        super().__init__()        

        self.data : Dict[pd.DataFrame] = {}
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

        # Сохранить результаты метрик
        save_results_metrics_action = QAction("Сохранить результаты", self)
        save_results_metrics_action.triggered.connect(self.save_resuls_metrics)
        file_menu.addAction(save_results_metrics_action)

        # Выход
        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(qApp.quit)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)



    def create_new_window(self):
        ...

    def load_data(self):
        ...
    
    def save_resuls_metrics(self):
        ...
                

def main():#
    app = QApplication(sys.argv)
    main_window = ViewMetrics()
    main_window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()