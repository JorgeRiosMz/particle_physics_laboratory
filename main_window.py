from ui_main_window import Ui_MainWindow
from particula import Particula
from registro_particulas import Registro_particulas

from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem

from PySide2.QtCore import Slot



class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.registro_particulas = Registro_particulas()
        
        self.ui.disponibilidad_pushButton.clicked.connect(self.disponibilidad_id)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.agregar_inicio)
        self.ui.agregar_final_pushButton.clicked.connect(self.agregar_final)
        self.ui.imprimir_pushButton.clicked.connect(self.imprimir)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)
        
        self.ui.imprimir_tabla_pushButton.clicked.connect(self.imprimir_tabla)
        self.ui.limpiar_tabla_pushButton.clicked.connect(self.limpiar_tabla)
        self.ui.buscar_tabla_pushButton.clicked.connect(self.buscar_tabla)
        
        self.ui.actionGuardar.triggered.connect(self.guardar_archivo)
        self.ui.actionAbrir.triggered.connect(self.cargar_archivo)
        
        
#___Agregar__________________________________________________________
        
        
    @Slot()
    def disponibilidad_id(self):
        pass
    
    
        
    @Slot()
    def agregar_inicio(self):
        particula = self.crear_particula()
        self.registro_particulas.agregar_particula_inicio(particula)
        
        
    @Slot()
    def agregar_final(self):
        particula = self.crear_particula()
        self.registro_particulas.agregar_particula_final(particula)
        
        
        
    def crear_particula(self):
        _id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.direccion_x_spinBox.value()
        destino_y = self.ui.direccion_y_spinBox.value()
        velocidad = self.ui.velocidad_horizontalSlider.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        
        particula = Particula(_id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        return particula
        
    
    
    @Slot()
    def imprimir(self):
        self.limpiar()
        self.registro_particulas.imprimir_particulas()
        self.ui.plainTextEdit.insertPlainText(str(self.registro_particulas))
    
    
    
    @Slot()
    def limpiar(self):
        self.ui.plainTextEdit.clear()
        
        
#___Tabla_busqueda___________________________________________________
        
        
    @Slot()
    def buscar_tabla(self):
        self.crear_tabla()      
        
        situacion_busqueda = False  
        id = self.ui.buscar_tabla_lineEdit.text()
        
        for particula in self.registro_particulas:
            if id == particula.id:
                self.limpiar_tabla()
                
                particula_items = self.a_item_tabla(particula)
                self.imprimir_particula(0, particula_items)
                
                situacion_busqueda = True
                return
            
        if situacion_busqueda != True:
            QMessageBox.warning(self, "Alerta", f"Problema al encontrar particula con id = '{id}'")            
    
    
    
    @Slot()
    def imprimir_tabla(self):
        self.crear_tabla()
        self.ui.tableWidget.setRowCount(len(self.registro_particulas))
        
        row = 0
        
        for particula in self.registro_particulas:
            particula_items = self.a_item_tabla(particula)
            self.imprimir_particula(row, particula_items)
            
            row += 1
        
        
    
    @Slot()
    def crear_tabla(self):
        self.ui.tableWidget.setColumnCount(10)
        header = ["ID",
                  "Origen X", "Origen Y",
                  "Destino X", "Destino Y",
                  "Velocidad", "Distancia",
                  "Red", "Green", "Blue"]
        self.ui.tableWidget.setHorizontalHeaderLabels(header)
    
    
    
    @Slot()
    def limpiar_tabla(self):
        self.ui.tableWidget.clear()
    
    
    
    def a_item_tabla(self, particula):
        id = QTableWidgetItem(str(particula.id))
        
        origen_x = QTableWidgetItem(str(particula.posicion_origen.x))
        origen_y = QTableWidgetItem(str(particula.posicion_origen.y))
        
        destino_x = QTableWidgetItem(str(particula.posicion_destino.x))
        destino_y = QTableWidgetItem(str(particula.posicion_destino.y))
        
        velocidad = QTableWidgetItem(str(particula.movimiento.velocidad))
        distancia = QTableWidgetItem(str(particula.movimiento.distancia))
        
        red   = QTableWidgetItem(str(particula.color[0]))
        green = QTableWidgetItem(str(particula.color[1]))
        blue  = QTableWidgetItem(str(particula.color[2]))
        
        particula_items = [id, origen_x, origen_y, destino_x, destino_y, velocidad, distancia, red, green, blue]
        
        return particula_items
        
        
        
    @Slot()
    def imprimir_particula(self,row, particula_items):
        i = 0
        for i in range(10):
            self.ui.tableWidget.setItem(row, i, particula_items[i])

        
        
#___Archivos_________________________________________________________        


    @Slot()
    def guardar_archivo(self):
        direccion = QFileDialog.getSaveFileName(
            self, 'Guardar Archivo', '.', 'JSON (*.json)')[0]
        
        if self.registro_particulas.guardar_particulas(direccion):
            QMessageBox.information(
                self, 'Exito', 'Archivo Guardado' + direccion)
            
        else:
            QMessageBox.information(
                self, 'Error', 'Error con el archivo' + direccion)
        
        
        
    @Slot()
    def cargar_archivo(self):
        direccion = QFileDialog.getOpenFileName(
            self, 'Abrir Archivo', '.', 'JSON (*.json)')[0]
        self.registro_particulas.cargar_particulas(direccion)