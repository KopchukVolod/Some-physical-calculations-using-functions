# Thef_to_c takes(F - 32) * 5/9.
# The function c_to_f takes a temperature in Celsius as input and returns the equivalent temperature in Fahrenheit using the conversion formula C * 9/5 + 32.
# The function get_force takes a mass and acceleration as inputs and returns the force using the formula F = m * a.
# The function get_energy takes a mass as input and returns the energy using the formula E = m * c^2, where c is the speed of light and is set to 3*10**8 by default.
# The function get_work takes a mass, acceleration, and distance as inputs and returns the work done using the formula W = F * d, where F is the force calculated using get_force function.
# The code also calculates the following values:
#
# f100_in_celsius is the equivalent temperature of 100°F in Celsius, calculated using f_to_c function.
# c0_in_fahrenheit is the equivalent temperature of 0°C in Fahrenheit, calculated using c_to_f function.
# train_force is the force exerted by a train with a mass of 22680 kg and acceleration of 10 m/s^2, calculated using get_force function.
# bomb_energy is the energy released by a 1 kg bomb, calculated using get_energy function.
# train_work is the work done by the same train over a distance of 100 meters, calculated using get_work function.
# The code then prints out some statements that display the calculated values using string concatenation with str() function.

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

def f_to_c(f_temp):
  c_temp =  (f_temp - 32) * 5/9
  return c_temp
  
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c=3*10**8):
  return mass * c
bomb_energy = get_energy(bomb_mass)
print(bomb_energy)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) +  " Joules of work over " + str(train_distance) + " meters.")






 