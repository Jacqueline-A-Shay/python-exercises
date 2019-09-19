#!/usr/bin/env python
# coding: utf-8

# In[86]:


import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec # for create grids for subplot
get_ipython().run_line_magic('matplotlib', 'inline')
import math
import random
import numpy


# In[34]:


x = range(-20,20)

y = [(i**2 - i + 2) for i in x]
plt.annotate('0 , 0', xy=(0, 0), xytext=(0, 80),arrowprops={'facecolor': 'blue'})
plt.plot(x,y)
plt.show()


# In[52]:


x = range(500)
y = [math.sqrt(i) for i in x]
plt.plot(x,y)
plt.show()


# In[53]:


x = range(-100,100)
y = [i**3 for i in x]
plt.plot(x,y)


# In[51]:


x = range(-500,500)
y =[math.tan(i) for i in x]
plt.plot(x,y)


# In[65]:


x = range(-100,300)
y = [2*i for i in x]
plt.plot(x,y)


# In[82]:


x = range(500)
y = [math.sqrt(i) for i in x]
plt.subplot(331)
plt.plot(x,y,c = 'blue')
plt.title('$y = √x$')

x = range(-100,100)
y = [i**3 for i in x]
plt.subplot(333)
plt.plot(x,y, c = 'red')
plt.title('$y = x^3$')


x = range(-500,500)
y =[math.tan(i) for i in x]
plt.subplot(337)
plt.plot(x,y, c = "green")
plt.title("$y = tan (x)$")

x = range(-100,303)
y = [2*i for i in x]
plt.subplot(339)
plt.plot(x,y, c = "orange")
plt.title("$y = 2^x$")

plt.suptitle('Math Demo')

plt.show()


# In[102]:


x = range(500)
y = [math.sqrt(i) for i in x]

a = range(-100,100)
b = [i**3 for i in a]

c = range(-500,500)
d =[math.tan(i) for i in c]

e = range(-100,303)
f = [2*i for i in e]


fig = plt.figure(1)
gridspec.GridSpec(2,3) 

# large subplot
plt.subplot2grid((2,3), (0,0), colspan=3, rowspan=1)
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=5)
plt.title("$y = tan (x)$", fontweight="bold", size=20)
plt.plot(c,d, color='orange',linewidth=7)

# small subplot 1
plt.subplot2grid((2,3), (1,0))
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=5)
plt.title('$y = √x$',fontweight="bold", size=20)
# plt.xlabel('Data values')
# plt.ylabel('Frequency')
plt.plot(x,y,color='b',linewidth=6)

# small subplot 2
plt.subplot2grid((2,3), (1,1))
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=5)
plt.title('$y = x^3$',fontweight="bold", size=20)
# plt.xlabel('Data values')
# plt.ylabel('Frequency')
plt.plot(a,b, color='r',linewidth=6)

# small subplot 3
plt.subplot2grid((2,3), (1,2))
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=5)
plt.title("$y = 2^x$", fontweight="bold", size=20)
# plt.xlabel('Data values')
# plt.ylabel('Frequency')
plt.plot(e,f, color='g',linewidth=6)

# fit subplots and save fig
#fig.tight_layout()
plt.suptitle('Math Demo', fontweight="bold", size=25)

fig.set_size_inches(w=22,h=14)
fig_name = 'math.png'
fig.savefig(fig_name)




# ax.set_title('v = 1',fontweight="bold", size=20) # Title
# ax.set_ylabel('Active Wee1', fontsize = 20.0) # Y label
# ax.set_xlabel('Active Cdc2-cyclin B', fontsize = 20) # X label


# In[ ]:





# In[83]:


# Plot figure with subplots of different sizes
fig = plt.figure(1)
# set up subplot grid
# give the figure a grid of 3 rows and 3 columns
# n_rows, n_cols, position
gridspec.GridSpec(2,3) 

# large subplot
plt.subplot2grid((2,3), (0,0), colspan=3, rowspan=1)
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=5)
plt.title("$y = tan (x)$")
#plt.xlabel('Data values')
#plt.ylabel('Frequency')
plt.hist(dist_norm, bins=30, color='orange')



# plt.subplot2grid(size/ overall grid, location)

# figure’s overall grid, which is 3 rows and 3 columns (3,3) 
# Specify the location of the large subplot: start counting from row 0 column 0 (0,0) 
# and make a subplot across 2 columns and 3 rows colspan=2, rowspan=3. 
# (Remember, Python indexes from 0, so the 3 rows or columns will be indexed as row or 
# column 0, 1, 2.)

# For this subplot:
# for the x and y axes, set the number of bins to maximum of 5
# give the plot a title
# give the x and y axes titles
# plot a histogram of the data with 30 bins and set the colour

# small subplot 1
plt.subplot2grid((2,3), (1,0))
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=5)
plt.title('$y = √x$')
# plt.xlabel('Data values')
# plt.ylabel('Frequency')
plt.hist(dist_tdis, bins=30, color='b')

# small subplot 2
plt.subplot2grid((2,3), (1,1))
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=5)
plt.title('$y = x^3$')
# plt.xlabel('Data values')
# plt.ylabel('Frequency')
plt.hist(dist_fdis, bins=30, color='r')

# small subplot 3
plt.subplot2grid((2,3), (1,2))
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=5)
plt.title("$y = 2^x$")
# plt.xlabel('Data values')
# plt.ylabel('Frequency')
plt.hist(dist_chsq, bins=30, color='g')

# fit subplots and save fig
fig.tight_layout()
fig.set_size_inches(w=11,h=7)
fig_name = 'math.png'
fig.savefig(fig_name)


# In[ ]:





# In[ ]:




