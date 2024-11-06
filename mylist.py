#Question One & Two(Create empty list & Append)

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#Question Three(Insert value)
my_list = [10, 20, 30, 40]  
my_list.insert(1, 15)  
print(my_list)

#Question Four(Extend list)
my_list = [10, 15, 20, 30, 40]  #  the current list
my_list.extend([50, 60, 70])
print(my_list)

#Question Five(Remove last element)
my_list =[10, 15, 20, 30, 40, 50, 60, 70]
my_list.pop()
print(my_list)

# Question Six(Sort List in ASC)
my_list = [10,15,20,30,40,50,60]
my_list.sort()
print(my_list)

#Question Seven(Find and print index of value 30)
my_list = [10,15,20,30,40,50,60]
print(my_list.index(30))
