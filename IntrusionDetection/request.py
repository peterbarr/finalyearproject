#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

url = 'http://localhost:5000/results'

r = requests.post(url,json={"src_bytes":491,
                            "dst_bytes":0,
             			    "same_srv_rate":1.0,
             			    "diff_srv_rate":0.0,
             			    "dst_host_same_srv_rate":0.17,
             			    "flag":1
                            })

print(r.json())
