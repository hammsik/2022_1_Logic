import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB(self.scoredb, 'Name')

    def initUI(self):
        self.name = QLabel("Name :")
        self.age = QLabel("Age :")
        self.score = QLabel("Score :")
        self.amount = QLabel("Amount :")
        self.key = QLabel("Key :")
        self.result = QLabel("<Result>")

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.resultEdit = QTextEdit()
        self.keyEdit = QComboBox()
        self.keyEdit.addItem("Name")
        self.keyEdit.addItem("Age")
        self.keyEdit.addItem("Score")

        self.showB = QPushButton("Show")
        self.addB = QPushButton("Add")
        self.delB = QPushButton("Del")
        self.findB = QPushButton("Find")
        self.incB = QPushButton("Inc")


        self.showB.clicked.connect(self.showbuttonClicked)
        self.addB.clicked.connect(self.addbuttonClicked)
        self.delB.clicked.connect(self.delbuttonClicked)
        self.findB.clicked.connect(self.findbuttonClicked)
        self.incB.clicked.connect(self.incbuttonClicked)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.name)
        hbox1.addWidget(self.nameEdit)
        hbox1.addWidget(self.age)
        hbox1.addWidget(self.ageEdit)
        hbox1.addWidget(self.score)
        hbox1.addWidget(self.scoreEdit)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.result)
        hbox3.addStretch()
        hbox3.addWidget(self.key)
        hbox3.addWidget(self.keyEdit)
        hbox3.addWidget(self.showB)

        v1box = QVBoxLayout()
        v1box.addWidget(self.addB)
        v1box.addWidget(self.delB)
        v1box.addWidget(self.findB)
        v1box.addWidget(self.incB)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.resultEdit)
        hbox4.addLayout(v1box)

        hbox = QVBoxLayout()
        hbox.addLayout(hbox1)
        hbox.addLayout(hbox2)
        hbox.addLayout(hbox3)
        hbox.addLayout(hbox4)

        self.setLayout(hbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def showbuttonClicked(self):
        self.showScoreDB(self.scoredb, self.keyEdit.currentText())

    def addbuttonClicked(self):
        try:
            record = {"Name":self.nameEdit.text(), "Age":int(self.ageEdit.text()), "Score":int(self.scoreEdit.text())}
            self.scoredb += [record]
            self.showbuttonClicked()
        except:
            pass

    def delbuttonClicked(self):
        for p in self.scoredb[:]:
            if p['Name'] == self.nameEdit.text():
                self.scoredb.remove(p)
        self.showbuttonClicked()


    def findbuttonClicked(self):
        self.resultEdit.setPlainText('')
        for p in sorted(self.scoredb, key=lambda person: person[self.keyEdit.currentText()]):
            if p['Name'] == self.nameEdit.text():
                for attr in sorted(p):
                    self.resultEdit.insertPlainText(
                        attr + " = " + str(p[attr]) + ('\t\t' if type(p[attr]) == str and len(p[attr]) < 5 else '\t'))
                self.resultEdit.insertPlainText('\n')

    def incbuttonClicked(self):
        for p in self.scoredb:
            if p["Name"] == self.nameEdit.text():
                p['Score'] += int(self.amountEdit.text())
        self.showbuttonClicked()

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

    def showScoreDB(self, db, keyname):
        self.resultEdit.setPlainText('')
        for p in sorted(db, key = lambda person : person[keyname]):
            for attr in sorted(p):
                self.resultEdit.insertPlainText(attr + " = " + str(p[attr]) + ('\t\t' if type(p[attr]) == str and len(p[attr]) < 5 else '\t'))
            self.resultEdit.insertPlainText('\n')

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())