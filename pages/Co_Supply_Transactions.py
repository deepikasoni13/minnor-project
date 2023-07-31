import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# change plotly theme

st.set_page_config(layout='wide')
# function to load the data only once
@st.cache_data()
def load_supply_chain_data():
   df=pd.read_csv(r'datasets\DataCoSupplyChainDataset.csv',encoding='UTF-8', encoding_errors='ignore' )
   return df

with st.spinner("loading datasets"):
   df=load_supply_chain_data()
st.sidebar.header("navigation")
if st.sidebar.checkbox("show supply_chain_datasets"):
   st.subheader('📅 raw dataset')
   st.dataframe(df)

st.header('Product Type')
type_count = df['Type'].value_counts()
fig1 = px.pie(type_count,type_count.index, type_count.values)
st.plotly_chart(fig1, use_container_width=True)

st.header('Delievery Status')
delivery_status_count = df['Delivery Status'].value_counts()
fig2 = px.pie(delivery_status_count,delivery_status_count.index, delivery_status_count.values)
st.plotly_chart(fig2, use_container_width=True)

st.header('Days for shipment (scheduled)')
days_for_shipment_count= df['Days for shipment (scheduled)'].value_counts()
fig3 = px.pie(days_for_shipment_count,days_for_shipment_count.index, days_for_shipment_count.values)
st.plotly_chart(fig3, use_container_width=True)


st.header('Late delivery risk')
late_delivery_risk_count = df['Late_delivery_risk'].value_counts()
fig5 = px.bar(late_delivery_risk_count,late_delivery_risk_count.index, late_delivery_risk_count.values)
st.plotly_chart(fig5, use_container_width=True)

st.header('Category Id')
category_id_count = df['Category Id'].value_counts()
fig6= px.bar(category_id_count,category_id_count.index, category_id_count.values)
st.plotly_chart(fig6, use_container_width=True)

st.header('Category name')
category_name_count= df['Category Name'].value_counts()
fig7 = px.bar(category_name_count,category_name_count.index, category_name_count.values)
st.plotly_chart(fig7, use_container_width=True)

st.header('Customer City')
customer_city_count = df['Customer City'].value_counts()
fig8 = px.pie(customer_city_count,customer_city_count.index,customer_city_count.values)
st.plotly_chart(fig8, use_container_width=True)

st.header('customer country')
customer_country_count = df['Customer Country'].value_counts()
fig9 = px.pie(customer_country_count,customer_country_count.index, customer_country_count.values)
st.plotly_chart(fig9, use_container_width=True)

st.header('customer frame')
customer_fname_count = df['Customer Fname'].value_counts()
fig10= px.pie(customer_fname_count,customer_fname_count.index, customer_fname_count.values)
st.plotly_chart(fig10, use_container_width=True)

st.header('customer lname')
customer_lname_count= df['Customer Lname'].value_counts()
fig11 = px.pie(customer_lname_count,customer_lname_count.index, customer_lname_count.values)
st.plotly_chart(fig11, use_container_width=True)

st.header('customer segment')
customer_segment_count = df['Customer Segment'].value_counts()
fig12 = px.bar(customer_segment_count,customer_segment_count.index, customer_segment_count.values)
st.plotly_chart(fig12, use_container_width=True)

st.header('customer state')
customer_state_count = df['Customer State'].value_counts()
fig13 = px.pie(customer_state_count,customer_state_count.index, customer_state_count.values)
st.plotly_chart(fig13, use_container_width=True)

st.header('customer zipcode')
customer_zipcode_count = df['Customer Zipcode'].value_counts()
fig14 = px.pie(customer_zipcode_count,customer_zipcode_count.index, customer_zipcode_count.values)
st.plotly_chart(fig14, use_container_width=True)


st.header('department id')
department_id_count = df['Department Id'].value_counts()
fig15 = px.pie(department_id_count,department_id_count.index,department_id_count.values)
st.plotly_chart(fig15, use_container_width=True)


st.header('department name')
department_name_count = df['Department Name'].value_counts()
fig16 = px.pie(department_name_count,department_name_count.index,department_name_count.values)
st.plotly_chart(fig16, use_container_width=True)


st.header('longitude')
longititude_count = df['Longitude'].value_counts()
fig17 = px.histogram(longititude_count,longititude_count.index, longititude_count.values)
st.plotly_chart(fig17, use_container_width=True)

st.header('order city')
Order_city_count = df['Order City'].value_counts()
fig18= px.pie(Order_city_count,Order_city_count.index,Order_city_count.values)
st.plotly_chart(fig18, use_container_width=True)


st.header('order item product price')
order_item_product_price_count = df['Order Item Product Price'].value_counts()
fig19= px.histogram(order_item_product_price_count,order_item_product_price_count.index,order_item_product_price_count.values)
st.plotly_chart(fig19, use_container_width=True)

st.header('sales')
sales_count = df['Sales'].value_counts()
fig20= px.histogram(sales_count,sales_count.index,sales_count.values)
st.plotly_chart(fig20, use_container_width=True)


st.header('Customer Email')
customer_email_count = df['Customer Email'].value_counts()
fig21= px.pie(customer_email_count,customer_email_count.index,customer_email_count.values)
st.plotly_chart(fig21, use_container_width=True)