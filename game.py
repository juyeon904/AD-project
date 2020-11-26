import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from action import Action
from tamagotchi import Tamagotchi

class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class Game(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.hunger = 50
        self.clean = 50
        self.tired = 50
        self.study_cnt = 0
        self.age = 1
        self.stress = 50
        self.all = 50
        self.face = "face_smile.png"

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 200, 1340, 700)
        self.setWindowTitle('Tamagotchi')

        self.vbox = QVBoxLayout()

        self.hbox0 = QHBoxLayout()
        self.hbox0.addWidget(QLabel(' 지금은 '))
        self.status_text = QLineEdit()
        self.status_text.setReadOnly(True)
        self.hbox0.addWidget(self.status_text)
        self.hbox0.addStretch(1)

        self.age_label = QLabel('나이 : ', self)
        self.age_output = QLineEdit(self)
        self.age_output.setReadOnly(True)
        self.age_output.resize(30, 30)
        self.age_output.setText(str(self.age))
        self.hbox0.addWidget(self.age_label)
        self.hbox0.addWidget(self.age_output)
        self.hbox0.addStretch(1)

        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(QLabel('다마고치'))
        self.hbox1.addStretch(1)
        self.character_text = QLabel()
        self.hbox1.addWidget(self.character_text)
        self.hbox1.addStretch(1)
        self.character_text.setPixmap(QPixmap(self.face))

        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(QLabel('밥 주 기 '))
        self.feed_edit = QLineEdit()
        self.hbox2.addWidget(self.feed_edit)
        feedButton = Button(' 입력 ', self.button_clicked)
        self.hbox2.addWidget(feedButton)
        self.hbox2.addWidget(feedButton)
        self.hbox2.addStretch(1)

        buttonGroups = ['  씻기기  ', '  재우기  ', '공부시키기', ' 놀아주기 ']
        for btnText in buttonGroups :
            button = Button(btnText, self.button_clicked)
            self.hbox2.addWidget(button)

        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()
        self.hbox7 = QHBoxLayout()

        self.all_text = QLineEdit()
        self.hunger_text = QLineEdit()
        self.clean_text = QLineEdit()
        self.tired_text = QLineEdit()
        self.stress_text = QLineEdit()

        self.action = Action()
        self.tamagotchi = Tamagotchi()

        layoutGroups = [self.hbox0, self.hbox1, self.hbox2, self.hbox3, self.hbox4, self.hbox5, self.hbox6, self.hbox7]
        gaugeGroups = ['종     합 ', '배 부 름 ', '청     결 ', '피     로 ', '스트레스']
        textGroups = [self.all_text, self.hunger_text, self.clean_text, self.tired_text, self.stress_text]
        valueGroups = [self.action.currentAll, self.action.currentHunger, self.action.currentClean,
                       self.action.currentTired, self.action.currentStress]

        for i in range(len(gaugeGroups)) :
            layoutGroups[i+3].addWidget(QLabel(gaugeGroups[i]))
            textGroups[i].setReadOnly(True)
            layoutGroups[i+3].addWidget(textGroups[i])
            textGroups[i].setText(valueGroups[i])

        for hbox in layoutGroups:
            self.vbox.addLayout(hbox)
        self.setLayout(self.vbox)

        self.show()

    def button_clicked(self):
        key = self.sender().text()

        if key == ' 입력 ':
            # 배부름 게이지바 업데이트
            try:
                food = int(self.feed_edit.text())
                self.hunger_text.setText(self.action.feeding(food))
                self.feed_edit.clear()
                self.clean_text.setText(self.action.washing(-10))
                self.tired_text.setText(self.action.sleeping(-10))
                self.status_text.setText("먹는 중~")
            except:
                self.feed_edit.setText("Error!")


        elif key == '  씻기기  ':
            # 청결 게이지바 업데이트
            self.clean_text.setText(self.action.washing(100))
            self.hunger_text.setText(self.action.feeding(-10))
            self.tired_text.setText(self.action.sleeping(-10))
            self.status_text.setText("씻는 중~")

        elif key == '  재우기  ':
            # 피로 게이지바 업데이트
            self.tired_text.setText(self.action.sleeping(50))
            self.hunger_text.setText(self.action.feeding(-10))
            self.clean_text.setText(self.action.washing(-10))
            self.status_text.setText("자는 중~")

        elif key == '공부시키기':
            # 스트레스 게이지바 업데이트
            self.stress_text.setText(self.action.studying())
            self.hunger_text.setText(self.action.feeding(-10))
            self.clean_text.setText(self.action.washing(-10))
            self.tired_text.setText(self.action.sleeping(-10))
            self.status_text.setText("공부 중~")
            self.age = self.tamagotchi.ageCount(self.action.study_cnt)
            self.age_output.setText(str(self.age))

        elif key == ' 놀아주기 ':
            # 스트레스 게이지바 업데이트
            self.stress_text.setText(self.action.playing())
            self.hunger_text.setText(self.action.feeding(-10))
            self.clean_text.setText(self.action.washing(-10))
            self.tired_text.setText(self.action.sleeping(-10))
            self.status_text.setText("노는 중~")

        self.action.all_gauge()
        self.all_text.setText(self.action.currentAll)
        self.face = self.tamagotchi.faceChange(self.action.all)
        self.character_text.setPixmap(QPixmap(self.face))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game()
    sys.exit(app.exec_())
