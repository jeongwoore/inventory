# app.py
import sys, os
from PyQt5.QtWidgets import QApplication, QDialog
from login_dialog import LoginDialog
from main_window import MainWindow

# Qt platform plugin 경로 지정 (Windows)
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.path.join(
    sys.prefix, "Lib", "site-packages", "PyQt5", "Qt", "plugins", "platforms"
)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginDialog()
    if login.exec_() == QDialog.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
