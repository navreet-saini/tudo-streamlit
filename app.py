import streamlit as st
from auth_db import csr,conn
import pandas as pd
# st.title("my web app")

# query="select * from signup;"

# df=pd.read_sql(query,conn)
# st.dataframe(df)


# my_file =st.file_uploader("upload you file to view data...",type=["csv"])
# if my_file !=None:
#     data=pd.read_csv(my_file,encoding="latin-1")
#     st.dataframe(data)


st.header(" my Todo app")

if "authenticate" not in st.session_state:
    st.session_state.authenticate=False
    
if "username" not in st.session_state:
    st.session_state.username=""

    
if st.session_state.authenticate:
    st.subheader(f" Add Todo({st.session_state.username})")
    todo_title=st.text_input("Enter Todo Title:")
    todo_detail=st.text_area("Brief about Todo:")
    btn=st.button("click me")

    if btn:
        if todo_title =="" or todo_detail=="":
            st.warning("Please fill up all fields")
        else:
            csr.execute(f"insert into mytodos(todo_added,todo_title,todo_desc) values('{st.session_state.username}','{todo_title}','{todo_detail}');")
            conn.commit()

            st.success("Todo Added succesfully...")
            st.balloons()
    st.subheader("My All Todos....")
    col1,col2,col3,col4=st.columns(4)

    with col1:
        st.write("Todo_id")
    with col2:
        st.write("Todo  Title")
    with col3:
        st.write("Description")
    with col4:
        st.write("Delete Todo")

    todo_id,title,desc,dlt=st.columns(4)
    csr.execute(f"select  * from mytodos where todo_added ='{st.session_state.username}';")
    all_todo=csr.fetchall()

    for id,added,title,dec,done in all_todo:
        todo_id,tit,desc,dlt=st.columns(4)
        with todo_id:
            checked= st.checkbox(" Done ",key={id},value=bool(done))

            if checked != bool(done):
                csr.execute(f"update mytodos set todo_done = {checked} where todo_id= {id}")
                conn.commit()
        with tit:
            st.write(f"{title}")
        with desc:
            st.write(f"{dec}")
        with dlt:
            x=st.button(" ⛔ Delete ", key=f"{id}")
            if x:
                csr.execute(f"delete from mytodos where todo_id={id}")
                conn.commit()
                st.snow()
                st.rerun()
        st.write("____________________________________")

    

    

else:
    st.warning("Please login first....")
    st.markdown("[Go to login Page](./login)")
