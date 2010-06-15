from numpy import *
from patch import *
from punto import *
from variables import *

# global patchesList

# recibe 2 parches i y j, retorna el F_ij  (al parecer, F_ij != F_ji)
def formfactor(i,j,visib):
    if(i==j):
        return 0.0
    p_i = patchesList[i]
    p_j = patchesList[j]
    # patchesList = PL
    # segun http://www.gamedev.net/reference/articles/article653.asp
    #       http://wiki.cgsociety.org/index.php/Radiosity#Form_Factor_Determination
    #
    # F_ij = [(cos thetai * cos thetaj)/pi*r^2]*H_ij*dAj
    c_i = p_i.center
    c_j = p_j.center
    n_i = p_i.normal
    n_j = p_j.normal
    d_ij = c_i.resta(c_j, 1)
    
    r = math.sqrt( (c_i.x-c_j.x)**2 + (c_i.y-c_j.y)**2 + (c_i.z-c_j.z)**2) #centro p_i, p_j
    if (r==0):
        return 0.0

    dAj = p_j.area
    H_ij = visib
    
    #cosenos segun http://www.geoan.com/vectores/angulo.html
    costi = (d_ij.x*n_i.x + d_ij.y*n_i.y + d_ij.z*n_i.z)/((math.sqrt(d_ij.x**2 + d_ij.y**2 + d_ij.z**2))*(math.sqrt(n_i.x**2 + n_i.y**2 + n_i.z**2 )))
    costj = (d_ij.x*n_j.x + d_ij.y*n_j.y + d_ij.z*n_j.z)/((math.sqrt(d_ij.x**2 + d_ij.y**2 + d_ij.z**2))*(math.sqrt(n_j.x**2 + n_j.y**2 + n_j.z**2 )))
    
    signo = 1.0
    # if( costi>0 and costj>0):
    #     signo = 1.0
    
    # F_ij = 
    ff = signo * 1.0 * ((costi*costj)/(math.pi*(r**2)))*H_ij*dAj
    # print "ff = ",ff
    if(ff > 1):
        print "ff>1"
        return 1.0
    if(ff < 0):
        return 0.0
    
    return ff
    
def sistema(a,b):
    x = linalg.solve(a, b)
    return x
 
def visibility(i,j) :
    p_i = patchesList[i]
    p_j = patchesList[j]
    
    x1 = p_i.center.x
    y1 = p_i.center.y
    z1 = p_i.center.z
    
    x2 = p_j.center.x
    y2 = p_j.center.y
    z2 = p_j.center.z
    
    i = (x2-x1)
    j = (y2-y1)
    k = (z2-z1)
    
    for x, p in enumerate(patchesList):
        if(x == i or x == j):
            continue
        cp = p.center
        
        l = cp.x
        m = cp.y
        n = cp.z
        r = p.pradio
        
        a = i**2 + j**2 + k**2
        b = 2*i*(x1 - l) + 2*j*(y1 - m) + 2*k*(z1 - n)
        c = l**2 + m**2 + n**2 + x1**2 + y1**2 + z1**2 + 2*(-l*x1 -m*y1 -n*z1) - r**2
        
        det = b**2 - 4*a*c
        if(det <= 0):
            return 1.0
        return 0.0
        
def visibility2(i,j) :
    p_i = patchesList[i]
    p_j = patchesList[j]
    dist = (p_i.center.resta(p_j.center,1)).modulo()
    if( dist == 0):
        return 1.0
    
    x1 = p_i.center.x
    y1 = p_i.center.y
    z1 = p_i.center.z
    
    x2 = p_j.center.x
    y2 = p_j.center.y
    z2 = p_j.center.z
    
    i = (x2-x1)
    j = (y2-y1)
    k = (z2-z1)
    
    for x, p in enumerate(patchesList):
        if(x == i or x == j):
            continue
            
        dist = (p_i.center.resta(p.center,1)).modulo()
        if( dist == 0):
            continue
        dist = (p_j.center.resta(p.center,1)).modulo()
        if( dist == 0):
            continue
            
        n = p.normal
        
        a = n.x
        b = n.y
        c = n.z
        
        np = -1.0*n.producto(p.p1)
        
        den = a*i + b*j + c*k
        if(den == 0):
            # print "den = 0"
            continue
        num = -1.0*( a*x1 + b*y1 + c*z1 + np)
        
        t = num/den
        
        int_x = x1 + i*t
        int_y = y1 + j*t
        int_z = z1 + k*t
        
        # print "interseccion  ",int_x,"--",int_y,"--",int_z,"--"
        
        inter = Punto(int_x, int_y, int_z)
        
        v1 = p.p1.resta(inter,1)
        v2 = p.p2.resta(inter,1)
        v3 = p.p3.resta(inter,1)
        v4 = p.p4.resta(inter,1)
        
        if( v1.modulo() == 0 or v2.modulo() == 0 or v3.modulo() == 0 or v4.modulo() == 0):
            continue
        
        # print v1.imprimir("v1")
        # print v2.imprimir("v2")
        # print v3.imprimir("v3")
        # print v4.imprimir("v4")
        
        ang1 = v1.anguloEntre(v2)
        ang2 = v2.anguloEntre(v3)
        ang3 = v3.anguloEntre(v4)
        ang4 = v4.anguloEntre(v1)
        total = ang1 + ang2 + ang3 + ang4
        
        if( total >= 350 ):
            return 0.0
    
    return 1.0
        
# recibe dos parches, y determina el factor de visibilidad entre los centros de ambos (valor 0 o 1)
# def visibility(i,j):
#     if(i==j):
#         return 1
    
#     p_i = patchesList[i]
#     p_j = patchesList[j]
#     rvalue = 1
#     ci = p_i.center
#     cj = p_j.center
    
#     #  PARA CADA PARCHE P EN LA ESCENA
#     for p in patchesList:
#         cp = p.center
#     #     CALCULAR ANGULO THETA ENTRE VECTORES PI,PJ Y PI,CP
#         v = cp.resta(ci,1)
#         w = cj.resta(ci,1)
#         if( v.modulo() == 0 or w.modulo() == 0):
#             return 1
#         theta = v.anguloEntre(w)
#     #     CALCULAR DISTANCIA COMO (CP-PI)SEN THETA
#         d = math.sin(theta) * v.modulo()
#     #     CALCULAR MAYOR DISTANCIA ENTRE UN VERTICE DE P Y EL CENTRO DE P (DIS_MAX = DM)
#         dm = p.pradio
#         dmm = p.pmradio
#     #     CALCULAR ANGULO ENTRE NORMAL DE P Y R, ANGULO = TH
#         alpha = p.normal.anguloEntre(w)
#     #     CALCULAR DD = DM*COS(TH) -> 'CUANTO SE ACERCA P A R'
#         dd = dm*math.cos(alpha)
#         ddm = dmm*math.cos(alpha)
#     #     SI D < DD => RECTA ATRAVIESA PARCHE
#     #        RETURN 0
#         if( d < ddm ):
#             return 0
#         # elif(d < dd):
#         #     rvalue = 0.5
#         # FIN DEL LOOP
    
#     #  RETURN 1
#     return rvalue

