import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self) :
        name = QLabel("Name :")
        age = QLabel("Age :")
        score = QLabel("Score :")
        amount = QLabel("Amount :")
        key = QLabel("Key :")
        result = QLabel("<Result>")
        addB = QPushButton("Add")
        delB = QPushButton("Del")
        findB = QPushButton("Find")
        lncB = QPushButton("lnc")
        showB = QPushButton("Show")


        nameEdit = QLineEdit()
        ageEdit = QLineEdit()
        scoreEdit = QLineEdit()
        amountEdit = QLineEdit()
        resultEdit = QTextEdit()
        keyEdit = QComboBox()

        grid = QGridLayout()
        #grid.setSpacing()

        grid.addWidget(name, 1, 0)
        grid.addWidget(nameEdit, 1, 1)

        grid.addWidget(age, 1, 2)
        grid.addWidget(ageEdit, 1, 3)

        grid.addWidget(score, 1, 4)
        grid.addWidget(scoreEdit, 1, 5)

        grid.addWidget(amount, 2, 0)
        grid.addWidget(amountEdit, 2, 1)

        grid.addWidget(key, 3, 4)
        grid.addWidget(keyEdit, 3, 5)

        grid.addWidget(result, 3, 0)
        grid.addWidget(resultEdit, 4, 0, 6, 5)

        grid.addWidget(addB, 4, 5)
        grid.addWidget(delB, 5, 5)
        grid.addWidget(findB, 6, 5)
        grid.addWidget(lncB, 7, 5)
        grid.addWidget(showB, 8, 5)

        self.setLayout(grid)

        self.setGeometry(300, 300, 500, 600)
        self.setWindowTitle('Assignment6')

        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())