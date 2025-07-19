import streamlit as st
from auth_db import csr,conn
def logout_this():
    st.session_state.authenticate= False
    st.session_state.username=""
    st.rerun()

if "authenticate" not in st.session_state:
    st.session_state.authenticate=False
if "username" not in st.session_state:
    st.session_state.username=""

if st.session_state.authenticate:
    st.write(f"already login as : {st.session_state.username}")
    st.write("Click on logout to end the session....!")
    if st.button("Logout"):
        logout_this()    # it breaks the session
else:
    st.title("my Login page")
    user_name=st.text_input("enter your username: ")
    password=st.text_input("enter your password: ",type="password")
    btn=st.button("Login")

    if btn:
        if user_name=="" or password=="" :
            st.error("please fill all fields")
            st.snow()
        else:
            csr.execute(f"select * from signup where user_name = '{user_name}';")
            check_username=csr.fetchone()
            if check_username is None:
                st.warning("username not found")
            else:
                if password != check_username[5]:
                    st.warning("Please enter valid password")
                else:
                    st.session_state.authenticate= True
                    st.session_state.username=check_username[1]
                    st.session_state.full_name=check_username[2]
                    st.write(check_username)
                    st.write(f"you succesfully login as {check_username[1]}")
                    st.success("Login succesfully")
                    st.balloons()