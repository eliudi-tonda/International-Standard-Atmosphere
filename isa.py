

import time
import sys
import math

R = 287.05
g = 9.8
gamma = 1.4

try:
    height = float(input('Enter height  :  '))

    
except ValueError:
    print('Enter only positive numbers ',end = '' , flush = True)
    time.sleep(0.8)
    sys.exit()
    
height_message = '''
    Press 1 if it is in meters
    Press 2 if it is in feet
    press 3 if it is in kilometers
'''
for letter in height_message:
    print(letter , end='' , flush = True )
    time.sleep(0.08)
    
option = input('Enter 1,2 or 3 for height units : ')


def height_conversion(height):
    if option == '1':
        global height_required
        height_required = height
        
        msg = f'the height is {height} in meters'
        for letter in msg:
            print(letter , end = '',flush = True)
            time.sleep(0.08)
        return height_required
            
    elif option == '2':
        height1 = 0.3048*height
        msg = f'the height is {height1} in meters'
        for letter in msg:
            print(letter , end = '',flush = True)
            time.sleep(0.08)
        
        height_required = height1
        return height_required
        
    elif option == '3':
        height2 = 1000*height
        msg = f'the height is {height2} in meters'
        for letter in msg:
            print(letter , end = '',flush = True)
            time.sleep(0.08)
            
        height_required = height2
        return height_required
            
    else:
        warning ='sorry options are 1,2 and 3 only please check again'
        for i in warning:
            print(i , end = '' , flush = True)
            time.sleep(0.08)
            
    

def gradient_layer_1():

    message = '''
                This height falls in layer that goes 0km to 11km above the sea level.
                Temperature at sea level is  15 degrees which which is 288.16K.
                In this layer temperature goes on decreasing (negative temp gradient).
                
                temp_sea_level = 288.16 K
                lapse_rate = -6.5e-3 K/m
                pressure_sea_level = 101325 Pa
                density_sea_level = 1.225 kg/m**3
    '''
    
    for letter in message:
       print(letter , end = '' , flush = True)
       time.sleep(0.08)
        
    temp_sea_level = 288.16
    lapse_rate = -6.5e-3
    pressure_sea_level = 101325
    density_sea_level = 1.225
    
    # call the height conversion function to make same units 
    height_conversion(height)
    
    
    print()
    print()
    # starting temperature calculation
    temp_at_height = temp_sea_level + lapse_rate*height_required
    print(f'temperature at {height} is {temp_at_height:.2f} kelvin',end='',flush=True)
    time.sleep(0.08)
    
    print()
    print()
    #starting calculating pressure
    pressure_at_height = pressure_sea_level*(temp_at_height/temp_sea_level)**(-g/(lapse_rate*R))
    print(f'pressure at {height_required} is {pressure_at_height:.2f} Pa',end='',flush=True)
    time.sleep(0.08)
    
    print()
    print()
    density_at_height = pressure_at_height/(R*temp_at_height)
    print(f'density of air at {height_required} is {density_at_height:.2f} kg/m**3',end='',flush=True)
    time.sleep(0.08)
    
    print()
    print()
    velocity_at_height = (gamma*R*temp_at_height)**(1/2)
    print(f'Velocity of air at {height_required} is {velocity_at_height:.2f} m/s', end='',flush=True)
    time.sleep(0.08)
    print()
    print()



def isothermal_layer_1():

    message_ = '''
                This height falls in layer that goes 11km to 25km 
                above the sea level and it is called the isothermal.
                In this layer temperature tends to be the same throughout.
                
                temp_reference = 216.66 K
                lapse_rate = 0 K/m
                pressure_reference  =  22656.06 Pa
                density_reference = 0.36 kg/m**3
                reference_height = 11000 m
    '''
    
    for letter in message_:
        print(letter,end='',flush=True)
        time.sleep(0.08)
    
    # call the height conversion function to make same units 
    height_conversion(height)
        
    temp_reference = 216.66 
    pressure_initial  =  22632.06 
    density_reference = 0.36 
    reference_height = 11000
    
    print(' ')
    # starting pressure calculation
    height_change = height_required - 11000.0
    
    pressure_at_height = pressure_initial*math.exp(-(height_change*g)/(R*temp_reference))
    print(f'pressure at {height_required} is {pressure_at_height} Pa',end='',flush=True)
    time.sleep(0.08)
    
    density_at_height = pressure_at_height/(R*temp_reference)
    print(f'density of air at {height_required} m is {density_at_height} kg/m**3 ', end='' ,flush = True)
    time.sleep(0.08)
    
    print()
    velocity_at_height = (gamma*R*temp_reference)**(1/2)
    print(f'Velocity of air at {height_required} is {velocity_at_height:.2f} m/s', end='',flush=True)
    time.sleep(0.08)
    print()
    print()
    
    
       

def gradient_layer_2():

    message = '''
                This height falls in layer that goes 25km to 47km above the sea level.
                Temperature reference at this level is 216.666K.
                In this layer temperature goes on increasing (positive temp gradient).
                
                temp_reference = 216.66 K
                lapse_rate = 3e-3 K/m
                pressure_reference = 2518.18 Pa
                reference height = 25000 m
                
    '''
    
    for letter in message:
       print(letter , end = '' , flush = True)
       time.sleep(0.08)
        
    temp_reference = 216.66
    lapse_rate = 3e-3 
    pressure_reference = 2518.18
    
    # call the height conversion function to make same units 
    height_conversion(height)
    
    
    print()
    print()
    # starting temperature calculation
    height_difference = height_required - 25000.0
    temp_at_height = temp_reference + lapse_rate*height_difference
    print(f'temperature at {height} m is {temp_at_height:.2f} kelvin',end='',flush=True)
    time.sleep(0.08)
    
    print()
    print()
    #starting calculating pressure
    pressure_at_height = pressure_reference*(temp_at_height/temp_reference)**(-g/(lapse_rate*R))
    print(f'pressure at {height_required} is {pressure_at_height:.2f} Pa',end='',flush=True)
    time.sleep(0.08)
    
    print()
    print()
    density_at_height = pressure_at_height/(R*temp_at_height)
    print(f'density of air at {height_required} is {density_at_height:.4f} kg/m**3',end='',flush=True)
    time.sleep(0.08)
    
    print()
    print()
    velocity_at_height = (gamma*R*temp_at_height)**(1/2)
    print(f'Velocity of air at {height_required} is {velocity_at_height:.2f} m/s', end='',flush=True)
    time.sleep(0.08)
    print()
    print()
    

def isothermal_layer_2():

    message_ = '''
                This height falls in layer that goes 47km to 53km 
                above the sea level and it is called the isothermal.
                In this layer temperature tends to be the same throughout.
                
                temp_reference = 282.66 K
                lapse_rate = 0 K/m
                pressure_reference  =  110.91 Pa
                reference_height = 47000 m
    '''
    
    for letter in message_:
        print(letter,end='',flush=True)
        time.sleep(0.08)
    
    # call the height conversion function to make same units 
    height_conversion(height)
        
    temp_reference = 282.66 
    pressure_initial  =  110.91 
    reference_height = 47000
    
    print(' ')
    # starting pressure calculation
    height_change = height_required - reference_height
    
    pressure_at_height = pressure_initial*math.exp(-(height_change*g)/(R*temp_reference))
    print(f'pressure at {height_required} is {pressure_at_height:.2f} Pa',end='',flush=True)
    time.sleep(0.08)
    
    print()
    density_at_height = pressure_at_height/(R*temp_reference)
    print(f'density of air at {height_required} m is {density_at_height:.4f} kg/m**3 ', end='' ,flush = True)
    time.sleep(0.08)
    
    print()
    velocity_at_height = (gamma*R*temp_reference)**(1/2)
    print(f'Velocity of air at {height_required} is {velocity_at_height:.2f} m/s', end='',flush=True)
    time.sleep(0.08)
    print()
    print()
    
    
def gradient_layer_3():

    message = '''
                This height falls in layer that goes 53km to 79km above the sea level.
                Temperature reference at this level is 282.66K.
                In this layer temperature goes on decreasing (negative temp gradient).
                
                temp_reference = 282.66 K
                lapse_rate = -4.5e-3 K/m
                pressure_reference = 51.87 Pa
                reference height = 53000 m
                
    '''
    
    for letter in message:
       print(letter , end = '' , flush = True)
       time.sleep(0.08)
        
    temp_reference = 282.66
    lapse_rate = -4.5e-3 
    pressure_reference = 51.87
    reference_height = 53000
    
    # call the height conversion function to make same units 
    height_conversion(height)
    
    
    print()
    print()
    # starting temperature calculation
    height_difference = height_required - reference_height
    temp_at_height = temp_reference + lapse_rate*height_difference
    print(f'temperature at {height} m is {temp_at_height:.2f} kelvin',end='',flush=True)
    time.sleep(0.08)
    
    print()
    print()
    #starting calculating pressure
    pressure_at_height = pressure_reference*(temp_at_height/temp_reference)**(-g/(lapse_rate*R))
    print(f'pressure at {height_required} is {pressure_at_height:.2f} Pa',end='',flush=True)
    time.sleep(0.08)
    
    print()
    print()
    density_at_height = pressure_at_height/(R*temp_at_height)
    print(f'density of air at {height_required} is {density_at_height:.4f} kg/m**3',end='',flush=True)
    time.sleep(0.08)
    
    print()
    print()
    velocity_at_height = (gamma*R*temp_at_height)**(1/2)
    print(f'Velocity of air at {height_required} is {velocity_at_height:.2f} m/s', end='',flush=True)
    time.sleep(0.08)
    print()
    print()
 

def isothermal_layer_3():

    message_ = '''
                This height falls in layer that goes 79km to 90km 
                above the sea level and it is called the isothermal.
                In this layer temperature tends to be the same throughout.
                
                temp_reference = 165.66 K
                lapse_rate = 0 K/m
                pressure_reference  =  1.23 Pa
                reference_height = 79000 m
    '''
    
    for letter in message_:
        print(letter,end='',flush=True)
        time.sleep(0.08)
    
    # call the height conversion function to make same units 
    height_conversion(height)
        
    temp_reference = 165.66 
    pressure_initial  =  1.23 
    reference_height = 79000
    
    print(' ')
    # starting pressure calculation
    height_change = height_required - reference_height
    
    pressure_at_height = pressure_initial*math.exp(-(height_change*g)/(R*temp_reference))
    print(f'pressure at {height_required} is {pressure_at_height:.3f} Pa',end='',flush=True)
    time.sleep(0.08)
    
    print()
    density_at_height = pressure_at_height/(R*temp_reference)
    print(f'density of air at {height_required} m is {density_at_height:.8f} kg/m**3 ', end='' ,flush = True)
    time.sleep(0.08)
    
    print()
    velocity_at_height = (gamma*R*temp_reference)**(1/2)
    print(f'Velocity of air at {height_required} is {velocity_at_height:.3f} m/s', end='',flush=True)
    time.sleep(0.08)
    print()
    print()
  

def gradient_layer_4():

    message = '''
                This height falls in layer that goes 90km plus above the sea level.
                Temperature reference at this level is 165.66K.
                In this layer temperature goes on increasing (positive temp gradient).
                
                temp_reference = 165.66 K
                lapse_rate = 4e-3 K/m
                pressure_reference = 0.184 Pa
                reference height = 90000 m
                
    '''
    
    for letter in message:
       print(letter , end = '' , flush = True)
       time.sleep(0.08)
        
    temp_reference = 165.66
    lapse_rate = 4e-3 
    pressure_reference = 0.154
    
    # call the height conversion function to make same units 
    height_conversion(height)
    
    
    print()
    print()
    # starting temperature calculation
    height_difference = height_required - 90000.0
    temp_at_height = temp_reference + lapse_rate*height_difference
    print(f'temperature at {height} m is {temp_at_height:.2f} kelvin',end='',flush=True)
    time.sleep(0.08)
    
    print()
    print()
    #starting calculating pressure
    pressure_at_height = pressure_reference*(temp_at_height/temp_reference)**(-g/(lapse_rate*R))
    print(f'pressure at {height_required} is {pressure_at_height:.4f} Pa',end='',flush=True)
    time.sleep(0.08)
    
    print()
    print()
    density_at_height = pressure_at_height/(R*temp_at_height)
    print(f'density of air at {height_required} is {density_at_height:.8f} kg/m**3',end='',flush=True)
    time.sleep(0.08)
    
    print()
    print()
    velocity_at_height = (gamma*R*temp_at_height)**(1/2)
    print(f'Velocity of air at {height_required} is {velocity_at_height:.3f} m/s', end='',flush=True)
    time.sleep(0.08)
    print()
    print()
 
height_required = height_conversion(height) 
 
# initiating layers
if height_required >= 0.0 and height_required <= 11000.0:
    gradient_layer_1()       
    
elif height_required > 11000.0 and height_required <= 25000.0:
    isothermal_layer_1()
    
elif height_required > 25000.0 and height_required <=47000.0:
    gradient_layer_2()
    
elif height_required > 47000.0 and height_required <= 53000.0:
    isothermal_layer_2()
    
elif height_required > 53000.0 and height_required <= 79000.0:
    gradient_layer_3()

elif height_required > 79000.0 and height_required <= 90000.0:
    isothermal_layer_3()
 
elif height_required > 90000.0:
    gradient_layer_4() 