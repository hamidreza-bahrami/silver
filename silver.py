import streamlit as st
import pandas as pd
import numpy as np
import pickle 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import time
st.set_page_config(page_title='قیمت نقره - RoboAi', layout='centered', page_icon='🤖')

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
    with st.sidebar:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(' ')
        with col2:
            st.image('img.png')
        with col3:
            st.write(' ')
        st.divider()
        st.write("<h4 style='text-align: right; color: gray;'>تخمین قیمت نقره با دقت 98 درصد</h>", unsafe_allow_html=True)
        st.write("<h4 style='text-align: right; color: gray;'>ساخته شده با جمع آوری داده 15 سال بازار سهام</h>", unsafe_allow_html=True)
        st.divider()
        st.write('Developed & Designed by')
        st.write('Hamidreza Bahrami')
    
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
        text1 = 'بر اساس داده های وارد شده، قیمت نقره به دلار برابر خواهد بود با'
        text2 = 'Based on my analysis, Silver Price is going to be:'
        def stream_data1():
            for word in text1.split(" "):
                yield word + " "
                time.sleep(0.09)
        st.write_stream(stream_data1)
        def stream_data2():
                for word in text2.split(" "):
                    yield word + " "
                    time.sleep(0.09)
        st.write_stream(stream_data2)
        st.subheader(prediction[0])
show_page()
