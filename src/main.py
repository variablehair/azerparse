import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QFrame
from PyQt5.QtCore import pyqtSlot, Qt

from lexicon.getsyncat import getsyncat

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
        self.lookup_entry_box.resize(150, 25)

        self.lookup_result_label = QLabel(self)
        self.lookup_result_label.setFrameStyle(QFrame.Sunken)
        self.lookup_result_label.resize(400, 35)
        self.lookup_result_label.move(0, 100)
        self.lookup_result_label.setText('Enter a query and press Lookup')
        self.lookup_result_label.setAlignment(Qt.AlignCenter)
        self.lookup_result_label.setStyleSheet("font: 12pt sans-serif")

        self.resize(400, 200)
        self.setWindowTitle('Azerparse')    
        self.show()

    @pyqtSlot()
    def on_lookup_button_click(self):
        query = self.lookup_entry_box.text().upper()
        result = str(getsyncat(query))
        self.lookup_result_label.setText(result)
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    azerparse = Azerparse()
    sys.exit(app.exec_())