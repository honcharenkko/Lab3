import datetime


class Ticket:
    def __init__(self, total_price = 0, nummer = 0000, price = 990):
        self.total_price = total_price
        self.nummer = nummer
        self.price = price

    def getinfo(self):
        return "Ціна квитка: ", self.price

    def buy(self):
        self.total_price += self.price
        return "КВИТОК ПРИДБАНО"


class AdvanceTicket(Ticket):
    def buy(self):
        self.total_price += self.price - (self.price / 100 * 40)
        return "КВИТОК ПРИДБАНО"

class LateTicket(Ticket):
    def buy(self):
        self.total_price = self.price + (self.price/100 * 10)
        return "КВИТОК ПРИДБАНО"

class StudentTicket(Ticket):
    def buy(self):
        self.total_price += self.price - (self.price / 2)
        return "КВИТОК ПРИДБАНО"


t1 = AdvanceTicket()
t2 = Ticket()
t3 = LateTicket()
t4 = StudentTicket()

onprog = True
vremya = datetime.datetime.now()
vremya1 = datetime.datetime(2023, 11, 15)
x = vremya1 - vremya
while onprog:
    a = int(input("1-ДАТА \n2-КВИТКИ \n3-КОШИК \n0-ЗАВЕРШИТИ \nОБЕРІТЬ ФУНКЦІЮ:"))
    if a == 1:
        while a ==1:
            print("ВАША ДАТА:", vremya.strftime("%x"))
            print("ДАТА ЗАХОДУ:", vremya1.strftime("%x"))
            print("ЗАЛИШИЛОСЬ",x.days,"ДНІВ")
            break
    elif a == 2:
        while a == 2:
            print("1-ЗАВЧАСНИЙ \n2-ЗВИЧАЙНИЙ \n3-ПІЗНІЙ \n4-СТУДЕНТСЬКИЙ \n0-НАЗАД")
            b = int(input("Оберіть тип квитку:"))
            if b == 1:
                print("INFO: КВИТОК МОЖНА КУПИТИ ЛИШЕ ЗА 60 ДНІВ ДО ЗАХОДУ")
                if x.days > 60:
                    print(t1.buy())
                else: print("КУПИТИ КВИТОК ВЖЕ ПІЗНО! ОБЕРІТЬ ІНШИЙ!")
            elif b == 2:
                print("INFO: КВИТОК МОЖНА КУПИТИ У ПРОМІЖКУ ВІД 59 ДО 11 ДНІВ ДО ЗАХОДУ")
                if 11 < x.days < 60:
                    print(t2.buy())
                else:
                    print("КУПИТИ КВИТОК НЕМОЖНА! ОБЕРІТЬ ІНШИЙ!")
            elif b == 3:
                print("INFO: КВИТОК МОЖНА КУПИТИ ЗА 10 ДНІВ ДО ЗАХОДУ")
                if x.days < 11:
                    print(t3.buy())
                else: print("КУПИТИ КВИТОК РАНО! ОБЕРІТЬ ІНШИЙ!")
            elif b == 4:
                print("INFO: КВИТОК МОЖНА КУПИТИ СТУДЕНТАМ")
                studak = input("ВВЕДІТЬ НОМЕР СТУДЕНТСЬКОГО:")
                exist = "st" in studak
                if exist:
                    print(t4.buy())
                else: print("ТАКИЙ СТУДАК НЕ ДІЙСНИЙ")
            if b == 0:
                break
    elif a == 3:
        busket = t1.total_price + t2.total_price + t3.total_price + t4.total_price
        print("СУМА ЗАМОВЛЕННЯ:", busket)
    if a == 0:
        break