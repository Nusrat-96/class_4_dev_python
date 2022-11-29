list1=[]
for i in range (0,10):
    input_list= (input())
    if input_list in (list1):
        print ("Already in the list")
    else:
        list1.append(input_list)
print(list1)
