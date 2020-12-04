from PyQt5.QtWidgets import QMessageBox #불러와야 하는 PyQt5 라이브러리 호출하기

class Action:

    def __init__(self): #초기화(생성자) - 초기 수치 설정
        self.hunger = 50 #초기 배고픔 수치 = 50으로 설정하기
        self.clean = 50 #초기 청결 수치 = 50으로 설정하기
        self.tired = 50 #초기 피로 수치 = 50으로 설정하기
        self.study_cnt = 0 #초기 공부 횟수 = 0으로 설정하기
        self.age = 1 #초기 나이 = 1살로 설정하기
        self.stress = 50 #초기 스트레스 수치 = 50으로 설정하기
        self.all = 50 #초기 종합 수치 = 50으로 설정하기
        self.endGame = False #게임 오버 되지 않았음을 나타내는 변수 설정하기

        # 해당 수치만큼 각각 "■" 상태창에 출력하기, 가독성을 위해 "■" 1개 당 2.5%의 가중치를 갖음
        self.currentHunger = "■" * int(self.hunger / 2.5) + str(self.hunger) + "%"
        self.currentClean = "■" * int(self.clean / 2.5) + str(self.clean) + "%"
        self.currentTired = "■" * int(self.tired / 2.5) + str(self.tired) + "%"
        self.currentStress = "■" * int(self.stress / 2.5) + str(self.stress) + "%"
        self.currentAll = "■" * int(self.all / 2.5) + str(self.all) + "%"

    def feeding(self, food): #밥 먹이는 함수 정의하기
        if (self.hunger + food <= 100 and self.hunger + food >= 0):
            self.hunger += food #현재 배고픔 수치에 입력한 값을 더한 결과가 0 이상 100 이하일 경우에만 제대로 밥을 먹은 것으로 인정
        else:
            self.endGame = True #배고픔 수치가 0 미만이나 100 초과가 될 경우 게임 오버
        self.currentHunger = "■" * int(self.hunger / 2.5) + str(self.hunger) + "%" #배고픔 수치 업데이트하기

        return self.currentHunger #배고픔 수치 업데이트하기

    def washing(self, wash): #씻기는 함수 정의하기
        if (self.clean + int(wash) < 0):
            self.endGame = True #청결 수치가 0 미만일 경우 게임 오버
        elif (self.clean + int(wash) >= 100):
            self.clean = 100 #위의 조건을 만족하지 않을 경우에만 제대로 씻은 것으로 인정
        else:
            self.clean += int(wash)
        self.currentClean = "■" * int(self.clean / 2.5) + str(self.clean) + "%"

        return self.currentClean #청결 수치 업데이트하기

    def sleeping(self, sleep): #재우는 함수 정의하기
        if (self.tired - int(sleep) > 100):
            self.endGame = True #피로 수치가 100 초과일 경우 게임 오버
        elif (self.tired - int(sleep) <= 0):
            self.tired = 0 #현재 피로 수치에 50을 뺀 값이 0 이하일 경우 피로 수치 0으로 설정하기
        else:
            self.tired -= int(sleep) #위의 조건들 만족하지 않은 경우 현재 피로 수치에 50을 뺀 값을 새로운 피로 수치로 설정하기
        self.currentTired = "■" * int(self.tired / 2.5) + str(self.tired) + "%"

        return self.currentTired #피로 수치 업데이트하기

    def studying(self): #공부시키는 함수 정의하기
        self.study_cnt += 1  # 공부 횟수 카운팅

        # 스트레스 게이지바 업데이트
        if (self.stress + 30 > 100):
            self.endGame = True #현재 스트레스 수치가 70 초과인 경우 공부시키기 버튼을 누르면 게임 오버
        else:
            self.stress += 30 #위의 조건 만족하지 않을 경우 현재 스트레스 수치에 30을 더한 값을 새로운 스트레스 수치로 설정하기
            self.currentStress = "■" * int(self.stress / 2.5) + str(self.stress) + "%"

        return self.currentStress #스트레스 수치 업데이트하기

    def playing(self): #놀아주는 함수 정의하기
        if (self.stress - 15 <= 0):
            self.endGame = True #현재 스트레스 수치가 15 이하인 경우 놀아주기 버튼을 누르면 게임 오버
        else:
            self.stress -= 15 #위의 조건 만족하지 않을 경우 현재 스트레스 수치에 15를 뺀 값을 새로운 스트레스 수치로 설정하기
        self.currentStress = "■" * int(self.stress / 2.5) + str(self.stress) + "%"

        return self.currentStress #스트레스 수치 업데이트하기

    def all_gauge(self): #종합 수치 함수 정의하기
        if ((self.hunger + self.clean < 60) or (self.tired + self.stress >= 140)):
            if (self.all - 10 <= 0):
                self.all = 0
            else:
                self.all -= 10 #배고픔과 청결 수치의 합이 60 미만이거나 피로와 스트레스 수치의 합이 140 이상인 경우 종합 수치가 10 이하면 종합 수치 0으로, 10 초과면 현재 종합 수치에 10을 뺀 값을 새로운 종합 수치로 설정하기
        if ((self.hunger + self.clean >= 140) or (self.tired + self.stress < 60)):
            if (self.all + 10 >= 100):
                self.all = 100
            else:
                self.all += 10 #배고픔과 청결 수치의 합이 140 이상이거나 피로와 스트레스 수치의 합이 60 미만인 경우 종합 수치가 90 이상이면 종합 수치 100으로, 90 미만이면 현재 종합 수치에 10을 더한 값을 새로운 종합 수치로 설정하기
        self.currentAll = "■" * int(self.all / 2.5) + str(self.all) + "%" #종합 수치 업데이트 하기
        if (self.all < 0):
            self.endGame = True #종합 수치가 0 미만일 경우 게임 오버
