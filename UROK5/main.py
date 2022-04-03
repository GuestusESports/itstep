#para_1

print("Привіт! Ця програма каже, чи твоє число є парним, чи ні.")
print("Введи число нижче!")
num=int(input())
if num % 2 == 0:
    print("Твоє число парне!")
else:
    print("Твоє число не парне!")

#para_2

def add(P, Q):
    return P + Q


def subtract(P, Q):
    return P - Q


def multiply(P, Q):
    return P * Q


def divide(P, Q):
    return P / Q

print("Виберіть операцію.")
print("a. Додавання")
print("b. Віднімання")
print("c. Множення")
print("d. Ділення")

choice = input("Виберіть (a/ b/ c/ d): ")

num_1 = int(input("Введіть перше число: "))
num_2 = int(input("Введіть друге число: "))

if choice == 'a':
    print(num_1, " + ", num_2, " = ", add(num_1, num_2))

elif choice == 'b':
    print(num_1, " - ", num_2, " = ", subtract(num_1, num_2))

elif choice == 'c':
    print(num_1, " * ", num_2, " = ", multiply(num_1, num_2))
elif choice == 'd':
    print(num_1, " / ", num_2, " = ", divide(num_1, num_2))
else:
    print("Неправильний знак.4")