from punto import *
from patch import *

def patchesIcosaedro(tx,ty,tz,w, lum):
    puntos = [Punto(tx+w*0.000000, ty+w*0.000000, tz+w*-1.000000),
                 Punto(tx+w* 0.723600 , ty+w*-0.525720 , tz+w*-0.447215),
                 Punto(tx+w*-0.276385 , ty+w*-0.850640 , tz+w*-0.447215),
                 Punto(tx+w*-0.894425 , ty+w* 0.000000 , tz+w*-0.447215),
                 Punto(tx+w*-0.276385 , ty+w* 0.850640 , tz+w*-0.447215),
                 Punto(tx+w* 0.723600 , ty+w* 0.525720 , tz+w*-0.447215),
                 Punto(tx+w* 0.276385 , ty+w*-0.850640 , tz+w* 0.447215),
                 Punto(tx+w*-0.723600 , ty+w*-0.525720 , tz+w* 0.447215),
                 Punto(tx+w*-0.723600 , ty+w* 0.525720 , tz+w* 0.447215),
                 Punto(tx+w* 0.276385 , ty+w* 0.850640 , tz+w* 0.447215),
                 Punto(tx+w* 0.894425 , ty+w* 0.000000 , tz+w* 0.447215),
                 Punto(tx+w* 0.000000 , ty+w* 0.000000 , tz+w* 1.000000)]
    patches = [ Patch( puntos[2] , puntos[0] , puntos[1]) ,
                 Patch( puntos[1] , puntos[0] , puntos[5]) ,
                 Patch( puntos[3] , puntos[0] , puntos[2]) ,
                 Patch( puntos[4] , puntos[0] , puntos[3]) ,
                 Patch( puntos[5] , puntos[0] , puntos[4]) ,
                 Patch( puntos[1] , puntos[5] , puntos[10]),
                 Patch( puntos[2] , puntos[1] , puntos[6]) ,
                 Patch( puntos[3] , puntos[2] , puntos[7]) ,
                 Patch( puntos[4] , puntos[3] , puntos[8]) ,
                 Patch( puntos[5] , puntos[4] , puntos[9]) ,
                 Patch( puntos[10], puntos[6] , puntos[1]) ,
                 Patch( puntos[6] , puntos[7] , puntos[2]) ,
                 Patch( puntos[7] , puntos[8] , puntos[3]) ,
                 Patch( puntos[8] , puntos[9] , puntos[4]) ,
                 Patch( puntos[9] , puntos[10], puntos[5]) ,
                 Patch( puntos[6] , puntos[10], puntos[11]),
                 Patch( puntos[7] , puntos[6] , puntos[11]),
                 Patch( puntos[8] , puntos[7] , puntos[11]),
                 Patch( puntos[9] , puntos[8] , puntos[11]),
                 Patch( puntos[10], puntos[9] , puntos[11])]
    
    for x in range(0,len(patches)):
        patch = patches[x]
        patch.reflectance_red = 0.3
        patch.reflectance_green = 0.9
        patch.reflectance_blue = 0.3
        
        patch.emmision_red = lum
        patch.emmision_green = lum
        patch.emmision_blue = lum
        patch.normal = (patch.center.resta(Punto(tx,ty,tz),1)).normalizar()
    
    return patches
    
def patchesIcosaedro_2(tx,ty,tz,w, lum):
    puntos =   [
                 Punto(tx+w*0.000000 , ty+w*0.000000, ty+w* -1.000000),
				 Punto(tx+w*0.723600 , ty+w*-0.525720, ty+w* -0.447215),
				 Punto(tx+w*-0.276385, ty+w* -0.850640, ty+w* -0.447215),
				 Punto(tx+w*-0.894425, ty+w* 0.000000, ty+w* -0.447215),
				 Punto(tx+w*-0.276385, ty+w* 0.850640, ty+w* -0.447215),
				 Punto(tx+w*0.723600 , ty+w*0.525720, ty+w* -0.447215),
				 Punto(tx+w*0.276385 , ty+w*-0.850640, ty+w* 0.447215),
				 Punto(tx+w*-0.723600, ty+w* -0.525720, ty+w* 0.447215),
				 Punto(tx+w*-0.723600, ty+w* 0.525720, ty+w* 0.447215),
				 Punto(tx+w*0.276385 , ty+w*0.850640, ty+w* 0.447215),
				 Punto(tx+w*0.894425 , ty+w*0.000000, ty+w* 0.447215),
				 Punto(tx+w*0.000000 , ty+w*0.000000, ty+w* 1.000000),
				 Punto(tx+w*0.425323 , ty+w*-0.309011, ty+w* -0.850654),
				 Punto(tx+w*-0.162456, ty+w* -0.499995, ty+w* -0.850654),
				 Punto(tx+w*0.262869 , ty+w*-0.809012, ty+w* -0.525738),
				 Punto(tx+w*0.425323 , ty+w*0.309011, ty+w* -0.850654),
				 Punto(tx+w*0.850648 , ty+w*0.000000, ty+w* -0.525736),
				 Punto(tx+w*-0.525730, ty+w* 0.000000, ty+w* -0.850652),
				 Punto(tx+w*-0.688189, ty+w* -0.499997, ty+w* -0.525736),
				 Punto(tx+w*-0.162456, ty+w* 0.499995, ty+w* -0.850654),
				 Punto(tx+w*-0.688189, ty+w* 0.499997, ty+w* -0.525736),
				 Punto(tx+w*0.262869 , ty+w*0.809012, ty+w* -0.525738),
				 Punto(tx+w*0.951058 , ty+w*0.309013, ty+w* 0.000000),
				 Punto(tx+w*0.951058 , ty+w*-0.309013, ty+w* 0.000000),
				 Punto(tx+w*0.587786 , ty+w*-0.809017, ty+w* 0.000000),
				 Punto(tx+w*0.000000 , ty+w*-1.000000, ty+w* 0.000000),
				 Punto(tx+w*-0.587786, ty+w* -0.809017, ty+w* 0.000000),
				 Punto(tx+w*-0.951058, ty+w* -0.309013, ty+w* 0.000000),
				 Punto(tx+w*-0.951058, ty+w* 0.309013, ty+w* 0.000000),
				 Punto(tx+w*-0.587786, ty+w* 0.809017, ty+w* 0.000000),
				 Punto(tx+w*0.000000 , ty+w*1.000000, ty+w* 0.000000),
				 Punto(tx+w*0.587786 , ty+w*0.809017, ty+w* 0.000000),
				 Punto(tx+w*0.688189 , ty+w*-0.499997, ty+w* 0.525736),
				 Punto(tx+w*-0.262869, ty+w* -0.809012, ty+w* 0.525738),
				 Punto(tx+w*-0.850648, ty+w* 0.000000, ty+w* 0.525736),
				 Punto(tx+w*-0.262869, ty+w* 0.809012, ty+w* 0.525738),
				 Punto(tx+w*0.688189 , ty+w*0.499997, ty+w* 0.525736),
				 Punto(tx+w*0.525730 , ty+w*0.000000, ty+w* 0.850652),
				 Punto(tx+w*0.162456 , ty+w*-0.499995, ty+w* 0.850654),
				 Punto(tx+w*-0.425323, ty+w* -0.309011, ty+w* 0.850654),
				 Punto(tx+w*-0.425323, ty+w* 0.309011, ty+w* 0.850654),
				 Punto(tx+w*0.162456 , ty+w*0.499995, ty+w* 0.850654)
				]
    patches = [
                Patch( puntos[14], puntos[12], puntos[1]),
                Patch( puntos[12], puntos[14], puntos[13]),
                Patch( puntos[2],  puntos[13], puntos[14]),
                Patch( puntos[13], puntos[0], puntos[12]),
                Patch( puntos[16], puntos[1], puntos[12]),
                Patch( puntos[12], puntos[15], puntos[16]),
                Patch( puntos[5],  puntos[16], puntos[15]),
                Patch( puntos[12], puntos[0], puntos[15]),
                Patch( puntos[18], puntos[13], puntos[2]),
                Patch( puntos[13], puntos[18], puntos[17]),
                Patch( puntos[3],  puntos[17], puntos[18]),
                Patch( puntos[17], puntos[0], puntos[13]),
                Patch( puntos[20], puntos[17], puntos[3]),
                Patch( puntos[17], puntos[20], puntos[19]),
                Patch( puntos[4],  puntos[19], puntos[20]),
                Patch( puntos[19], puntos[0], puntos[17]),
                Patch( puntos[21], puntos[19], puntos[4]),
                Patch( puntos[19], puntos[21], puntos[15]),
                Patch( puntos[5],  puntos[15], puntos[21]),
                Patch( puntos[15], puntos[0], puntos[19]),
                Patch( puntos[23], puntos[1], puntos[16]),
                Patch( puntos[16], puntos[22], puntos[23]),
                Patch( puntos[10], puntos[23], puntos[22]),
                Patch( puntos[22], puntos[16], puntos[5]),
                Patch( puntos[25], puntos[2], puntos[14]),
                Patch( puntos[14], puntos[24], puntos[25]),
                Patch( puntos[6],  puntos[25], puntos[24]),
                Patch( puntos[24], puntos[14], puntos[1]),
                Patch( puntos[27], puntos[3], puntos[18]),
                Patch( puntos[18], puntos[26], puntos[27]),
                Patch( puntos[7],  puntos[27], puntos[26]),
                Patch( puntos[26], puntos[18], puntos[2]),
                Patch( puntos[29], puntos[4], puntos[20]),
                Patch( puntos[20], puntos[28], puntos[29]),
                Patch( puntos[8],  puntos[29], puntos[28]),
                Patch( puntos[28], puntos[20], puntos[3]),
                Patch( puntos[31], puntos[5], puntos[21]),
                Patch( puntos[21], puntos[30], puntos[31]),
                Patch( puntos[9],  puntos[31], puntos[30]),
                Patch( puntos[30], puntos[21], puntos[4]),
                Patch( puntos[32], puntos[23], puntos[10]),
                Patch( puntos[23], puntos[32], puntos[24]),
                Patch( puntos[6],  puntos[24], puntos[32]),
                Patch( puntos[24], puntos[1], puntos[23]),
                Patch( puntos[33], puntos[25], puntos[6]),
                Patch( puntos[25], puntos[33], puntos[26]),
                Patch( puntos[7],  puntos[26], puntos[33]),
                Patch( puntos[26], puntos[2], puntos[25]),
                Patch( puntos[34], puntos[27], puntos[7]),
                Patch( puntos[27], puntos[34], puntos[28]),
                Patch( puntos[8],  puntos[28], puntos[34]),
                Patch( puntos[28], puntos[3], puntos[27]),
                Patch( puntos[35], puntos[29], puntos[8]),
                Patch( puntos[29], puntos[35], puntos[30]),
                Patch( puntos[9],  puntos[30], puntos[35]),
                Patch( puntos[30], puntos[4], puntos[29]),
                Patch( puntos[36], puntos[31], puntos[9]),
                Patch( puntos[31], puntos[36], puntos[22]),
                Patch( puntos[10], puntos[22], puntos[36]),
                Patch( puntos[22], puntos[5], puntos[31]),
                Patch( puntos[38], puntos[6], puntos[32]),
                Patch( puntos[32], puntos[37], puntos[38]),
                Patch( puntos[11], puntos[38], puntos[37]),
                Patch( puntos[37], puntos[32], puntos[10]),
                Patch( puntos[39], puntos[7], puntos[33]),
                Patch( puntos[33], puntos[38], puntos[39]),
                Patch( puntos[11], puntos[39], puntos[38]),
                Patch( puntos[38], puntos[33], puntos[6]),
                Patch( puntos[40], puntos[8], puntos[34]),
                Patch( puntos[34], puntos[39], puntos[40]),
                Patch( puntos[11], puntos[40], puntos[39]),
                Patch( puntos[39], puntos[34], puntos[7]),
                Patch( puntos[41], puntos[9], puntos[35]),
                Patch( puntos[35], puntos[40], puntos[41]),
                Patch( puntos[11], puntos[41], puntos[40]),
                Patch( puntos[40], puntos[35], puntos[8]),
                Patch( puntos[37], puntos[10], puntos[36]),
                Patch( puntos[36], puntos[41], puntos[37]),
                Patch( puntos[11], puntos[37], puntos[41]),
                Patch( puntos[41], puntos[36], puntos[9])
            ]
    
    for x in range(0,len(patches)):
        patch = patches[x]
        patch.reflectance_red = 0.3
        patch.reflectance_green = 0.4
        patch.reflectance_blue = 0.3
        
        patch.emmision_red = lum
        patch.emmision_green = lum
        patch.emmision_blue = lum
        patch.normal = (patch.center.resta(Punto(tx,ty,tz),1)).normalizar()
        patch.normal.x *= -1.0
        patch.normal.y *= -1.0
        patch.normal.z *= -1.0
    
    return patches
    
def patchesCubo(tx,ty,tz,w,lum):
    puntos = [  Punto(tx+w* 0.005020 , ty+w* 0.005368 , tz+w*-0.467305),
                 Punto(tx+w* 0.705485 , ty+w*-0.493011 , tz+w*-0.468423),
                 Punto(tx+w*-0.695622 , ty+w*-0.492753 , tz+w*-0.468423),
                 Punto(tx+w*-0.694644 , ty+w* 0.005368 , tz+w*-0.468423),
                 Punto(tx+w*-0.694969 , ty+w* 0.507002 , tz+w*-0.468423),
                 Punto(tx+w* 0.705485 , ty+w* 0.507689 , tz+w*-0.468423),
                 Punto(tx+w* 0.704098 , ty+w*-0.492232 , tz+w* 0.426006),
                 Punto(tx+w*-0.695445 , ty+w*-0.493011 , tz+w* 0.426006),
                 Punto(tx+w*-0.695445 , ty+w* 0.507953 , tz+w* 0.426006),
                 Punto(tx+w* 0.705082 , ty+w* 0.507099 , tz+w* 0.426006),
                 Punto(tx+w* 0.704800 , ty+w* 0.005368 , tz+w* 0.426006),
                 Punto(tx+w* 0.005020 , ty+w* 0.005368 , tz+w* 0.426360) ]
    patches = [ Patch( puntos[2 ] , puntos[0 ], puntos[1 ]),
                 Patch( puntos[1 ] , puntos[0 ], puntos[5 ]),
                 Patch( puntos[3 ] , puntos[0 ], puntos[2 ]),
                 Patch( puntos[4 ] , puntos[0 ], puntos[3 ]),
                 Patch( puntos[5 ] , puntos[0 ], puntos[4 ]),
                 Patch( puntos[1 ] , puntos[5 ], puntos[10]),
                 Patch( puntos[2 ] , puntos[1 ], puntos[6 ]),
                 Patch( puntos[3 ] , puntos[2 ], puntos[7 ]),
                 Patch( puntos[4 ] , puntos[3 ], puntos[8 ]),
                 Patch( puntos[5 ] , puntos[4 ], puntos[9 ]),
                 Patch( puntos[10] , puntos[6 ], puntos[1 ]),
                 Patch( puntos[6 ] , puntos[7 ], puntos[2 ]),
                 Patch( puntos[7 ] , puntos[8 ], puntos[3 ]),
                 Patch( puntos[8 ] , puntos[9 ], puntos[4 ]),
                 Patch( puntos[9 ] , puntos[10], puntos[5 ]),
                 Patch( puntos[6 ] , puntos[10], puntos[11]),
                 Patch( puntos[7 ] , puntos[6 ], puntos[11]),
                 Patch( puntos[8 ] , puntos[7 ], puntos[11]),
                 Patch( puntos[9 ] , puntos[8 ], puntos[11]),
                 Patch( puntos[10] , puntos[9 ], puntos[11]) ]
                 
    for patch in patches:
        patch.reflectance_red = 0.3
        patch.reflectance_green = 0.9
        patch.reflectance_blue = 0.3
        
        patch.emmision_red = lum
        patch.emmision_green = lum
        patch.emmision_blue = lum
        #patch.normal = (patch.center.resta(Punto(tx,ty,tz),1)).normalizar()
    
    return patches