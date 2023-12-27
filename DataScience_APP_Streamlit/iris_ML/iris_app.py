import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title='Iris Classification')
st.title('Iris flower classification model')

st.markdown(""" 
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> 
    """, unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def get_model():
    model=pickle.load(open('iris_model.pickle','rb'))
    return model

#Sepal length	Sepal width	Petal length	Petal width
spl=st.text_input("Enter Sepal Length","")
spw=st.text_input("Enter sepal widht","")
pel=st.text_input("Enter Petal Lenght","")
pew=st.text_input("Enter Petal width","")

if st.button("Check Flower Type"):
    values=[spl,spw,pel,pew]
    num_values=[]
    for x in values:
        num_values.append(float(x))
    
    #2 dimension
    num_values=np.asarray(num_values).reshape(1,-1)
    predictions=get_model().predict(num_values)
    predictions=int(predictions)
    if predictions==0:
        st.write("Flower is Iris-Sentosa") 
    elif predictions==1:
        st.write("Flower is Iris-verginia")
    else:
        st.write("Flower is Iris-versicolor")









    