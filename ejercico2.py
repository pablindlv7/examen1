from msilib.schema import Media
import psycopg2
import numpy as np
import statistics as stat

def input_numero(msj=" "):
    numero =0
    while True:
        try:
            numero=int(input(msj))
            break
        except ValueError:
            print("Error, ingrese un número")  
    return numero

try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "12345678",
        dbname = "examen"
    )
    print("conexión exitosa")
except psycopg2.Error as e:
    print("Ocurrio un error en la conexion")
    print("Verifique los parametros")


while True:
 print("""
    Ejercicio 2 Rendimiento Academico
    
    1) Introducir los valores de las 5 notas
    2) Mostrar Historial de las notas
    0) Apagar consola
   
    """)
 
 opcion = int(input_numero("Elige una opción: ") ) 

 if opcion == 1:
        
            n1 = float(input_numero("nota 1: ") )
            n2 = float(input_numero("nota 2: ") )
            n3 = float(input_numero("nota 3: ") )
            n4 = float(input_numero("nota 4: ") )
            n5 = float(input_numero("nota 5: ") )

            lista = [n1,n2,n3,n4,n5]
            media = np.mean(lista)
            print("Media:", media)
            mediana = np.median(lista)
            print("Mediana:", mediana)
            desviacion_estandar = np.std(lista)
            print("desviacion_estandar:",desviacion_estandar)
            varianza = np.var(lista)
            print("varianza:",varianza)
            numero_mayor = max(lista)
            numero_menor = min(lista)
            rango = numero_mayor - numero_menor
            print("rango:",rango)
            moda=stat.mode(lista)
            print("moda:",moda)


            cursor = conexion.cursor()
            cursor.execute("INSERT INTO ejercicio2(n1,n2,n3,n4,n5,media,mediana,desv_estandar,varianza,rango,moda) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(n1,n2,n3,n4,n5,media,mediana,desviacion_estandar,varianza,rango,moda))
            conexion.commit()
            cursor.close() 

                
 elif opcion == 2:  

            cursor = conexion.cursor()
            SQL = 'SELECT*FROM ejercicio2;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            cursor.close()

 elif opcion == 0:
        break
 else :
    print("Error,Ingrese un número") 