import time
import sys
import math

opening = '''
                INTERNATIONAL STANDARD ATMOSPHERE
                            CALCULATOR
                -------------------------------------
        This program took away 13 hours from someone's life 
                            
            '''
for letter in opening:
    print(letter,end='',flush=True)
    time.sleep(0.08)


R = 287.05
g = 9.8
gamma = 1.4

try:
    height = float(input('Enter height for atmosphere calculation  :  '))
    if height <0:
        print( print('Enter only positive numbers ',end = '' , flush = True))
        time.sleep(0.08)

    
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
            
    

def troposphere():

    message = '''
                This height falls in layer that goes 0km to 11km above the sea level.
                It is called troposphere
                In this layer temperature goes on decreasing (negative temp gradient).
                
                temp_sea_level = 288.15 K
                lapse_rate = -6.5e-3 K/m
                pressure_sea_level = 101325 Pa
                density_sea_level = 1.225 kg/m**3
    '''
    
    for letter in message:
       print(letter , end = '' , flush = True)
       time.sleep(0.08)
        
    temp_sea_level = 288.15
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



def tropopause():

    message_ = '''
                This height falls in layer that goes 11km to 20km 
                above the sea level and it is called Tropopause.
                In this layer temperature tends to be the same throughout.
                
                temp_reference = 216.65 K
                lapse_rate = 0 K/m
                pressure_reference  =  22632.06 Pa
                density_reference = 0.3639 kg/m**3
                reference_height = 11000 m
    '''
    
    for letter in message_:
        print(letter,end='',flush=True)
        time.sleep(0.08)
    
    # call the height conversion function to make same units 
    height_conversion(height)
        
    temp_reference = 216.65
    pressure_initial  =  22632.06 
    density_reference = 0.3639
    reference_height = 11000
    
    print(' ')
    # starting pressure calculation
    height_change = height_required - reference_height

    print()
    print()
    pressure_at_height = pressure_initial*math.exp(-(height_change*g)/(R*temp_reference))
    print(f'pressure at {height_required} is {pressure_at_height} Pa',end='',flush=True)
    time.sleep(0.08)

    print()
    print()
    density_at_height = pressure_at_height/(R*temp_reference)
    print(f'density of air at {height_required} m is {density_at_height} kg/m**3 ', end='' ,flush = True)
    time.sleep(0.08)
    
    print()
    print()
    velocity_at_height = (gamma*R*temp_reference)**(1/2)
    print(f'Velocity of air at {height_required} is {velocity_at_height:.2f} m/s', end='',flush=True)
    time.sleep(0.08)
    print()
    print()
    
    
       

def lower_stratosphere():

    message = '''
                This height falls in layer that goes 20km to 32km above the sea level.
                It is called lower stratosphere
                In this layer temperature goes on increasing (positive temp gradient).
                
                temperature reference = 216.65 K
                lapse rate = 0.001 K/m
                pressure reference = 5474.89 Pa
                reference height = 20000 m
                
    '''
    
    for letter in message:
       print(letter , end = '' , flush = True)
       time.sleep(0.08)
        
    temp_reference = 216.65
    lapse_rate = 0.001 
    pressure_reference = 5474.89
    
    # call the height conversion function to make same units 
    height_conversion(height)
    
    
    print()
    print()
    # starting temperature calculation
    height_difference = height_required - 20000.0
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


def upper_stratosphere():

    message = '''
                This height falls in layer that goes 32km to 47km above the sea level.
                In this layer temperature goes on increasing (positive temp gradient).
                It is called upper stratosphere
                
                temp_reference = 228.65 K
                lapse_rate = 2.8e-3 K/m
                pressure_reference = 868.2 Pa
                reference height = 32000 m
                
    '''
    
    for letter in message:
       print(letter , end = '' , flush = True)
       time.sleep(0.08)
        
    temp_reference = 228.65
    lapse_rate = 2.8e-3 
    pressure_reference = 868.2
    
    # call the height conversion function to make same units 
    height_conversion(height)
    
    
    print()
    print()
    # starting temperature calculation
    height_difference = height_required - 20000.0
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
    


def stratopause():

    message_ = '''
                This height falls in layer that goes 47km to 51km 
                above the sea level and it is called the Stratopause.
                In this layer temperature tends to be the same throughout.
                
                temp_reference = 270.65 K
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
    print()
    # starting pressure calculation
    height_change = height_required - reference_height

    print()
    print()
    pressure_at_height = pressure_initial*math.exp(-(height_change*g)/(R*temp_reference))
    print(f'pressure at {height_required} is {pressure_at_height:.2f} Pa',end='',flush=True)
    time.sleep(0.08)
    
    print()
    print()
    density_at_height = pressure_at_height/(R*temp_reference)
    print(f'density of air at {height_required} m is {density_at_height:.4f} kg/m**3 ', end='' ,flush = True)
    time.sleep(0.08)
    
    print()
    print()
    velocity_at_height = (gamma*R*temp_reference)**(1/2)
    print(f'Velocity of air at {height_required} is {velocity_at_height:.2f} m/s', end='',flush=True)
    time.sleep(0.08)
    print()
    print()
    
    
def lower_mesosphere():

    message = '''
                This height falls in layer that goes 51km to 71km above the sea level.
                In this layer temperature goes on decreasing (negative temp gradient).
                It is called lower mesosphere
                
                temp_reference = 270.65 K
                lapse_rate = -2.8e-3 K/m
                pressure_reference = 66.94 Pa
                reference height = 51000 m
                
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
 

def upper_mesosphere():

    message = '''
                This height falls in layer that goes 71km to 84km above the sea level.
                In this layer temperature goes on decreasing (negative temp gradient).
                It is called upper mesosphere
                
                temp_reference = 214.65 K
                lapse_rate = -2e-3 K/m
                pressure_reference = 3.96Pa
                reference height = 51000 m
                
    '''
    
    for letter in message:
       print(letter , end = '' , flush = True)
       time.sleep(0.08)
        
    temp_reference = 214.65
    lapse_rate = -2e-3 
    pressure_reference = 51.87
    reference_height = 71000
    
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


def uppermost_layer():

    message = '''
                This height falls in layer that goes 84km plus above the sea level.
                In this layer temperature does not follow any particular equation
                It is called upper atmosphere
                
                temp_reference = 186.95 K
                lapse_rate = not contant
                pressure_reference = 0.184 Pa
                reference height = 84000 m
                
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
    troposphere()     
    
elif height_required > 11000.0 and height_required <= 20000.0:
    tropopause()
    
elif height_required > 20000.0 and height_required <=32000.0:
    lower_stratosphere()

elif height_required > 32000.0 and height_required <=47000.0:
    upper_stratosphere()
    
elif height_required > 47000.0 and height_required <= 51000.0:
    stratopause()
    
elif height_required > 51000.0 and height_required <= 71000.0:
    lower_mesosphere()

elif height_required > 71000.0 and height_required <= 84000.0:
    upper_mesosphere()
 
elif height_required > 84000.0:
    uppermost_layer()


closing = '''    --------------------------
                  ISA CALCULATOR 
                     Version 1
            Developed by Eliudi Elphace Tonda
                     05 September 2026
        ---------------------------------------
                     '''
for letter in closing:
    print(letter,end='',flush=True)
    time.sleep(0.08)
