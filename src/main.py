import sys, os

THIS_PATH = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

sys.path.append(THIS_PATH)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QFrame, QScrollArea
from PyQt5.QtCore import pyqtSlot, Qt
import string

import methods_main

class Azerparse(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        #syncat lookup related UI things
        self.lookup_button = QPushButton('Lookup', self)
        self.lookup_button.resize(self.lookup_button.sizeHint())
        self.lookup_button.move(20, 50)
        self.lookup_button.clicked.connect(self.on_lookup_button_click)
        
        self.lookup_entry_box = QLineEdit(self)
        self.lookup_entry_box.move(20, 20)
        self.lookup_entry_box.resize(400, 25)

        self.lookup_result_label = QLabel(self)
        self.lookup_result_label.setFrameStyle(QFrame.Sunken)
        self.lookup_result_label.setText('Enter a query and press Lookup')
        self.lookup_result_label.resize(700, 100)
        self.lookup_result_label.setStyleSheet("font: 12pt sans-serif")

        self.result_scrollarea = QScrollArea(self)
        self.result_scrollarea.setWidget(self.lookup_result_label)
        self.result_scrollarea.setSizeAdjustPolicy(QScrollArea.AdjustToContents)
        self.result_scrollarea.setFixedHeight(400)
        self.result_scrollarea.move(100, 100)

        self.resize(900, 600)
        self.setWindowTitle('Azerparse')    
        self.show()

    @pyqtSlot()
    def on_lookup_button_click(self):
        user_input = self.lookup_entry_box.text()
        user_input = user_input.strip()
        query_list = user_input.split(' ')

        output_str = ''

        for query in query_list:
            output_str += (' ##########\t' + query + '\t########## \n\n')
            single_output = methods_main.process_word(query)
            output_str += single_output
            output_str += '\n\n'

        self.lookup_result_label.setText(output_str)
        self.lookup_result_label.adjustSize()
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    azerparse = Azerparse()
    sys.exit(app.exec_())