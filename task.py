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
        self.index = 0
        self.setupUi(self)
        self.btn_edit.setVisible(False)
        self.btn_delete.clicked.connect(
            lambda: self.list_of_tasks.tasks_listWidget.takeItem(self.list_of_tasks.tasks_listWidget.currentRow()))
        self.btn_top.clicked.connect(self.move_to_top)
        self.lineEdit.selectionChanged.connect(self.on_text_changed)
        self.lineEdit.focus_out.connect(lambda: self.lineEdit.setReadOnly(True))

    def focusOutEvent(self, e):
        print("focusOutEvent", e)

    def on_text_changed(self):
        word = self.lineEdit.selectedText()
        print("word", word, len(word))
        if word:
            self.lineEdit.setReadOnly(False)


        # if self.btn_checkbox.isChecked:
        #     self.change_stylesheet()

    def move_to_top(self):
        self.top_button_clicked.emit(self.index)

        # item, widget = self.list_of_tasks.item_to_widget(self.index)
        # # current_row = self.list_of_tasks.tasks_listWidget.takeItem(self.list_of_tasks.tasks_listWidget.currentRow())
        # # current_row = self.index
        # self.list_of_tasks.tasks_listWidget.takeItem(self.index)
        # self.list_of_tasks.tasks_listWidget.removeItemWidget(item)
        #
        # item = QListWidgetItem()
        #
        # widget.lineEdit.setText(self.lineEdit.text())
        #
        # item.setSizeHint(widget.sizeHint())
        # # widget.setFocus()
        # self.tasks_listWidget.addItem(item)
        # self.tasks_listWidget.setItemWidget(item, widget)

        #
        # widget.lineEdit.setText(self.list_of_tasks.task_lineEdit.text())
        #
        # item.setSizeHint(widget.sizeHint())
        # # widget.setFocus()
        # self.list_of_tasks.tasks_listWidget.addItem(item)
        # self.list_of_tasks.tasks_listWidget.setItemWidget(item, widget)

    # def move_to_top(self):
    #     current_row = self.list_of_tasks.tasks_listWidget.currentRow()
    #     if current_row != -1:
    #         item = self.list_of_tasks.tasks_listWidget.takeItem(current_row)
    #         widget = self.list_of_tasks.tasks_listWidget.itemWidget(item)
    #
    #         # Remove the widget from the list widget
    #         self.list_of_tasks.tasks_listWidget.removeItemWidget(item)
    #
    #         # Insert the item at the top
    #         self.list_of_tasks.tasks_listWidget.insertItem(0, item)
    #         self.list_of_tasks.tasks_listWidget.setItemWidget(item, widget)
    #         print(123)

    def change_stylesheet(self):
        self.lineEdit.setStyleSheet('text-decoration: line-through;')
