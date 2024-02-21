name = input ("What is your name ? ")
age = input ("What is your age ? ")
location = input ("What is your location ? ")

print ("Your name is " + name )
print ("Your age is " + age )
print ("Your location is " + location )

message = "Your name is {} and your age is {} years old in {}". format(name, age, location)
print(message)