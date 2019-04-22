import os
import sys
from gtts import gTTS
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('EnglishtoDiscordEmotes')

        self.text = QLabel("(Discord emotes result will appear here)")
        self.textbox = QLineEdit("Enter English Text to Convert Here")
        self.button = QPushButton("Convert (Text will be copied to clipboard)")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # Connecting the signal
        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        print("Input: " + str(self.textbox.text()))
        output = ""
        self.text.setText("Converting...")

        for char in str(self.textbox.text().lower()):
            if char == " ":
                output = output + "   "
            elif char == "a":
                output = output + " :regional_indicator_a:"
            elif char == "b":
                output = output + " :regional_indicator_b:"
            elif char == "c":
                output = output + " :regional_indicator_c:"
            elif char == "d":
                output = output + " :regional_indicator_d:"
            elif char == "e":
                output = output + " :regional_indicator_e:"
            elif char == "f":
                output = output + " :regional_indicator_f:"
            elif char == "g":
                output = output + " :regional_indicator_g:"
            elif char == "h":
                output = output + " :regional_indicator_h:"
            elif char == "i":
                output = output + " :regional_indicator_u:"
            elif char == "j":
                output = output + " :regional_indicator_j:"
            elif char == "k":
                output = output + " :regional_indicator_k:"
            elif char == "l":
                output = output + " :regional_indicator_l:"
            elif char == "m":
                output = output + " :regional_indicator_m:"
            elif char == "n":
                output = output + " :regional_indicator_n:"
            elif char == "o":
                output = output + " :regional_indicator_o:"
            elif char == "p":
                output = output + " :regional_indicator_p:"
            elif char == "q":
                output = output + " :regional_indicator_q:"
            elif char == "r":
                output = output + " :regional_indicator_r:"
            elif char == "s":
                output = output + " :regional_indicator_s:"
            elif char == "t":
                output = output + " :regional_indicator_t:"
            elif char == "u":
                output = output + " :regional_indicator_u:"
            elif char == "v":
                output = output + " :regional_indicator_v:"
            elif char == "w":
                output = output + " :regional_indicator_w:"
            elif char == "x":
                output = output + " :regional_indicator_x:"
            elif char == "y":
                output = output + " :regional_indicator_y:"
            elif char == "z":
                output = output + " :regional_indicator_z:"
            else:
                output = output + char

        self.text.setText(output)
        clipboard = QApplication.clipboard()
        clipboard.clear(mode=clipboard.Clipboard)
        clipboard.setText(output, mode=clipboard.Clipboard)
        print("Output: " + output)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 300)
    widget.setFixedSize(800, 300)
    widget.show()

    sys.exit(app.exec_())