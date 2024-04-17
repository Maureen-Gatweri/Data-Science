
#accessing a first item in a tuple. tuples are accessed using the indexing method
my_tuple = ("Faith", "Maureen", "Kate,", "Andrew", "Zack", "Kinsley")
print(my_tuple[0])
print(my_tuple)

#Accessing the last item in a tuple
print(my_tuple[-1])

#adding an item in a tuple. Tuples are immutable, if you want to add an item, you first of all change it to a list then add items then return it to a tuple.

data = (3,8,8,"Mwendwa")
#making the tuple a list
list1 = list(data)
#adding an item
list1.append(6)
#return the new elements to a tuple.
list1= tuple(list1)
print(list1)

#removing an item from a tuple
tupple = ("Mwende", "Murkomen", "Tubei", "Yiamat", "Pearl")
list3 = list(tupple)
list3.remove("Yiamat")
list3 =tuple(list3)
print(list3)

#concatenation
my_tuple2 = my_tuple + tupple
print(my_tuple2)


my_tuple3 = my_tuple2 + data
print(my_tuple3)
print(my_tuple3[0])
