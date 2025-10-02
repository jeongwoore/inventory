from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from db_helper import DB, DB_CONFIG
from insert_dialog import InsertDialog
from update_dialog import UpdateDialog
from delete_dialog import DeleteDialog

class InventoryWindow(QMainWindow) :

    def __init__(self):
        super().__init__()   # 상속받은 부모 클래스의 생성자 호출
        self.setWindowTitle("버거킹 재고 관리")
        #  self.setWindowIcon(QIcon("hotdog.png"))
        self.resize(800, 600)   # 윈도우(결과창) 크기 조절
        
        self.db = DB(**DB_CONFIG)

        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        form_box = QHBoxLayout()
        self.btn_insert = QPushButton("추가")
        self.btn_update = QPushButton("수정")
        self.btn_delete = QPushButton("삭제")

        self.btn_insert.clicked.connect(self.open_dialog_insert)
        self.btn_update.clicked.connect(self.open_dialog_update)
        self.btn_delete.clicked.connect(self.open_dialog_delete)

        form_box.addWidget(self.btn_insert)
        form_box.addWidget(self.btn_update)
        form_box.addWidget(self.btn_delete)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["카테고리", "메뉴번호", "메뉴이름", "가격", "남은수량"])
        self.table.setEditTriggers(self.table.NoEditTriggers) 
        self.table.verticalHeader().setVisible(False)

        vbox.addLayout(form_box)
        vbox.addWidget(self.table)

        self.load_items()

    def load_items(self):
        rows = self.db.fetch_items()
        self.table.setRowCount(len(rows))
        for r, row in enumerate(rows):
            category = row['category']
            id = row['id']
            name = row['name']
            price = str(row['price'])
            stock = str(row['stock'])

            self.table.setItem(r, 0, QTableWidgetItem(category))
            self.table.setItem(r, 1, QTableWidgetItem(str(id)))
            self.table.setItem(r, 2, QTableWidgetItem(name))
            self.table.setItem(r, 3, QTableWidgetItem(price))
            self.table.setItem(r, 4, QTableWidgetItem(stock))
            
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    def open_dialog_insert(self) :
        dialog = InsertDialog()
        if dialog.exec_() == InsertDialog.Accepted :
            self.load_items()
    
    def open_dialog_update(self) :
        dialog = UpdateDialog()
        if dialog.exec_() == UpdateDialog.Accepted :
            self.load_items()
            
    def open_dialog_delete(self) :
        dialog = DeleteDialog()
        if dialog.exec_() == DeleteDialog.Accepted :
            self.load_items()
