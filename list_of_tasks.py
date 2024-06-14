from PySide6.QtWidgets import QWidget, QListWidgetItem

from list_of_tasks_ui import Ui_Form
from task import Task


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_add_task.clicked.connect(self.add_clicked)
        self.tasks_listWidget.itemDoubleClicked(self.change_mode)

    def add_clicked(self):
        if self.task_lineEdit:
            widget = Task()
            item = QListWidgetItem()

            widget.lineEdit.setText(self.task_lineEdit.text())

            item.setSizeHint(widget.sizeHint())
            self.tasks_listWidget.addItem(item)
            self.tasks_listWidget.setItemWidget(item, widget)

    def item_to_widget(self):
        item = self.tasks_listWidget.currentItem()
        widget = self.tasks_listWidget.itemWidget(item)
        return item, widget

    def change_mode(self):
        item, widget= self.item_to_widget()

