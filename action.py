class Action:


    def feeding(self, quantity):
        if (self.hunger + int(self.feed_edit.text()) >= 100):
            self.hunger = 100
            self.hunger_text.setText("■" * (self.hunger) + str(self.hunger) + "%")
            self.status_text.setText("먹는중~")
            self.feed_edit.clear()
        else:
            self.hunger += int(self.feed_edit.text())
            self.hunger_text.setText("■" * (self.hunger) + str(self.hunger) + "%")
            self.status_text.setText("먹는중~")
            self.feed_edit.clear()

        # 배부름 게이지를 종합 게이지에 반영
        if (self.hunger >= 70):
            if (self.all + 10 >= 100):
                self.all = 100
                self.all_text.setText("■" * (self.all) + str(self.all) + "%")
            else:
                self.all += 10
                self.all_text.setText("■" * (self.all) + str(self.all) + "%")
        elif (self.hunger < 30):
            if (self.all - 10 >= 100):
                self.all = 100
                self.all_text.setText("■" * (self.all) + str(self.all) + "%")
            else:
                self.all -= 10
                self.all_text.setText("■" * (self.all) + str(self.all) + "%")

    def washing(self):
        self.clean = 100
        return self.clean


    def sleeping(self):
        self.fatigue = self.fatigue + 50
        return self.fatigue

    def endingLife(self):
        return true
