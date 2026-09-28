import streamlit as st

st.title("📊 Marks amd Grade Calculator")

name = st.text_input("Enter student name: ")
num_subjects = st.number_input("Number of subjects", min_value = 1, max_value = 20, value= 5)

marks = []

for i in range(int(num_subjects)):
    mark = st.number_input(
        f'Marks for Subject {i+1}', 
        min_value = 0.0,
        max_value = 100.0,
        value = 0.0
    )
    marks.append(mark)

if st.button("Calculate Result"):
    total = sum(marks)
    percentage = total/num_subjects

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    st.subheader("Result")

    st.write(f'Student: {name}')
    st.write(f'Total Marks: {total}/{num_subjects*100}')
    st.write(f'Percentage : {percentage:.2f}%')
    st.write(f'Grade: {grade}')

    if grade == "F":
        st.error("Result: FAIL")
    else:
        st.success("Result:PASS")