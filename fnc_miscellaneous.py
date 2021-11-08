#exec(open('fnc_miscellaneous.py').read())
import math

#calculate inner product of vector A and B
def inner_prod(A,B):
    result = 0
    for i in range(len(A)):
        result += A[i]*B[i]

    return result

#measure the magnitude of a vector A
def measure_vec(A):
    temp = 0
    for i in range(len(A)):
        temp += A[i]**2
    result = temp**0.5

    return result

#measure the angle between vector A and B
def measure_theta(A,B):
    
    result = math.acos(inner_prod(A, B)/(measure_vec(A)*measure_vec(B)))
    
    return result

#get the unit vector of vector A
def unitize(A):
    result = []
    for i in range(len(A)):
        result.append(A[i]/measure_vec(A))

    return result

#transform a point in Cartesian Cordinate System to Polar Coordinate System in three-dimensional space
def tf2PCS(x, y, z):
    mag = measure_vec([x,y,z])
    theta_1 = measure_theta([x,0],[x,y])
    theta_2 = measure_theta([x,y,0],[x,y,z])
    
    return [mag, theta_1, theta_2]

#transform a point in Polar Coordinate System to Cartesian Cordinate System in three-dimensional space
#r is radius, theta_1 is an angle between (x,0) and (x,y), theta_2 is an angle between (x,y,0) and (x,y,z)
def tf2CCS(r, theta_1, theta_2):
    sol_x = r*math.cos(theta_1)*math.cos(theta_2)
    sol_y = r*math.sin(theta_1)*math.cos(theta_2)
    sol_z = r*math.sin(theta_2)
    
    return [sol_x, sol_y, sol_z]
