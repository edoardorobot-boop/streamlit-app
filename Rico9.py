import streamlit as st
import sqlite3

def iniciar_db():
    conexion = sqlite3.connect("Oscar.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS niños (id INT PRIMARY KEY, nombre VARCHAR(40))")
    conexion.commit()
    conexion.close()

iniciar_db()

st.title("Sistema DIF")
menu = ["Registrar joven", "Ver lista", "Actualiizar joven", "Eliminar joven"]
opcion = st.sidebar.selectbox("Elige una ocion", menu)

if opcion == "Registrar joven":
    st.subheader("Nuevo Registro")
    mi_id = st.number_input("Introduce ID (numero) : ", min_value=1, step=1)
    mi_nombre = st.text_input("Ingresa el nombre del joven")

    if st.button("Guardar"):
        try:
            edo = sqlite3.connect("Oscar.db")
            cursor = edo.cursor()
            cursor.execute("INSERT INTO niños VALUES (?, ?)", (mi_id, mi_nombre))
            edo.commit()
            edo.close()
            st.success(f" Alumno {mi_nombre} registrado con exito")
        except sqlite3.IntegrityError:
            st.error(f" Error: El ID {mi_id} ya existe. Intenta con otro")
elif opcion == "Ver lista":
    st.subheader(" Lista de jovenes")
    edo = sqlite3.connect("Oscar.db")
    cursor = edo.cursor()
    cursor.execute("SELECT * FROM niños")
    filas = cursor.fetchall()
    edo.close()

    if not filas:
        st.info("La lista esta vacia")
    else:
        st.table(filas)

elif opcion == "Actualizar joven":
    st.subheader(" Modificar Registro")
    id_actualizar = st.number_input("ID del joven a modificar: ", min_value=1, step=1)
    nuevo_nombre = st.text_input("NUEVO nombre: ")
    if st.button("Actualizar"):
        edo = sqlite3.connect("Oscar.db")
        cursor = edo.cursor()
        cursor.execute("UPDATE niños SET nombre = ? WHERE id = ?", (nuevo_nombre, id_actualizar))
        edo.commit()

        if cursor.rowcount > 0:
            st.success(f" Registro con ID {id_actualizar} Actualizado correctamente.")
        else:
            st.warning(f" No se encontro ningun joven con el ID {id_actualizar}.")
            edo.close()
elif opcion == "Eliminar joven":
    st.subheader("  Borrar Registro")
    id_borrar = st.number_input("ID del joven a eliminar: ", min_value=1, step=1)

    if st.button("Eliminar", type="primary"):
        edo = sqlite3.connect("Oscar.db")
        cursor = edo.cursor()
        cursor.execute("DELETE FROM niños WHERE id = ?", (id_borrar,))
        edo.commit()

        if cursor.rowcount > 0:
            st.success(f"  Registro ID {id_borrar} eliminado.")
        else:
            st.warning(f"  No se encontro ningun alumno con el ID {id_borrar}.")
        edo.close()
                
            
            
        

    
                

