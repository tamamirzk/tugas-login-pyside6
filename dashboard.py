from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel)

class Ui_DashboardWindow(object):
    def setupUi(self, DashboardWindow):
        if not DashboardWindow.objectName():
            DashboardWindow.setObjectName(u"DashboardWindow")
        DashboardWindow.resize(800, 600)
        DashboardWindow.setStyleSheet(u"QWidget#centralwidget{\n"
    "	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.023, stop:0 rgba(255, 140, 140, 255), stop:1 rgba(94, 122, 255, 255));\n"
    "	border-radius: 20px;\n"
    "}\n"
    "\n"
    "QLabel{\n"
    "	color: white;\n"
    "   text-align: center;\n"  # Align text to center
    "}\n")

        self.centralwidget = QWidget(DashboardWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        # Create labels for displaying text
        self.page_name = QLabel("Dashboard", self.centralwidget)
        self.page_name.setObjectName(u"page_name")
        self.verticalLayout.addWidget(self.page_name)

        self.label_name = QLabel("Nama: Mochamad Rizky Tamami", self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.verticalLayout.addWidget(self.label_name)

        self.label_nim = QLabel("NIM: 1001230028", self.centralwidget)
        self.label_nim.setObjectName(u"label_nim")
        self.verticalLayout.addWidget(self.label_nim)

        self.label_prodi = QLabel("Prodi: Sistem Informasi", self.centralwidget)
        self.label_prodi.setObjectName(u"label_prodi")
        self.verticalLayout.addWidget(self.label_prodi)

        DashboardWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DashboardWindow)

        QMetaObject.connectSlotsByName(DashboardWindow)
    # setupUi

    def retranslateUi(self, DashboardWindow):
        DashboardWindow.setWindowTitle(QCoreApplication.translate("DashboardWindow", u"Dashboard", None))
