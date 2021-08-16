#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
from PIL import  Image
def app():
    st.markdown("<h1 style='text-align: center; color: black;'>Dashboard Overview</h1>", unsafe_allow_html=True)
    
    html_temp="""
    <h4 style='text-align: center; color: black;'>For more understanding, please visit our 
    <a href="https://public.tableau.com/app/profile/jitendra.sharma1080/viz/Dashboard_Cost_Implement/HospitalTreatmentCostAnalysis?publish=yes" style="color: blue; font-weight: bold;">Tableau</a> dashboard file
    </h4>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    display = Image.open('Dashboard_Cost Analysis.png')
    display = np.array(display)
    #st.title("Rental Share",)
    #st.markdown("<style> body {background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");background-size: cover;}</style>", unsafe_allow_html=True)
    st.image(display, width = 720)


# In[ ]:




