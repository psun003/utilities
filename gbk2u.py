#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv
import os


# In[12]:


directory = os.path.join("C:\\Users\\pu.sun\\OneDrive - Keppel Group\\Work\\KIH_Audit\\Emma")


# In[15]:


for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
            f=open(file,'rt', encoding="utf8")
            file_as_list=f.read().splitlines()
            new_file = file.rstrip('.csv')+'_converted.csv'
            with open(new_file, 'w+',encoding="utf-8-sig") as output_file:
                for row in file_as_list:
                    row1=row.replace(u'\ufeff','').encode('latin1').decode('gb2312')
                    output_file.write(row1+'\n')
                output_file.close()
            f.close()


# In[ ]:




