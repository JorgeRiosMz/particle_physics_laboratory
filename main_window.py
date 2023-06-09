from ui_main_window import Ui_MainWindow
from particula import Particula
from registro_particulas import Registro_particulas

from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform

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
        
        self.scene = QGraphicsScene()
        self.ui.scene.setScene(self.scene)
        
        self.ui.imprimir_particula_scene.clicked.connect(self.buscar_particula_scene)
        self.ui.imprimir_todas_scene.clicked.connect(self.imprimir_todas_scene)
        self.ui.limpiar_scene.clicked.connect(self.limpiar_scene)
        
        self.ui.actionPor_Distancia.triggered.connect(self.sort_by_distancia)
        self.ui.actionPor_Velocidad.triggered.connect(self.sort_by_velocidad)
        self.ui.actionPor_ID.triggered.connect(self.sort_by_id)
        
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

        

#___Scene____________________________________________________________


    @Slot()
    def wheelEvent(self, event):
        print(event.delta())
        if event.delta() > 0:
            self.ui.scene.scale(1.2, 1.2)
        else:
            self.ui.scene.scale(0.8, 0.8)



    @Slot()
    def imprimir_particula_scene(self, particula:Particula):
        x_ori = particula.posicion_origen.x
        y_ori = particula.posicion_origen.y
        x_des = particula.posicion_destino.x
        y_des = particula.posicion_destino.y
        
        color = QColor(particula.color[0], particula.color[1], particula.color[2])
        pen = QPen()
        pen.setWidth(4)
        pen.setColor(color)
        
        self.scene.addEllipse(x_ori, y_ori, 3, 3, pen)
        self.scene.addEllipse(x_des, y_des, 3, 3, pen)
        self.scene.addLine(x_ori, y_ori, x_des, y_des, pen)



    @Slot()
    def imprimir_todas_scene(self):
        self.limpiar_scene()
        for particula in self.registro_particulas:
            self.imprimir_particula_scene(particula)



    @Slot()
    def buscar_particula_scene(self):
        situacion_busqueda = False  
        id = self.ui.buscar_scene_lineEdit.text()
        
        for particula in self.registro_particulas:
            if id == particula.id:
                self.limpiar_scene()
                self.imprimir_particula_scene(particula)
                
                situacion_busqueda = True
                return
            
        if situacion_busqueda != True:
            QMessageBox.warning(self, "Alerta", f"Problema al encontrar particula con id = '{id}'")
            
            
            
    @Slot()
    def limpiar_scene(self):
        self.scene.clear()


#___Ordenamientos____________________________________________________

    def get_p_id(self, particula):
        return particula.id
    def get_p_distancia(self, particula):
        return particula.movimiento.distancia
    def get_p_velocidad(self, particula):
        return particula.movimiento.velocidad
    
    @Slot()
    def sort_by_id(self):
        self.registro_particulas.particulas.sort(key = self.get_p_id)
        
    @Slot()
    def sort_by_distancia(self):
        self.registro_particulas.particulas.sort(key = self.get_p_distancia, reverse = True) 
    
    @Slot()
    def sort_by_velocidad(self):
        self.registro_particulas.particulas.sort(key = self.get_p_velocidad)


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