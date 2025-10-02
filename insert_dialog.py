# login_dialog.py
from PyQt5.QtWidgets import *
from db_helper import DB, DB_CONFIG

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("추가")
        self.db = DB(**DB_CONFIG)

        self.pcategory = QLineEdit()
        self.pid = QLineEdit()
        self.pname = QLineEdit()   # 문자열 입력 받기
        self.pprice = QLineEdit()
        self.pstock = QSpinBox()   # 숫자 입력용 필드

        form = QFormLayout()
        form.addRow("카테고리", self.pcategory)
        form.addRow("메뉴번호", self.pid)
        form.addRow("메뉴이름", self.pname)
        form.addRow("가격", self.pprice)
        form.addRow("남은수량", self.pstock)

        
        buttonBox = QHBoxLayout()

        self.btn_submit = QPushButton("추가")
        self.btn_submit.clicked.connect(self.submit)
        self.btn_cancel = QPushButton("취소")
        self.btn_cancel.clicked.connect(self.reject) # 대화창 닫기

        buttonBox.addWidget(self.btn_submit)
        buttonBox.addWidget(self.btn_cancel)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(buttonBox)
        # layout.addWidget(buttonBox)
        self.setLayout(layout)

    def submit(self):
        category = self.pcategory.text().strip()
        id = self.pid.text().strip()
        name = self.pname.text().strip()   # strip : 불필요한 존재 제거
        price = self.pprice.text().strip()
        stock = self.pstock.value()   # spinbox는 정수 값을 반환하는 메소드가 따로 있음(value는 정수 반환)
        if not category or not id or not name or not price or not stock:
            QMessageBox.warning(self, "오류", "데이터를 빠짐없이 입력하세요.")
            return
        ok = self.db.insert_items(category, name, price, stock)
        if ok:
            QMessageBox.information(self, "완료", "추가되었습니다.")
        else:
            QMessageBox.critical(self, "실패", "추가 중 오류가 발생했습니다.")
        self.accept()   # 대화창의 동작 완료를 뜻하는 메소드