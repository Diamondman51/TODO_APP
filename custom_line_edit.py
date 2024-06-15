from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit


class CustomLineEdit(QLineEdit):
    focus_out = Signal()
    # focus_in = Signal()
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def focusOutEvent(self, event):
        # Handle focus out event
        # print("Focus out event", event)
        super().focusOutEvent(event)
        self.focus_out.emit()
        self.clearFocus()

    # def focusInEvent(self, event):
    #     super().focusInEvent(event)
    #     self.focus_in.emit()