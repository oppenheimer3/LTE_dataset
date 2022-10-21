import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import leafmap.foliumap as leafmap
import seaborn as sns
from plott import bar,scatter,line,speed,snr
# from plot import bar

df=pd.read_csv('all_data.csv')
df1=pd.read_csv('RSSI.csv')
df0=pd.read_csv('serving_cells.csv')
df2=pd.read_csv('clean_data.csv')



st.title('LTE Dataset')

parameters=st.selectbox('RSSI VS',('RSRP','SNR','Serving cell distance','Mean of transport','Speed'))

if parameters =='Mean of transport':
    st.pyplot(bar(df2))
if parameters =='RSRP':
    st.pyplot(scatter(df2))
if parameters =='Serving cell distance':
    st.pyplot(line(df2))
if parameters =='Speed':
    sf=speed(df2)
    st.line_chart(sf,x='Speed',y='RSSI')
if parameters=='SNR':
    lf=snr(df2)
    st.line_chart(lf,x='snr',y='RSSI')



fig, ax = plt.subplots()
sns.heatmap(df2.corr(), ax=ax)
st.pyplot(fig)

st.header('Serving cells location')

st.map(df0)
st.header('RSSI heatmap')

m = leafmap.Map()
m.add_heatmap(
    df1,
    latitude="latitude",
    longitude="longitude",
    value="RSSI",
    name="Heat map",
    radius=20,
)
m.to_streamlit(height=500)
