class App:
    def __init__(self, some_property: str = "something"):
        self.some_property = some_property


def app(some_property: str = "something"):
    return App(some_property=some_property)
