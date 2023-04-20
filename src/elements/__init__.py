from .button import ButtonElement


class AllElements:
    def __init__(self, driver):
        self.button = ButtonElement(driver)
