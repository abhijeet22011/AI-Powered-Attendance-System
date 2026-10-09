import streamlit as st

from src.dashboard.home_dashboard import home_dashboard
from src.dashboard.teacher_dashboard import teacher_dashboard
from src.dashboard.student_dashboard import student_dashboard

def main():
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_dashboard()

        case 'student':
            student_dashboard()

        case None:
            home_dashboard()   

main()