# empty list
my_list = []


# append 10,20,30,40 to my_list
my_list.extend([10, 20, 30, 40])


# insert 15 in the second position
my_list.insert(1, 15)


# extend my_list with another list
my_list.extend([50, 60, 70])


# remove last element from my_list
my_list.pop(-1)


# sort my_list in ascending order
my_list.sort()


# find and print the index of the value 30 in my_list
index = my_list.index(30)
print(index)
