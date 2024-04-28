import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem,QPushButton,QWidget,QLabel,QVBoxLayout

class MySQLTableViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        

    def initUI(self):
        self.setWindowTitle('MySQL Table Viewer')
        self.setGeometry(100, 100, 800, 600)

        # Создаем таблицу Qt для отображения данных
        self.tableWidget = QTableWidget(self)
        self.secondScreen = SecondScreen()
        self.tableWidget.setGeometry(50, 50, 700, 500)

        # Подключаемся к базе данных MySQL
        try:
            self.conn = mysql.connector.connect(
                host='0.0.0.0',
                user='test',
                password='testtest',
                database='test'
            )
            self.cursor = self.conn.cursor()
            
            # Замените 'ваша_таблица' на имя вашей таблицы
            self.cursor.execute('SELECT * FROM recipes')
            rows = self.cursor.fetchall()
            
            # Определите количество строк и столбцов для таблицы Qt
            num_rows = len(rows)
            num_cols = len(rows[0])
            self.tableWidget.setRowCount(num_rows)
            self.tableWidget.setColumnCount(num_cols)
            
            # Заполните таблицу Qt данными из MySQL
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(i, j, item)
        
        except mysql.connector.Error as e:
            print("Ошибка подключения к MySQL:", e)
        
        finally:
            self.cursor.close()
            self.conn.close()

        self.button = QPushButton('Перейти на другой экран', self)
        self.button.setGeometry(50, 500, 200, 30)
        self.button.clicked.connect(self.showSecondScreen)
    def showSecondScreen(self,checked):
        
        
        if self.secondScreen.isVisible():
            self.secondScreen.hide()
        else:
            self.secondScreen.show()    
        self.setCentralWidget(self.secondScreen)

class SecondScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Создаем простой текст для второго экрана
        label = QLabel('Это второй экран')
        layout.addWidget(label)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    viewer = MySQLTableViewer()
    viewer.show()
    app.exec()

if __name__ == '__main__':
    main()
