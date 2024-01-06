import streamlit as st
import pandas as pd
import numpy as np
import pickle 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import time

def load_model():
    with open('saved.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data['model']
x = data['x']

def show_page():
    st.write("<h1 style='text-align: center; color: blue;'>مدل پیش بینی قیمت نقره</h1>", unsafe_allow_html=True)
    st.write("<h2 style='text-align: center; color: gray;'>ETF پیش بینی بر اساس شاخص های صندوق</h2>", unsafe_allow_html=True)
    st.write("<h3 style='text-align: center; color: gray;'>شاخص های زیر را وارد کنید</h3>", unsafe_allow_html=True)
    st.write("<h4 style='text-align: center; color: gray;'>Robo-Ai.ir طراحی شده توسط</h4>", unsafe_allow_html=True)
    st.link_button("Robo-Ai بازگشت به", "https://robo-ai.ir")
    
    SPX = st.slider('شاخص سهام 500 شرکت بزرگ ایالات متحده (S & P 500)', 676.0, 2872.0, 700.0)

    USO = st.slider('شاخص نفت خام ایالات متحده', 7.96, 117.4, 10.0)

    GLD	 = st.slider('شاخص طلا', 70.0, 184.5, 80.0)

    EUR_USD = st.slider('نسبت یورو به دلار', 1.039, 1.59, 1.050)

    button = st.button('محاسبه و پیش بینی')
    if button:
        with st.chat_message("assistant"):
                    with st.spinner('''درحال بررسی، لطفا صبور باشید'''):
                        time.sleep(3)
                        st.success(u'\u2713''بررسی انجام شد')
                        x = np.array([[SPX, USO, GLD, EUR_USD]])

        prediction = model.predict(x)
        st.write("<h4 style='text-align: right; color: gray;'>:بر اساس داده های وارد شده، قیمت نقره به دلار برابر خواهد بود با</h4>", unsafe_allow_html=True)
        st.subheader(prediction[0])
show_page()