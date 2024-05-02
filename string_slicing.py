#string slicing
 
name="HAPPY"
print(name[:1])
print(name[0:2])
print(name[0:3])
print(name[0:4])
print(name[0:5])
 
print(name[4])
print(name[3:5])
print(name[2:5])
print(name[1:5])
print(name[0:5])

x=slice(0,2)
print(name[x])
 
 #list
 
cities=["coimbatore","madurai","trichy","chennai","salem"]

#acessing the list
print(cities[::3])

#modified the list (Exchange the values)
cities[4]="kerala"
print(cities)

#append the list (insert the last place)
cities.append("thuthukudi")
print(cities)

#insert the value in the choose the user index place
cities.insert(1,"bombay")
print(cities)

#pop the list (delete the value in list and display the deleted value)
Delete=cities.pop(5)
print(cities)
print(Delete)

#length of the list
print(len(cities)) 

#REVERSE THE list
cities.reverse()
print(cities)

#______________________________________ EXCERISE_______________________________________#

