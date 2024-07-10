# Day 2: 30 Days of python programming

first_name = 'John'
last_name = 'Joseph'
full_name = 'John Joseph'
country = 'United States'
city = 'Philadelphia'
age = 22
year = 2024
is_married = False
is_true = True
is_light_on = True
my_info = {
    full_name,
    country,
    city,
    age
}

print(my_info) #Check to make sure variables are declared correctly

#Exercise Level 2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(my_info))

print(len(first_name))

print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
divison = num_one / num_two
print(divison)
remainder = num_two % num_one
print(remainder)
exp = num_one ** num_two
print(exp)
floor_divison = num_one // num_two
print(floor_divison)

radius = 30
pi = 3.14
area_of_circle = pi * radius ** 2
print(area_of_circle)
circum_of_circle = 2 * pi * radius
print(circum_of_circle)
user = input('Enter the Radius ')
user_area = pi * int(user) ** 2
print(user_area)

print('Please enter the following information: ')
user_first = input('First Name: ')
user_last = input('Last Name: ')
user_age = input('Age: ')
user_country = input('Country: ')

print(user_first)  
print(user_last)  
print(int(user_age))  
print(user_country)
