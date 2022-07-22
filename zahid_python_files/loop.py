print("while loops")

#simple while loop
print("simple while loop")
i = 1
while i < 10:
  print(i)
  i += 2

#break in while loop
print("break containing while loop")
i = 1
while i < 100:
  print(i)
  if (i == 3):
    break
  i += 1

#continue statment in while loop
print("continue statment containing while loop")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i) 

#the else statment containing while loop
print("else statment containing while loop")
i = 1
while i < 6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")

print("for loops")

#print a list through for loop
print("for loop for list printing")

vehicle_list=["car", "vain","trailer","bike"]
for x in vehicle_list:
    print(x)

#for loop throuth a string
print("string in for loop")
for x in "Automotive":
    print(x)


#using break statment in the for loop
print("Break in for loop")
for x in vehicle_list:
    print(x)
    if x=="trailer":
        break

print("second method for break ")
for x in vehicle_list:
    if x== "trailer":
        break
    print(x)

#using continue statment in for loop
print("continue for loop")
for x in vehicle_list:
    if x == "vain":
        continue
    print(x)

#useing range function in for loop
print("range in for loop")
for x in range(6):
    print(x)