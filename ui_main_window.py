# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(818, 649)
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.registro_label = QLabel(self.tab)
        self.registro_label.setObjectName(u"registro_label")
        self.registro_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.registro_label, 0, 0, 1, 5)

        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_4.addWidget(self.plainTextEdit, 1, 1, 4, 4)

        self.disponibilidad_pushButton = QPushButton(self.tab)
        self.disponibilidad_pushButton.setObjectName(u"disponibilidad_pushButton")

        self.gridLayout_4.addWidget(self.disponibilidad_pushButton, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.origen_label = QLabel(self.frame_2)
        self.origen_label.setObjectName(u"origen_label")
        self.origen_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.origen_label, 0, 0, 1, 4)

        self.direccion_label = QLabel(self.frame_2)
        self.direccion_label.setObjectName(u"direccion_label")
        self.direccion_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.direccion_label, 3, 0, 1, 4)

        self.velocidad_label = QLabel(self.frame_2)
        self.velocidad_label.setObjectName(u"velocidad_label")
        self.velocidad_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.velocidad_label, 6, 0, 1, 1)

        self.direccion_y_label = QLabel(self.frame_2)
        self.direccion_y_label.setObjectName(u"direccion_y_label")
        self.direccion_y_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.direccion_y_label, 5, 0, 1, 1)

        self.origen_y_label = QLabel(self.frame_2)
        self.origen_y_label.setObjectName(u"origen_y_label")
        self.origen_y_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.origen_y_label, 2, 0, 1, 1)

        self.origen_x_label = QLabel(self.frame_2)
        self.origen_x_label.setObjectName(u"origen_x_label")
        self.origen_x_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.origen_x_label, 1, 0, 1, 1)

        self.origen_x_spinBox = QSpinBox(self.frame_2)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")

        self.gridLayout_2.addWidget(self.origen_x_spinBox, 1, 1, 1, 3)

        self.origen_y_spinBox = QSpinBox(self.frame_2)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")

        self.gridLayout_2.addWidget(self.origen_y_spinBox, 2, 1, 1, 3)

        self.direccion_x_label = QLabel(self.frame_2)
        self.direccion_x_label.setObjectName(u"direccion_x_label")
        self.direccion_x_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.direccion_x_label, 4, 0, 1, 1)

        self.direccion_x_spinBox = QSpinBox(self.frame_2)
        self.direccion_x_spinBox.setObjectName(u"direccion_x_spinBox")

        self.gridLayout_2.addWidget(self.direccion_x_spinBox, 4, 1, 1, 3)

        self.direccion_y_spinBox = QSpinBox(self.frame_2)
        self.direccion_y_spinBox.setObjectName(u"direccion_y_spinBox")

        self.gridLayout_2.addWidget(self.direccion_y_spinBox, 5, 1, 1, 3)

        self.velocidad_horizontalSlider = QSlider(self.frame_2)
        self.velocidad_horizontalSlider.setObjectName(u"velocidad_horizontalSlider")
        self.velocidad_horizontalSlider.setMaximum(150)
        self.velocidad_horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.velocidad_horizontalSlider, 6, 1, 1, 2)

        self.velocidad_contador_label = QLabel(self.frame_2)
        self.velocidad_contador_label.setObjectName(u"velocidad_contador_label")
        self.velocidad_contador_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.velocidad_contador_label, 6, 3, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 3, 0, 1, 1)

        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.color_label = QLabel(self.frame)
        self.color_label.setObjectName(u"color_label")
        self.color_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.color_label, 0, 0, 1, 2)

        self.red_label = QLabel(self.frame)
        self.red_label.setObjectName(u"red_label")
        self.red_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.red_label, 1, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.frame)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.red_spinBox, 1, 1, 1, 1)

        self.green_label = QLabel(self.frame)
        self.green_label.setObjectName(u"green_label")
        self.green_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.green_label, 2, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.frame)
        self.green_spinBox.setObjectName(u"green_spinBox")

        self.gridLayout.addWidget(self.green_spinBox, 2, 1, 1, 1)

        self.blue_label = QLabel(self.frame)
        self.blue_label.setObjectName(u"blue_label")
        self.blue_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.blue_label, 3, 0, 1, 1)

        self.blue_spinBox = QSpinBox(self.frame)
        self.blue_spinBox.setObjectName(u"blue_spinBox")

        self.gridLayout.addWidget(self.blue_spinBox, 3, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 4, 0, 2, 1)

        self.limpiar_pushButton = QPushButton(self.tab)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout_4.addWidget(self.limpiar_pushButton, 5, 1, 1, 1)

        self.imprimir_pushButton = QPushButton(self.tab)
        self.imprimir_pushButton.setObjectName(u"imprimir_pushButton")

        self.gridLayout_4.addWidget(self.imprimir_pushButton, 5, 2, 1, 1)

        self.agregar_inicio_pushButton = QPushButton(self.tab)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout_4.addWidget(self.agregar_inicio_pushButton, 5, 3, 1, 1)

        self.agregar_final_pushButton = QPushButton(self.tab)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout_4.addWidget(self.agregar_final_pushButton, 5, 4, 1, 1)

        self.id_lineEdit = QLineEdit(self.tab)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout_4.addWidget(self.id_lineEdit, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.gridLayout_6 = QGridLayout(self.tab2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabla_de_busqueda_label = QLabel(self.tab2)
        self.tabla_de_busqueda_label.setObjectName(u"tabla_de_busqueda_label")
        self.tabla_de_busqueda_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.tabla_de_busqueda_label, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.tab2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.buscar_tabla_pushButton = QPushButton(self.frame_3)
        self.buscar_tabla_pushButton.setObjectName(u"buscar_tabla_pushButton")

        self.gridLayout_5.addWidget(self.buscar_tabla_pushButton, 1, 1, 1, 1)

        self.buscar_tabla_lineEdit = QLineEdit(self.frame_3)
        self.buscar_tabla_lineEdit.setObjectName(u"buscar_tabla_lineEdit")

        self.gridLayout_5.addWidget(self.buscar_tabla_lineEdit, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.tab2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget = QTableWidget(self.frame_4)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 2)

        self.imprimir_tabla_pushButton = QPushButton(self.frame_4)
        self.imprimir_tabla_pushButton.setObjectName(u"imprimir_tabla_pushButton")

        self.gridLayout_3.addWidget(self.imprimir_tabla_pushButton, 1, 0, 1, 1)

        self.limpiar_tabla_pushButton = QPushButton(self.frame_4)
        self.limpiar_tabla_pushButton.setObjectName(u"limpiar_tabla_pushButton")

        self.gridLayout_3.addWidget(self.limpiar_tabla_pushButton, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_4, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab2, "")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 818, 30))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionAbrir)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar (ctrl + s)", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir (ctrl + o)", None))
        self.registro_label.setText(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.disponibilidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Comprobar disponibilidad", None))
        self.origen_label.setText(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.direccion_label.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.velocidad_label.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.direccion_y_label.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.origen_y_label.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.origen_x_label.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.direccion_x_label.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.velocidad_contador_label.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.color_label.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.red_label.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.green_label.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.blue_label.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.imprimir_pushButton.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.tabla_de_busqueda_label.setText(QCoreApplication.translate("MainWindow", u"Tabla de busqueda", None))
        self.buscar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.imprimir_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Imprimir Tabla", None))
        self.limpiar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Tabla de busqueda", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

