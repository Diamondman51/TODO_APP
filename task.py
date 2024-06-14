from PySide6.QtWidgets import QWidget

from task_ui import Ui_Form


class Task(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)