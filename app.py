# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:55:18 2023

@author: HERLAB26
"""

# Predictor app
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# load the saved model
GWR_model = pickle.load(open('C:/Users/HERLAB26/Documents/Desktop/DKUT/Project/GWR-model/Potential_GWR_model.sav', 'rb'))

#sidebar for navigation
with st.sidebar:
    selected = option_menu('Groundwater Recharge Prediction\n Taita Taveta County',
                           ["Run The Model"],
                           icons = ['droplet','droplet-half','droplet-fill'],
                           default_index=0)
if (selected == 'Run The Model'):
    # page title
    st.title('Taita Taveta Groundwater Recharge Predictor')
    print('Must contain decimal(.)')
    
    Depth = st.text_input('Depth')
    WS = st.text_input('WRL/SWL')
    Drawd = st.text_input('Drawdown(m)')
    Yield = st.text_input('Yield (M3)')
    Transm = st.text_input('Transmissivity')
    Precip = st.text_input('Precipitation (MM/YR)')
    
    # prediction
    gw_prediction = ''
    
    # creating the prediction button
    if st.button('START'):
        prediction_gwr = GWR_model.predict([[Depth, WS, Drawd, Yield, Transm, Precip]])
        
        if (prediction_gwr[0] == 0):
            gw_prediction = 'Poor Groundwater Recharge Area'
            
        else:
            gw_prediction = 'Potential Groundwater Recharge Area'
    
    st.success(gw_prediction)
        
        