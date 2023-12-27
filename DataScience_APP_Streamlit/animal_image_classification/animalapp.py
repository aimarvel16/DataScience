from sklearn.preprocessing import LabelBinarizer
from tensorflow import keras
from PIL import Image
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
#from keras.preprocessing import image
import keras.utils as image
import numpy as np

import numpy as np
import pandas as pd
import streamlit as st
import tensorflow as tf

st.set_page_config(page_title='CatDog Recognition')
st.title('Cat and Dog Classification')

@st.cache(allow_output_mutation=True)
def get_best_model():
    model = keras.models.load_model('animal_model.h5',compile=False)
    model.make_predict_function()          # Necessary
    print('Model loaded. Start serving...')
    return model

st.subheader('Classify the image')
image_file = st.file_uploader('Choose the Image', ['jpg', 'png'])
print(image_file)


if image_file is not None:
    
    image = Image.open(image_file)
    st.image(image, caption='Input Image')

    image = image.resize((150,150),Image.ANTIALIAS)
    img_array = np.array(image)
    
    x = np.expand_dims(img_array, axis=0)
    images = np.vstack([x])
    model=get_best_model()
    classes = model.predict(images, batch_size=10)
    if classes>0.5:
        prediction = 'Dog'
    else:
        prediction = 'Cat'
    st.write(f'The image is predicted as {prediction}')
