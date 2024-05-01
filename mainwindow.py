from PySide2.QtWidgets import QMainWindow, QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from random import randint
from algoritmos import get_puntos, puntos_mas_cercanos
from pprint import pprint

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    self.puntos = []
#Botones
    self.ui.dibujar.clicked.connect(self.dibujar)
    self.ui.limpiar.clicked.connect(self.limpiar)
#Declaracion de objeto escena
    self.scene = QGraphicsScene()
    self.ui.graphicsView.setScene(self.scene)
#FUERZA BRUTA 22/04/2024
    self.ui.spinBox_puntos.valueChanged[int].connect(self.spinBox_puntos)
    self.ui.horizontalSlider.valueChanged[int].connect(self.slider_puntos)
    self.ui.actionPuntos.triggered.connect(self.dibujar_puntos)
    self.ui.actionPuntos_Cercanos.triggered.connect(self.mostrar_puntos_cercanos)

  @Slot()
  def mostrar_puntos_cercanos(self):
    resultado = puntos_mas_cercanos(self.puntos)
    pprint(resultado)
    for punto1, punto2 in resultado:
      x1 = punto1[0]
      y1 = punto1[1]
      x2 = punto2[0]
      y2 = punto2[1]

      self.scene.addLine(x1+3,y1+3,x2+3,y2+3)
      

  @Slot()
  def dibujar_puntos(self, x):
    self.puntos = get_puntos(self.ui.spinBox_puntos.value())
    pprint(self.puntos)

    for punto in self.puntos:
      x = punto[0]
      y = punto[1]
      self.scene.addEllipse(x,y,6,6)
      

  @Slot(int)
  def spinBox_puntos(self, x):
    #print(x)
    self.ui.horizontalSlider.setValue(x)

  @Slot(int)
  def slider_puntos(self, x):
    #print(x)
    self.ui.spinBox_puntos.setValue(x)

  @Slot()
  def dibujar(self):
    pen = QPen()
    pen.setWidth(2)
    for i in range (0,100):
      r = randint(0,255)
      g = randint(0,255)
      b = randint(0,255)
      color = QColor(r,g,b)
      pen.setColor(color)

      x_origen = randint(0, 500)
      y_origen = randint(0, 500)
      x_destino = randint(0, 500)
      y_destino = randint(0, 500)

      #Origen (0,0)
      self.scene.addEllipse(x_origen,y_origen,6,6,pen)   #(x,y,diametro1,diametro2)
      self.scene.addEllipse(x_destino,y_destino,6,6,pen)
      self.scene.addLine(x_origen+3,y_origen+3,x_destino+3,y_destino+3,pen)

  @Slot()
  def limpiar(self):
    self.scene.clear()

#Zoom
  def wheelEvent(self,event):
    #print(event.delta())
    if event.delta() > 0:
      self.ui.graphicsView.scale(1.2,1.2)
    else:
      self.ui.graphicsView.scale(0.8,0.8)