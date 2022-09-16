import sys
import socketio
from PyQt5.QtCore import center, Qt

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow, QStackedWidget

from UI.MainWidget.mainWidget import MainWidget

from UI.styles import windowStyle

from UI.Components.button_container import buttonClickNoise

import threading
import time

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        #TODO: fix server comm integration
        # SocketIO connection
        # self.connected = False
        # self.sio = socketio.Client()
        # try:
        #     self.sio.connect('http://127.0.0.1:5000')
        #     print("Connected")
        #     self.connected = True
        # except socketio.exceptions.ConnectionError as err:
        #     print("ConnectionError:", err)

        self.generalLayout = QVBoxLayout()
        self.generalLayout.setAlignment(Qt.AlignCenter)

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

         # Make sure to pass in 'self' to the child widget for it to access parent to for methods and children
        self.mainWidget = MainWidget(self)

        self.setWindowTitle('Main Window')  # Sets name of window
        # Adds central widget where we are going to do most of our work
        self.setCentralWidget(self.homePage)
        self.setGeometry(0, 0, 1600, 900)

    #TODO: fix server comm integration
    # def emit_message(self, message, data):
    #     if self.connected:
    #         self.sio.emit(message, data)
    #     else:
    #         print('Not connected to server')



def stimOnsetOffset():
    mainStack = window.mainWidget.findChild(QStackedWidget,"Main Widget")
    
    while True:
        if stopThread:
            print("exiting stim controller thread")
            break
        
        time.sleep(2)
        print("ding")

if __name__ == '__main__':
    buttonClickNoise()
    app = QApplication(sys.argv)
    global window
    window = Window()
    window.setStyleSheet(windowStyle)

    global stopThread
    stopThread = False
    x = threading.Thread(target=stimOnsetOffset)
    x.start()

    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        stopThread = True
        print('Closing Window...')
