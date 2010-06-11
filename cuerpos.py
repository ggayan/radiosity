from punto import *
from patch import *
from variables import *

def patchesCubo(origin,lengthx,lengthy,lengthz,lum,color):
    
    patchesCubo = []
    
    iterationsx = (int)(SECTIONS*lengthx)
    iterationsy = (int)(SECTIONS*lengthy)
    iterationsz = (int)(SECTIONS*lengthz)
    
    x0 = origin.x
    y0 = origin.y
    z0 = origin.z
    
    for i in range(0, iterationsx): #eje horizonal
        for j in range(0, iterationsy): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto(x0, y0, z0)
            p2 = Punto(x0 + step, y0, z0)
            p3 = Punto(x0, y0 + step, z0)
            p4 = Punto(x0 + step, y0 + step, z0)
            patch = Patch(p3, p4, p2, p1)
            y0 += step
                
            patch.reflectance_red = color[0]
            patch.reflectance_green = color[1]
            patch.reflectance_blue = color[2]
            # asocio el parche recien creado a la lista
            patchesCubo.append(patch)
        x0 += step
        y0 = origin.y
    #planoXZ
    x0 = origin.x
    y0 = origin.y
    z0 = origin.z
    
    for i in range(0, iterationsx): #eje horizonal
        for j in range(0, iterationsz): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto(x0, y0, z0)
            p2 = Punto(x0, y0, z0 + step)
            p3 = Punto(x0 + step, y0, z0)
            p4 = Punto(x0 + step, y0, z0 + step)
            patch = Patch(p3, p4, p2, p1)
            z0 += step
                
            patch.reflectance_red = color[0]
            patch.reflectance_green = color[1]
            patch.reflectance_blue = color[2]
            # asocio el parche recien creado a la lista
            patchesCubo.append(patch)
        x0 += step
        z0 = origin.z
        
    #planoYZ
    x0 = origin.x
    y0 = origin.y
    z0 = origin.z
    
    for i in range(0, iterationsz): #eje horizonal
        for j in range(0, iterationsy): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto( x0, y0, z0)
            p2 = Punto( x0, y0 + step, z0)
            p3 = Punto( x0, y0, z0 + step)
            p4 = Punto( x0, y0 + step, z0 + step)
            patch = Patch(p3, p4, p2, p1)
            y0 += step
                
            patch.reflectance_red = color[0]
            patch.reflectance_green = color[1]
            patch.reflectance_blue = color[2]
            # asocio el parche recien creado a la lista
            patchesCubo.append(patch)
        z0 += step
        y0 = origin.y
        ############################################################
    x0 = origin.x
    y0 = origin.y
    z0 = origin.z
    
    for i in range(0, iterationsx): #eje horizonal
        for j in range(0, iterationsy): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto(x0, y0, z0+lengthz)
            p2 = Punto(x0 + step, y0, z0+lengthz)
            p3 = Punto(x0, y0 + step, z0+lengthz)
            p4 = Punto(x0 + step, y0 + step, z0+lengthz)
            patch = Patch(p1, p2, p4, p3)
            y0 += step
                
            patch.reflectance_red = color[0]
            patch.reflectance_green = color[1]
            patch.reflectance_blue = color[2]
            # asocio el parche recien creado a la lista
            patchesCubo.append(patch)
        x0 += step
        y0 = origin.y
    #planoXZ
    x0 = origin.x
    y0 = origin.y
    z0 = origin.z
    
    for i in range(0, iterationsx): #eje horizonal
        for j in range(0, iterationsz): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto(x0, y0+lengthy, z0)
            p2 = Punto(x0, y0+lengthy, z0 + step)
            p3 = Punto(x0 + step, y0+lengthy, z0)
            p4 = Punto(x0 + step, y0+lengthy, z0 + step)
            patch = Patch(p1, p2, p4, p3)
            z0 += step
                
            patch.reflectance_red = color[0]
            patch.reflectance_green = color[1]
            patch.reflectance_blue = color[2]
            # asocio el parche recien creado a la lista
            patchesCubo.append(patch)
        x0 += step
        z0 = origin.z
        
    #planoYZ
    x0 = origin.x
    y0 = origin.y
    z0 = origin.z
    
    for i in range(0, iterationsz): #eje horizonal
        for j in range(0, iterationsy): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto( x0+lengthx, y0, z0)
            p2 = Punto( x0+lengthx, y0 + step, z0)
            p3 = Punto( x0+lengthx, y0, z0 + step)
            p4 = Punto( x0+lengthx, y0 + step, z0 + step)
            patch = Patch(p1, p2, p4, p3)
            y0 += step
                
            patch.reflectance_red = color[0]
            patch.reflectance_green = color[1]
            patch.reflectance_blue = color[2]
            # asocio el parche recien creado a la lista
            patchesCubo.append(patch)
        z0 += step
        y0 = origin.y
	return patchesCubo
    
def uvsphere(tx,ty,tz,w,lum, color):
    puntos = [   Punto( tx+w*0.309017  , ty+w*0.000000  , tz+w*0.951057  ),
                 Punto( tx+w*0.587785  , ty+w*0.000000  , tz+w*0.809017  ),
                 Punto( tx+w*0.809017  , ty+w*0.000000  , tz+w*0.587785  ),
                 Punto( tx+w*0.951057  , ty+w*0.000000  , tz+w*0.309017  ),
                 Punto( tx+w*1.000000  , ty+w*0.000000  , tz+w*-0.000000 ),
                 Punto( tx+w*0.951056  , ty+w*0.000000  , tz+w*-0.309017 ),
                 Punto( tx+w*0.809017  , ty+w*0.000000  , tz+w*-0.587785 ),
                 Punto( tx+w*0.587785  , ty+w*0.000000  , tz+w*-0.809017 ),
                 Punto( tx+w*0.309017  , ty+w*0.000000  , tz+w*-0.951057 ),
                 Punto( tx+w*-0.000000 , ty+w*-0.000000 , tz+w*-1.000000 ),
                 Punto( tx+w*0.250000  , ty+w*0.181636  , tz+w*-0.951057 ),
                 Punto( tx+w*0.475528  , ty+w*0.345491  , tz+w*-0.809017 ),
                 Punto( tx+w*0.654509  , ty+w*0.475528  , tz+w*-0.587785 ),
                 Punto( tx+w*0.769421  , ty+w*0.559017  , tz+w*-0.309017 ),
                 Punto( tx+w*0.809017  , ty+w*0.587785  , tz+w*0.000000  ),
                 Punto( tx+w*0.769421  , ty+w*0.559017  , tz+w*0.309017  ),
                 Punto( tx+w*0.654509  , ty+w*0.475528  , tz+w*0.587785  ),
                 Punto( tx+w*0.475528  , ty+w*0.345492  , tz+w*0.809017  ),
                 Punto( tx+w*0.250000  , ty+w*0.181636  , tz+w*0.951057  ),
                 Punto( tx+w*0.095491  , ty+w*0.293893  , tz+w*0.951057  ),
                 Punto( tx+w*0.181636  , ty+w*0.559017  , tz+w*0.809017  ),
                 Punto( tx+w*0.250000  , ty+w*0.769421  , tz+w*0.587785  ),
                 Punto( tx+w*0.293893  , ty+w*0.904509  , tz+w*0.309017  ),
                 Punto( tx+w*0.309017  , ty+w*0.951057  , tz+w*0.000000  ),
                 Punto( tx+w*0.293893  , ty+w*0.904509  , tz+w*-0.309017 ),
                 Punto( tx+w*0.250000  , ty+w*0.769421  , tz+w*-0.587785 ),
                 Punto( tx+w*0.181636  , ty+w*0.559017  , tz+w*-0.809017 ),
                 Punto( tx+w*0.095491  , ty+w*0.293892  , tz+w*-0.951057 ),
                 Punto( tx+w*-0.095491 , ty+w*0.293892  , tz+w*-0.951057 ),
                 Punto( tx+w*-0.181636 , ty+w*0.559017  , tz+w*-0.809017 ),
                 Punto( tx+w*-0.250000 , ty+w*0.769421  , tz+w*-0.587785 ),
                 Punto( tx+w*-0.293893 , ty+w*0.904509  , tz+w*-0.309017 ),
                 Punto( tx+w*-0.309017 , ty+w*0.951057  , tz+w*0.000000  ),
                 Punto( tx+w*-0.293893 , ty+w*0.904509  , tz+w*0.309017  ),
                 Punto( tx+w*-0.250000 , ty+w*0.769421  , tz+w*0.587785  ),
                 Punto( tx+w*-0.181636 , ty+w*0.559017  , tz+w*0.809017  ),
                 Punto( tx+w*-0.095492 , ty+w*0.293893  , tz+w*0.951057  ),
                 Punto( tx+w*-0.250000 , ty+w*0.181636  , tz+w*0.951057  ),
                 Punto( tx+w*-0.475528 , ty+w*0.345491  , tz+w*0.809017  ),
                 Punto( tx+w*-0.654509 , ty+w*0.475528  , tz+w*0.587785  ),
                 Punto( tx+w*-0.769421 , ty+w*0.559017  , tz+w*0.309017  ),
                 Punto( tx+w*-0.809017 , ty+w*0.587785  , tz+w*0.000000  ),
                 Punto( tx+w*-0.769421 , ty+w*0.559017  , tz+w*-0.309017 ),
                 Punto( tx+w*-0.654509 , ty+w*0.475528  , tz+w*-0.587785 ),
                 Punto( tx+w*-0.475528 , ty+w*0.345491  , tz+w*-0.809017 ),
                 Punto( tx+w*-0.250000 , ty+w*0.181636  , tz+w*-0.951057 ),
                 Punto( tx+w*-0.309017 , ty+w*-0.000000 , tz+w*-0.951057 ),
                 Punto( tx+w*-0.587785 , ty+w*-0.000000 , tz+w*-0.809017 ),
                 Punto( tx+w*-0.809017 , ty+w*-0.000000 , tz+w*-0.587785 ),
                 Punto( tx+w*-0.951057 , ty+w*-0.000000 , tz+w*-0.309017 ),
                 Punto( tx+w*-1.000000 , ty+w*-0.000000 , tz+w*0.000000  ),
                 Punto( tx+w*-0.951057 , ty+w*-0.000000 , tz+w*0.309017  ),
                 Punto( tx+w*-0.809017 , ty+w*-0.000000 , tz+w*0.587785  ),
                 Punto( tx+w*-0.587785 , ty+w*-0.000000 , tz+w*0.809017  ),
                 Punto( tx+w*-0.309017 , ty+w*-0.000000 , tz+w*0.951057  ),
                 Punto( tx+w*-0.250000 , ty+w*-0.181636 , tz+w*0.951057  ),
                 Punto( tx+w*-0.475528 , ty+w*-0.345492 , tz+w*0.809017  ),
                 Punto( tx+w*-0.654509 , ty+w*-0.475529 , tz+w*0.587785  ),
                 Punto( tx+w*-0.769421 , ty+w*-0.559017 , tz+w*0.309017  ),
                 Punto( tx+w*-0.809017 , ty+w*-0.587786 , tz+w*0.000000  ),
                 Punto( tx+w*-0.769421 , ty+w*-0.559017 , tz+w*-0.309017 ),
                 Punto( tx+w*-0.654509 , ty+w*-0.475529 , tz+w*-0.587785 ),
                 Punto( tx+w*-0.475528 , ty+w*-0.345492 , tz+w*-0.809017 ),
                 Punto( tx+w*-0.250000 , ty+w*-0.181636 , tz+w*-0.951057 ),
                 Punto( tx+w*-0.095491 , ty+w*-0.293893 , tz+w*-0.951057 ),
                 Punto( tx+w*-0.181636 , ty+w*-0.559017 , tz+w*-0.809017 ),
                 Punto( tx+w*-0.250000 , ty+w*-0.769421 , tz+w*-0.587785 ),
                 Punto( tx+w*-0.293893 , ty+w*-0.904509 , tz+w*-0.309017 ),
                 Punto( tx+w*-0.309017 , ty+w*-0.951057 , tz+w*0.000000  ),
                 Punto( tx+w*-0.293893 , ty+w*-0.904509 , tz+w*0.309017  ),
                 Punto( tx+w*-0.250000 , ty+w*-0.769421 , tz+w*0.587785  ),
                 Punto( tx+w*-0.181636 , ty+w*-0.559017 , tz+w*0.809017  ),
                 Punto( tx+w*-0.095491 , ty+w*-0.293893 , tz+w*0.951057  ),
                 Punto( tx+w*0.000000  , ty+w*0.000000  , tz+w*1.000000  ),
                 Punto( tx+w*0.095492  , ty+w*-0.293893 , tz+w*0.951057  ),
                 Punto( tx+w*0.181636  , ty+w*-0.559017 , tz+w*0.809017  ),
                 Punto( tx+w*0.250000  , ty+w*-0.769421 , tz+w*0.587785  ),
                 Punto( tx+w*0.293893  , ty+w*-0.904509 , tz+w*0.309017  ),
                 Punto( tx+w*0.309017  , ty+w*-0.951057 , tz+w*0.000000  ),
                 Punto( tx+w*0.293893  , ty+w*-0.904509 , tz+w*-0.309017 ),
                 Punto( tx+w*0.250000  , ty+w*-0.769421 , tz+w*-0.587785 ),
                 Punto( tx+w*0.181636  , ty+w*-0.559017 , tz+w*-0.809017 ),
                 Punto( tx+w*0.095492  , ty+w*-0.293893 , tz+w*-0.951057 ),
                 Punto( tx+w*0.250000  , ty+w*-0.181635 , tz+w*-0.951057 ),
                 Punto( tx+w*0.475528  , ty+w*-0.345491 , tz+w*-0.809017 ),
                 Punto( tx+w*0.654509  , ty+w*-0.475528 , tz+w*-0.587785 ),
                 Punto( tx+w*0.769421  , ty+w*-0.559017 , tz+w*-0.309017 ),
                 Punto( tx+w*0.809017  , ty+w*-0.587785 , tz+w*0.000000  ),
                 Punto( tx+w*0.769421  , ty+w*-0.559017 , tz+w*0.309017  ),
                 Punto( tx+w*0.654509  , ty+w*-0.475528 , tz+w*0.587785  ),
                 Punto( tx+w*0.475529  , ty+w*-0.345491 , tz+w*0.809017  ),
                 Punto( tx+w*0.250000  , ty+w*-0.181636 , tz+w*0.951057  ) ]
        
    patches = [  Patch(puntos[9], puntos[10], puntos[8], puntos[8]),   ##
                 Patch(puntos[8], puntos[10], puntos[11], puntos[7 ]),
                 Patch(puntos[7], puntos[11], puntos[12], puntos[6 ]),
                 Patch(puntos[6], puntos[12], puntos[13], puntos[5 ]),
                 Patch(puntos[5], puntos[13], puntos[14], puntos[4 ]),
                 Patch(puntos[4], puntos[14], puntos[15], puntos[3 ]),
                 Patch(puntos[3], puntos[15], puntos[16], puntos[2 ]),
                 Patch(puntos[2], puntos[16], puntos[17], puntos[1 ]),
                 Patch(puntos[18], puntos[0], puntos[1], puntos[17 ]),
                 Patch(puntos[0], puntos[18], puntos[73], puntos[73]), ##
                 Patch(puntos[18], puntos[19], puntos[73], puntos[73]), ##
                 Patch(puntos[17], puntos[20], puntos[19], puntos[18 ]),
                 Patch(puntos[16], puntos[21], puntos[20], puntos[17 ]),
                 Patch(puntos[15], puntos[22], puntos[21], puntos[16 ]),
                 Patch(puntos[14], puntos[23], puntos[22], puntos[15 ]),
                 Patch(puntos[13], puntos[24], puntos[23], puntos[14 ]),
                 Patch(puntos[12], puntos[25], puntos[24], puntos[13 ]),
                 Patch(puntos[11], puntos[26], puntos[25], puntos[12 ]),
                 Patch(puntos[10], puntos[27], puntos[26], puntos[11 ]),
                 Patch(puntos[9], puntos[27], puntos[10], puntos[10]), ##
                 Patch(puntos[9], puntos[28], puntos[27], puntos[27]), ##
                 Patch(puntos[27], puntos[28], puntos[29], puntos[26 ]),
                 Patch(puntos[26], puntos[29], puntos[30], puntos[25 ]),
                 Patch(puntos[25], puntos[30], puntos[31], puntos[24 ]),
                 Patch(puntos[24], puntos[31], puntos[32], puntos[23 ]),
                 Patch(puntos[23], puntos[32], puntos[33], puntos[22 ]),
                 Patch(puntos[22], puntos[33], puntos[34], puntos[21 ]),
                 Patch(puntos[21], puntos[34], puntos[35], puntos[20 ]),
                 Patch(puntos[20], puntos[35], puntos[36], puntos[19 ]),
                 Patch(puntos[19], puntos[36], puntos[73], puntos[73]), ##
                 Patch(puntos[36], puntos[37], puntos[73], puntos[73]), ##
                 Patch(puntos[35], puntos[38], puntos[37], puntos[36 ]),
                 Patch(puntos[34], puntos[39], puntos[38], puntos[35 ]),
                 Patch(puntos[33], puntos[40], puntos[39], puntos[34 ]),
                 Patch(puntos[32], puntos[41], puntos[40], puntos[33 ]),
                 Patch(puntos[31], puntos[42], puntos[41], puntos[32 ]),
                 Patch(puntos[30], puntos[43], puntos[42], puntos[31 ]),
                 Patch(puntos[29], puntos[44], puntos[43], puntos[30 ]),
                 Patch(puntos[28], puntos[45], puntos[44], puntos[29 ]),
                 Patch(puntos[9], puntos[45], puntos[28], puntos[28]), ##
                 Patch(puntos[9], puntos[46], puntos[45], puntos[45]), ##
                 Patch(puntos[45], puntos[46], puntos[47], puntos[44 ]),
                 Patch(puntos[44], puntos[47], puntos[48], puntos[43 ]),
                 Patch(puntos[43], puntos[48], puntos[49], puntos[42 ]),
                 Patch(puntos[42], puntos[49], puntos[50], puntos[41 ]),
                 Patch(puntos[41], puntos[50], puntos[51], puntos[40 ]),
                 Patch(puntos[40], puntos[51], puntos[52], puntos[39 ]),
                 Patch(puntos[39], puntos[52], puntos[53], puntos[38 ]),
                 Patch(puntos[38], puntos[53], puntos[54], puntos[37 ]),
                 Patch(puntos[37], puntos[54], puntos[73], puntos[73]), ##
                 Patch(puntos[54], puntos[55], puntos[73], puntos[73]), ##
                 Patch(puntos[53], puntos[56], puntos[55], puntos[54 ]),
                 Patch(puntos[52], puntos[57], puntos[56], puntos[53 ]),
                 Patch(puntos[51], puntos[58], puntos[57], puntos[52 ]),
                 Patch(puntos[50], puntos[59], puntos[58], puntos[51 ]),
                 Patch(puntos[49], puntos[60], puntos[59], puntos[50 ]),
                 Patch(puntos[48], puntos[61], puntos[60], puntos[49 ]),
                 Patch(puntos[47], puntos[62], puntos[61], puntos[48 ]),
                 Patch(puntos[46], puntos[63], puntos[62], puntos[47 ]),
                 Patch(puntos[9], puntos[63], puntos[46], puntos[46]), ##
                 Patch(puntos[9], puntos[64], puntos[63], puntos[63]), ##
                 Patch(puntos[63], puntos[64], puntos[65], puntos[62 ]),
                 Patch(puntos[62], puntos[65], puntos[66], puntos[61 ]),
                 Patch(puntos[61], puntos[66], puntos[67], puntos[60 ]),
                 Patch(puntos[60], puntos[67], puntos[68], puntos[59 ]),
                 Patch(puntos[59], puntos[68], puntos[69], puntos[58 ]),
                 Patch(puntos[58], puntos[69], puntos[70], puntos[57 ]),
                 Patch(puntos[57], puntos[70], puntos[71], puntos[56 ]),
                 Patch(puntos[56], puntos[71], puntos[72], puntos[55 ]),
                 Patch(puntos[55], puntos[72], puntos[73], puntos[73]), ##
                 Patch(puntos[72], puntos[74], puntos[73], puntos[73]), ##
                 Patch(puntos[71], puntos[75], puntos[74], puntos[72 ]),
                 Patch(puntos[70], puntos[76], puntos[75], puntos[71 ]),
                 Patch(puntos[69], puntos[77], puntos[76], puntos[70 ]),
                 Patch(puntos[68], puntos[78], puntos[77], puntos[69 ]),
                 Patch(puntos[67], puntos[79], puntos[78], puntos[68 ]),
                 Patch(puntos[66], puntos[80], puntos[79], puntos[67 ]),
                 Patch(puntos[65], puntos[81], puntos[80], puntos[66 ]),
                 Patch(puntos[64], puntos[82], puntos[81], puntos[65 ]),
                 Patch(puntos[9], puntos[82], puntos[64], puntos[64 ]), ##
                 Patch(puntos[9], puntos[83], puntos[82], puntos[82]), ##
                 Patch(puntos[82], puntos[83], puntos[84], puntos[81 ]),
                 Patch(puntos[81], puntos[84], puntos[85], puntos[80 ]),
                 Patch(puntos[80], puntos[85], puntos[86], puntos[79 ]),
                 Patch(puntos[79], puntos[86], puntos[87], puntos[78 ]),
                 Patch(puntos[78], puntos[87], puntos[88], puntos[77 ]),
                 Patch(puntos[77], puntos[88], puntos[89], puntos[76 ]),
                 Patch(puntos[76], puntos[89], puntos[90], puntos[75 ]),
                 Patch(puntos[75], puntos[90], puntos[91], puntos[74 ]),
                 Patch(puntos[74], puntos[91], puntos[73], puntos[73]), ##
                 Patch(puntos[91], puntos[0], puntos[73], puntos[73]), ##
                 Patch(puntos[0], puntos[91], puntos[90], puntos[1 ]),
                 Patch(puntos[89], puntos[2], puntos[1], puntos[90 ]),
                 Patch(puntos[88], puntos[3], puntos[2], puntos[89 ]),
                 Patch(puntos[87], puntos[4], puntos[3], puntos[88 ]),
                 Patch(puntos[86], puntos[5], puntos[4], puntos[87 ]),
                 Patch(puntos[85], puntos[6], puntos[5], puntos[86 ]),
                 Patch(puntos[84], puntos[7], puntos[6], puntos[85 ]),
                 Patch(puntos[83], puntos[8], puntos[7], puntos[84 ]),
                 Patch(puntos[9], puntos[8], puntos[83], puntos[83]) ] ##
    for patch in patches:
        patch.reflectance_red = color[0]
        patch.reflectance_green = color[1]
        patch.reflectance_blue = color[2]
        
        patch.emmision_red = lum
        patch.emmision_green = lum
        patch.emmision_blue = lum
        patch.normal = (patch.center.resta(Punto(tx,ty,tz),1)).normalizar()
    return patches