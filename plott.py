import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df2=pd.read_csv('clean_data.csv')

def bar(df2):
    bus_Avr=df2[df2['type']=='bus']['RSSI'].mean()
    car_avr=df2[df2['type']=='car']['RSSI'].mean()
    static_Avr=df2[df2['type']=='static']['RSSI'].mean()
    pedestrian_Avr=df2[df2['type']=='pedestrian']['RSSI'].mean()
    train_Avr=df2[df2['type']=='train']['RSSI'].mean()
    df_type={'bus':bus_Avr,'car':car_avr,'static':static_Avr,'pedestrian':pedestrian_Avr,'train':train_Avr}
    type=list(df_type.keys())
    avr=list(df_type.values())
    fig = plt.figure(figsize = (10, 5))

    # creating the bar plot
    plt.bar(type, avr, color ='blue',
            width = 0.4)

    plt.xlabel("Mean of transport")
    plt.ylabel("RSSI")
    plt.title("RSSI vs Mean of transport")
    
    return fig

def scatter(df0):
    fig = plt.figure(figsize = (10, 5))
    plt.scatter(df0['RSRP'],df0['RSSI'],color='red')
    plt.xlim(-120,-55)
    plt.xlabel("RSRP")
    plt.ylabel("RSSI")
    plt.title("RSSI vs RSRP")
    return fig

def line(df0):
    
    dis=df0.ServingCell_Distance.unique()
    avr=[]
    for d in dis:
        avr.append(df0[df0['ServingCell_Distance']==d]['RSSI'].mean())
    gf=pd.DataFrame(dis,columns=['dis'])
    gf['avr']=avr
    gf.set_index('dis',inplace=True)
    gf.sort_index(inplace=True)
    fig = plt.figure(figsize = (10, 5))
    plt.plot(gf.index,gf['avr'],color='green')
    plt.xlim(0,5000)
    plt.xlabel("Distance from serving cell")
    plt.ylabel("RSSI")
    plt.title("RSSI vs Distance from serving cell")
    return fig

def speed(df2):
    sf=df2[['Speed','RSSI']]
    sf.set_index('Speed',inplace=True)
    sf.sort_index(inplace=True)
    sf.reset_index(inplace=True)

    return sf

def snr(df0):
    
    s=df0.SNR.unique()
    avr=[]
    for d in s:
        avr.append(df0[df0['SNR']==d]['RSSI'].mean())
    gf=pd.DataFrame(s,columns=['snr'])
    gf['RSSI']=avr
    gf.set_index('snr',inplace=True)
    gf.sort_index(inplace=True)
    gf.reset_index(inplace=True)
    return gf