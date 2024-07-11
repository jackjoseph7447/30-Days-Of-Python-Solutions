# Day 3 Exercises

age = 22
height = 6.25
complex = 1j + 2

user_tri_base = input('Enter the triangle base ')
user_tri_height = input('Enter the triangle height ')
user_tri_area = 0.5 * int(user_tri_base) * int(user_tri_height)
print('The area of the triangle is', user_tri_area)

user_side_a = input('Side A: ')
user_side_b = input('Side B: ')
user_side_c = input('Side C: ')
user_tri_sides_prim = int(user_side_a) + int(user_side_b) + int(user_side_c)
print('The perimeter of the triangle is', user_tri_sides_prim)

user_rec_width = int(input('Rectangle Width: '))
user_rec_height = int(input('Rectangle Height: ')) #Can make int when in taking values
user_rec_area = user_rec_height * user_rec_width
user_rec_prim = (user_rec_height * 2) + (user_rec_width * 2) #Rework
print('The area of the rectangle is', user_rec_area)
