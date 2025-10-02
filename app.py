# app.py
import sys
from PyQt5.QtWidgets import QApplication
from main_window import InventoryWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryWindow()
    window.show()
    sys.exit(app.exec_())