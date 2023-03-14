import streamlit as st
import plotly.express as px

st.title('Temperature Graph')

df = []
times = []
temperatures = []

with open('temperatures.txt', 'r') as file:
    df.append(file.read())

df = df[0]

df = df.split('\n')

for i in df:
    i = i.split(',')
    times.append(i[0])
    temperatures.append(i[-1])

figure = px.line(x=times, y=temperatures)
st.plotly_chart(figure)
