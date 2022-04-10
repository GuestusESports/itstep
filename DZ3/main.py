class Nokia_3310:
    price=100
    power=5
    battery=9999999
    print("I am unbreakable phone!")
class Samsung (Nokia_3310):
    print("I am unbreakable phone!")
class iPhone (Samsung, Nokia_3310):
    battery=0.1
    power=0.1
    price=9999999999999
    print("I can be broken if someone touch me!")