from PySide6.QtWidgets import QApplication

from list_of_tasks import Window

app = QApplication()

window = Window()
window.show()
if __name__ == '__main__':
    app.exec()