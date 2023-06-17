from abc import ABC, abstractmethod

class PasswordItem:
    def __init__(self, password):
        self.password = password

    def get(self):
        return self.password

class Target(ABC):

    @abstractmethod
    def ex(self) -> None:
        pass

class Real(Target):
    def ex(self) -> None:
        print("Давайте посчитаем что-то: \n18 * 3 =", 18*3)

class Proxy(Target):

    def __init__(self, real_target: Real) -> None:
        self._real_target = real_target

    def ex(self) -> None:

        if self.access():
            self._real_target.ex()

    def access(self) -> bool:
        realpassword = 18032002
        print("Proxy: Проверка доступа...")
        if realpassword == password.get():
            return True
        else:
            print("В доступе отказано")
            return False


def client(target: Target) -> None:
    target.ex()


if __name__ == "__main__":
    password = PasswordItem(657483)
    print(password.get())
    print("Запуск напрямую, без Proxy:")
    print("===========================")
    real_target = Real()
    client(real_target)

    print("\nЗапуск с Proxy и неправильным паролем:")
    print("======================================")
    proxy = Proxy(real_target)
    client(proxy)

    password = PasswordItem(18032002)
    print("\nЗапуск с Proxy и правильным паролем:")
    print("====================================")
    proxy = Proxy(real_target)
    client(proxy)