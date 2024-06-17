# # # # from PySide6.QtWidgets import QApplication, QListWidget, QVBoxLayout, QWidget, QPushButton, QListWidgetItem, QLabel
# # # #
# # # #
# # # # def move_last_item_to_top(list_widget):
# # # #     count = list_widget.count()
# # # #     if count > 1:
# # # #         # Take the last item and its associated widget
# # # #         last_item = list_widget.takeItem(count - 1)
# # # #         widget = list_widget.itemWidget(last_item)
# # # #
# # # #         # Remove the widget from the list widget
# # # #         list_widget.removeItemWidget(last_item)
# # # #
# # # #         # Create a temporary container to keep the widget alive
# # # #         temp_container = QWidget()
# # # #         temp_container.setLayout(QVBoxLayout())
# # # #         temp_container.layout().addWidget(widget)
# # # #
# # # #         # Insert the item at the top
# # # #         list_widget.insertItem(0, last_item)
# # # #
# # # #         # Reassign the widget to the item
# # # #         list_widget.setItemWidget(last_item, widget)
# # # #
# # # #         # Delete the temporary container
# # # #         temp_container.deleteLater()
# # # #
# # # #
# # # # app = QApplication([])
# # # #
# # # # # Create a main window
# # # # main_window = QWidget()
# # # # layout = QVBoxLayout(main_window)
# # # #
# # # # # Create a QListWidget
# # # # list_widget = QListWidget()
# # # #
# # # # # Add some items with associated widgets to the list
# # # # for i in range(10):
# # # #     item = QListWidgetItem(f'Item {i}')
# # # #     label = QLabel(f'Widget {i}')
# # # #     list_widget.addItem(item)
# # # #     list_widget.setItemWidget(item, label)
# # # #
# # # # # Add a button to trigger the move operation
# # # # button = QPushButton('Move Last Item to Top')
# # # # button.clicked.connect(lambda: move_last_item_to_top(list_widget))
# # # #
# # # # layout.addWidget(list_widget)
# # # # layout.addWidget(button)
# # # #
# # # # main_window.setLayout(layout)
# # # # main_window.show()
# # # #
# # # # app.exec()
# # # import sys
# # # from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QVBoxLayout, QWidget, QLabel
# # # from PySide6.QtCore import Qt
# # #
# # #
# # # class MyWindow(QWidget):
# # #     def __init__(self):
# # #         super().__init__()
# # #
# # #         self.setWindowTitle('Item Entered Example')
# # #         self.setGeometry(100, 100, 300, 200)
# # #
# # #         self.layout = QVBoxLayout()
# # #
# # #         self.label = QLabel("Hover over an item", self)
# # #         self.layout.addWidget(self.label)
# # #
# # #         self.list_widget = QListWidget(self)
# # #         self.layout.addWidget(self.list_widget)
# # #
# # #         for i in range(10):
# # #             item = QListWidgetItem(f"Item {i + 1}")
# # #             self.list_widget.addItem(item)
# # #
# # #         # Enable hover events
# # #         self.list_widget.setMouseTracking(True)
# # #
# # #         # Connect the itemEntered signal to the slot
# # #         self.list_widget.itemEntered.connect(self.on_item_entered)
# # #
# # #         self.setLayout(self.layout)
# # #
# # #     def on_item_entered(self, item):
# # #         self.label.setText(f"Hovered over: {item.text()}")
# # #
# # #
# # # if __name__ == "__main__":
# # #     app = QApplication(sys.argv)
# # #     window = MyWindow()
# # #     window.show()
# # #     sys.exit(app.exec())
# # import sys
# # from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QVBoxLayout, QWidget, QLabel
# # from PySide6.QtCore import Qt
# #
# #
# # class MyWindow(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #
# #         self.setWindowTitle('Item Entered Example')
# #         self.setGeometry(100, 100, 300, 200)
# #
# #         self.layout = QVBoxLayout()
# #
# #         self.label = QLabel("Hover over an item", self)
# #         self.layout.addWidget(self.label)
# #
# #         self.list_widget = QListWidget(self)
# #         self.layout.addWidget(self.list_widget)
# #
# #         for i in range(10):
# #             item = QListWidgetItem(f"Item {i + 1}")
# #             self.list_widget.addItem(item)
# #
# #         # Enable hover events
# #         self.list_widget.setMouseTracking(True)
# #
# #         # Connect the itemEntered signal to the slot
# #         self.list_widget.itemEntered.connect(self.on_item_entered)
# #
# #         self.setLayout(self.layout)
# #
# #     def on_item_entered(self, item):
# #         self.label.setText(f"Hovered over: {item.text()}")
# #         # Set focus to the entered item
# #         self.list_widget.setCurrentItem(item)
# #
# #
# # if __name__ == "__main__":
# #     app = QApplication(sys.argv)
# #     window = MyWindow()
# #     window.show()
# #     sys.exit(app.exec())
#
#
# import time
#
# from PySide6.QtCore import QThread, Signal
# from PySide6.QtWidgets import (
#     QApplication,
#     QWidget,
#     QTableWidget,
#     QVBoxLayout,
#     QPushButton,
#     QProgressBar,
#     QLabel, QTableWidgetItem
# )
#
#
# # --- Data Source (Replace with your actual data source) ---
# class DataProvider:
#     def __init__(self, total_rows):
#         self.total_rows = total_rows
#
#     def get_data_chunk(self, start_row, chunk_size):
#         data = []
#         for i in range(start_row, min(start_row + chunk_size, self.total_rows)):
#             # Simulate data loading
#             time.sleep(0.1)  # Adjust delay for testing
#             data.append(f"Row {i}")
#         return data
#
#
# # --- Thread for loading data chunks ---
# class DataLoadingThread(QThread):
#     data_chunk_ready = Signal(list, int, int)  # Signal for new data
#
#     def __init__(self, data_provider, chunk_size, parent=None):
#         super().__init__(parent)
#         self.data_provider = data_provider
#         self.chunk_size = chunk_size
#         self.current_row = 0
#
#     def run(self):
#         while self.current_row < self.data_provider.total_rows:
#             data_chunk = self.data_provider.get_data_chunk(
#                 self.current_row, self.chunk_size
#             )
#             self.data_chunk_ready.emit(
#                 data_chunk, self.current_row, self.current_row + len(data_chunk)
#             )
#             self.current_row += self.chunk_size
#             time.sleep(0.1)  # Adjust for testing
#
#
# # --- Main Window ---
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Partial Loading QTableWidget")
#
#         # UI elements
#         self.table_widget = QTableWidget()
#         self.progress_bar = QProgressBar()
#         self.load_button = QPushButton("Load Data")
#         self.status_label = QLabel("Ready")
#
#         # Layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.table_widget)
#         layout.addWidget(self.progress_bar)
#         layout.addWidget(self.load_button)
#         layout.addWidget(self.status_label)
#         self.setLayout(layout)
#
#         # Connect signals
#         self.load_button.clicked.connect(self.load_data)
#
#     def load_data(self):
#         # Disable button, set status, and initialize progress
#         self.load_button.setEnabled(False)
#         self.status_label.setText("Loading...")
#         self.progress_bar.setValue(0)
#         self.progress_bar.setMaximum(100)
#
#         # Set up data source and thread
#         self.data_provider = DataProvider(total_rows=100)  # Replace with your total rows
#         self.loading_thread = DataLoadingThread(
#             self.data_provider, chunk_size=10
#         )
#         self.loading_thread.data_chunk_ready.connect(self.on_data_chunk_ready)
#         self.loading_thread.start()
#
#     def on_data_chunk_ready(self, data_chunk, start_row, end_row):
#         # Add new data to the table
#         self.table_widget.setColumnCount(1)
#         self.table_widget.setRowCount(end_row)
#         self.table_widget.setHorizontalHeaderLabels(["Data"])
#
#         for row, item in enumerate(data_chunk):
#             self.table_widget.setItem(start_row + row, 0, QTableWidgetItem(item))
#
#         # Update progress bar and status
#         progress = int((end_row / self.data_provider.total_rows) * 100)
#         self.progress_bar.setValue(progress)
#         if progress == 100:
#             self.status_label.setText("Data Loaded")
#             self.load_button.setEnabled(True)
#
#
# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()

n = int(input())
print('YES' if n%2!=0 or (n%2!=0 and 6<=n<=20) else 'NO')