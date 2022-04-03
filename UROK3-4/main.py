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
            print("Ви стали дед інсайдом і вас вигнали з дитячого садочку((")
            self.alive=False
        