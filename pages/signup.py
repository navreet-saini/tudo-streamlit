import streamlit as st
from auth_db import csr,conn

st.title("SignUp Here")
col1,col2=st.columns(2)
with col1:
    user_name=st.text_input("enter unique username: ")
with col2:
    full_name=st.text_input("enter your full name: ")

phone=st.number_input("enter your phone number: ",max_value=9999999999,min_value=0000000000)

email=st.text_input("enter your email address: ")

password=st.text_input("enter your password: ",type="password")

confirm_pass=st.text_input("Confirm password: ",type="password")

address=st.text_area("enter your address: ")

btn=st.button('Sign Up')


if btn:
    if user_name=="" or full_name=="" or phone=="" or email=="" or password==" " or confirm_pass=="":
        st.error("please fill all fields")
        st.snow()
    else:
        if password !=confirm_pass:
            st.warning("passwords do not match")
            st.snow()
        else:
            try:
                csr.execute(f"insert into signup(user_name,full_name,phone_no,email,password) values('{user_name}','{full_name}','{phone}','{email}','{password}')")
                conn.commit()

                st.success("sign up succesfully")
                st.balloons()

                st.markdown("[Go to login page](./login)")
            except Exception as e:
                st.error("Please check username must be unique")
