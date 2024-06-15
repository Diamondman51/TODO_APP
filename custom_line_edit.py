from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit


class CustomLineEdit(QLineEdit):
    focus_out = Signal()
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def focusOutEvent(self, event):
        # Handle focus out event
        print("Focus out event")
        super().focusOutEvent(event)
        self.focus_out.emit()