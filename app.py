import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('model/random_forest_model.pkl')

# UI Header
st.set_page_config(page_title="Student Status Prediction", layout="centered")
st.title("🎓 Student Dropout & Success Prediction")
st.write("Aplikasi ini memprediksi status mahasiswa: **Dropout**, **Graduated**, atau **Enrolled** berdasarkan data akademik mereka.")

# Fungsi input user
def user_input_features():
    st.header("📝 Masukkan Data Mahasiswa")

    col1, col2 = st.columns(2)

    with col1:
        Application_mode = st.number_input('Application Mode (angka)', min_value=0)
        Debtor = st.selectbox('Debtor (1: Ya, 0: Tidak)', [0, 1])
        Tuition_fees_up_to_date = st.selectbox('Tuition Fees Up to Date (1: Ya, 0: Tidak)', [0, 1])
        Gender = st.selectbox('Gender (1: Laki-laki, 0: Perempuan)', [0, 1])
        Scholarship_holder = st.selectbox('Scholarship Holder (1: Ya, 0: Tidak)', [0, 1])
        Displaced = st.selectbox('Displaced (1: Ya, 0: Tidak)', [0, 1])
        Age_at_enrollment = st.number_input('Age at Enrollment', min_value=0)
        Previous_qualification_grade = st.number_input('Previous Qualification Grade', min_value=0.0)
        Admission_grade = st.number_input('Admission Grade', min_value=0.0)
        Curricular_units_1st_sem_enrolled = st.number_input('1st Sem - Enrolled Units', min_value=0)
        Curricular_units_1st_sem_approved = st.number_input('1st Sem - Approved Units', min_value=0)

    with col2:
        Curricular_units_1st_sem_grade = st.number_input('1st Sem - Grade', min_value=0.0)
        Curricular_units_2nd_sem_enrolled = st.number_input('2nd Sem - Enrolled Units', min_value=0)
        Curricular_units_2nd_sem_approved = st.number_input('2nd Sem - Approved Units', min_value=0)
        Curricular_units_2nd_sem_grade = st.number_input('2nd Sem - Grade', min_value=0.0)

    # Hitung variabel turunan secara otomatis
    Total_enrolled_units = Curricular_units_1st_sem_enrolled + Curricular_units_2nd_sem_enrolled
    Total_approved_unit = Curricular_units_1st_sem_approved + Curricular_units_2nd_sem_approved
    Approval_rate = (Total_approved_unit / Total_enrolled_units * 100) if Total_enrolled_units > 0 else 0
    Average_grade = Curricular_units_1st_sem_grade + Curricular_units_2nd_sem_grade

    features = np.array([[Curricular_units_2nd_sem_enrolled, Curricular_units_2nd_sem_approved, Curricular_units_2nd_sem_grade,
                          Curricular_units_1st_sem_enrolled, Curricular_units_1st_sem_approved, Curricular_units_1st_sem_grade,
                          Admission_grade, Previous_qualification_grade, Age_at_enrollment,
                          Tuition_fees_up_to_date, Scholarship_holder, Gender, Debtor,
                          Application_mode, Displaced, Total_enrolled_units, Total_approved_unit, Approval_rate, Average_grade]])

    return features, {
        'Application_mode': Application_mode,
        'Debtor': Debtor,
        'Tuition_fees_up_to_date': Tuition_fees_up_to_date,
        'Gender': Gender,
        'Scholarship_holder': Scholarship_holder,
        'Age_at_enrollment': Age_at_enrollment,
        'Previous_qualification_grade': Previous_qualification_grade,
        'Admission_grade': Admission_grade,
        'Displaced': Displaced,
        'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
        'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
        'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
        'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
        'Total_enrolled_units': Total_enrolled_units,
        'Total_approved_unit': Total_approved_unit,
        'Approval_rate': Approval_rate,
        'Average_grade': Average_grade
    }

# Ambil input
input_data, raw_data = user_input_features()

# Tampilkan input
with st.expander("📊 Lihat Data yang Dimasukkan"):
    st.json(raw_data)

# Prediksi
if st.button('🔮 Prediksi Status Mahasiswa'):
    prediction = model.predict(input_data)
    status_map = {0: 'Dropout', 1: 'Enrolled', 2: 'Graduated'}
    prediction_label = status_map.get(prediction[0], "Unknown")

    st.success(f"🎯 **Prediksi Status:** {prediction_label}")
