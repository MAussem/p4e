# for i in [5, 4, 3, 2, 1]:
# print(i)
#print("Bye Bye")

#l = 5
# while l > 0:
# print(l)
#l = l - 1
# print("Blasoff!")
# print(l)

#largest_so_far = -1
#print('Before', largest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15]:
# if the_num > largest_so_far:
#largest_so_far = the_num
#print(largest_so_far, the_num)
#print('After', largest_so_far)

#smallest = None
# print('Before')
# for the_num in [9, 41, 12, 3, 74, 15]:
# if smallest is None:
#smallest = the_num
# elif the_num < smallest:
#smallest = the_num
#print(smallest, the_num)
#print('After', smallest)

#found = False
#print('Before', found)
# for value in [9, 41, 12, 3, 74, 15]:
# if value == 3:
#found = True
# break
#print('After', found)

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        fn = int(num)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = fn
    elif fn < smallest:
        smallest = fn

    if largest is None:
        largest = fn
    elif fn > largest:
        largest = fn
print("Maximum is", largest)
print("Minimum is", smallest)
