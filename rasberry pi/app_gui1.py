

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.setEnabled(True)
        mainwindow.resize(1906, 990)
        mainwindow.setStyleSheet("background-color: rgb(227, 227, 227);")
        mainwindow.setAnimated(True)
        mainwindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stacked_widget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked_widget.setGeometry(QtCore.QRect(-10, 0, 1921, 1021))
        self.stacked_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stacked_widget.setObjectName("stacked_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_destination_3 = QtWidgets.QLabel(self.page)
        self.label_destination_3.setGeometry(QtCore.QRect(0, 70, 161, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_destination_3.setFont(font)
        self.label_destination_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding: 6px;\n"
"padding-bottom: 40px\n"
"")
        self.label_destination_3.setObjectName("label_destination_3")
        self.button_cost = QtWidgets.QPushButton(self.page)
        self.button_cost.setEnabled(True)
        self.button_cost.setGeometry(QtCore.QRect(40, 580, 331, 171))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_cost.setFont(font)
        self.button_cost.setMouseTracking(False)
        self.button_cost.setStyleSheet("QPushButton#button_cost {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-width: 5px;\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    border-color:  rgb(18, 136, 73);\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#button_cost:pressed {\n"
"    border-color: rgb(255, 170, 0)\n"
"}\n"
"")
        self.button_cost.setObjectName("button_cost")
        self.button_eco = QtWidgets.QPushButton(self.page)
        self.button_eco.setEnabled(True)
        self.button_eco.setGeometry(QtCore.QRect(400, 580, 331, 171))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_eco.setFont(font)
        self.button_eco.setAutoFillBackground(False)
        self.button_eco.setStyleSheet("QPushButton#button_eco {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-width: 5px;\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    border-color: rgb(18, 136, 73);\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#button_eco:pressed {\n"
"    background-color: rgb(18, 136, 73);\n"
"    border-color: rgb(255, 255, 255);    \n"
"}")
        self.button_eco.setObjectName("button_eco")
        self.label_destination = QtWidgets.QLabel(self.page)
        self.label_destination.setGeometry(QtCore.QRect(20, 270, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_destination.setFont(font)
        self.label_destination.setStyleSheet("background-color: rgb(0, 189, 92);")
        self.label_destination.setObjectName("label_destination")
        self.line_edit_destination = QtWidgets.QLineEdit(self.page)
        self.line_edit_destination.setGeometry(QtCore.QRect(240, 270, 841, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(20)
        self.line_edit_destination.setFont(font)
        self.line_edit_destination.setStyleSheet(" QLineEdit {\n"
"\n"
"     border-radius: 10px;\n"
"     padding: 0 8px;\n"
"     background-color: white;\n"
"     selection-background-color: white;\n"
" }\n"
"\n"
"")
        self.line_edit_destination.setText("")
        self.line_edit_destination.setFrame(False)
        self.line_edit_destination.setObjectName("line_edit_destination")
        self.output_box = QtWidgets.QPlainTextEdit(self.page)
        self.output_box.setEnabled(True)
        self.output_box.setGeometry(QtCore.QRect(1280, 240, 561, 451))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiLight")
        font.setPointSize(16)
        self.output_box.setFont(font)
        self.output_box.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"\n"
"    border-top: none;           /* No border on top */\n"
"    border-left: none;          /* No border on left */\n"
"    border-right: none;         /* No border on right */\n"
"    border-bottom-left-radius: 10px;  /* Curved bottom-left */\n"
"    border-bottom-right-radius: 10px; /* Curved bottom-right */\n"
"    padding: 5px 2px;  ")
        self.output_box.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.output_box.setReadOnly(True)
        self.output_box.setObjectName("output_box")
        self.label_start = QtWidgets.QLabel(self.page)
        self.label_start.setGeometry(QtCore.QRect(20, 190, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_start.setFont(font)
        self.label_start.setStyleSheet("background-color: rgb(0, 189, 92);")
        self.label_start.setObjectName("label_start")
        self.heading_box = QtWidgets.QPlainTextEdit(self.page)
        self.heading_box.setGeometry(QtCore.QRect(1280, 40, 561, 201))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(36)
        self.heading_box.setFont(font)
        self.heading_box.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"\n"
"    border-bottom: none;         /* No border on bottom */\n"
"    border-left: none;           /* No border on left */\n"
"    border-right: none;          /* No border on right */\n"
"    border-top-left-radius: 10px;   /* Curved top-left */\n"
"    border-top-right-radius: 10px;  /* Curved top-right */\n"
"    padding: 5px 10px;  ")
        self.heading_box.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.heading_box.setReadOnly(True)
        self.heading_box.setObjectName("heading_box")
        self.label_destination_2 = QtWidgets.QLabel(self.page)
        self.label_destination_2.setGeometry(QtCore.QRect(0, 500, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_destination_2.setFont(font)
        self.label_destination_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding: 6px;\n"
"padding-bottom: 40px\n"
"")
        self.label_destination_2.setObjectName("label_destination_2")
        self.line_edit_start = QtWidgets.QLineEdit(self.page)
        self.line_edit_start.setGeometry(QtCore.QRect(240, 180, 841, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(20)
        self.line_edit_start.setFont(font)
        self.line_edit_start.setStyleSheet(" QLineEdit {\n"
"     border-radius: 10px;\n"
"     padding: 0 8px;\n"
"    background-color: white;\n"
"     selection-background-color: white;\n"
" }\n"
"\n"
"")
        self.line_edit_start.setText("")
        self.line_edit_start.setFrame(False)
        self.line_edit_start.setObjectName("line_edit_start")
        self.button_fastest = QtWidgets.QPushButton(self.page)
        self.button_fastest.setEnabled(True)
        self.button_fastest.setGeometry(QtCore.QRect(760, 580, 331, 171))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.button_fastest.setFont(font)
        self.button_fastest.setStyleSheet("QPushButton#button_fastest {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-width: 5px;\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    border-color:  rgb(18, 136, 73);\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#button_fastest:pressed {\n"
"    border-color: rgb(255, 170, 0)\n"
"}\n"
"")
        self.button_fastest.setObjectName("button_fastest")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 550, 1121, 231))
        self.label_2.setStyleSheet("background-color: rgb(0, 189, 92);\n"
" border-radius: 10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(-70, 120, 1191, 271))
        self.label.setStyleSheet(" border-radius: 10px;\n"
"background-color: rgb(0, 189, 92);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.create_route_button = QtWidgets.QPushButton(self.page)
        self.create_route_button.setGeometry(QtCore.QRect(1280, 710, 561, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.create_route_button.setFont(font)
        self.create_route_button.setStyleSheet("QPushButton#create_route_button {\n"
"\n"
"    background-color: rgb(0, 192, 92);\n"
"    border-width: 1px;\n"
"    border-radius: 20px;\n"
"    border-color:  rgb(0, 192, 92);\n"
"\n"
"}")
        self.create_route_button.setObjectName("create_route_button")
        self.current_location_button = QtWidgets.QPushButton(self.page)
        self.current_location_button.setGeometry(QtCore.QRect(730, 400, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.current_location_button.setFont(font)
        self.current_location_button.setStyleSheet("QPushButton#current_location_button {\n"
"    background-color: rgb(0, 192, 92);\n"
"    border-width: 1px;\n"
"    border-radius: 20px;\n"
"    border-color:  rgb(0, 192, 92);\n"
"}")
        self.current_location_button.setObjectName("current_location_button")
        self.label_destination_2.raise_()
        self.label_destination_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.button_cost.raise_()
        self.button_eco.raise_()
        self.label_destination.raise_()
        self.line_edit_destination.raise_()
        self.output_box.raise_()
        self.label_start.raise_()
        self.heading_box.raise_()
        self.line_edit_start.raise_()
        self.button_fastest.raise_()
        self.create_route_button.raise_()
        self.current_location_button.raise_()
        self.stacked_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.logo = QtWidgets.QLabel(self.page_2)
        self.logo.setGeometry(QtCore.QRect(720, 250, 481, 281))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("C:\\Users\\monty\\OneDrive\\Desktop\\rasberry pi\\logo.jpg"))
        self.logo.setObjectName("logo")
        self.enter_button = QtWidgets.QPushButton(self.page_2)
        self.enter_button.setGeometry(QtCore.QRect(770, 550, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.enter_button.setFont(font)
        self.enter_button.setStyleSheet("QPushButton#enter_button {\n"
"\n"
"    background-color: rgb(0, 192, 92);\n"
"    border-width: 1px;\n"
"    border-radius: 20px;\n"
"    border-color:  rgb(0, 192, 92);\n"
"\n"
"}")
        self.enter_button.setObjectName("enter_button")
        self.stacked_widget.addWidget(self.page_2)
        mainwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainwindow)
        self.stacked_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "MoveEco"))
        self.label_destination_3.setText(_translate("mainwindow", "Set Route"))
        self.button_cost.setText(_translate("mainwindow", "SAVER"))
        self.button_eco.setText(_translate("mainwindow", "ECO "))
        self.label_destination.setText(_translate("mainwindow", "DESTINATION"))
        self.label_start.setText(_translate("mainwindow", "START"))
        self.label_destination_2.setText(_translate("mainwindow", "Choose Mode"))
        self.button_fastest.setText(_translate("mainwindow", "SPEED"))
        self.create_route_button.setText(_translate("mainwindow", "Create Route"))
        self.current_location_button.setText(_translate("mainwindow", "Use current location"))
        self.enter_button.setText(_translate("mainwindow", "CLICK TO START"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_mainwindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
