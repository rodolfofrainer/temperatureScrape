import streamlit as st
import plotly.express as px

import sqlite3

st.title('Temperature Graph')

df = []
times = []
temperatures = []

connection = sqlite3.connect('temperatures.db')

cursor = connection.cursor()
cursor.execute('SELECT * from temperatures')
df = cursor.fetchall()


for i in list(df):
    times.append(i[-1])
    temperatures.append(i[0])

figure = px.line(x=times, y=temperatures)
st.plotly_chart(figure)
