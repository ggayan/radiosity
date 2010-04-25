from numpy import *

# recibe 2 parches i y j, retorna el F_ij  (al parecer, F_ij != F_ji)
def formfactor(p_i,p_j):
    # segun http://www.gamedev.net/reference/articles/article653.asp
    #       http://wiki.cgsociety.org/index.php/Radiosity#Form_Factor_Determination
    #
    # F_ij = [(cos thetai * cos thetaj)/pi*r^2]*H_ij*dAj
    c_i = centro(p_i)
    c_j = centro(p_j)
    n_i = normal(p_i)
    n_j = normal(p_j)
    d_ij = Punto(c_j.x-c_i.x, c_j.y-c_i.y, c_j.z-c_i.z)
    
    H_ij = 1  # en este caso, todos los parches son visibles para todos (no hay obstaculos)
    r = math.sqrt(math.pow(c_i.x-c_j.x,2)+math.pow(c_i.y-c_j.y,2)+math.pow(c_i.z-c_j.z,2)) #centro p_i, p_j
    dAj = area(p_j)
    #cosenos segun http://www.geoan.com/vectores/angulo.html
    costi = (d_ij.x*n_i.x + d_ij.y*n_i.y + d_ij.z*n_i.z)/((math.sqrt(d_ij.x*d_ij.x + d_ij.y*d_ij.y + d_ij.z*d_ij.z))*(math.sqrt(n_i.x*n_i.x+n_i.y*n_i.y+n_i.z*n_i.z)))
    costj = (d_ij.x*n_j.x + d_ij.y*n_j.y + d_ij.z*n_j.z)/((math.sqrt(d_ij.x*d_ij.x + d_ij.y*d_ij.y + d_ij.z*d_ij.z))*(math.sqrt(n_j.x*n_j.x+n_j.y*n_j.y+n_j.z*n_j.z)))
    
    # F_ij = 
    return ((costi*costj)/(math.pi*math.pow(r,2)))*H_ij*dAj
    
def sistema(A,b):
