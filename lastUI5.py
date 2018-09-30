# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lastUI5.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1110, 750)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 0)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1080, 700))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        #파일리스트
        self.tableWidget_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget_2.setGeometry(QtCore.QRect(860, 0, 210, 330))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.itemDoubleClicked.connect(self.showItem)
        #레이블리스트
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(860, 380, 210, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(2)
        #previous
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(860, 330, 100, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.previous_picture)
        #next
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(970, 330, 100, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.next_picture)
        #좌표 추가
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(760, 620, 90, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.addxybutton)
        #좌표 표시
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 620, 90, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.xyshowbutton)
        #save
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setGeometry(QtCore.QRect(910, 640, 100, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.savebtn)
        #폴더 탐색
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 0, 720, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.browse)
        #현재 이미지 이름
        self.label_imname = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_imname.setGeometry(QtCore.QRect(15, 30, 340, 30))
        self.label_imname.setObjectName("label_imname")
        #폴더 위치
        self.label_forder = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_forder.setGeometry(QtCore.QRect(15, 60, 450, 30))
        self.label_forder.setObjectName("label_forder")
        #이미지
        self.label_picture = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_picture.setGeometry(QtCore.QRect(20, 100, 800, 470))
        self.label_picture.setObjectName("label_picture")

        self.scrollAreaWidgetContents2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents2.setGeometry(QtCore.QRect(20, 100, 800, 470))
        self.scrollAreaWidgetContents2.setObjectName("scrollAreaWidgetContents2")

        self.scrollArea2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents2)
        self.scrollArea2.setGeometry(QtCore.QRect(20, 110, 800, 450))
        self.scrollArea2.setWidgetResizable(True) 
        self.scrollArea2.setWidget(self.label_picture)

        self.Qv = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents2)
        self.Qv.addWidget(self.scrollArea2)
        
        #1좌표
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(500, 570, 200, 20))
        self.label_4.setObjectName("label_4")
        #2좌표
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(500, 590, 200, 20))
        self.label_5.setObjectName("label_5")
        #3좌표
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(500, 610, 200, 20))
        self.label_6.setObjectName("label_6")
        #4좌표
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setGeometry(QtCore.QRect(500, 630, 200, 20))
        self.label_7.setObjectName("label_7")

        #검색 창
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setGeometry(QtCore.QRect(720, 0, 130, 30))
        self.lineEdit.setObjectName("lineEdit")
        #검색
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setGeometry(QtCore.QRect(720, 30, 130, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.search)
        #xml 생성 버튼 
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setGeometry(QtCore.QRect(860, 0, 210, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.xmlcreate)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        #파일
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        #관리자
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        #이미지축소/확대
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        #관리자모드 설정 해제
        self.action_0 = QtWidgets.QAction(MainWindow)
        self.action_0.setObjectName("action_0")
        self.action_0.triggered.connect(self.admin)
        #레이블 추가
        self.action_1 = QtWidgets.QAction(MainWindow)
        self.action_1.setObjectName("action_1")
        self.action_1.setEnabled(False)
        self.action_1.triggered.connect(self.doit)
        #분류
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_2.setEnabled(False)
        self.action_2.triggered.connect(self.doit2)

        #종료
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_3.setShortcut("Ctrl+Q")
        self.action_3.setStatusTip('Leave The App')
        self.action_3.triggered.connect(self.close_application)

        #레이블 삭제
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_4.setEnabled(False)
        self.action_4.triggered.connect(self.doit3)

        #이미지 확대
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_5.setShortcut("Ctrl++")
        self.action_5.triggered.connect(self.zoomin)

        #이미지 축소
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_6.setShortcut("Ctrl+-")
        self.action_6.triggered.connect(self.zoomout)

        #이미지 원상복구
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_7.setShortcut("Ctrl+S")
        self.action_7.triggered.connect(self.original_picture)



        self.menu.addAction(self.action_3)


        self.menu_2.addAction(self.action_0)
        self.menu_2.addAction(self.action_1)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_4)

        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)
        self.menu_3.addAction(self.action_7)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "<-"))
        self.pushButton_3.setText(_translate("MainWindow", "->"))
        self.pushButton_4.setText(_translate("MainWindow", "좌표 추가"))
        self.pushButton_5.setText(_translate("MainWindow", "좌표 표시"))
        self.pushButton_6.setText(_translate("MainWindow", "SAVE"))
        self.pushButton_7.setText(_translate("MainWindow", "폴더 탐색"))
        self.label_imname.setText(_translate("MainWindow", "현재 이미지 이름"))
        self.label_forder.setText(_translate("MainWindow", "폴더 위치"))
        self.label_picture.setText(_translate("MainWindow", "이미지"))
        self.label_4.setText(_translate("MainWindow", "첫번째좌표"))
        self.label_5.setText(_translate("MainWindow", "두번째좌표"))
        self.label_6.setText(_translate("MainWindow", "세번째좌표"))
        self.label_7.setText(_translate("MainWindow", "네번째좌표"))
        self.lineEdit.setText(_translate("MainWindow", "검색할 사진의 번호를 입력해주세요..."))
        self.pushButton_8.setText(_translate("MainWindow", "검색"))
        self.pushButton_9.setText(_translate("MainWindow", "xml 생성"))
        self.menu.setTitle(_translate("MainWindow", "파일"))
        self.menu_2.setTitle(_translate("MainWindow", "관리자"))
        self.menu_3.setTitle(_translate("MainWindow", "이미지 확대/축소"))
        self.action_0.setText(_translate("MainWindow", "관리자 모드 해제"))
        self.action_1.setText(_translate("MainWindow", "레이블 추가"))
        self.action_2.setText(_translate("MainWindow", "분류"))
        self.action_3.setText(_translate("MainWindow", "종료"))
        self.action_4.setText(_translate("MainWindow", "삭제"))
        self.action_5.setText(_translate("MainWindow", "이미지 확대"))
        self.action_6.setText(_translate("MainWindow", "이미지 축소"))
        self.action_7.setText(_translate("MainWindow", "이미지 원상복구"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())

