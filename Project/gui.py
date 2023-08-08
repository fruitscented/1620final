# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 500)
        MainWindow.setMinimumSize(QtCore.QSize(350, 500))
        MainWindow.setMaximumSize(QtCore.QSize(350, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_volume_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_volume_up.setGeometry(QtCore.QRect(70, 180, 93, 28))
        self.button_volume_up.setObjectName("button_volume_up")
        self.button_volume_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_volume_down.setGeometry(QtCore.QRect(70, 210, 93, 28))
        self.button_volume_down.setObjectName("button_volume_down")
        self.button_channel_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_up.setGeometry(QtCore.QRect(190, 180, 93, 28))
        self.button_channel_up.setObjectName("button_channel_up")
        self.button_channel_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_down.setGeometry(QtCore.QRect(190, 210, 93, 28))
        self.button_channel_down.setObjectName("button_channel_down")
        self.radio_mute = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_mute.setGeometry(QtCore.QRect(70, 110, 95, 20))
        self.radio_mute.setObjectName("radio_mute")
        self.text_status = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.text_status.setGeometry(QtCore.QRect(50, 270, 256, 31))
        self.text_status.setObjectName("text_status")
        self.text_muted = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.text_muted.setGeometry(QtCore.QRect(50, 310, 256, 31))
        self.text_muted.setObjectName("text_muted")
        self.text_channel = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.text_channel.setGeometry(QtCore.QRect(50, 400, 91, 31))
        self.text_channel.setObjectName("text_channel")
        self.text_volume = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.text_volume.setGeometry(QtCore.QRect(50, 360, 91, 31))
        self.text_volume.setObjectName("text_volume")
        self.volume_num = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.volume_num.setGeometry(QtCore.QRect(160, 360, 91, 31))
        self.volume_num.setObjectName("volume_num")
        self.channel_num = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.channel_num.setGeometry(QtCore.QRect(160, 400, 91, 31))
        self.channel_num.setObjectName("channel_num")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 60, 211, 51))
        self.groupBox.setObjectName("groupBox")
        self.radio_on = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radio_on.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.radio_on.setObjectName("radio_on")
        self.radio_off = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radio_off.setGeometry(QtCore.QRect(154, 20, 51, 20))
        self.radio_off.setObjectName("radio_off")
        self.radio_off.setChecked(True)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(47, 30, 251, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 40, 20, 211))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(50, 240, 251, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(290, 40, 20, 211))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 160, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 160, 55, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 26))
        self.menubar.setObjectName("menubar")
        self.menuREMOTE = QtWidgets.QMenu(parent=self.menubar)
        self.menuREMOTE.setObjectName("menuREMOTE")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuREMOTE.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_volume_up.setText(_translate("MainWindow", "Up"))
        self.button_volume_down.setText(_translate("MainWindow", "Down"))
        self.button_channel_up.setText(_translate("MainWindow", "Up"))
        self.button_channel_down.setText(_translate("MainWindow", "Down"))
        self.radio_mute.setText(_translate("MainWindow", "Mute"))
        self.text_status.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ff0000;\">POWER OFF</span></p></body></html>"))
        self.text_muted.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">UNMUTED</span></p></body></html>"))
        self.text_channel.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Channel:</span></p></body></html>"))
        self.text_volume.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Volume:</span></p></body></html>"))
        self.volume_num.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">0</span></p></body></html>"))
        self.channel_num.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "TV Power"))
        self.radio_on.setText(_translate("MainWindow", "On"))
        self.radio_off.setText(_translate("MainWindow", "Off"))
        self.label.setText(_translate("MainWindow", "Volume"))
        self.label_2.setText(_translate("MainWindow", "Channel"))
        self.menuREMOTE.setTitle(_translate("MainWindow", "REMOTE "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())