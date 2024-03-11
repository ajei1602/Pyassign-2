# empty list
my_list= []
# appending to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
#inserting 15
my_list.insert(1,15)
print("updated list = \n",my_list)
# extending my_list
my_list = [10,15,20,30,40]
print("list1:", my_list)
anotherlist= [50,60,70]
print("list2:", anotherlist)
#join two lists
my_list.extend(anotherlist)
print("list after extend:", my_list)
#removing last element
my_list= [10,15,20,30,40,50,60,70]
del my_list[-1]
print(my_list)
# sorting in ascending order
my_list= [10,15,20,30,40,50,60]
print(my_list)
my_list.sort()
print(my_list)
# Finding and printing the index of 30
index= my_list.index(30)
print("The index of",30, "in the list is:", index)




        
