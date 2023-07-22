import streamlit as st

def main():
    
    st.set_page_config(layout="wide")
    # Custom CSS to hide the sidebar by default
    hide_sidebar_style = """
        <style>
        MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """
    st.markdown(hide_sidebar_style, unsafe_allow_html=True)
    # Default parameters for subjects_1
    default_subjects_1_credits = [15, 15, 15, 15, 15]
    default_subjects_1_weights1 = [0.15, 0.2, 0.3, 0.1, 0.15]
    default_subjects_1_weights2 = [0.85, 0.8, 0.7, 0.9, 0.85]

    # Default parameters for subjects_2
    default_subjects_2_credits = [15, 15, 15, 15, 45]
    default_subjects_2_weights = [0.8, 0.8, 0.8, 0.8, 0.8]
    
    
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    parameter_to_modify = st.sidebar.selectbox("Select Parameter to Modify",
                                               ["Select One", "Group 1 Credits", "Group 1 Weights 1", "Group 1 Weights 2",
                                                "Group 2 Credits", "Group 2 Weights"])

    if parameter_to_modify == "Group 1 Credits":
        subjects_1_credits = [st.sidebar.number_input(f"Credits for {subject}:", value=default_subjects_1_credits[i])
                              for i, subject in enumerate(
                ["Data and Society", "Data Analysis", "Business Intelligence", "Database Design", "DPrep"])]
    else:
        subjects_1_credits = default_subjects_1_credits.copy()

    if parameter_to_modify == "Group 1 Weights 1":
        subjects_1_weights1 = [st.sidebar.number_input(f"Weight for {subject} {mark_type}:",
                                                       value=default_subjects_1_weights1[i])
                               for i, (subject, mark_type) in enumerate(
                zip(["Data and Society", "Data Analysis", "Business Intelligence", "Database Design", "DPrep"],
                    ["Engagement", "Presentation", "Infographic", "Quizzes", "Reading Record"]))]
    else:
        subjects_1_weights1 = default_subjects_1_weights1.copy()

    if parameter_to_modify == "Group 1 Weights 2":
        subjects_1_weights2 = [st.sidebar.number_input(f"Weight for {subject} {mark_type}:",
                                                       value=default_subjects_1_weights2[i])
                               for i, (subject, mark_type) in enumerate(
                zip(["Data and Society", "Data Analysis", "Business Intelligence", "Database Design", "DPrep"],
                    ["Essay", "Individual Report", "Company Report", "Exam", "Proposal"]))]
    else:
        subjects_1_weights2 = default_subjects_1_weights2.copy()

    if parameter_to_modify == "Group 2 Credits":
        subjects_2_credits = [st.sidebar.number_input(f"Credits for {subject}:", value=default_subjects_2_credits[i])
                              for i, subject in enumerate(
                ["Introduction to Data Science", "Data Visualization", "Data Mining", "Big Data Analytics", "Dissertation"])]
    else:
        subjects_2_credits = default_subjects_2_credits.copy()

    if parameter_to_modify == "Group 2 Weights":
        subjects_2_weights = [st.sidebar.number_input(f"Weight for {subject}:", value=default_subjects_2_weights[i])
                              for i, subject in enumerate(
                ["Introduction to Data Science", "Data Visualization", "Data Mining", "Big Data Analytics", "Dissertation"])]
    else:
        subjects_2_weights = default_subjects_2_weights.copy()
        
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)    
    caption = "Group 1 consists of the modules that has multiple assessments, whereas Group 2 encompasses the modules that have only one assessment."
    st.sidebar.write(f"<p style='font-size: 10px;'>{caption}</p>", unsafe_allow_html=True)
    total_marks = 0
    st.markdown("<h3 style='text-align: center;'>Weighted Marks Estimator</h3>", unsafe_allow_html=True)
    # Separator
    st.markdown("<hr>", unsafe_allow_html=True)
    # Display the Overall marks dynamically
    overall_text = st.markdown("<h5 style='text-align: center;'>Your score:</h5><h3 style='text-align: center;'> {:.1f}</h3>".format(total_marks), unsafe_allow_html=True)
    # Separator
    st.markdown("<hr>", unsafe_allow_html=True)

    #st.markdown("<h5 style='text-align: center;'>Enter the marks for each module and assessment</h5>", unsafe_allow_html=True)

    subjects_1 = ["Data and Society", "Data Analysis", "Business Intelligence", "Database Design", "DPrep"]
    subjects_1_marks = [0, 0, 0, 0, 0]
    subjects_1_weighted_marks = [0, 0, 0, 0, 0]
    subjects_1_marks1_name = ["Engagement", "Presentation", "Infographic", "Quizzes", "Reading Record"]
    subjects_1_marks1 = []
    subjects_1_marks2_name = ["Essay", "Individual Report", "Company Report", "Exam", "Proposal"]
    subjects_1_marks2 = []

    subjects_2 = ["Introduction to Data Science", "Data Visualization", "Data Mining", "Big Data Analytics", "Dissertation"]
    subjects_2_weighted_marks = [0, 0, 0, 0, 0]
    subjects_2_marks = []

    # Get user input for subjects_1_marks1 and subjects_1_marks2
    col1, col2 = st.columns(2)
    for i in range(len(subjects_1)):
        with col1:
            subject_1_mark1 = st.text_input(f"{subjects_1[i]} {subjects_1_marks1_name[i]}:", value='0')
            subjects_1_marks1.append(int(subject_1_mark1))
        with col2:
            subject_1_mark2 = st.text_input(f"{subjects_1[i]} {subjects_1_marks2_name[i]}:", value='0')
            subjects_1_marks2.append(int(subject_1_mark2))

    col1, col2 = st.columns(2)
    # Get user input for subjects_2_marks
    for i in range(len(subjects_2)):
        with col1:
            if (i % 2 == 1 and subjects_2[i] != "Dissertation"):
                subject_2_mark = st.text_input(f"{subjects_2[i]}:", value='0')
                subjects_2_marks.append(int(subject_2_mark))
        with col2:
            if (i % 2 == 0 and subjects_2[i] != "Dissertation"):
                subject_2_mark = st.text_input(f"{subjects_2[i]}:", value='0')
                subjects_2_marks.append(int(subject_2_mark))

    subject_2_mark = st.text_input(f"{subjects_2[4]}:", value='0')
    subjects_2_marks.append(int(subject_2_mark))

    for i in range(len(subjects_1)):
        subjects_1_marks[i] = subjects_1_marks1[i] * subjects_1_weights1[i] + subjects_1_marks2[i] * subjects_1_weights2[i]
        subjects_1_weighted_marks[i] = (subjects_1_marks[i] * subjects_1_credits[i]) / 180

    for i in range(len(subjects_2)):
        subjects_2_weighted_marks[i] = (subjects_2_marks[i] * subjects_2_credits[i]) / 180
        total_marks += subjects_1_weighted_marks[i] + subjects_2_weighted_marks[i]

    # Update the Overall marks based on the calculated total_marks
    overall_text.markdown("<h5 style='text-align: center;'>Your score:</h5><h3 style='text-align: center;'> {:.1f}</h3>".format(total_marks), unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
