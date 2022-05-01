import random
class student:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=5
        self.hunger=50
        self.alive=True
    def to_eat(self):
        self.progress-=0.2
        self.gladness+=5
        self.hunger+=30
    def to_have_a_shower(self):
        print("Пора би помитись, ато смердить від мене капец")
        self.progress-=0.2
        self.gladness+=5
    def to_go_to_toilet(self):
        print("Щось в туалет захотілось")
        self.progress -= 0.5
        self.gladness += 7
        self.hunger-=3
    def to_study(self):
        print("Навчання... speedrun to 12 балів поїхали")
        self.progress+=0.12
        self.gladness-=3
        self.hunger-=2
    def go_for_a_walk(self):
        print("Підем погуляєм, чи шо")
        self.gladness+=5
        self.progress-=1
        self.hunger+=1
    def to_play(self):
        print("Іграєм в роблокс адопт мі, поїхали скамити всіх на петів")
        self.progress-=0.12
        self.gladness+=5
        self.hunger-=3
    def to_sleep(self):
        print("Поспимо... *чути хропіння*")
        self.gladness+=3
    def to_chill(self):
        print("Відпочинок... іграєм в бравл старс")
        self.gladness+=5
        self.progress-=0.1
        self.hunger-=3
    def is_alive(self):
        if self.progress<-0.5:
            print("Ви не попали в туалет вчасно і тепер весь дитячий садочок смердить.Вас вигнали з дитячого садочку за це((")
            self.alive=False
        elif self.hunger<=0:
            print("Ви померли від голоду(((.. F")
            self.alive=False
        elif self.gladness<=0:
            print("Ви стали дед інсайдом((")
            self.alive=False
        elif self.progress > 10:
            print("Ви стали самим крутим карапузом в дитячому садочку і переходите в перший клас раніше інших 😎😎, але, по дорозі додому, впали в туалет, і, втопились там...")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")
    def live(self,day):
        day = "Day" + str(day) + "of" + self.name + "Life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.go_for_a_walk()
            self.to_chill()
            self.to_go_to_toilet()
            self.to_have_a_shower()
            self.to_play()
            self.end_of_day()
            self.is_alive()
vadymko = student(name="Вадимко")
for day in range(365):
    if vadymko.alive == False:
        break
vadymko.live(day)