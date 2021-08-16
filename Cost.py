#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pickle
#with open('Random_regression.pkl', 'rb') as file:
#    Pickled_LR_Model = pickle.load(file)
#Pickled_LR_Model


# In[2]:


import numpy as np
import pickle
import pandas as pd
import streamlit as st


pickle_in = open("regr_pickle","rb")
resgressor = pickle.load(pickle_in)


def predict_cost(BODY_WEIGHT, TOTAL_LENGTH_OF_STAY, LENGTH_OF_STAY_ICU,
       COST_OF_IMPLANT):
    
    x = pd.DataFrame([[BODY_WEIGHT,TOTAL_LENGTH_OF_STAY,LENGTH_OF_STAY_ICU,COST_OF_IMPLANT]],columns=['BODY_WEIGHT','TOTAL_LENGTH_OF_STAY','LENGTH_OF_STAY_ICU','COST_OF_IMPLANT'])
    prediction = resgressor.predict(x)
    prediction1 = prediction.astype(int)
    #prediction = prediction.astype(float)
    #prediction_n = np.round(np.exp(prediction)-1)
    print(prediction1)
    return(prediction1)


def main():
    st.title("Hospital Treatment Cost  Prediction")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Hostal Treatment Cost PREDICTION APP </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    col1,col2 = st.beta_columns(2)
    with col1:
        BODY_WEIGHT = st.text_input("BODY_WEIGHT","Type Here")
        TOTAL_LENGTH_OF_STAY = st.text_input("TOTAL_LENGTH_OF_STAY","Type Here")
        LENGTH_OF_STAY_ICU = st.text_input("LENGTH_OF_STAY_ICU","Type Here")
        COST_OF_IMPLANT = st.text_input("COST_OF_IMPLANT","Type Here")
    
    result=""
    if st.button("Predict"):
        result = predict_cost(BODY_WEIGHT, TOTAL_LENGTH_OF_STAY, LENGTH_OF_STAY_ICU,
       COST_OF_IMPLANT)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets get value")
        st.text("Streamlit used")


# In[7]:


if __name__ =='__main__':
    main()


# In[ ]:





# In[ ]:




