#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pyautogui')


# In[25]:


import pyautogui as py
py.PAUSE = 1.5
py.hotkey("ctrl", "t")
py.write("https://highcompanybr.com/")
py.press("enter")
py.scroll(-350)
py.click(x=1276, y=693)
py.click(x=1025, y=526)
py.press("m")
py.press("enter")
py.click(x=1027, y=783)


# In[23]:


import time
time.sleep(3)
print(py.position())


# In[ ]:




