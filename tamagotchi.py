class Tamagotchi: #다마고치 표정 + 나이 설정하기

    def __init__(self): #초기화(생성자) - 기본 표정 + 나이 설정
        self.face = "face_smile.png" #기본 표정 = 웃는 표정
        self.age = 1 #기본 나이 = 1살

    def faceChange(self, all): #표정이 바뀌는 경우 설정
        if all <= 30: #종합 수치가 30 이하인 경우
            self.face = "face_sad.png" #슬픈 표정으로 바뀌기
        elif all <= 60: #종합 수치가 30 초과 60 이하인 경우
            self.face = "face_smile.png" #다시 웃는 표정으로 복귀
        elif all <= 90: #종합 수치가 60 초과 90 이하인 경우
            self.face = "face_wink.png" #윙크하는 표정으로 바뀌기
        else: #종합 수치가 90 초과 100 이하인 경우
            self.face = "face_kiss.png" #뽀뽀하는 표정으로 바뀌기

        return self.face #다마고치의 표정 리턴인자로 돌려주기

    def ageCount(self, study_cnt): #나이 먹는 조건 설정
        if study_cnt % 5 == 0: #5번, 10번, 15번... 이 될 때마다 나이를 먹게 되므로 5의 배수인 경우로 조건 설정
            self.age += 1 #나이를 한 살 추가하기

        return self.age #다마고치의 나이를 리턴인자로 돌려주기