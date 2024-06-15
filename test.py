from PySide6.QtWidgets import QApplication, QListWidget, QVBoxLayout, QWidget, QPushButton, QListWidgetItem, QLabel


def move_last_item_to_top(list_widget):
    count = list_widget.count()
    if count > 1:
        # Take the last item and its associated widget
        last_item = list_widget.takeItem(count - 1)
        widget = list_widget.itemWidget(last_item)

        # Remove the widget from the list widget
        list_widget.removeItemWidget(last_item)

        # Create a temporary container to keep the widget alive
        temp_container = QWidget()
        temp_container.setLayout(QVBoxLayout())
        temp_container.layout().addWidget(widget)

        # Insert the item at the top
        list_widget.insertItem(0, last_item)

        # Reassign the widget to the item
        list_widget.setItemWidget(last_item, widget)

        # Delete the temporary container
        temp_container.deleteLater()


app = QApplication([])

# Create a main window
main_window = QWidget()
layout = QVBoxLayout(main_window)

# Create a QListWidget
list_widget = QListWidget()

# Add some items with associated widgets to the list
for i in range(10):
    item = QListWidgetItem(f'Item {i}')
    label = QLabel(f'Widget {i}')
    list_widget.addItem(item)
    list_widget.setItemWidget(item, label)

# Add a button to trigger the move operation
button = QPushButton('Move Last Item to Top')
button.clicked.connect(lambda: move_last_item_to_top(list_widget))

layout.addWidget(list_widget)
layout.addWidget(button)

main_window.setLayout(layout)
main_window.show()

app.exec()