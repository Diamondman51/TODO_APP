from PySide6.QtWidgets import QWidget, QListWidgetItem

from list_of_tasks_ui import Ui_Form
from task import Task


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_add_task.clicked.connect(self.add_clicked)
        self.tasks_listWidget.itemDoubleClicked.connect(self.change_mode)

        # self.tasks_listWidget.removeItemWidget()

    def add_clicked(self):
        if self.task_lineEdit:
            widget = Task(self)
            item = QListWidgetItem()

            widget.lineEdit.setText(self.task_lineEdit.text())

            item.setSizeHint(widget.sizeHint())
            # widget.setFocus()
            self.tasks_listWidget.addItem(item)
            self.tasks_listWidget.setItemWidget(item, widget)
            self.task_lineEdit.clear()
            # widget.btn_top.clicked.connect(lambda: print('btn_top'))

    def item_to_widget(self):
        item: QListWidgetItem = self.tasks_listWidget.currentItem()
        widget: Task = self.tasks_listWidget.itemWidget(item)
        return item, widget

    def change_mode(self):
        item, widget = self.item_to_widget()
        widget.lineEdit.setReadOnly(False)
        widget.btn_edit.setVisible(True)
        widget.frame.setVisible(False)
        widget.btn_edit.clicked.connect(lambda: widget.lineEdit.setReadOnly(True))
        widget.btn_edit.clicked.connect(lambda: widget.btn_edit.setVisible(False))
        # widget.lineEdit.textChanged.connect(lambda: widget.lineEdit.setReadOnly(True))
        # self.tasks_listWidget.takeItem(self.tasks_listWidget.row(item))
