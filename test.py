import streamlit as st
import pandas as pd
import pickle
import time
from PIL import Image

st.set_page_config(page_title="Halaman Modelling", layout="wide")


add_selectitem = st.sidebar.selectbox("Pilih modeling yang akan digunakan", ("Home", "About Data", "EDA", "Predict your data", "Author"))

def home():
    st.write("""
            # Welcome to my machine learning dashboard

            This dashboard created by : [@SalsabilaSekarNadia](https://www.linkedin.com/in/salsabila-sekar-nadia-33859a1b0/)
            """)



def heart():
    st.write("""
        This app predicts for Heart Disease
        Data obtained from [Data heart disease](https://archive.ics.uci.edu/dataset/45/heart+disease) by UCI Machine Learning
    """)
    st.sidebar.header("Input Data")
    uploaded_file = st.sidebar.file_uploader("Upload your data here!",type=["csv"] )
    if uploaded_file is not None:
        input_df =pd.read_csv( uploaded_file)
    else:
        def inputan_manual():
            st.header("Manual input")
            # "cp","thalach","slope","exang", "oldpeak", "ca",  "thal","sex", "age"
            # 1.) definisiin cp
            cp = st.slider("Chest Pain Type", 1, 4, 2) # maksd angkanya = mulai dari1, berakhir di 4, defaultnya 2
            if cp == 1:
                text_cp = "Nyeri Dada Tipe Angina"
            elif cp == 2:
                text_cp = "Nyeri Dada Tidak Stabil"
            elif cp == 3:
                text_cp = "Nyeri Dada Tidak Stabil Parah"
            else:
                text_cp = "Tiada kaitan masalah jantung"
            st.write("Jenis Chest Pain : ", text_cp)
            thalach = st.slider("Maximum heart rate achieved", 71,202,80)
            slope = st.slider("Segmen ST pada elektrokardiogram", 0, 2, 1)
            exang = st.slider("Exercise induced angina", 0, 1, 1)
            oldpeak = st.slider("Segmen ST pada depresi/menurun", 0.0, 6.2, 2.1)
            ca = st.slider("Jumlah pembuluh darah utama", 0, 3, 1)
            thal = st.slider("Thalium",  0, 3, 1)
            sex = st.selectbox ("Gender", ("Perempuan", "laki laki"))
            if sex == "Perempuan":
                sex = 0
            else :
                sex =1
            age= st.slider("Usia", 29, 80, 30)
            # 4.) exang
            # 5.) oldpeak
            # 6.) ca
            # 7.) Thal
            # 8.) sex
            data = {
                'cp' : cp,
                'thalach' : thalach,
                'slope' : slope,
                'exang' :exang,
                'oldpeak' : oldpeak,
                'ca' : ca,
                'thal' : thal,
                'sex' : sex,
                'age': age
            }

            features = pd.DataFrame(data, index=[0])
            return features

    input_df = inputan_manual()
    img = Image.open("heart-Disease.jpg")
    st.image(img, width = 500)
    if st.button("Predict"):
        df = input_df
        st.write(df)
        with open("model_terpilih.pkl", "rb") as file:
            model = pickle.load(file)
        pred = model.predict(df)
        result = ['No heart disease' if pred == 0 else "Got heart disease"]
        st.subheader("Prediction!")
        output = str(result[0])
        with st.spinner("wait a minute..."):
            time.sleep(3)
            st.success(f"Prediction: {output}")




if add_selectitem == "Predict your data" :
    heart()
elif add_selectitem == "Home" :
    home()
elif add_selectitem == "Home" :
    st.write_stream("Belum")
elif add_selectitem == "Home" :
    st.write_stream("belum") 

