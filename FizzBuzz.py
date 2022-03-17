#!/usr/bin/env python
# coding: utf-8

# In[47]:


number = int(input())
list1 = list(range(1,number + 1))
list2 = []
for i in list1:
    if i % 3 == 0 and i % 5 == 0:
        list2.append("FizzBuzz")
    elif i % 3 == 0:
        list2.append("Fizz")
    elif i % 5 == 0:
        list2.append("Buzz")
    else:
        list2.append(i)
print(list2)        


# 

# In[ ]:




