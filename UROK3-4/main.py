import random
class student:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True
    def to_study(self):
        print("Навчання... speedrun to 12 балів поїхали")
        self.pgrogress+=0.12
        self.gladness-=3
    def to_sleep(self):
        print("Спання... Zzz...")
        self.gladness+=3
    def to_chill(self):
        print("Відпочивання... іграєм в бравл старс")
        self.gladness+=5
        self.progress-=0.1
    def is_alive(self):
        if self.progress<-0.5:
            print("Ви не попали в туалет вчасно і тепер весь дитячий садочок смердить.Вас вигнали з дитячого садочку за це((")
            self.alive=False
        elif self.gladness<=0:
            print("Ви стали дед інсайдом((")
            self.alive=False
        elif self.progress > 5:
            print("Ви стали самим крутим карапузом в дитячому садочку і переходите в перший клас раніше інших 😎😎, але, по дорозі додому, впали в туалет, і, втопились там...")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")
    def live(self):
        day = "Day" + str(day) + "of" + self.name + "Life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
        nick = Student(name="Nick")
        for day in range(365):
            if nick.alive == False:
                break
            nick.live(day)