from numpy import *
from patch import *
from punto import *

# recibe 2 parches i y j, retorna el F_ij  (al parecer, F_ij != F_ji)
def formfactor(p_i,p_j):
    # segun http://www.gamedev.net/reference/articles/article653.asp
    #       http://wiki.cgsociety.org/index.php/Radiosity#Form_Factor_Determination
    #
    # F_ij = [(cos thetai * cos thetaj)/pi*r^2]*H_ij*dAj
    c_i = p_i.cn
    c_j = p_j.cn
    n_i = p_i.nr
    n_j = p_j.nr
    d_ij = Punto(c_i.x-c_j.x, c_i.y-c_j.y, c_i.z-c_j.z)
    
    H_ij = visibility(p_i,p_j)  # en este caso, todos los parches son visibles para todos (no hay obstaculos)
    r = math.sqrt(math.pow(c_i.x-c_j.x,2)+math.pow(c_i.y-c_j.y,2)+math.pow(c_i.z-c_j.z,2)) #centro p_i, p_j
    if r==0:
        return 0
    dAj = p_j.ar
    
    #cosenos segun http://www.geoan.com/vectores/angulo.html
    costi = (d_ij.x*n_i.x + d_ij.y*n_i.y + d_ij.z*n_i.z)/((math.sqrt(d_ij.x*d_ij.x + d_ij.y*d_ij.y + d_ij.z*d_ij.z))*(math.sqrt(n_i.x*n_i.x+n_i.y*n_i.y+n_i.z*n_i.z)))
    costj = (d_ij.x*n_j.x + d_ij.y*n_j.y + d_ij.z*n_j.z)/((math.sqrt(d_ij.x*d_ij.x + d_ij.y*d_ij.y + d_ij.z*d_ij.z))*(math.sqrt(n_j.x*n_j.x+n_j.y*n_j.y+n_j.z*n_j.z)))
    
    # F_ij = 
    return ((costi*costj)/(math.pi*math.pow(r,2)))*H_ij*dAj
    
def sistema(a,b):
    x = linalg.solve(a, b)
    return x
    
# recibe dos parches, y determina el factor de visibilidad entre los centros de ambos (valor entre 0 y 1)
def visibility(p_i,p_j):
    #  calcular recta entre centros de pi y pj, recta = r
    #  para cada parche p en la escena
    #     calcular distancia del centro de p a la recta (distancia = d)
    #     calcular mayor distancia entre un vertice de p y el centro de p (dis_max = dm)
    #     calcular angulo entre normal de p y r, angulo = th
    #     calcular dd = dm*cos(th) -> 'cuanto se acerca p a r'
    #     si d < dd => recta atraviesa parche
    #        return 0
    #  return 1
    
    return 1

