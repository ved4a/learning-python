cars = ['audi', 'jaguar', 'bmw', 'mercedes']

for car in cars: # looping through list
    if car == 'bmw': # with a condition
        print(car.upper())
    else:
        print(car.title())

# checking for equality
car = 'jaguar' # set the value of 'car' to be 'jaguar'
car == 'audi' # is the value of 'car' audi? -> False
car == 'jaguar' # is the value of 'car' jaguar? -> True

# equality test is case-sensitive, so:
car == 'Jaguar' # this would be False

# can also test for inequalities
requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print('Hold the anchovies!')