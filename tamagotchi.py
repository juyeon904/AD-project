class Tamagotchi:

    def __init__(self):
        self.face = "face_smile.png"
        self.age = 1

    def faceChange(self, all):
        if all <= 30:
            self.face = "face_sad.png"
        elif all <= 60:
            self.face = "face_smile.png"
        elif all <= 90:
            self.face = "face_wink.png"
        else:
            self.face = "face_kiss.png"

        return self.face

    def ageCount(self, study_cnt):
        if study_cnt % 5 == 0:
            self.age += 1
        return self.age
