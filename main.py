import sys
from PySide2.QtWidgets import QApplication
from main_window import MainWindow



def crear_aplicacion():
    app = QApplication()

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())



if __name__ == "__main__":
    crear_aplicacion()
    
else:
    exit(1)