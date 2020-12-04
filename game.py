import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *  # 불러와야 하는 PyQt5 라이브러리 호출하기

from action import Action
from tamagotchi import Tamagotchi  # 불러와야 하는 함수들 객체로 생성하고 이름 부여하기


class Button(QToolButton):
    def __init__(self, text, callback):  # 초기화(생성자)
        super().__init__()  # 자식 클래스에서 부모 클래스의 생성자 호출하기 - 부모 클래스의 초기화 함수 수행
        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Preferred)  # 가로 크기 = sizeHint()가 최적의 크기, 그렇지만 줄거나 늘어날 수 있으며 공간이 더 있는 경우 사용할 수 있음(최소 크기 = minimumSizeHint()) + 세로 크기 = sizeHint()가 최적의 크기, 그렇지만 줄거나 늘어날 수 있음(최소 크기 = minimumSizeHint())
        self.setText(text)  # 버튼에 표시될 텍스트 설정하기
        self.clicked.connect(callback)  # 버튼이 클릭되면 메소드에 연결

    def sizeHint(self):  # 버튼의 사이즈 리턴하는 함수 정의하기
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 10)  # 버튼의 세로 크기 = height에 10픽셀 더한 값
        size.setWidth(max(size.width(), size.height()))  # 버튼의 가로 크기 = width와 height 중 더 큰 값
        return size  # 사이즈 리턴하기


class Game(QWidget):
    def __init__(self, parent=None):  # 초기화(생성자) - 게임이 시작될 때 초기 조건 설정하는 함수 정의하기
        super().__init__(parent)  # 자식 클래스에서 부모 클래스의 생성자 호출하기 - 부모 클래스의 초기화 함수 수행
        self.hunger = 50  # 초기 배고픔 수치 = 50으로 설정하기
        self.clean = 50  # 초기 청결 수치 = 50으로 설정하기
        self.tired = 50  # 초기 피로 수치 = 50으로 설정하기
        self.study_cnt = 0  # 초기 공부 횟수 = 0으로 설정하기
        self.age = 1  # 초기 나이 = 1살로 설정하기
        self.stress = 50  # 초기 스트레스 수치 = 50으로 설정하기
        self.all = 50  # 초기 종합 수치 = 50으로 설정하기
        self.face = "face_smile.png"  # 초기 다마고치의 표정 웃는 표정으로 설정하기
        self.endGame = False  # 게임 오버 되지 않았음을 나타내는 변수 설정하기
        self.startGame = True  # 게임이 시작되었음을 나타내는 변수 설정하기
        self.initUI()

    def initUI(
            self):  # 화면에 출력될 창들 만들고 위치 지정하기 - 나이, 이름, 행동(~하는 중), 표정, 버튼(먹이기, 씻기기, 재우기, 공부시키기, 놀아주기), 수치(종합, 배부름, 청결, 피로, 스트레스)
        self.setGeometry(500, 150, 800, 800)  # 창의 위치와 크기 조절 - (500, 150) 위치에 출력, 가로 800, 세로 800
        self.setWindowTitle('Tamagotchi')  # 창의 제목 설정 = 'Tamagotchi'

        self.vbox = QVBoxLayout()  # 수직 상자 정렬 레이아웃 만들기

        self.hbox0 = QHBoxLayout()  # 0번 수평 상자 정렬 레이아웃 만들기
        self.hbox0.addStretch(1)  # 공간 확보 위해 0번 수평 상자에 스트레치 요소 추가 - 위젯 앞에 공간 확보
        self.tama_label = QLabel('TAMAGOTCHI', self) # 타이틀 만들기
        font = self.tama_label.font()
        font.setPointSize(font.pointSize() + 15) # 폰트크기 크게
        font.setBold(True) # 폰트 굵게
        font.setFamily('Pixel') # 글씨체 변경
        self.tama_label.setFont(font) # 타이틀 폰트 설정
        #self.tama_label.setStyleSheet('color:white;') # 폰트색상
        self.hbox0.addWidget(self.tama_label) # 0번 수평 상자에 타이틀 표시하는 창 배치하기
        self.hbox0.addStretch(1) # 공간 확보 위해 0번 수평 상자에 스트레치 요소 추가 - 위젯 뒤에 공간 확보

        self.hbox1 = QHBoxLayout()  # 1번 수평 상자 정렬 레이아웃 만들기
        self.hbox1.addStretch(1)  # 공간 확보 위해 1번 수평 상자에 스트레치 요소 추가 - 위젯 앞에 공간 확보
        self.age_output = QLineEdit(self)  # 나이(QLineEdit 객체)를 표시할 칸 만들기
        self.age_output.setReadOnly(True)  # 나이 창에 입력이 불가능하도록 만들기 - 프로그램 수행 결과만 출력되게끔 만들기
        self.age_output.setFixedWidth(20)  # 나이 창의 크기 20픽셀로 고정하기
        self.age_output.setText(str(self.age))  # 나이 창에 age 값 출력하기
        self.age_output.setAlignment(Qt.AlignHCenter) # 텍스트 가운데 정렬
        self.age_label2 = QLabel('살 ', self)  # 나이 단위 위젯 만들기
        self.hbox1.addWidget(self.age_output)  # 1번 수평 상자에 나이 표시하는 창 배치하기
        self.hbox1.addWidget(self.age_label2)  # 1번 수평 상자에(나이 표시하는 창 옆에) 나이 단위(' 살') 배치하기

        self.name_text = QLineEdit(self)  # 이름(QLineEdit 객체)를 표시할 칸 만들기
        self.name_text.setReadOnly(True)  # 이름 창에 입력이 불가능하도록 만들기 - 프로그램 처음에 실행할 때 입력한 이름만 출력되게끔 만들기
        self.name_text.setFixedWidth(80)  # 이름 창의 크기 80픽셀로 고정하기
        self.name_text.setAlignment(Qt.AlignHCenter) # 텍스트 가운데 정렬
        self.hbox1.addWidget(self.name_text)  # 1번 수평 상자에(나이 단위 옆에) 이름 표시하는 창 배치하기
        self.hbox1.addWidget(QLabel('은/는 '))  # 1번 수평 상자에(이름 표시하는 창 옆에) 조사(' 은/는 ') 배치하기

        self.status_text = QLineEdit()  # 상태(QLineEdit 객체)를 표시할 칸 만들기
        self.status_text.setReadOnly(True)  # 상태 창에 입력이 불가능하도록 만들기 - 프로그램 수행 결과만 출력되게끔 만들기
        self.status_text.setFixedWidth(80)  # 이름 창의 크기 80픽셀로 고정하기
        self.status_text.setAlignment(Qt.AlignHCenter) # 텍스트 가운데 정렬
        self.hbox1.addWidget(self.status_text)  # 1번 수평 상자에(조사 옆에) 상태 표시하는 창 배치하기
        self.hbox1.addStretch(1)  # 공간 확보 위해 1번 수평 상자에 스트레치 요소 추가 - 위젯 뒤에 공간 확보, 위젯 가운데 정렬

        self.hbox2 = QHBoxLayout()  # 2번 수평 상자 정렬 레이아웃 만들기
        self.hbox2.addStretch(1)  # 공간 확보 위해 2번 수평 상자에 스트레치 요소 추가 - 위젯 앞에 공간 확보
        self.character_text = QLabel()  # 다마고치의 표정이 들어갈 공간 확보하기
        self.hbox2.addWidget(self.character_text)  # 2번 수평 상자에 다마고치의 표정 표시하는 창 배치하기
        self.hbox2.addStretch(1)  # 공간 확보 위해 2번 수평 상자에 스트레치 요소 추가 - 위젯 뒤에 공간 확보, 위젯 가운데 정렬
        self.character_text.setPixmap(QPixmap(self.face))  # 창에 다마고치의 표정 이미지 나타내기

        self.hbox3 = QHBoxLayout()  # 3번 수평 상자 정렬 레이아웃 만들기
        self.hbox3.addStretch(1)  # 공간 확보 위해 3번 수평 상자에 스트레치 요소 추가 - 위젯 앞에 공간 확보
        self.hbox3.addWidget(QLabel('밥의 양 : '))  # 3번 수평 상자에 텍스트('밥의 양 : ') 배치하기
        self.feed_edit = QLineEdit('0')  # 밥을 얼마나 줄 것인지 텍스트 입력 가능하게 만들기, 디폴트 값 0
        self.feed_edit.setFixedWidth(90)  # 밥의 양 나타내는 창의 크기 90픽셀로 고정하기
        self.feed_edit.setAlignment(Qt.AlignRight) # 텍스트 우측정렬
        self.hbox3.addWidget(self.feed_edit)  # 3번 수평 상자에(텍스트 옆에) 밥의 양 나타내는 창 배치하기

        buttonGroups = ['먹이기', '씻기기', '재우기', '공부시키기', '놀아주기']  # 버튼을 그룹으로 묶기 - 뒤에 나오는 버튼 생성 코드의 반복 개선 위해 사용할 것
        for btnText in buttonGroups:  # 버튼 생성 코드의 반복 개선 - 반복문 사용해 동일(유사)한 코드를 연속해서 쓰는 것 개선
            button = Button(btnText, self.button_clicked)
            button.setFixedWidth(120)  # 버튼의 크기 고정 - 120픽셀
            self.hbox3.addWidget(button)  # 2번 수평 상자에 새로 생성한 버튼 위젯 추가
        self.hbox3.addStretch(1)  # 공간 확보 위해 3번 수평 상자에 스트레치 요소 추가 - 위젯 뒤에 공간 확보, 버튼 위젯 가운데 정렬

        self.hbox4 = QHBoxLayout()  # 4번 수평 상자 정렬 레이아웃 만들기
        self.hbox5 = QHBoxLayout()  # 5번 수평 상자 정렬 레이아웃 만들기
        self.hbox6 = QHBoxLayout()  # 6번 수평 상자 정렬 레이아웃 만들기
        self.hbox7 = QHBoxLayout()  # 7번 수평 상자 정렬 레이아웃 만들기
        self.hbox8 = QHBoxLayout()  # 8번 수평 상자 정렬 레이아웃 만들기

        self.all_text = QLineEdit()  # 종합 수치(QLineEdit 객체)를 표시할 칸 만들기
        self.hunger_text = QLineEdit()  # 배고픔 수치(QLineEdit 객체)를 표시할 칸 만들기
        self.clean_text = QLineEdit()  # 청결 수치(QLineEdit 객체)를 표시할 칸 만들기
        self.tired_text = QLineEdit()  # 피로 수치(QLineEdit 객체)를 표시할 칸 만들기
        self.stress_text = QLineEdit()  # 스트레스 수치(QLineEdit 객체)를 표시할 칸 만들기

        self.action = Action()  # action 객체 호출하기
        self.tamagotchi = Tamagotchi()  # tamagotchi 객체 호출하기

        # 수평 상자, 텍스트, 상태 수치를 각각 그룹으로 묶기 - 뒤에 나오는 버튼 생성 코드의 반복 개선 위해 사용할 것
        layoutGroups = [self.hbox0, self.hbox1, self.hbox2, self.hbox3, self.hbox4, self.hbox5, self.hbox6,
                        self.hbox7, self.hbox8]
        gaugeGroups = ['종     합', '배 부 름', '청     결', '피     로', '스트레스']
        textGroups = [self.all_text, self.hunger_text, self.clean_text, self.tired_text, self.stress_text]
        valueGroups = [self.action.currentAll, self.action.currentHunger, self.action.currentClean,
                       self.action.currentTired, self.action.currentStress]

        for i in range(len(gaugeGroups)):
            # 반복문 사용해 동일(유사) 코드의 반복 방지 - 다마고치의 상태(종합, 배부름, 청결, 피로, 스트레스) 나타내는 창 배치하기, 폰트 사이즈변경
            layoutGroups[i + 4].addWidget(QLabel(gaugeGroups[i]))
            textGroups[i].setReadOnly(True)
            layoutGroups[i + 4].addWidget(textGroups[i])
            textGroups[i].setText(valueGroups[i])
            font = textGroups[i].font()
            font.setPointSize(font.pointSize() - 1)
            textGroups[i].setFont(font)
            textGroups[i].setFixedWidth(730)

        for hbox in layoutGroups:  # 수평 상자 레이아웃을 수직 상자 레이아웃 안으로 배치 - 반복문 사용해 동일(유사) 코드의 반복 방지
            self.vbox.addLayout(hbox)
        self.setLayout(self.vbox)  # 최종적으로 수직 상자를 창의 메인 레이아웃으로 설정하기

        if self.startGame == True:  # 게임이 시작되었을 경우에 수행될 작업 설정하기
            self.nameInput()  # 다마고치의 이름 정하는 함수 호출하기
        if self.startGame == False: # 다마고치의 이름을 정하지 않았다면 다시 초기화면으로
            self.nameInput()

        self.show()

    def button_clicked(self):  # 버튼이 눌렸을 때 의도한 명령 수행하게 하는 함수 정의하기
        key = self.sender().text()  # sender 메소드 호출해 신호 소스 결정 - 현재 눌려진 버튼을 key에 저장

        if key == '먹이기':  # 밥 주기('먹이기') 버튼이 눌린 경우
            # 배부름 게이지바 업데이트
            try:
                food = int(self.feed_edit.text())  # 입력한 밥의 양을 int로 바꾸기
                self.hunger_text.setText(self.action.feeding(food))  # 입력한 밥의 양만큼 배부름 수치 증가시키기
                self.feed_edit.clear()  # 입력한 값을 지우고 다시 빈 칸 출력하기
                self.clean_text.setText(self.action.washing(-10))
                self.tired_text.setText(self.action.sleeping(-10))  # 한 번 밥을 줄 때마다 청결 수치 10씩 감소시키고 피로 수치 10씩 증가시키기
                self.status_text.setText("먹는 중~")  # 상태 창에 '먹는 중~' 출력하기
            except:
                self.feed_edit.setText("Error!")  # 의도한 것과 다른 값이 입력되는 경우 에러 띄우기


        elif key == '씻기기':  # 씻기기 버튼이 눌린 경우
            # 청결 게이지바 업데이트
            self.clean_text.setText(self.action.washing(100))  # 청결 수치 100으로 만들기
            self.hunger_text.setText(self.action.feeding(-10))
            self.tired_text.setText(self.action.sleeping(-10))  # 한 번 씻길 때마다 배부름 수치 10씩 감소시키고 피로 수치 10씩 증가시키기
            self.status_text.setText("씻는 중~")  # 상태 창에 '씻는 중~' 출력하기

        elif key == '재우기':  # 재우기 버튼이 눌린 경우
            # 피로 게이지바 업데이트
            self.tired_text.setText(self.action.sleeping(50))
            self.hunger_text.setText(self.action.feeding(-10))
            self.clean_text.setText(self.action.washing(-10))  # 한 번 재울 때마다 피로 수치 50씩 감소시키고 배부름 수치와 청결 수치 10씩 감소시키기
            self.status_text.setText("자는 중~")  # 상태 창에 '자는 중~' 출력하기

        elif key == '공부시키기':  # 공부시키기 버튼이 눌린 경우
            # 스트레스 게이지바 업데이트
            self.stress_text.setText(self.action.studying())
            self.hunger_text.setText(self.action.feeding(-10))
            self.clean_text.setText(self.action.washing(-10))
            self.tired_text.setText(
                self.action.sleeping(-10))  # 한 번 공부시킬 때마다 스트레스 수치 정해진 만큼 증가시키고 배부름 수치와 청결 수치 10씩 감소, 피로 수치 10씩 증가시키기
            self.status_text.setText("공부 중~")  # 상태 창에 '공부 중~' 출력하기
            self.age = self.tamagotchi.ageCount(
                self.action.study_cnt)  # 공부를 5의 배수만큼(5번, 10번, 15번, ...) 할 때마다 나이를 한 살씩 증가시키기
            self.age_output.setText(str(self.age))  # 변화된 나이 값을 화면의 나이 값 나타내는 창에 출력하기

        elif key == '놀아주기':  # 놀아주기 버튼이 눌린 경우
            # 스트레스 게이지바 업데이트
            self.stress_text.setText(self.action.playing())
            self.hunger_text.setText(self.action.feeding(-10))
            self.clean_text.setText(self.action.washing(-10))
            self.tired_text.setText(
                self.action.sleeping(-10))  # 한 번 공부시킬 때마다 스트레스 수치 정해진 만큼 감소시키고 배부름 수치와 청결 수치 10씩 감소, 피로 수치 10씩 증가시키기
            self.status_text.setText("노는 중~")  # 상태 창에 '노는 중~' 출력하기

        self.action.all_gauge()
        self.all_text.setText(self.action.currentAll)  # 종합 수치 나타내기
        self.face = self.tamagotchi.faceChange(self.action.all)  # 종합 수치에 따라서 다마고치의 표정 선택하기
        self.character_text.setPixmap(QPixmap(self.face))  # 선택된 다마고치의 표정을 화면의 다마고치 표정 나타내는 창에 출력하기
        self.end = self.action.endGame

        # 게임 오버 조건 만족하면 게임 오버
        if self.end == True:
            self.endingLife()
        # 5살 되면 게임 클리어
        if self.age == 5:
            self.clearGame()

    # 게임 오버 메세지 창
    def endingLife(self):
        QMessageBox.about(self, 'GAME OVER!', 'Game Over,,, 너 때문이야,,,༼ つ ◕_◕ ༽つ༼ つ ◕_◕ ༽つ')

    # 게임 클리어 메세지 창
    def clearGame(self):
        QMessageBox.about(self, 'GAME CLEAR!', "키워주셔서 감사합니다 ٩(*´∀`*)۶" + '\n' + "이제 저는 저 넓은 세상 밖으로 나갈 거에요! 신난다!")

    def nameInput(self):  # 게임이 시작되었을 때 다마고치의 이름 정하는 함수 정의하기
        # 주의사항 메세지 창 생성
        QMessageBox.about(self, '♡ C A U T I O N ♡',
                          '1. 이름은 네 글자 이하로 입력해 주세요!' + '\n' + '2. 밥은 입력한 만큼 퍼센티지로 반영됩니다!' + '\n' + '      ( ex. 30 g -> 30 % )')
        name, ok = QInputDialog.getText(self, 'INPUT NAME', '♡✧。°₊·다마고치의 이름은‧₊°。✧♡')

        if ok == True:  # ok 버튼이 눌린 경우에 수행할 작업 정의하기
            if len(str(name)) == 0 or len(str(name)) > 4:  # 이름을 입력하지 않거나 이름의 길이가 4자를 초과할 경우 수행할 작업 정의하기
                self.name_text.setText('다마고치')  # 이름을 기본값인 '다마고치'로 설정
            else:
                self.name_text.setText(str(name))  # 입력한 텍스트를 다마고치의 이름으로 정하고 name에 넣기
        else:
            self.startGame = False # 게임을 스타트하지 못하도록 함


if __name__ == '__main__':
    app = QApplication(sys.argv)

    fontDB = QFontDatabase()
    fontDB.addApplicationFont('./1훈떡볶이 R.ttf')
    app.setFont(QFont('1훈떡볶이 R')) #폰트 변경

    ex = Game()
    sys.exit(app.exec_())  # app 통해 exec_() 메서드 호출 - 이벤트 루프에 진입, 무한 반복하며 이벤트 처리(해당 윈도우가 계속 화면 상에 나타나 있을 수 있게 함)