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
    patches = [  Patch( puntos[2] , puntos[0] , puntos[1]) ,
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
        patch.reflectance_green = 1.0
        patch.reflectance_blue = 0.3
        
        patch.emmision_red = lum
        patch.emmision_green = lum
        patch.emmision_blue = lum
        patch.normal = (patch.center.resta(Punto(tx,ty,tz),1)).normalizar()
    
    return patches
    
def patchesCubo(tx,ty,tz,w,lum):
    puntos = [   Punto(tx+w* 0.005020 , ty+w* 0.005368 , tz+w*-0.467305),
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
    patches = [  Patch( puntos[2 ] , puntos[0 ], puntos[1 ]),
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
                 
    for x in range(0,len(patches)):
        patch = patches[x]
        patch.reflectance_red = 0.3
        patch.reflectance_green = 1.0
        patch.reflectance_blue = 0.3
        
        patch.emmision_red = lum
        patch.emmision_green = lum
        patch.emmision_blue = lum
        # patch.normal = (patch.center.resta(Punto(tx,ty,tz),1)).normalizar()
    
    return patches