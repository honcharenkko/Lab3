import calendar

class Pizza:
    def __init__(self, title=None, price=0, total_price=0, ingrid=None, size=None):
        self.title = title
        self.price = price
        self.total_price = total_price
        self.ingrid = ingrid
        self.size = size
    def ingrinf(self):
        return "Інгрідієнти вашої піци: " + str((', '.join(self.ingrid)))
    def bezalen(self):
        self.total_price += self.price
        return "Ціна замовлення: " + str(self.total_price)
    def mehr_ingrid(self):
        qw = int(input("Хочете додати інгрідієнти?\n1-Так\n2-Ні\nВвід:"))
        if qw == 1:
            while qw == 1:
                er = int(input("Оберіть інгрідієнт:\n1-Огірки\n2-Помідори\n3-Цибуля\n4-Оливки\n5-Ковбаски\n6-Бекон\n0-Закінчити\nВвід:"))
                if er == 1:
                    self.ingrid.append("Огірки")
                    self.price += 5
                if er == 2:
                    self.ingrid.append("Помідори")
                    self.price += 3
                if er == 3:
                    self.ingrid.append("Цибуля")
                    self.price += 1
                if er == 4:
                    self.ingrid.append("Оливки")
                    self.price += 7
                if er == 5:
                    self.ingrid.append("Ковбаски")
                    self.price += 10
                if er == 6:
                    self.ingrid.append("Бекон")
                    self.price += 8
                if er == 0:
                    break
        if qw == 2:
            return "Інгрідієнтів не додано!"
    def pizinf(self):
        op = int(input("1-Big\n2-Medium\n3-Small\nОберіть розмір піцци:"))
        if op == 1:
            self.size = "Big"
            self.price += 50
        if op == 2:
            self.size = "Medium"
            self.price = self.price
        if op == 3:
            self.size = "Small"
            self.price -= 50

        return "Інформація за піццу: \nНазва:"+ self.title + "\nЦіна:"+ str(self.price) + "\nРозмір:"+ str(self.size)

class Montag(Pizza):
    def __init__(self):
        super().__init__()
        self.title = 'Margarita'
        self.price = 320
        self.size = "Medium"
        self.ingrid = ["Сир", "Помідори", "Базилік", "Томатний соус"]
class Dienstag(Pizza):
    def __init__(self):
        super().__init__()
        self.title = 'Pepperoni'
        self.price = 300
        self.size = "Medium"
        self.ingrid = ["Моцарела", "Ковбаски", "Частник", "Томатний соус"]
class Mittwoch(Pizza):
    def __init__(self):
        super().__init__()
        self.title = 'Quattro Formaggi'
        self.price = 359
        self.size = "Medium"
        self.ingrid = ["Моцарела", "Рокфор", "Мааздам", "Пармізан", "Соус Бешамель"]
class Donnerstag(Pizza):
    def __init__(self):
        super().__init__()
        self.title = 'Mushroom Paradise'
        self.price = 289
        self.size = "Medium"
        self.ingrid = ["Шампіньйони", "Курка", "Укроп", "Томатний соус", "Моцарела"]
class Freitag(Pizza):
    def __init__(self):
        super().__init__()
        self.title = 'Hawaiian Pizza'
        self.price = 399
        self.size = "Medium"
        self.ingrid = ["Ананас", "Помідори", "Моцарела", "Томатний соус"]

wday = calendar.weekday(2022, 11, 16)
#ПОНЕДІЛОК - 2022, 11, 14
#ВІВТОРОК - 2022, 11, 15
#СЕРЕДА - 2022, 11, 16
#ЧЕТВЕР - 2022, 11, 17
#П'ЯТНИЦЯ - 2022, 11, 18
#СУБОТА - 2022, 11, 19
if calendar.day_name[wday] == "Monday":
    q = Montag()
    print(q.pizinf())
    q.mehr_ingrid()
    print(q.ingrinf())
    print(q.bezalen())
elif calendar.day_name[wday] == "Tuesday":
    q = Dienstag()
    print(q.pizinf())
    q.mehr_ingrid()
    print(q.ingrinf())
    print(q.bezalen())
elif calendar.day_name[wday] == "Wednesday":
    q = Mittwoch()
    print(q.pizinf())
    q.mehr_ingrid()
    print(q.ingrinf())
    print(q.bezalen())
elif calendar.day_name[wday] == "Thursday":
    q = Donnerstag()
    print(q.pizinf())
    q.mehr_ingrid()
    print(q.ingrinf())
    print(q.bezalen())
elif calendar.day_name[wday] == "Friday":
    q = Freitag()
    print(q.pizinf())
    q.mehr_ingrid()
    print(q.ingrinf())
    print(q.bezalen())
elif calendar.day_name[wday] == "Saturday" or "Sunday":
    print("Піцерія Зачинена!")
