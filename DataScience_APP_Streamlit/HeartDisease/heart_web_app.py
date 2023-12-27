import pickle
import streamlit as st
import numpy as np

st.set_page_config(page_title='Heart disease Classification')
st.title('Heart Disease')
st.markdown(""" 
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> 
    """, unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def get_model():
    loaded_model = pickle.load(open('model.pickle', "rb"))
    return loaded_model


#adding a single-line text input widget

age = st.text_input('Enter age: ', '')
sex = st.text_input('Enter sex(1,0): ', '')
cp = st.text_input('Enter cp 0-4: ', '')
trestbps= st.text_input('Enter trestbps 100-150: ', '')
chol = st.text_input('Enter chol 200-400: ', '')
fbs = st.text_input('Enter fbs 1-0: ', '')
restecg = st.text_input('Enter restecg 0-1: ', '')
thalach = st.text_input('Enter thalach 120-180: ', '')
exang = st.text_input('Enter exang 0-1 ', '')
oldpeak = st.text_input('Enter oldpeak 0.5-4.0: ', '')
slope = st.text_input('Enter  slope 0-2', '')
ca = st.text_input('Enter ca: 0-2', '')
thal = st.text_input('Enter thal 1-2: ', '')

if st.button('Heart or Not'):

    namelist=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    value_int=[]
    #displaying the entered text
    st.write('Your inputs are ',namelist )

    for x in namelist:
        value_int.append(float(x))

    #change to two di
    value_int=np.asarray(value_int)
    value_int=value_int.reshape(1,-1)

    value=get_model().predict(value_int)
    value=int(value)
    if value==1:
        st.write('Yes , Heart Disease' )
    else:
        st.write("No, No heart disease")

