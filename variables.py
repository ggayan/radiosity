windowId = -1

#parametros del punto de vista
# punto de vista inicial
IVX = 4
IVY = 4
IVZ = 4

# objetivo de camara inicial
LAX = 0
LAY = 0
LAZ = 0

#el punto desde el cual miro
VIEWPOINT_X = IVX
VIEWPOINT_Y = IVY
VIEWPOINT_Z = IVZ

#el punto al cual miro
LOOK_AT_X = LAX
LOOK_AT_Y = LAY
LOOK_AT_Z = LAZ

#el vector que indica hacia donde es 'arriba' para la camara
UP_VECTOR_X = 0
UP_VECTOR_Y = 1
UP_VECTOR_Z = 0

#resolucion de la ventana
WIDTH = 800
HEIGHT = 600

#variables de los planos
SECTIONS = 1 #numero de triangulos por unidad de espacio

# intensidad de fuentes luminosas
INITINTEN = 100.0
INTENSITY = 1

# variables de los planos
size = 7.0
step = 1 / SECTIONS

XY_reflectance_red = 0.3
XY_reflectance_green = 0.3
XY_reflectance_blue = 0.3

XZ_reflectance_red = 0.1
XZ_reflectance_green = 0.6
XZ_reflectance_blue = 0.1

YZ_reflectance_red = 0.1
YZ_reflectance_green = 0.1
YZ_reflectance_blue = 0.6

FormFactors = None
Visibilidad = None

#lista completa de los parches
patchesList = []

#lista de luces
lightsList = []