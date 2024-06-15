from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QListWidgetItem

# from list_of_tasks import Window
from task_ui import Ui_Form


class Task(QWidget, Ui_Form):
    check_button_clicked = Signal(bool, int)
    top_button_clicked = Signal(int)
    delete_button_clicked = Signal(int)
    text_changed = Signal(str, int)

    def __init__(self, list_of_tasks):
        super().__init__()
        self.list_of_tasks = list_of_tasks
        self.index = None
        self.setupUi(self)
        self.btn_edit.setVisible(False)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.btn_top.clicked.connect(self.move_to_top)
        self.lineEdit.selectionChanged.connect(self.on_text_changed)
        self.lineEdit.focus_out.connect(lambda: self.lineEdit.setReadOnly(True))
        self.btn_checkbox.clicked.connect(self.change_stylesheet)
        # self.lineEdit.focus_in.connect(lambda: self.lineEdit.setReadOnly(False))

    def on_text_changed(self):
        word = self.lineEdit.selectedText()
        print("word", word, len(word))
        if word:
            self.lineEdit.setReadOnly(False)

        # if self.btn_checkbox.isChecked:
        #     self.change_stylesheet()

    def move_to_top(self):
        self.top_button_clicked.emit(self.index)

    def change_stylesheet(self, event):
        self.lineEdit.setStyleSheet('text-decoration: line-through;') if event else self.lineEdit.setStyleSheet('')
        connection = self.list_of_tasks.create_connection()
        cursor = connection.cursor()

        query = '''update tasks set is_done=%s where text=%s'''
        cursor.execute(query, (event, self.lineEdit.text()))
        connection.commit()
        connection.close()

    def btn_delete_clicked(self):
        connection = self.list_of_tasks.create_connection()
        cursor = connection.cursor()

        query = '''delete from tasks where text=%s'''
        cursor.execute(query, (self.lineEdit.text(), ))
        connection.commit()
        connection.close()

        # Now delete from the QListWidget
        self.list_of_tasks.tasks_listWidget.takeItem(self.index)
        # self.list_of_tasks.tasks_listWidget.update()
