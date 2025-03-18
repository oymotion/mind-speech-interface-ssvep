from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit

from UI.Components.button_container import ButtonContainer  # buttonClickNoise

# from gtts import gTTS

# from playsound import playsound

import os
import pyttsx3


class YesNoWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        layout = self.createLayout(parent)
        self.setObjectName("YN Page")
        self.setLayout(layout)
        self.tts = pyttsx3.init()

    def createLayout(self, parent):
        layout = QHBoxLayout()
        labels = ["Yes", "No"]
        buttons = []

        for i in range(len(labels)):
            button = ButtonContainer(labels[i], freqName=f"YN {i+1}")
            button.setObjectName(labels[i])
            layout.addWidget(button)
            buttons.append(button)

        buttons[0].clicked.connect(lambda: yesNoVoice(parent, buttons, buttons[0], "Yes"), self.tts)
        buttons[1].clicked.connect(lambda: yesNoVoice(parent, buttons, buttons[1], "No"), self.tts)

        return layout


def TTS(tts, text):
    tts.say(text)
    # tts.runAndWait()


def yesNoVoice(parent, buttons, selected, text, tts):
    disableOtherButtonsYN(parent, buttons, selected)
    TTS(tts, text)


# make the yn array of buttons single select + display selection input field
def disableOtherButtonsYN(parent, buttons, selected):
    # buttonClickNoise()

    inputField = parent.findChild(QLineEdit, "Input")

    if selected.isChecked():

        inputField.setText(selected.objectName())

        for button in buttons:
            if button != selected:
                button.setChecked(False)
    else:
        inputField.clear()
