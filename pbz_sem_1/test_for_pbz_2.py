import sys
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout, QPushButton, QMessageBox

class RadioWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Radio Button Example')
        self.setGeometry(100, 100, 300, 200)

        # Создаем радио-кнопки
        self.radio_button1 = QRadioButton('INSERT (Добавление записи)', self)
        self.radio_button2 = QRadioButton('Update (Обновление существующей записи)', self)
        self.radio_button1.setChecked(True)  # Устанавливаем изначальное состояние (выбрана первая опция)

        # Создаем кнопку для проверки выбранной опции
        self.check_button = QPushButton('Проверить', self)

        # Подключаем слот к кнопке
        self.check_button.clicked.connect(self.showResult)

        # Создаем макет и добавляем радио-кнопки и кнопку
        layout = QVBoxLayout()
        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)
        layout.addWidget(self.check_button)

        self.setLayout(layout)

    def showResult(self):
        if self.radio_button1.isChecked():
            result_message = 'Успешно'
        else:
            result_message = 'Провал'

        QMessageBox.information(self, 'Результат', result_message)

def main():
    app = QApplication(sys.argv)
    radio_widget = RadioWidget()
    radio_widget.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()