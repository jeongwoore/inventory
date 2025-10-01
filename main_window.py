# main_window.py
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from db_helper import DB

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu List")
        self.setGeometry(100, 100, 400, 300)
        self.db = DB()
        self.setup_ui()

    def setup_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        # menu 테이블 내용 가져오기
        data = self.db.fetchall("SELECT * FROM menu")

        self.table.setRowCount(len(data))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["카테고리", "메뉴이름", "가격", "남은수량"])

        for row_idx, row_data in enumerate(data):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(row_data['카테고리'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(row_data['메뉴이름']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(row_data['가격'])))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(row_data['남은수량'])))
