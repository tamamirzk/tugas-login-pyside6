from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen
from dashboard import Ui_DashboardWindow
from login import Ui_Login
import sys
import csv


class LoginUI(QMainWindow):
    def __init__(self, show_dashboard_callback):
        super(LoginUI, self).__init__()
        self.ui = Ui_Login(show_dashboard_callback)  # Pass show_dashboard_callback here
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.handle_login)
        self.show_dashboard_callback = show_dashboard_callback

    def handle_login(self):
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        user_data = self.ui.read_user_data('users.csv')
        if self.ui.validate_login(email, password, user_data):
            print("Login berhasil!")
            self.show_dashboard_callback(self)
        else:
            print("Email atau kata sandi salah.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    def show_dashboard(self):
        self.dashboard_window = QMainWindow()
        self.dashboard = Ui_DashboardWindow()
        self.dashboard.setupUi(self.dashboard_window)
        self.dashboard_window.show()

    w = LoginUI(show_dashboard)
    w.show()

    sys.exit(app.exec())


