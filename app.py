import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model_obesity.pkl", "rb"))

st.set_page_config(
    page_title="Obesity Classification",
    page_icon="🏃",
    layout="centered"
)

st.title("🏃 Klasifikasi Tingkat Obesitas")
st.write("Prediksi tingkat obesitas berdasarkan gaya hidup menggunakan Machine Learning")

# Input User

Gender = st.selectbox("Gender", ["Female", "Male"])
Age = st.number_input("Age", 1, 100, 21)
Height = st.number_input("Height (meter)", 0.5, 2.5, 1.70)
Weight = st.number_input("Weight (kg)", 10.0, 300.0, 70.0)

family_history_with_overweight = st.selectbox(
    "Family History with Overweight",
    ["No", "Yes"]
)

FAVC = st.selectbox(
    "Frequent High Calorie Food Consumption",
    ["No", "Yes"]
)

FCVC = st.slider(
    "Vegetable Consumption",
    1.0,
    3.0,
    2.0
)

NCP = st.slider(
    "Main Meals Per Day",
    1.0,
    4.0,
    3.0
)

CAEC = st.selectbox(
    "Eating Between Meals",
    ["no", "Sometimes", "Frequently", "Always"]
)

SMOKE = st.selectbox(
    "Smoke",
    ["No", "Yes"]
)

CH2O = st.slider(
    "Daily Water Consumption",
    1.0,
    3.0,
    2.0
)

SCC = st.selectbox(
    "Monitor Calories",
    ["No", "Yes"]
)

FAF = st.slider(
    "Physical Activity",
    0.0,
    3.0,
    1.0
)

TUE = st.slider(
    "Technology Usage",
    0.0,
    2.0,
    1.0
)

CALC = st.selectbox(
    "Alcohol Consumption",
    ["No", "Sometimes", "Frequently", "Always"]
)

MTRANS = st.selectbox(
    "Transportation",
    [
        "Automobile",
        "Bike",
        "Motorbike",
        "Public_Transportation",
        "Walking"
    ]
)

# Encoding sederhana

Gender = 1 if Gender == "Male" else 0
family_history_with_overweight = 1 if family_history_with_overweight == "Yes" else 0
FAVC = 1 if FAVC == "Yes" else 0
SMOKE = 1 if SMOKE == "Yes" else 0
SCC = 1 if SCC == "Yes" else 0

CAEC_dict = {
    "no":0,
    "Sometimes":1,
    "Frequently":2,
    "Always":3
}

CALC_dict = {
    "No":0,
    "Sometimes":1,
    "Frequently":2,
    "Always":3
}

MTRANS_dict = {
    "Automobile":0,
    "Bike":1,
    "Motorbike":2,
    "Public_Transportation":3,
    "Walking":4
}

CAEC = CAEC_dict[CAEC]
CALC = CALC_dict[CALC]
MTRANS = MTRANS_dict[MTRANS]

if st.button("Prediksi"):

    data = [[
        Gender,
        Age,
        Height,
        Weight,
        family_history_with_overweight,
        FAVC,
        FCVC,
        NCP,
        CAEC,
        SMOKE,
        CH2O,
        SCC,
        FAF,
        TUE,
        CALC,
        MTRANS
    ]]

    prediction = model.predict(data)

    kelas = {
        0: "Insufficient Weight",
        1: "Normal Weight",
        2: "Overweight Level I",
        3: "Overweight Level II",
        4: "Obesity Type I",
        5: "Obesity Type II",
        6: "Obesity Type III"
    }

    st.success(
        f"Hasil Prediksi : {kelas[int(prediction[0])]}"
    )