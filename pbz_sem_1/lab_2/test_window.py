import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Главное окно')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Кнопка для перехода к редактированию Table 1
        self.button_table1 = QPushButton('Редактировать Table 1', self)
        layout.addWidget(self.button_table1)
        self.button_table1.clicked.connect(self.openTable1Window)

        # Кнопка для перехода к редактированию Table 2
        self.button_table2 = QPushButton('Редактировать Table 2', self)
        layout.addWidget(self.button_table2)
        self.button_table2.clicked.connect(self.openTable2Window)

        # Кнопка для перехода к редактированию Table 3
        self.button_table3 = QPushButton('Редактировать Table 3', self)
        layout.addWidget(self.button_table3)
        self.button_table3.clicked.connect(self.openTable3Window)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def openTable1Window(self):
        self.table1Window = TableWindow('Table 1')
        self.table1Window.show()

    def openTable2Window(self):
        self.table2Window = TableWindow('Table 2')
        self.table2Window.show()

    def openTable3Window(self):
        self.table3Window = TableWindow('Table 3')
        self.table3Window.show()

class TableWindow(QMainWindow):
    def __init__(self, table_name):
        super().__init__()

        self.table_name = table_name
        self.initUI()

    def initUI(self):
        self.setWindowTitle(f'Редактирование {self.table_name}')
        self.setGeometry(200, 200, 400, 200)

        # Кнопка возврата
        self.back_button = QPushButton('Назад', self)
        self.back_button.setGeometry(20, 20, 80, 30)
        self.back_button.clicked.connect(self.goBack)

    def goBack(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
