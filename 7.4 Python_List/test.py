# How to create a List 

my_list = [1,2,3,4,5]

last_ele = my_list[-1] #you can access the last element by using negative index

print(last_ele)

# Modifiy the list by using append

#add element in current list. It will add to the end.

my_list.append(6)

print(my_list[-1])

#add element to specific postion by insert()

my_list.insert(0,7) #the number 7 will at postion 0.

result_insert = my_list

print(result_insert)

#remove element fro specific postion by using remove()

my_list.remove(2)

result_remove = my_list

print(result_remove)

#trim out the specific position of the list using by :

result_slice = my_list[0:2] # it will start with index 0 and print upto 1.
