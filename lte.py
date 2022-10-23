from altair.vegalite.v4.schema import FontStyle
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import leafmap.foliumap as leafmap
import seaborn as sns
from plott import bar,scatter,line,speed,snr
import joblib

model=joblib.load('LTE.joblib')


df=pd.read_csv('all_data.csv')
df1=pd.read_csv('RSSI.csv')
df0=pd.read_csv('serving_cells.csv')
df2=pd.read_csv('clean_data.csv')



st.title('LTE Dataset')
st.header('RSSI Prediction APP')

Speed = st.text_input('Speed')
Operatorname = st.text_input('Operator name')
CellID = st.text_input('Cell ID')
RSRP = st.text_input('RSRP')
ServingCell_Distance = st.text_input('Distance from serving cell')
type = st.text_input('mean of transport')

if Operatorname=='A':
    Operatorname=0
else: Operatorname=1
if type=='bus':
    type=0
elif type=='car':
    type=1
elif type=='pedestrian':
    type=2
elif type=='train':
    type=4
else: type=3
if Speed!='' and Operatorname!='' and CellID!=''and RSRP!=''and ServingCell_Distance!='' and type!='':
    array=np.array([float(Speed),int(Operatorname),int(CellID),int(RSRP),float(ServingCell_Distance),int(type)]).reshape(1,-1)
    prediction=model.predict(array)
    st.write('Predicted RSSI is: ',prediction[0],)







st.header('Data visualization')


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
