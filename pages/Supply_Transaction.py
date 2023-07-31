import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# change plotly theme

st.set_page_config(layout='wide')
# function to load the data only once
@st.cache_data()
def load_supply_chain_data():
   df=pd.read_csv('datasets/supply_chain_data.csv')
   return df

with st.spinner("loading datasets"):
   df=load_supply_chain_data()
st.sidebar.header("navigation")
if st.sidebar.checkbox("show supply_chain_datasets"):
   st.subheader('📅 raw dataset')
   st.dataframe(df)

st.subheader('analysis of data')
rows,cols = df.shape
Price = df['Price']
Customerdemographics = df['Customer demographics']

st.metric("Rows", rows)

st.subheader("Price distribution")
df.sort_values('Price', ascending=False, inplace=True)
fig1 = px.bar(df, 'SKU', 'Price')
fig1a = px.histogram(df, 'Price')
fig1b = px.box(df, 'Price')
c1, c2, c3 = st.columns(3)
c1.plotly_chart(fig1, use_container_width=True)
c2.plotly_chart(fig1a, use_container_width=True)
c3.plotly_chart(fig1b, use_container_width=True)

st.metric("Rows", rows)
st.subheader("Availability")
df.sort_values('Availability', ascending=False,inplace=True)
fig2= px.bar(df,'SKU','Availability')
fig2a= px.histogram(df,'Availability')
fig2b= px.box(df,'Availability')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig2, use_container_width=True)
c2.plotly_chart(fig2a, use_container_width=True)
c3.plotly_chart(fig2b, use_container_width=True)
 

st.metric("Rows", rows)
st.subheader("Number of products sold")
df.sort_values('Number of products sold', ascending=False,inplace=True)
fig3=px.bar(df,'SKU','Number of products sold')
fig3a= px.histogram(df,'Number of products sold')
fig3b= px.box(df,'Number of products sold')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig3, use_container_width=True)
c2.plotly_chart(fig3a, use_container_width=True)
c3.plotly_chart(fig3b, use_container_width=True)


st.metric("Rows", rows)
st.subheader("Revenue generated")
df.sort_values('Revenue generated',ascending=False,inplace=True)
fig4= px.bar(df,'SKU','Revenue generated')
fig4a= px.histogram(df,'Revenue generated')
fig4b= px.box(df,'Revenue generated')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig4, use_container_width=True)
c2.plotly_chart(fig4a, use_container_width=True)
c3.plotly_chart(fig4b, use_container_width=True)



st.metric("Rows", rows)
st.subheader("Stock levels")
df.sort_values('Stock levels', ascending=False,inplace=True)
fig5= px.bar(df,'SKU','Stock levels')
fig5a= px.histogram(df,'Stock levels')
fig5b= px.box(df,'Stock levels')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig5, use_container_width=True)
c2.plotly_chart(fig5a, use_container_width=True)
c3.plotly_chart(fig5b, use_container_width=True)



st.metric("Rows", rows)
st.subheader("Lead times")
df.sort_values('Lead times', ascending=False,inplace=True)
fig6= px.bar(df,'SKU','Lead times')
fig6a= px.histogram(df,'SKU','Lead times')
fig6b= px.box(df,'SKU','Lead times')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig6, use_container_width=True)
c2.plotly_chart(fig5a, use_container_width=True)
c3.plotly_chart(fig5b, use_container_width=True)


st.metric("Rows", rows)
st.subheader("Order quantities")
df.sort_values('Order quantities', ascending=False,inplace=True)
fig6= px.bar(df,'SKU','Order quantities')
fig6a= px.histogram(df,'Order quantities')
fig6b= px.box(df,'Order quantities')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig6, use_container_width=True)
c2.plotly_chart(fig6a, use_container_width=True)
c3.plotly_chart(fig6b, use_container_width=True)


st.metric("Rows", rows)
st.subheader("Shipping times")
df.sort_values('Shipping times', ascending=False,inplace=True)
fig7= px.bar(df,'SKU','Shipping times')
fig7a= px.histogram(df,'Shipping times')
fig7b= px.box(df,'Shipping times')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig7, use_container_width=True)
c2.plotly_chart(fig7a, use_container_width=True)
c3.plotly_chart(fig7b, use_container_width=True)


st.metric("Rows", rows)
st.subheader("Supplier name")
df.sort_values('Supplier name', ascending=False,inplace=True)
fig8= px.bar(df,'SKU','Supplier name')
fig8a= px.histogram(df,'Supplier name')
fig8b= px.box(df,'Supplier name')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig8, use_container_width=True)
c2.plotly_chart(fig8a, use_container_width=True)
c3.plotly_chart(fig8b, use_container_width=True)

st.metric("Rows", rows)
st.subheader("Shipping costs")
df.sort_values('Shipping costs', ascending=False,inplace=True)
fig9= px.bar(df,'SKU','Shipping costs')
fig9a= px.histogram(df,'Shipping costs')
fig9b= px.box(df,'Shipping costs')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig9, use_container_width=True)
c2.plotly_chart(fig9a, use_container_width=True)
c3.plotly_chart(fig9b, use_container_width=True)


st.metric("Rows", rows)
st.subheader("Production volumes")
df.sort_values('Production volumes', ascending=False,inplace=True)
fig10= px.bar(df,'SKU','Production volumes')
fig10a= px.histogram(df,'Production volumes')
fig10b= px.box(df,'Production volumes')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig10, use_container_width=True)
c2.plotly_chart(fig10a, use_container_width=True)
c3.plotly_chart(fig10b, use_container_width=True)


st.metric("Rows", rows)
st.subheader("Manufacturing lead time")
df.sort_values('Manufacturing lead time', ascending=False,inplace=True)
fig12= px.bar(df,'SKU','Manufacturing lead time')
fig12a= px.histogram(df,'Manufacturing lead time')
fig12b= px.box(df,'Manufacturing lead time')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig12, use_container_width=True)
c2.plotly_chart(fig12a, use_container_width=True)
c3.plotly_chart(fig12b, use_container_width=True)


st.metric("Rows", rows)
st.subheader("Manufacturing costs")
df.sort_values('Manufacturing costs', ascending=False,inplace=True)
fig13= px.bar(df,'SKU','Manufacturing costs')
fig13a= px.histogram(df,'Manufacturing costs')
fig13b= px.box(df,'Manufacturing costs')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig13, use_container_width=True)
c2.plotly_chart(fig13a, use_container_width=True)
c3.plotly_chart(fig13b, use_container_width=True)

st.metric("Rows", rows)
st.subheader("Defect rates")
df.sort_values('Defect rates', ascending=False,inplace=True)
fig14= px.bar(df,'SKU','Defect rates')
fig14a= px.histogram(df,'Defect rates')
fig14b= px.box(df,'Defect rates')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig14, use_container_width=True)
c2.plotly_chart(fig14a, use_container_width=True)
c3.plotly_chart(fig14b, use_container_width=True)


st.metric("Rows", rows)
st.subheader("Costs")
df.sort_values('Costs', ascending=False,inplace=True)
fig15= px.bar(df,'SKU','Costs')
fig15a= px.histogram(df,'Costs')
fig15b= px.box(df,'Costs')
c1,c2,c3=st.columns(3)
c1.plotly_chart(fig15, use_container_width=True)
c2.plotly_chart(fig15a, use_container_width=True)
c3.plotly_chart(fig15b, use_container_width=True)

rows,cols=df.shape
st.subheader('')
total_Product_type=df['Product type'].nunique()
c1,c2=st.columns(2)
c1.metric('Total products',rows)
c2.metric("Product type in all items",
          str(total_Product_type))
product_grp = df['Product type'].value_counts()

fig = px.pie(product_grp, product_grp.index, product_grp.values)
st.plotly_chart(fig, use_container_width=True)
st.warning(" 40% skincare is the highest level in all product items")

total_Shipping_carriers=df['Shipping carriers'].nunique()
c1,c2=st.columns(2)
c1.metric('Shipping carriers',rows)
c2.metric(" Shipping carriers in all items",
          str(total_Shipping_carriers))
Shipping_grp = df['Shipping carriers'].value_counts()
fig1 = px.pie(Shipping_grp, Shipping_grp.index, Shipping_grp.values)
st.plotly_chart(fig1, use_container_width=True)
st.warning(" 43% carrier B is the highest level comparing to others")


total_Location=df['Location'].nunique()
c1,c2=st.columns(2)
c1.metric('Location',rows)
c2.metric(" Location  in all items",
          str(total_Location))
Location_grp = df['Location'].value_counts()
fig2 = px.pie(Location_grp, Location_grp.index, Location_grp.values)
st.plotly_chart(fig2, use_container_width=True)
st.warning("25% kolkata is the highest level of location for the al items")


total_Inspection_results=df['Inspection results'].nunique()
c1,c2=st.columns(2)
c1.metric('Inspection results',rows)
c2.metric("Inspection results in all items",
          str(total_Inspection_results))
Inspection_grp = df['Inspection results'].value_counts()
fig3 = px.pie(Inspection_grp, Inspection_grp.index,Inspection_grp.values)
st.plotly_chart(fig3, use_container_width=True)
st.warning("41% is pending level it is highest and 23% is pass level it is lowest ")

total_Trasportation_modes=df['Transportation modes'].nunique()
c1,c2=st.columns(2)
c1.metric('Transportation modes',rows)
c2.metric("Transportation modes results in all items",
          str(total_Trasportation_modes))
Transportation_grp = df['Transportation modes'].value_counts()
fig4 = px.pie(Transportation_grp, Transportation_grp.index,Transportation_grp.values)
st.plotly_chart(fig4, use_container_width=True)
st.warning("29% road transportation is high and 17% sea level is low")


total_Routes=df['Routes'].nunique()
c1,c2=st.columns(2)
c1.metric('Routes',rows)
c2.metric("Routes in all items",
          str(total_Routes))
Routes_grp = df['Routes'].value_counts()
fig5= px.pie(Routes_grp,Routes_grp.index,Routes_grp.values)
st.plotly_chart(fig5, use_container_width=True)
st.warning("43% routeA is highest level")











