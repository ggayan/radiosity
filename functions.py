from numpy import *
from patch import *
from punto import *

global patchesList
counter = 0
# recibe 2 parches i y j, retorna el F_ij  (al parecer, F_ij != F_ji)
def formfactor(p_i,p_j,visib):
    # patchesList = PL
    # segun http://www.gamedev.net/reference/articles/article653.asp
    #       http://wiki.cgsociety.org/index.php/Radiosity#Form_Factor_Determination
    #
    # F_ij = [(cos thetai * cos thetaj)/pi*r^2]*H_ij*dAj
    c_i = p_i.center
    c_j = p_j.center
    n_i = p_i.normal
    n_j = p_j.normal
    d_ij = Punto(c_i.x-c_j.x, c_i.y-c_j.y, c_i.z-c_j.z)
    
    r = math.sqrt(math.pow(c_i.x-c_j.x,2)+math.pow(c_i.y-c_j.y,2)+math.pow(c_i.z-c_j.z,2)) #centro p_i, p_j
    if r==0:
        return 0

    dAj = p_j.area
    H_ij = visib  # en este caso, todos los parches son visibles para todos (no hay obstaculos)
    
    #cosenos segun http://www.geoan.com/vectores/angulo.html
    costi = (d_ij.x*n_i.x + d_ij.y*n_i.y + d_ij.z*n_i.z)/((math.sqrt(d_ij.x*d_ij.x + d_ij.y*d_ij.y + d_ij.z*d_ij.z))*(math.sqrt(n_i.x*n_i.x+n_i.y*n_i.y+n_i.z*n_i.z)))
    costj = (d_ij.x*n_j.x + d_ij.y*n_j.y + d_ij.z*n_j.z)/((math.sqrt(d_ij.x*d_ij.x + d_ij.y*d_ij.y + d_ij.z*d_ij.z))*(math.sqrt(n_j.x*n_j.x+n_j.y*n_j.y+n_j.z*n_j.z)))
    
    # F_ij = 
    return ((costi*costj)/(math.pi*math.pow(r,2)))*H_ij*dAj
    
def sistema(a,b):
    x = linalg.solve(a, b)
    return x
    
# recibe dos parches, y determina el factor de visibilidad entre los centros de ambos (valor 0 o 1)
def visibility(p_i,p_j,PL):
    global patchesList
    rvalue = 1
    patchesList = PL
    # # global counter
    # # centros de p_, p_j
    # ci = p_i.center
    # cj = p_j.center
    # # counter = counter + 1
    # # print "vis ",counter
    # #  PARA CADA PARCHE P EN LA ESCENA
    # for x in range(0,len(patchesList)):
    #     p = patchesList[x]
    #     cp = p.center
    # #     CALCULAR ANGULO THETA ENTRE VECTORES PI,PJ Y PI,CP
    #     v = cp.resta(ci,1)
    #     w = cj.resta(ci,1)
    #     if( v.modulo() == 0 or w.modulo() == 0):
    #         return 1
    #     theta = v.anguloEntre(w)
    # #     CALCULAR DISTANCIA COMO (CP-PI)SEN THETA
    #     d = math.sin(theta) * v.modulo()
    # #     CALCULAR MAYOR DISTANCIA ENTRE UN VERTICE DE P Y EL CENTRO DE P (DIS_MAX = DM)
    #     dm = p.pradio
    #     dmm = p.pmradio
    # #     CALCULAR ANGULO ENTRE NORMAL DE P Y R, ANGULO = TH
    #     alpha = p.normal.anguloEntre(w)
    # #     CALCULAR DD = DM*COS(TH) -> 'CUANTO SE ACERCA P A R'
    #     dd = dm*math.cos(alpha)
    #     ddm = dmm*math.cos(alpha)
    # #     SI D < DD => RECTA ATRAVIESA PARCHE
    # #        RETURN 0
    #     if( d < ddm ):
    #         return 0
    #     elif(d < dd):
    #         rvalue = 0.8
        # FIN DEL LOOP
    
    #  RETURN 1
    return rvalue

