import streamlit as st
import json
import requests
import pandas as pd


st.title("CRUD en PostgreSQL con FastAPI")
#api_url = st.text_input("URL de la API")

option = st.selectbox("Selecciona la operacion que quieres usar", 
                      ("INSERT", "READ", "UPDATE", "DELETE"))
    
if  option == "INSERT":
    st.write("")
    insert_name = st.text_input("Ingresa el nombre", "Escribe aqui...")
    insert_phone = st.text_input("Ingresa el celular")
    inputs = {"name":insert_name, "phone":insert_phone}

    if st.button("Apply"):
        res = requests.post(url="http://localhost:8000/api/insert", data=json.dumps(inputs))
        if res.status_code == 201:
            st.write(f"El registro ha sido agreagado con éxito.")
        else:
            st.error(f"Error. Codigo de estado: {res.status_code}")

elif option == "READ":
    if st.button("Apply"):
        res = requests.get(url="http://localhost:8000/")
        st.subheader("Response from user  fastapi_test DB ")
        response_data = res.json()
        df = pd.DataFrame(response_data)
        output = st.dataframe(df)

elif option == "UPDATE":
    st.write("")
    id = st.text_input("Escriba el ID donde desea actualizar: ")
    insert_name = st.text_input("Ingresa el nombre", "Escribe aqui...")
    insert_phone = st.text_input("Ingresa el celular")
    inputs = {"id":id, "name":insert_name, "phone":insert_phone}
    if st.button("Apply"):
        url_api = f"http://localhost:8000/api/update/{id}"
        res = requests.put(url=url_api, data=json.dumps(inputs))

elif option == "DELETE":
    id = st.text_input("Escriba el ID donde desea eliminar: ")
    if st.button("Apply"):
        url_api = f"http://localhost:8000/api/delete/{id}"
        res = requests.delete(url=url_api)

        if res.status_code == 204:
            st.write(f"El registro con el ID {id} ha sido eliminado con éxito.")
        else:
            st.error(f"Error al eliminar el ID {id}.\n Codigo de estado: {res.status_code}")