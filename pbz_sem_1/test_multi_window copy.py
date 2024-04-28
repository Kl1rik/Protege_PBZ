import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,QTableWidget,QTableWidgetItem,QLineEdit,QLabel,QRadioButton,QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Банк данных технологий создания различных продуктов')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Кнопка для перехода к редактированию Table 1
        self.button_table1 = QPushButton('Таблица продуктов', self)
        layout.addWidget(self.button_table1)
        self.button_table1.clicked.connect(self.openTable1Window)

        # Кнопка для перехода к редактированию Table 2
        self.button_table2 = QPushButton('Таблица рецептов', self)
        layout.addWidget(self.button_table2)
        self.button_table2.clicked.connect(self.openTable2Window)

        # Кнопка для перехода к редактированию Table 3
        self.button_table3 = QPushButton('Таблица поставщиков продуктов', self)
        layout.addWidget(self.button_table3)
        self.button_table3.clicked.connect(self.openTable3Window)

        self.button_table4 = QPushButton('Просмотр списка блюд, имеющих минимальную калорийность', self)
        layout.addWidget(self.button_table4)
        self.button_table4.clicked.connect(self.openTable4Window)

        self.button_table5 = QPushButton('Просмотр списка блюд и названия рецептов для каждого блюда', self)
        layout.addWidget(self.button_table5)
        self.button_table5.clicked.connect(self.openTable5Window)

        self.button_table6 = QPushButton('Добавление/Обновление информации о продуктах ', self)
        layout.addWidget(self.button_table6)
        self.button_table6.clicked.connect(self.openTable6Window)

        self.button_table7 = QPushButton('Добавление/Обновление информации о рецептах ', self)
        layout.addWidget(self.button_table7)
        self.button_table7.clicked.connect(self.openTable7Window)

        self.button_table8 = QPushButton('Добавление/Обновление информации о поставщиках продуктов ', self)
        layout.addWidget(self.button_table8)
        self.button_table8.clicked.connect(self.openTable8Window)

        self.button_table9 = QPushButton('Удаление записей из таблиц', self)
        layout.addWidget(self.button_table9)
        self.button_table9.clicked.connect(self.openTable9Window)

        self.button_table10 = QPushButton('Просмотр прайс-листа заданного поставщика на заданную дату', self)
        layout.addWidget(self.button_table10)
        self.button_table10.clicked.connect(self.openTable10Window)


        
        
        


        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def openTable1Window(self):
        self.table1Window = TableWindow1('Продукты')
        self.table1Window.show()

    def openTable2Window(self):
        self.table2Window = TableWindow2('Рецепты')
        self.table2Window.show()

    def openTable3Window(self):
        self.table3Window = TableWindow3('Поставщики')
        self.table3Window.show()

    def openTable4Window(self):
        self.table4Window = TableWindow4('Минимальная калорийность')
        self.table4Window.show()

    def openTable5Window(self):
        self.table5Window = TableWindow5('Список блюд')
        self.table5Window.show()    

    def openTable6Window(self):
        self.table6Window = TableWindow6('Продукты')
        self.table6Window.show()       

    def openTable7Window(self):
        self.table7Window = TableWindow7('Рецепты')
        self.table7Window.show()    

    def openTable8Window(self):
        self.table8Window = TableWindow8('Поставщики')
        self.table8Window.show()      

    def openTable9Window(self):
        self.table9Window = TableWindow9('Удаление')
        self.table9Window.show()     

    def openTable10Window(self):
        self.table10Window = TableWindow10('Поиск прайс листа')
        self.table10Window.show()          


class TableWindow(QMainWindow):
    def __init__(self, table_name):
        super().__init__()

        self.table_name = table_name
        self.initUI()

    def initUI(self):
        self.setWindowTitle(f'Редактирование {self.table_name}')
        self.setGeometry(400, 400, 600, 400)
    
        # Кнопка возврата
        self.back_button = QPushButton('Назад', self)
        self.back_button.setGeometry(20, 20, 80, 30)
        self.back_button.clicked.connect(self.goBack)

    def goBack(self):
        self.close()

class TableWindow1(QWidget):
    def __init__(self, table_name):
        super().__init__()

        self.table_name = table_name
        self.initUI()

    def initUI(self):
        self.setWindowTitle(f'Таблица {self.table_name}')
        self.setGeometry(400, 400, 600, 400)
    
        # Кнопка возврата
        self.back_button = QPushButton('Назад', self)
        self.back_button.setGeometry(230, 20, 80, 30)
        self.back_button.clicked.connect(self.goBack)

         # Создаем таблицу Qt для отображения данных
        self.tableWidget = QTableWidget(self)
        
        self.tableWidget.setGeometry(50, 80, 400, 600)
        
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
            self.cursor.execute('SELECT * FROM products')
            rows = self.cursor.fetchall()
            
            # Определите количество строк и столбцов для таблицы Qt
            num_rows = len(rows)
            num_cols = len(rows[0])
            columns = ["id","Продукт","Рецепт","Ингридиент"]
            self.tableWidget.setRowCount(num_rows)
            self.tableWidget.setColumnCount(num_cols)
            self.tableWidget.setHorizontalHeaderLabels(columns)
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


    def goBack(self):
        self.close()


class TableWindow2(QWidget):
    def __init__(self, table_name):
        super().__init__()

        self.table_name = table_name
        

        self.initUI()
        
        
        

    def initUI(self):

        self.setWindowTitle(f'Таблица {self.table_name}')
        self.setGeometry(60, 60, 800, 600)
        
    
        # Кнопка возврата
        self.back_button = QPushButton('Назад', self)
        self.back_button.setGeometry(350, 20, 80, 30)
        
        self.back_button.clicked.connect(self.goBack)
    
            
            

        # Создаем таблицу Qt для отображения данных
        self.tableWidget = QTableWidget(self)
        
        self.tableWidget.setGeometry(50, 80, 700, 500)
        
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
            columns = ["id","Выход продукта","Рецепт","Описание","Автор","Метод готовки","Ингридиент","Ингридиент","Ингридиент"]
            self.tableWidget.setRowCount(num_rows)
            self.tableWidget.setColumnCount(num_cols)
            self.tableWidget.setHorizontalHeaderLabels(columns)
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
    def goBack(self):
        self.close()        
        

class TableWindow3(QWidget):
    def __init__(self, table_name):
        super().__init__()

        self.table_name = table_name
        

        self.initUI()
        
        
        

    def initUI(self):

        self.setWindowTitle(f'Таблица {self.table_name}')
        self.setGeometry(60, 60, 800, 600)
        
    
        # Кнопка возврата
        self.back_button = QPushButton('Назад', self)
        self.back_button.setGeometry(350, 20, 80, 30)
        
        self.back_button.clicked.connect(self.goBack)
    
            
            

        # Создаем таблицу Qt для отображения данных
        self.tableWidget = QTableWidget(self)
        
        self.tableWidget.setGeometry(50, 80, 600, 400)
        
        # Подключаемся к базе данных MySQL
        try:
            self.conn = mysql.connector.connect(
                host='0.0.0.0',
                user='test',
                password='testtest',
                database='test'
            )
            self.cursor = self.conn.cursor()
            
            
            self.cursor.execute('SELECT * FROM supplier_ingredient')
            rows = self.cursor.fetchall()
            
            
            num_rows = len(rows)
            num_cols = len(rows[0])
            columns = ["id","Поставщик","Адрес"]
            self.tableWidget.setRowCount(num_rows)
            self.tableWidget.setColumnCount(num_cols)
            self.tableWidget.setHorizontalHeaderLabels(columns)
            
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(i, j, item)


            
            

        except mysql.connector.Error as e:
            print("Ошибка подключения к MySQL:", e)
        
        finally:
            self.cursor.close()
            self.conn.close()
   


    def goBack(self):
        self.close()        


class TableWindow4(QWidget):
    def __init__(self, table_name):
        super().__init__()

        self.table_name = table_name
        

        self.initUI()
        
        
        

    def initUI(self):

        self.setWindowTitle(f'Таблица {self.table_name}')
        self.setGeometry(60, 60, 800, 600)
        
    
        # Кнопка возврата
        self.back_button = QPushButton('Назад', self)
        self.back_button.setGeometry(350, 20, 80, 30)
        
        self.back_button.clicked.connect(self.goBack)
    
            
            

        # Создаем таблицу Qt для отображения данных
        self.tableWidget = QTableWidget(self)
        
        self.tableWidget.setGeometry(50, 80, 600, 400)
        
        # Подключаемся к базе данных MySQL
        try:
            self.conn = mysql.connector.connect(
                host='0.0.0.0',
                user='test',
                password='testtest',
                database='test'
            )
            self.cursor = self.conn.cursor()
            query = """
SELECT recipe_name AS 'Рецепт', recipe_def AS 'Описание', SUM(calories) AS 'Калорийность'
FROM (
    SELECT recipe_name, recipe_def, calories
    FROM recipes
    JOIN ingredients ON recipes.ingredient_id_1 = ingredients.ingredient_id
    UNION
    SELECT recipe_name, recipe_def, calories
    FROM recipes
    JOIN ingredients ON recipes.ingredient_id_2 = ingredients.ingredient_id
    UNION
    SELECT recipe_name, recipe_def, calories
    FROM recipes
    JOIN ingredients ON recipes.ingredient_id_3 = ingredients.ingredient_id
) AS subquery
GROUP BY subquery.recipe_name, subquery.recipe_def
ORDER BY SUM(calories)
"""
            
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            
            # Определите количество строк и столбцов для таблицы Qt
            num_rows = len(rows)
            num_cols = len(rows[0])
            columns = ["Рецепт","Описание","Калорийность"]
            self.tableWidget.setRowCount(num_rows)
            self.tableWidget.setColumnCount(num_cols)
            self.tableWidget.setHorizontalHeaderLabels(columns)
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
   


    def goBack(self):
        self.close()        

class TableWindow5(QWidget):
    def __init__(self, table_name):
        super().__init__()

        self.table_name = table_name
        

        self.initUI()
        
        
        

    def initUI(self):
        query ="""SELECT recipe_name AS Рецепт ,recipe_def AS Описание

FROM (



SELECT   recipe_name,recipe_def,calories
  from recipes 
  JOIN ingredients
    ON recipes.ingredient_id_1 = ingredients.ingredient_id 
  
UNION
    
     

SELECT recipe_name,recipe_def,calories 
  from recipes 
  JOIN ingredients
    ON recipes.ingredient_id_2 = ingredients.ingredient_id 
      
UNION

SELECT recipe_name,recipe_def,calories 
  from recipes 
  JOIN ingredients
    ON recipes.ingredient_id_3 = ingredients.ingredient_id 
      

ORDER BY recipe_def

) as subquerry

GROUP BY subquerry.recipe_name,subquerry.recipe_def 
ORDER BY subquerry.recipe_name





"""
        self.setWindowTitle(f'Таблица {self.table_name}')
        self.setGeometry(60, 60, 800, 600)
        
    
        # Кнопка возврата
        self.back_button = QPushButton('Назад', self)
        self.back_button.setGeometry(350, 20, 80, 30)
        
        self.back_button.clicked.connect(self.goBack)
    
            
            

        # Создаем таблицу Qt для отображения данных
        self.tableWidget = QTableWidget(self)
        
        self.tableWidget.setGeometry(50, 80, 600, 400)
        
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
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            
            # Определите количество строк и столбцов для таблицы Qt
            num_rows = len(rows)
            num_cols = len(rows[0])
            columns = ["id","Поставщик","Адрес"]
            self.tableWidget.setRowCount(num_rows)
            self.tableWidget.setColumnCount(num_cols)
            self.tableWidget.setHorizontalHeaderLabels(columns)
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
   


    def goBack(self):
        self.close()        

class TableWindow6(QWidget):
    def __init__(self,table_name):
        super().__init__()
        self.table_name = table_name

        self.initUI()

    def initUI(self):
    	
        self.setWindowTitle(f'Таблица {self.table_name}')
        self.setGeometry(100, 100, 400, 200)
        
        
        self.radio_button1 = QRadioButton('INSERT (Добавление записи)', self)
        self.radio_button2 = QRadioButton('Update (Обновление существующей записи)', self)
        self.radio_button1.setChecked(True) 
        

        # Создаем поля для ввода

        self.product_id_input = QLineEdit(self)
        self.product_id_input.setPlaceholderText('Код продукта (уникальное значение)')
        self.product_def_input = QLineEdit(self)
        self.product_def_input.setPlaceholderText('Название продукта')
        self.recipe_id_input = QLineEdit(self)
        self.recipe_id_input.setPlaceholderText('Код рецепта')
        self.ingredient_id_input = QLineEdit(self)
        self.ingredient_id_input.setPlaceholderText('Код ингредиента (ознакомьтесь с таблицей  )')

        self.back_button = QPushButton('Назад', self)
        self.back_button.clicked.connect(self.goBack)
        # Создаем кнопку "Добавить/Обновить"од
        self.add_button = QPushButton('Добавить/Обновить', self)
        self.add_button.clicked.connect(self.checkStatus)
	
        # Создаем макет и добавляем виджеты
        layout = QVBoxLayout()
        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)
        layout.addWidget(QLabel('Код продукта:'))
        layout.addWidget(self.product_id_input)
        layout.addWidget(QLabel('Название продукта:'))
        layout.addWidget(self.product_def_input)
        layout.addWidget(QLabel('Код рецепта:'))
        layout.addWidget(self.recipe_id_input)
        layout.addWidget(QLabel('Код ингредиента :'))
        layout.addWidget(self.ingredient_id_input)
        layout.addWidget(self.back_button)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def checkStatus(self):
        if self.radio_button1.isChecked():
            self.addProduct()

        else:
            self.updateProduct()


    def addProduct(self):
        # Получаем данные из полей ввода
        product_id = self.product_id_input.text()
        product_def = self.product_def_input.text()
        recipe_id = self.recipe_id_input.text()
        ingredient_id = self.ingredient_id_input.text()

        # Подключаемся к базе данных MySQL
        try:
            conn = mysql.connector.connect(
                host='0.0.0.0',
                user='test',
                password='testtest',
                database='test'
            )
            cursor = conn.cursor()

            # Выполняем INSERT запрос
            query = """
            INSERT INTO products (product_id, product_def, recipe_id, ingredient_id)
            VALUES (%s, %s, %s, %s)
            """
            values = (product_id, product_def, recipe_id, ingredient_id)
            cursor.execute(query, values)

            # Подтверждаем изменения в базе данных
            conn.commit()
            result_message = "Продукт успешно добавлен!"
            QMessageBox.information(self, 'Результат', result_message)

        except mysql.connector.Error as e:
            result_message = "Ошибка при добавлении продукта:" 
            QMessageBox.information(self, 'Результат', result_message)
  
        finally:
            cursor.close()
            conn.close()
     
    def updateProduct(self):

        # Получаем данные из полей ввода
        product_id = self.product_id_input.text()
        product_def = self.product_def_input.text()
        recipe_id = self.recipe_id_input.text()
        ingredient_id = self.ingredient_id_input.text()

        # Подключаемся к базе данных MySQL
        try:
            conn = mysql.connector.connect(
                host='0.0.0.0',
                user='test',
                password='testtest',
                database='test'
            )
            cursor = conn.cursor()

            # Выполняем Update запрос
            query = """
            Update products 
            SET 
             product_def = %s, 
             recipe_id = %s,
             ingredient_id = %s
            WHERE product_id = %s 
        
            """
            values = (product_def, recipe_id, ingredient_id,product_id)
            cursor.execute(query, values)

            # Подтверждаем изменения в базе данных
            conn.commit()
            result_message = "Продукт успешно обновлен!"
            QMessageBox.information(self, 'Результат', result_message)


        except mysql.connector.Error as e:
            result_message = "Ошибка при добавлении продукта:" 
            QMessageBox.information(self, 'Результат', result_message)
  
        finally:
            cursor.close()
            conn.close()










    def goBack(self):
        self.close()
        

class TableWindow7(QWidget):
    def __init__(self,table_name):
        super().__init__()
        self.table_name = table_name

        self.initUI()

    def initUI(self):
    	
        self.setWindowTitle(f'Таблица {self.table_name}')
        self.setGeometry(100, 100, 400, 200)

        self.radio_button1 = QRadioButton('INSERT (Добавление записи)', self)
        self.radio_button2 = QRadioButton('Update (Обновление существующей записи)', self)
        self.radio_button1.setChecked(True) 
        
        
        

        # Создаем поля для ввода
        self.recipe_id_input = QLineEdit(self)
        self.recipe_id_input.setPlaceholderText('Код рецепта(уникальное значение)')
        self.measure_input = QLineEdit(self)
        self.measure_input.setPlaceholderText('Выход(граммы)')
        self.recipe_name_input = QLineEdit(self)
        self.recipe_name_input.setPlaceholderText('Название рецепта')
        self.recipe_def_input = QLineEdit(self)
        self.recipe_def_input.setPlaceholderText('Описание рецепта')

        self.author_id_input = QLineEdit(self)
        self.author_id_input.setPlaceholderText('Код автора(1-20)')
        self.method_id_input = QLineEdit(self)
        self.method_id_input.setPlaceholderText('Код метода готовки(1-7)')
        self.ingredient_id_1_input = QLineEdit(self)
        self.ingredient_id_1_input.setPlaceholderText('Код ингредиента 1(если блюдо состоит из одного ингредиента заполните оставшиеся поля "0")')
        self.ingredient_id_2_input = QLineEdit(self)
        self.ingredient_id_2_input.setPlaceholderText('Код ингредиента 2')
        self.ingredient_id_3_input = QLineEdit(self)
        self.ingredient_id_3_input.setPlaceholderText('Код ингредиента 3')


        self.back_button = QPushButton('Назад', self)
        self.back_button.clicked.connect(self.goBack)
        # Создаем кнопку "Добавить/Обновить"
        self.add_button = QPushButton('Добавить/Обновить', self)

        self.add_button.clicked.connect(self.checkStatus)
     
            
        # Создаем макет и добавляем виджетыself.add_button.clicked.connect(self.addProduct)
        layout = QVBoxLayout()
        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)
        layout.addWidget(QLabel('Код рецепта:'))
        layout.addWidget(self.recipe_id_input)
        layout.addWidget(QLabel('Выход:'))
        layout.addWidget(self.measure_input)
        layout.addWidget(QLabel('Название рецепта:'))
        layout.addWidget(self.recipe_name_input)
        layout.addWidget(QLabel('Описание рецепта:'))
        layout.addWidget(self.recipe_def_input)
        layout.addWidget(QLabel('Код автора:'))
        layout.addWidget(self.author_id_input)
        layout.addWidget(QLabel('Код метода готовки:'))
        layout.addWidget(self.method_id_input)
        layout.addWidget(QLabel('Код ингредиента (ознакомьтесь с таблицей):'))
        layout.addWidget(self.ingredient_id_1_input)
        layout.addWidget(QLabel('Код ингредиента (ознакомьтесь с таблицей):'))
        layout.addWidget(self.ingredient_id_2_input)
        layout.addWidget(QLabel('Код ингредиента (ознакомьтесь с таблицей):'))
        layout.addWidget(self.ingredient_id_3_input)
        layout.addWidget(self.back_button)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def addProduct(self):
        # Получаем данные из полей ввода
        

        recipe_id = self.recipe_id_input.text()
        measure	= self.measure_input.text()	
        recipe_name	 = self.recipe_name_input.text()	
        recipe_def	 = self.recipe_def_input.text()	
        author_id	= self.author_id_input.text()	
        method_id	= self.method_id_input.text()	
        ingredient_id_1	= self.ingredient_id_1_input.text()
        ingredient_id_2	= self.ingredient_id_1_input.text()
        ingredient_id_3 = self.ingredient_id_1_input.text()

        # Подключаемся к базе данных MySQL
        try:
            conn = mysql.connector.connect(
                host='0.0.0.0',
                user='test',
                password='testtest',
                database='test'
            )
            cursor = conn.cursor()

            # Выполняем INSERT запрос
            query = """
            INSERT INTO recipes (recipe_id	,measure	,recipe_name	,recipe_def	,author_id	,method_id	,ingredient_id_1	,ingredient_id_2	,ingredient_id_3)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)
            """
            values = (recipe_id	,measure	,recipe_name	,recipe_def	,author_id	,method_id	,ingredient_id_1	,ingredient_id_2	,ingredient_id_3)
            cursor.execute(query, values)

            # Подтверждаем изменения в базе данных
            conn.commit()
            result_message = "Рецепт успешно добавлен!"
            QMessageBox.information(self, 'Результат', result_message)
            

        except mysql.connector.Error as e:
            result_message = "Ошибка при добавлении рецепта:" 
            QMessageBox.information(self, 'Результат', result_message)
  
        finally:
            cursor.close()
            conn.close()

    def updateProduct(self):
    # Получаем данные из полей ввода
        recipe_id = self.recipe_id_input.text()
        measure = self.measure_input.text()
        recipe_name = self.recipe_name_input.text()
        recipe_def = self.recipe_def_input.text()
        author_id = self.author_id_input.text()
        method_id = self.method_id_input.text()
        ingredient_id_1 = self.ingredient_id_1_input.text()
        ingredient_id_2 = self.ingredient_id_2_input.text()
        ingredient_id_3 = self.ingredient_id_3_input.text()

        # Подключаемся к базе данных MySQL
        try:
            conn = mysql.connector.connect(
                host='0.0.0.0',
                user='test',
                password='testtest',
                database='test'
            )
            cursor = conn.cursor()

            # Выполняем UPDATE запрос
            query = """
            UPDATE recipes 
            SET 
                measure = %s,
                recipe_name = %s,
                recipe_def = %s,
                author_id = %s,
                method_id = %s,
                ingredient_id_1 = %s,
                ingredient_id_2 = %s,
                ingredient_id_3 = %s
            WHERE recipe_id = %s
            """
            values = (
                measure,
                recipe_name,
                recipe_def,
                author_id,
                method_id,
                ingredient_id_1,
                ingredient_id_2,
                ingredient_id_3,
                recipe_id
                
            )
            cursor.execute(query, values)

            # Подтверждаем изменения в базе данных
            conn.commit()
            result_message = "Рецепт успешно обновлен!"
            QMessageBox.information(self, 'Результат', result_message)

        except mysql.connector.Error as e:
            result_message = "Ошибка при обновлении рецепта:" 
            QMessageBox.information(self, 'Результат', result_message)

        finally:
            cursor.close()
            conn.close()

    def checkStatus(self):
        if self.radio_button1.isChecked():
            self.addProduct()
        else:
            self.updateProduct()

        

    def goBack(self):
        self.close()        

class TableWindow8(QWidget):
    def __init__(self,table_name):
        super().__init__()
        self.table_name = table_name

        self.initUI()

    def initUI(self):
    	
        self.setWindowTitle(f'Таблица {self.table_name}')
        self.setGeometry(100, 100, 400, 200)

        self.radio_button1 = QRadioButton('INSERT (Добавление записи)', self)
        self.radio_button2 = QRadioButton('Update (Обновление существующей записи)', self)
        
        self.radio_button1.setChecked(True) 
        
        
        

        # Создаем поля для ввода
        self.supplier_id_input = QLineEdit(self)
        self.supplier_id_input.setPlaceholderText('Код поставщика(уникальное значение)')
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('Название поставщика')
        self.address_input = QLineEdit(self)
        self.address_input.setPlaceholderText('Адрес поставщика(ПР. 999 Проспект Доставки, Киев)')
        


        self.back_button = QPushButton('Назад', self)
        self.back_button.clicked.connect(self.goBack)
        # Создаем кнопку "Добавить/Обновить"
        self.add_button = QPushButton('Добавить/Обновить', self)
        
        self.add_button.clicked.connect(self.checkStatus)
        # Создаем макет и добавляем виджеты
        layout = QVBoxLayout()
        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)
        layout.addWidget(QLabel('Код поставщика:'))
        layout.addWidget(self.supplier_id_input)
        layout.addWidget(QLabel('Название:'))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel('Адрес:'))
        layout.addWidget(self.address_input)
        layout.addWidget(self.back_button)
        layout.addWidget(self.add_button)
        

        self.setLayout(layout)

    def addProduct(self):
        # Получаем данные из полей ввода
        

        supplier_id = self.supplier_id_input.text()
        name	= self.name_input.text()
        address	 = self.address_input.text()
        
        

        # Подключаемся к базе данных MySQL
        try:
            conn = mysql.connector.connect(
                host='0.0.0.0',
                user='test',
                password='testtest',
                database='test'
            )
            cursor = conn.cursor()

            # Выполняем INSERT запрос
            query = """
            INSERT INTO supplier_ingredient (supplier_id,name,address)
            VALUES (%s, %s, %s)
            """
            values = (supplier_id,name,address)
            cursor.execute(query, values)

            # Подтверждаем изменения в базе данных
            conn.commit()
            result_message = "Поставщик успешно добавлен!"
            QMessageBox.information(self, 'Результат', result_message)
            

        except mysql.connector.Error as e:
            result_message = "Ошибка при добавлении поставщика :" 
            QMessageBox.information(self, 'Результат', result_message)
  
        finally:
            cursor.close()
            conn.close()
     
    
    def goBack(self):
        self.close()  

    def checkStatus(self):
        if self.radio_button1.isChecked():
            self.addProduct()
        else: 
            self.updateProduct()          

    def updateProduct(self):
        # Получаем данные из полей ввода
        

        supplier_id = self.supplier_id_input.text()
        name	= self.name_input.text()
        address	 = self.address_input.text()
        
        

        # Подключаемся к базе данных MySQL
        try:
            conn = mysql.connector.connect(
                host='0.0.0.0',
                user='test',
                password='testtest',
                database='test'
            )
            cursor = conn.cursor()

            # Выполняем INSERT запрос
            query = """
            UPDATE supplier_ingredient 
            SET
                name = %s,
                address = %s
            WHERE supplier_id = %s
            
            """
            values = (name,address,supplier_id)
            cursor.execute(query, values)

            # Подтверждаем изменения в базе данных
            conn.commit()
            result_message  = "Поставщик успешно обновлен!"
            QMessageBox.information(self, 'Результат', result_message)
            

        except mysql.connector.Error as e:
            result_message = "Ошибка при добавлении поставщика :" 
            QMessageBox.information(self, 'Результат', result_message)
  
        finally:
            cursor.close()
            conn.close()
     
    
class TableWindow9(QWidget):
    def __init__(self,table_name):
        super().__init__()
        self.table_name = table_name

        self.initUI()

    def initUI(self):
    	
        self.setWindowTitle(f'Таблица {self.table_name}')
        self.setGeometry(100, 100, 400, 200)

        self.radio_button1 = QRadioButton('Таблица продукты', self)
        self.radio_button2 = QRadioButton('Таблица рецепты', self)
        self.radio_button3 = QRadioButton('Таблица поставщиков', self)
        
        self.radio_button1.setChecked(True) 
        
        
        

        # Создаем поля для ввода
        self.id_input = QLineEdit(self)
        self.id_input.setPlaceholderText('Код записи(ознакомтесь с таблицей)')
        

        self.back_button = QPushButton('Назад', self)
        self.back_button.clicked.connect(self.goBack)
        # Создаем кнопку "Добавить/Обновить"
        self.add_button = QPushButton('Удалить', self)
        
        self.add_button.clicked.connect(self.checkStatus)
        # Создаем макет и добавляем виджеты
        layout = QVBoxLayout()
        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)
        layout.addWidget(self.radio_button3)
        layout.addWidget(QLabel('Код :'))
        layout.addWidget(self.id_input)
        layout.addWidget(self.back_button)
        layout.addWidget(self.add_button)
        

        self.setLayout(layout)


    def deleteProduct(self, flag):
        # Получаем данные из полей ввода
        input_id = self.id_input.text()

        # Подключаемся к базе данных MySQL
        try:
            conn = mysql.connector.connect(
                host='0.0.0.0',
                user='test',
                password='testtest',
                database='test'
            )
            cursor = conn.cursor()

            # Выполняем Delete запрос
            query_product = """
            DELETE FROM products WHERE product_id = %s
            """

            query_recipe = """
            DELETE FROM recipes WHERE recipe_id = %s
            """
            query_suppliers = """
            DELETE FROM supplier_ingredient WHERE supplier_id = %s
            """
            values = (input_id,)  # Обратите внимание на запятую после input_id
            if flag == 1:
                cursor.execute(query_product, values)
            elif flag == 2:
                cursor.execute(query_recipe, values)
            elif flag == 3:
                cursor.execute(query_suppliers, values)
            # Подтверждаем изменения в базе данных
            conn.commit()
            result_message = "Запись успешно удалена!"
            QMessageBox.information(self, 'Результат', result_message)

        except mysql.connector.Error as e:
            result_message = "Ошибка при удалении (проверьте корректность id):" 
            QMessageBox.information(self, 'Результат', result_message)

        finally:
            cursor.close()
            conn.close()

     
    
    def goBack(self):
        self.close()  

    def checkStatus(self):
        if self.radio_button1.isChecked():
            self.deleteProduct(1)
        elif self.radio_button2.isChecked(): 
            self.deleteProduct(2)          
        elif self.radio_button3.isChecked():
            self.deleteProduct(3)    


class TableWindow10(QWidget):
    def __init__(self,table_name):
        super().__init__()
        self.table_name = table_name

        self.initUI()

    def initUI(self):
    	
        self.setWindowTitle(f'Таблица {self.table_name}')
        self.setGeometry(100, 100, 400, 200)

        
        
        
        

        # Создаем поля для ввода
        self.data_input = QLineEdit(self)
        self.data_input.setPlaceholderText('Дата(ознакомтесь с таблицей) Пр: 2023-09-14')
        

        self.back_button = QPushButton('Назад', self)
        self.back_button.clicked.connect(self.goBack)
        # Создаем кнопку "Добавить/Обновить"
        self.add_button = QPushButton('Поиск', self)
        
        

        self.tableWidget = QTableWidget(self)
        
        self.tableWidget.setGeometry(50, 80, 400, 600)

        self.add_button.clicked.connect(self.checkProduct)
        # Создаем макет и добавляем виджеты
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Дата :'))
        layout.addWidget(self.data_input)
        layout.addWidget(self.back_button)
        layout.addWidget(self.add_button)
        layout.addWidget(self.tableWidget)
        

        self.setLayout(layout)


    def checkProduct(self):
        # Получаем данные из полей ввода
        data_id = self.data_input.text()

        # Подключаемся к базе данных MySQL
        try:
            conn = mysql.connector.connect(
                host='0.0.0.0',
                user='test',
                password='testtest',
                database='test'
            )
            cursor = conn.cursor()

            # Выполняем Select запрос
            query = """
            SELECT date_receipt,supplier_ingredient.name,ingredient_def,address,price
            FROM supplier_ingredient
            JOIN ingredients ON supplier_ingredient.supplier_id = ingredients.supplier_id
            JOIN way_bills ON ingredients.bill_id = way_bills.bill_id
            WHERE date_receipt = %s
            """

            values = (data_id,)

            cursor.execute(query, values)
            # Получаем все строки результата
            rows = cursor.fetchall()

            if rows:
                # Определите количество строк и столбцов для таблицы Qt
                num_rows = len(rows)
                num_cols = len(rows[0])
                columns = ["Дата","Имя","Ингредиент","Адрес","Цена"]
                self.tableWidget.setRowCount(num_rows)
                self.tableWidget.setColumnCount(num_cols)
                self.tableWidget.setHorizontalHeaderLabels(columns)
                # Заполните таблицу Qt данными из MySQL
                for i, row in enumerate(rows):
                    for j, value in enumerate(row):
                        item = QTableWidgetItem(str(value))
                        self.tableWidget.setItem(i, j, item)
            else:
                # Если результат пуст, очистите таблицу
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(0)
                self.tableWidget.clearContents()
                QMessageBox.information(self, 'Результат', 'Нет данных для отображения.')

        except mysql.connector.Error as e:
            result_message = "Ошибка при поиске (проверьте корректность даты):" 
            QMessageBox.information(self, 'Результат', result_message)

        finally:
            cursor.close()
            conn.close()
        
        
    def goBack(self):
            self.close()  

      



def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
