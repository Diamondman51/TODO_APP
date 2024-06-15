from PySide6.QtWidgets import QWidget, QListWidgetItem

from list_of_tasks_ui import Ui_Form
from task import Task


class Window(QWidget, Ui_Form):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tasks_listWidget.setMouseTracking(True)
        self.btn_add_task.clicked.connect(self.add_clicked)
        self.tasks_listWidget.itemDoubleClicked.connect(self.change_mode)
        # self.tasks_listWidget.itemEntered.connect(self.set_current_row)
        # self.tasks_listWidget.currentItemChanged.connect(lambda x, y : print(self.tasks_listWidget.currentIndex().row()))

    # def set_current_row(self, item:QListWidgetItem):
    #     print(item.data())
    #     row = self.tasks_listWidget.row(item)
    #     print("row",row)
    #     # self.tasks_listWidget.setCurrentRow(self.tasks_listWidget.count() - 1)
    #     # print("Current row: ", self.tasks_listWidget.currentIndex().row())
    #
    #     # self.tasks_listWidget.removeItemWidget()

    def add_clicked(self):
        if self.task_lineEdit:
            widget = Task(self)
            widget.top_button_clicked.connect(self.on_top_button_clicked)

            widget.index = self.tasks_listWidget.count()
            item = QListWidgetItem()

            widget.lineEdit.setText(self.task_lineEdit.text())

            item.setSizeHint(widget.sizeHint())
            # widget.setFocus()
            self.tasks_listWidget.addItem(item)
            self.tasks_listWidget.setItemWidget(item, widget)
            self.task_lineEdit.clear()

            # widget.btn_top.clicked.connect(lambda: print('btn_top'))

    def on_top_button_clicked(self, row):
        # get widget then remove QlistWidgetItem
        widget = self.tasks_listWidget.itemWidget(self.tasks_listWidget.item(row))

        # add new QlistWidgetItem
        item = QListWidgetItem()
        item.setSizeHint(widget.sizeHint())
        self.tasks_listWidget.insertItem(0, item)

        # set widget
        self.tasks_listWidget.setItemWidget(item, widget)
        self.tasks_listWidget.takeItem(row + 1)
        self.restart_index()

    def restart_index(self):
        for i in range(self.tasks_listWidget.count()):
            item = self.tasks_listWidget.item(i)
            widget: Task = self.tasks_listWidget.itemWidget(item)
            widget.index = i

    def item_to_widget(self, index):
        # self.tasks_listWidget.currentIndex().row()
        item: QListWidgetItem = self.tasks_listWidget.item(index)

        widget: Task = self.tasks_listWidget.itemWidget(item)
        return item, widget

    def change_mode(self):
        index = self.tasks_listWidget.currentIndex().row()
        item, widget = self.item_to_widget(index)
        widget.lineEdit.setReadOnly(False)
        widget.btn_edit.setVisible(True)
        widget.frame.setVisible(False)
        widget.btn_edit.clicked.connect(lambda: widget.lineEdit.setReadOnly(True))
        widget.btn_edit.clicked.connect(lambda: widget.btn_edit.setVisible(False))
        # widget.lineEdit.textChanged.connect(lambda: widget.lineEdit.setReadOnly(True))
        # self.tasks_listWidget.takeItem(self.tasks_listWidget.row(item))
