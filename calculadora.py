import streamlit as st

def pedir_valores():
    Name  = st.text_input("Nombre")
    n1 = st.number_input("Numero 1")
    n2 = st.number_input("Numero 2")

    if st.button("Sumar"):

        st.success(f"Hola {Name}")
        st.write (f"{n1} + {n2} = {n1+n2}")

def pedir_resta():
    Name  = st.text_input("Nombre")
    n1 = st.number_input("Numero 1")
    n2 = st.number_input("Numero 2")

    if st.button("Restar"):

        st.success(f"Hola {Name}")
        st.write (f"{n1} - {n2} = {n1-n2}")
    
def pedir_multiplicacion():
    Name  = st.text_input("Nombre")
    n1 = st.number_input("Numero 1")
    n2 = st.number_input("Numero 2")

    if st.button("Multiplicar"):

        st.success(f"Hola {Name}")
        st.write (f"{n1} * {n2} = {n1*n2}")
        

opcion = st.sidebar.selectbox("Opciones", ["Suma", "Resta", "Multiplicacion", "Division", "Acerca de"])


match opcion:
    case "Suma":
        st.write ("Esta es la opcion suma...")
        pedir_valores()

    case "Resta":
        st.write ("Esta es la opcion resta...")
        pedir_resta()

    case "Multiplicacion":
        st.write ("Esta es la opcion multiplicacion...")
        pedir_multiplicacion()

    case "Division":
        st.write ("Esta es la opcion division...")
        pedir_valores()

    case "Acerca de":
        st.write ("Derechos reservados 2023")
        st.write ("UCOL-ICI-FIME")
        st.write ("Este es un ejemplo de calculadora en streamlit")
