#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Task1
year = int(input("Enter a year: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("{0} is a leap year".format(year))  
       else:  
           print("{0} is not a leap year".format(year))  
   else:  
       print("{0} is a leap year".format(year))  
else:  
   print("{0} is not a leap year".format(year)) 


# In[22]:


##Task2
n = int(input())
if (n<=1) and (n>=50000):
    print("Exit")
else:
    for i in range(0,n):
        print(i*i)


# In[28]:





# In[ ]:




