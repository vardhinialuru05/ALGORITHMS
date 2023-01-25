li = [1,2,3,4,5,6,7,8,9] #initializing a list
#li.insert(1,"vardhini")
#li.append("sharma") #puts at the last
#li.extend([10,11,12]) #or u can even do concat operation
#li += [10,11,12]
#li.pop() # pops the last index element from the list
#li.pop(2) #should give the index
#li.remove(2) # should give the value that we want to remove
print(li)
#list comprehension
li = [1,2,3,4]
li_new = []
for ele in li:
    li_new.append(ele**2)
print(li_new)
#so above all can be replaced with:
li_new =[ele**2 for ele in li]