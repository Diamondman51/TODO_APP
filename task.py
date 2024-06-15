from PySide6.QtWidgets import QWidget

# from list_of_tasks import Window
from task_ui import Ui_Form


class Task(QWidget, Ui_Form):
    def __init__(self, list_of_tasks):
        super().__init__()
        self.list_of_tasks = list_of_tasks
        self.setupUi(self)
        self.btn_edit.setVisible(False)
        self.btn_delete.clicked.connect(lambda: self.list_of_tasks.tasks_listWidget.takeItem(self.list_of_tasks.tasks_listWidget.currentRow()))
        self.btn_top.clicked.connect(self.move_to_top)
        if self.btn_checkbox.isChecked:
            self.change_stylesheet()

    # def move_to_top(self):
    #     item, widget = self.list_of_tasks.item_to_widget()
    #     last_item = self.list_of_tasks.tasks_listWidget.takeItem(self.list_of_tasks.tasks_listWidget.currentRow())
    #     self.list_of_tasks.tasks_listWidget.removeItemWidget(last_item)
    #     self.list_of_tasks.tasks_listWidget.insertItem(0, item)
    #     self.list_of_tasks.tasks_listWidget.setItemWidget(item, widget)

        # widget.lineEdit.setText(self.list_of_tasks.task_lineEdit.text())
        #
        # item.setSizeHint(widget.sizeHint())
        # # widget.setFocus()
        # self.list_of_tasks.tasks_listWidget.addItem(item)
        # self.list_of_tasks.tasks_listWidget.setItemWidget(item, widget)

    def move_to_top(self):
        current_row = self.list_of_tasks.tasks_listWidget.currentRow()
        if current_row != -1:
            item = self.list_of_tasks.tasks_listWidget.takeItem(current_row)
            widget = self.list_of_tasks.tasks_listWidget.itemWidget(item)

            # Remove the widget from the list widget
            self.list_of_tasks.tasks_listWidget.removeItemWidget(item)

            # Insert the item at the top
            self.list_of_tasks.tasks_listWidget.insertItem(0, item)
            self.list_of_tasks.tasks_listWidget.setItemWidget(item, widget)
            print(123)

    def change_stylesheet(self):
        self.lineEdit.setStyleSheet('text-decoration: line-through;')