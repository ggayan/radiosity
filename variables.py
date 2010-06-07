windowId = -1

#parametros del punto de vista
# punto de vista inicial
IVX = 4
IVY = 4
IVZ = 4

#el punto desde el cual miro
VIEWPOINT_X = IVX
VIEWPOINT_Y = IVY
VIEWPOINT_Z = IVZ

#el punto al cual miro
LOOK_AT_X = 0
LOOK_AT_Y = 0
LOOK_AT_Z = 0

#el vector que indica hacia donde es 'arriba' para la camara
UP_VECTOR_X = 0
UP_VECTOR_Y = 1
UP_VECTOR_Z = 0

#resolucion de la ventana
WIDTH = 800
HEIGHT = 600

#variables de los planos
SECTIONS = 8 #numero de triangulos por columna de un plano

# intensidad de fuentes luminosas
INITINTEN = 300.0
INTENSITY = 1

# variables de los planos
size = 7.0
step = size / SECTIONS

XY_reflectance_red = 0.9
XY_reflectance_green = 0.1
XY_reflectance_blue = 0.1

XZ_reflectance_red = 0.1
XZ_reflectance_green = 0.9
XZ_reflectance_blue = 0.1

YZ_reflectance_red = 0.1
YZ_reflectance_green = 0.1
YZ_reflectance_blue = 0.9

FormFactors = None
Visibilidad = None

#lista completa de los parches
patchesList = []

#lista de luces
lightsList = []