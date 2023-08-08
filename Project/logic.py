from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.radio_on.clicked.connect(lambda: self.power())
        self.radio_off.clicked.connect(lambda: self.power())
        self.radio_mute.clicked.connect(lambda: self.mute())
        self.button_volume_up.clicked.connect(self.volume_up)
        self.button_volume_down.clicked.connect(self.volume_down)
        self.button_channel_up.clicked.connect(self.channel_up)
        self.button_channel_down.clicked.connect(self.channel_down)

    def power(self):
        if self.radio_on.isChecked():
            self.text_status.setTextColor(QColor("green"))
            self.text_status.setText("POWER ON")


        if self.radio_off.isChecked():
            self.text_status.setTextColor(QColor("red"))
            self.text_status.setText("POWER OFF")

            self.radio_mute.setChecked(False)
            self.text_muted.setText("UNMUTED")


    def mute(self):
        if self.radio_on.isChecked():
            if self.radio_mute.isChecked():
                self.text_muted.setText("MUTED")
                volume = 0
                self.volume_num.setText("{}".format(volume))
            else:
                self.text_muted.setText("UNMUTED")
        if self.radio_off.isChecked():
            self.radio_mute.setChecked(False)
            self.text_muted.setText("UNMUTED")

    def volume_up(self):
        MAX_VOLUME = 2
        volume = int(self.volume_num.toPlainText())
        if self.radio_on.isChecked():
            if self.radio_mute.isChecked():
                self.text_muted.setText("UNMUTED")
                self.radio_mute.setChecked(False)
            if volume < MAX_VOLUME:
                volume += 1
                self.volume_num.setText("{}".format(volume))
            else:
                volume = MAX_VOLUME
                self.volume_num.setText("{}".format(volume))

    def volume_down(self):
        MIN_VOLUME = 0
        volume = int(self.volume_num.toPlainText())
        if self.radio_on.isChecked():
            if self.radio_mute.isChecked():
                self.text_muted.setText("UNMUTED")
                self.radio_mute.setChecked(False)
            if volume > MIN_VOLUME:
                volume -= 1
                self.volume_num.setText("{}".format(volume))
            else:
                volume = MIN_VOLUME
                self.volume_num.setText("{}".format(volume))

    def channel_up(self):
        MAX_CHANNEL = 3
        MIN_CHANNEL = 0
        channel = int(self.channel_num.toPlainText())
        if self.radio_on.isChecked():
            if channel < MAX_CHANNEL:
                channel += 1
                self.channel_num.setText("{}".format(channel))
            else:
                channel = MIN_CHANNEL
                self.channel_num.setText("{}".format(channel))

    def channel_down(self):
        MIN_CHANNEL = 0
        MAX_CHANNEL = 3
        channel = int(self.channel_num.toPlainText())
        if self.radio_on.isChecked():
            if channel > MIN_CHANNEL:
                channel -= 1
                self.channel_num.setText("{}".format(channel))
            else:
                channel = MAX_CHANNEL
                self.channel_num.setText("{}".format(channel))
