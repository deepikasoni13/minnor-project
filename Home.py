import streamlit as st
import pandas as pd

st.title("Supply Chain Analysis and Visualisation")
st.image("https://bcr.com.au/wp-content/uploads/2019/11/IT-Supply-Chain.jpg")

@st.cache_data()
def load_supply_chain_data():
   df=pd.read_csv(r'datasets\DataCoSupplyChainDataset.csv',encoding='UTF-8', encoding_errors='ignore' )
   return df

with st.spinner("loading datasets"):
   df=load_supply_chain_data()
# st.sidebar.header("navigation")

if st.checkbox("show supply_chain_datasets"):
   st.subheader('📅 Dataset 1')
   st.dataframe(df)

@st.cache_data()
def load_supply_chain_data2():
   df=pd.read_csv('datasets/supply_chain_data.csv')
   return df

with st.spinner("loading datasets"):
   df=load_supply_chain_data2()
# st.sidebar.header("navigation")

if st.checkbox("show supply_chain_datasets",key="dataset2"):
   st.subheader('📅 Dataset 2')
   st.dataframe(df)