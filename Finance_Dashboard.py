import streamlit as st
import pandas as pd
import random 
import time

st.title("Real_Time Data Dashboard")

#create empty placeholders
placeholder=st.empty()
#generate fake real data
data=[]
for i in range(20):
    new_value=random.randint(10, 100)
    data.append(new_value)
    df= pd.DataFrame(data, columns=['value'])
    with placeholder.container():
        st.subheader('Live data field')
        st.line_chart(df)
        time.sleep(2)