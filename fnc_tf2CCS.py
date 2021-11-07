#exec(open('fnc_tf2CCS.py').read())
import math
from sympy import *

x, y, z = symbols('x y z', real=True)

#r is radius, theta_1 is an angle between (x,0) and (x,y), theta_2 is an angle between (x,y,0) and (x,y,z)
def tf2CCS(r, theta_1, theta_2):
    sol_x = math.cos(theta_1)*math.cos(theta_2)
    sol_y = math.sin(theta_1)*math.cos(theta_2)
    sol_z = math.sin(theta_2)
    
    return [sol_x, sol_y, sol_z]
