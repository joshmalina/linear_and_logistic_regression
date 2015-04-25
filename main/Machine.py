import lin_reg

print("Welcome to our machine. Which algorithm would you like to run?")

print("1) univariate linear regression:")

algorithm = input("Your choice: ")

print("Thank you. What parameter would you like to run it on?")

print("1) wind speed")

parameter = input("Your choice: ")

print("Thank you for choising wind speed. In Beijing, the wind never reaches higher than 33 mph. \nPlease enter a windspeed of your choosing:")

speed = input("Your choice: ")

pol_val = lin_reg.predict_y_give_x(speed)

print("Our estimate for pollution levels at that speed is: ")
print(pol_val)