# 1. create an empty list
my_list = []

#Append elements 
my_list.append(20)
my_list.append(10)
my_list.append(30)
my_list.append(40)

#insert 15 at second position
my_list.insert(1, 15)

#extend with 50, 60, 70
my_list.extend([50, 60, 70])

#remove element 
my_list.pop()

#sort my list in ascending
my_list.sort()

# find and print
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)