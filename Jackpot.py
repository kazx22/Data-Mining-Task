#!/usr/bin/env python
# coding: utf-8

# In[8]:


mylist =['John',33,22.90,[1,2,3]]
mylist[3]

mytuple = (mylist) # This is Wrong
print(f"Wrong Tuple: {mytuple}")
mytuple = ('abcd', 786, 2.23, 'John', 70.2)
print(f"Right Tuple: {mytuple}")


# In[13]:


mylist = ['abcd', 786 , 2.23, 'john', 70.2]
tinylist = [123, 'john']
print(mylist)
print(mylist[0], 'and' , mylist[1])
print(mylist[1:3])
print(mylist[2:])
print(mylist[2:-1])
print(mylist[-1])
print(tinylist*2)
print(tinylist*2+mylist)


# In[18]:


mylist[3][0] = 'John'


# In[20]:


mylist
tinylist = (123, 'john')
print(tinylist)


# In[37]:


mylist = [5, 786 , 2.23, 1, 70.2,2,2]
print('Length',len(mylist))
mylist[::-1]
mylist.sort()
print('sorted',mylist)
mylist.count(2)
mylist.remove(2)
print('removed items', mylist)
mylist.pop()
print(mylist)


# In[ ]:


c = int(input('celsius'))
print(\n)
f = 9/5 * c + 32
print(f)
if(f>90):
    print('Heat Warning')
elif(f<30):
    print('Cold Warning')
else:
    print('Nice Weather')


# In[60]:


ip = int(input('Numbers'))
print('\n')
y = 0 
for i in range(ip):
    y= y+i
print(y)


# In[77]:


import random

att = int(input('Attempts'))
slot = int(input('Slot Numbers'))
slots = []
mac = []
count = 0

for i in range(att):
    for i in range(slot):
        slots.append(random.randint(1,7)) # [2,1,2,3] slot[0] = slot[1] = slot [2] = slot [3] (Y/N)       
    print(slots)
    x = random.randint(1,7)
    
    for i in range (slot):
        mac.append(x) # [2,1,2,3]
    if mac == slots:
        print('Win')
        count+=1
    else:
        print('Try Again')
    slots = []
wp = count / att
print('Percentage',wp)


# ## 

# In[88]:


att = int(input('Attempts'))
slot = int(input('Slot Numbers'))
slots = []
count = 0
c = 1
for i in range(att):
    for i in range(slot):
        slots.append(random.randint(1,3))      
    print(slots)
    for i in range(len(slots)-1):
            if(slots[i] == slots[i+1]):
                c+=1
                print("Win")
                continue
            else:
                break
    if(c == slots):
        print('You Win')
        count+=1
    else:
        print('Try Again')
    slots= []
print('Win Percantage', count/att)
            



# ## 

# In[ ]:




