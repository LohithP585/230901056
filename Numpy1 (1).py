#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([1,2,3])
print("One dimensional:",a)


# In[2]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print("Two dimonesional:",a)


# In[3]:


import numpy as np
a=np.array([[1,2,3],[3,4,5],[5,6,7]])
print("Three dimensional:",a)


# In[4]:


import numpy as np
a=np.zeros((3,4))
print("\narray with all zeros:",a)


# In[5]:


import numpy as np
a=np.random.random((4,5))
print("\nRandom value\n",a)


# In[6]:


import numpy as np 
a=np.arange(0,50,2)
print("\nThe sequence array:",a)


# In[11]:


import numpy as np 
a=np.array([[1,2,3,4,5],[11,22,33,44,55],[12,23,34,45,56]])
b=a.reshape(5,3)
print("\nThe original array:",a)
print("\nthe reshaped array:",b)


# In[13]:


import numpy as np
a=np.array([[1,2,3],[3,4,5],[5,6,7]])
flat=a.flatten()
print("\nThe original array:\n",a)
print("\nThe flattened array:\n",flat)


# In[22]:


import numpy as np
a=np.array([1,2,3,4])
print("\nthe dimension of the array:\n",a.ndim)


# In[23]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print("\nThe shape of array:\n",a.shape)


# In[24]:


import numpy as np
a=np.array([1,2,3])
print("\nThe datatype:",a.dtype)


# In[25]:


import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
size=len(a)
print("\nThe size of array:\n",size)


# In[ ]:




