import psycopg2
from PySide6.QtWidgets import QWidget, QListWidgetItem

from list_of_tasks_ui import Ui_Form
from task import Task


class Window(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_add_task.clicked.connect(self.add_clicked)
        self.tasks_listWidget.itemDoubleClicked.connect(self.change_mode)
        self.load_data_and_add()

    def add_clicked(self):
        if self.task_lineEdit:
            widget = Task(self)
            widget.index = self.tasks_listWidget.count()

            widget.top_button_clicked.connect(self.on_top_button_clicked)
            item = QListWidgetItem()

            widget.lineEdit.setText(self.task_lineEdit.text())

            item.setSizeHint(widget.sizeHint())
            self.tasks_listWidget.addItem(item)
            self.tasks_listWidget.setItemWidget(item, widget)
            self.task_lineEdit.clear()

            query = '''insert into tasks
                    values (%s, %s, now());'''

            connection = self.create_connection()
            cursor = connection.cursor()

            query_2 = '''select text, is_done 
                        from tasks
                        order by date desc'''

            cursor.execute(query, (widget.lineEdit.text(), widget.btn_checkbox.isChecked()))
            cursor.execute(query_2)
            connection.commit()
            connection.close()

    def on_top_button_clicked(self, row):
        # get widget then remove QlistWidgetItem
        widget = self.tasks_listWidget.itemWidget(self.tasks_listWidget.item(row))

        connection = self.create_connection()
        cursor = connection.cursor()

        # add new QlistWidgetItem
        item = QListWidgetItem()
        item.setSizeHint(widget.sizeHint())
        self.tasks_listWidget.insertItem(0, item)

        # set widget
        self.tasks_listWidget.setItemWidget(item, widget)
        self.tasks_listWidget.takeItem(row + 1)

        query = '''UPDATE tasks
                SET date = NOW()
                WHERE text = %s;
                select text, is_done from tasks
                order by date desc;
                '''
        cursor.execute(query, (widget.lineEdit.text(), ))
        connection.commit()
        connection.close()

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

    def create_connection(self):
        self.conn = psycopg2.connect(

            database='todo_app',
            user='postgres',
            password='Zshavkatov61@',
            host='localhost',
            port=5432
        )

        return self.conn

    def load_data_and_add(self):
        connection = self.create_connection()
        cursor = connection.cursor()

        query = '''select text, is_done 
                from tasks
                order by date desc'''

        cursor.execute(query)
        data = cursor.fetchall()
        self.tasks_listWidget.updatesEnabled()

        for task in data:
            widget = Task(self)
            widget.index = self.tasks_listWidget.count()

            widget.top_button_clicked.connect(self.on_top_button_clicked)
            item = QListWidgetItem()

            widget.lineEdit.setText(task[0])
            widget.btn_checkbox.setChecked(task[1])
            widget.change_stylesheet(task[1])

            item.setSizeHint(widget.sizeHint())
            self.tasks_listWidget.addItem(item)
            self.tasks_listWidget.setItemWidget(item, widget)

        connection.commit()
        connection.close()
