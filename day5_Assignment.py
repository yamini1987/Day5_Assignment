#!/usr/bin/env python
# coding: utf-8

# In[14]:


num_list=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [i  for i in num_list if i != 0]
    x.extend(a)
    return(x)
num_list.sort()
print(num_list)
print(move_zero([0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]))
#print(move_zero([0,2,3,4,6,7,10]))
#print(move_zero([10,0,11,12,0,14,17]))


# In[22]:


test_list1 = [10,20,40,60,70,80] 
test_list2 = [5,15,25,35,45,60] 
  
# printing original lists  
print ("The original list 1 is : " + str(test_list1)) 
print ("The original list 2 is : " + str(test_list2)) 
  
# using naive method  
# to combine two sorted lists 
size_1 = len(test_list1) 
size_2 = len(test_list2) 
  
res = [] 
i, j = 0, 0
  
while i < size_1 and j < size_2: 
    if test_list1[i] < test_list2[j]: 
      res.append(test_list1[i]) 
      i += 1
  
    else: 
      res.append(test_list2[j]) 
      j += 1
  
res = res + test_list1[i:] + test_list2[j:] 
  
# printing result 
print ("The combined sorted list is : " + str(res))


# In[20]:





# In[ ]:




