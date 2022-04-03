import random
class real life:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=50
        self.alive=True
    def to_eat(self):
        print("ОМНОМНММОМНМНМНМНММНМОМОМО АААААААААААА МОНМООНМММНМОММНРАМОМООММ ВКУСНААА")
        self.pgrogress+=0.12
        self.gladness-=3
    def to_drink(self):
        print("щас будем пити воду літрами як жигуль 92 бензин, поїхали")
        self.gladness+=3
    def to_go_to_toilet(self):
        print("Відпочивання... іграєм в бравл старс")
        self.gladness+=10
        self.progress-=5
    def to_sleep(self):
        print("Спим... іграєм в бравл старс по тихому")
        self.gladness+=10
        self.progress-=5
    def is_alive(self):
        if self.progress<-0.5:
            print("Ви були настільки голодні, що від вас залишився тільки скелет, і, ви померли((")
            self.alive=False
        elif self.gladness<=0:
            print("Ви стали дед інсайдом((")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")
    def live(self):
        day = "Day" + str(day) + "of" + self.name + "Life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
            self.to_go_to_toilet()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_drink()
            self.end_of_day()
            self.is_alive()
        SHARIK = real life(name="SHARIK")
        for day in range(365):
            if SHARIK.alive == False:
                break
            SHARIK.live(day)