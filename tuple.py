
#accessing a first item in a tuple
my_tuple = ("Faith", "Maureen", "Kate,", "Andrew", "Zack", "Kinsley")
print(my_tuple[0])

#adding an item in a tuple

data = (3,8,8,"Mwendwa")
list1 = list(data)
list1.append(6)
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