# _*_ coding: utf-8 _*_

def input_number():
    while True:
        usr_in = input("Zahl Bitte oder exit für beenden: ")
        if usr_in == "exit":
            return "ex"
        try:
            user_in = float(usr_in)
            return user_in
        except:
            print("Bitte eine Zahl eingeben")

def input_oberation(number):
    while True:
        user_in = input("Welche Oberation? ")
        if user_in == "+":
            number_2 = input_number()
            number += number_2
            return number
        elif user_in == "-":
            number_2 = input_number()
            number -= number_2
            return number
        elif user_in == "/":
            number_2 = input_number()
            number /= number_2
            return number
        elif user_in == "*":
            number_2 = input_number()
            number *= number_2
            return number
        else:
            print("Bitte einen der Folgenden Oberationen +, -, *, /")

while True:
    number = input_number()
    if number == "ex":
        break
    else:
        res = input_oberation(number)
        print(res)
