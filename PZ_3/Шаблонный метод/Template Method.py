# открывать лучше в PyCharm (только в тёмной теме белый будет серым)
from abc import ABC, abstractmethod

def del_l(text):
    print("\033[0m{}".format(text))

class Algorithm(ABC):

    def template_method(self):

        self.flagstock()
        self.draw_1()
        self.draw_2()
        self.draw_3()
        self.final()
        self.printer()

    def flagstock(self):
        print("Флагшток нарисован")

    @abstractmethod
    def draw_1(self):
        pass

    @abstractmethod
    def draw_2(self):
        pass

    @abstractmethod
    def draw_3(self):
        pass

    def final(self):
        print('Отрисовка флагов завершена!')

    def printer(self):
        n = 50
        print("=" * n)

class colors:
    def paint_white(self):
        def out_white(text):
            print("\033[47m{}".format(text))
        out_white("               ")

    def paint_red(self):
        def out_red(text):
            print("\033[41m{}".format(text))
        out_red("               ")

    def paint_green(self):
        def out_green(text):
            print("\033[42m{}".format(text))
        out_green("               ")

    def paint_blue(self):
        def out_blue(text):
            print("\033[44m{}".format(text))
        out_blue("               ")

class Rus_flag(Algorithm):
    def draw_1(self):
        z = colors()
        z.paint_white()

    def draw_2(self):
        z = colors()
        z.paint_blue()

    def draw_3(self):
        z = colors()
        z.paint_red()

    def final(self):
        del_l("Флаг России готов!")

class Ven_flag(Algorithm):
    def draw_1(self):
        z = colors()
        z.paint_red()

    def draw_2(self):
        z = colors()
        z.paint_white()

    def draw_3(self):
        z = colors()
        z.paint_green()

    def final(self):
        del_l("Флаг Венгрии готов!")

print("Рисуем флаг России")
a=Rus_flag()
a.template_method()

print("Рисуем флаг Венгрии")
d=Ven_flag()
d.template_method()
