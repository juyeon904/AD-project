class Action:

    def __init__(self):
        self.meal = 50
        self.clean = 50
        self.fatigue = 50


    def feeding(self, quantity):
        self.meal += (quantity / 10)
        return self.meal

    def washing(self):
        self.clean = 100
        return self.clean


    def sleeping(self):
        self.fatigue += 50
        return self.fatigue

    def endingLife(self):
        return true
