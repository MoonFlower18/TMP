from abc import ABC, abstractmethod

class Legs(ABC):
    def __init__(self, object: str):
        self._object = object

    @abstractmethod
    def create(self): pass


class Cap(ABC):
    def __init__(self, object: str):
        self._object = object

    @abstractmethod
    def create(self): pass


class SkandLegs(Legs):
    def __init__(self):
        super().__init__("Скандинавский")

    def create(self):
        print(f'Созданы ножки для стола: {self._object}')


class SkandCap(Cap):
    def __init__(self):
        super().__init__("Скандинавский")

    def create(self):
        print(f'Создана крышка для стола: {self._object}')



class ProvLegs(Legs):
    def __init__(self):
        super().__init__("Прованский")

    def create(self):
        print(f'Созданы ножки для стола: {self._object}')


class ProvCap(Cap):
    def __init__(self):
        super().__init__("Прованский")

    def create(self):
        print(f'Создана крышка для стола: {self._object}')




class GuiAbstractTable(ABC):
    @abstractmethod
    def getLegs(self) -> Legs: pass

    @abstractmethod
    def getCap(self) -> Cap: pass



class SkandGuiFactory(GuiAbstractTable):
    def getLegs(self) -> Legs:
        return SkandLegs()

    def getCap(self) -> Cap:
        return SkandCap()



class ProvGuiFactory(GuiAbstractTable):
    def getLegs(self) -> Legs:
        return ProvLegs()

    def getCap(self) -> Cap:
        return ProvCap()



class Application:
    def __init__(self, table: GuiAbstractTable):
        self._gui_table = table

    def create_gui(self):
        legs = self._gui_table.getLegs()
        cap = self._gui_table.getCap()
        legs.create()
        cap.create()


def create_factory(objectname: str) -> GuiAbstractTable:
    tabled = {
        "Скандинавский": SkandGuiFactory,
        "Прованский": ProvGuiFactory
    }
    return tabled[objectname]()



objectname = "Скандинавский"
cr = create_factory(objectname)
app = Application(cr)
app.create_gui()


objectname = "Прованский"
cr = create_factory(objectname)
app = Application(cr)
app.create_gui()