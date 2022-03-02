import psycopg2

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
    Ejercicio 3 Calcular el IVA
    
    1) Introducir el valor del producto en quetzales
    2) Mostrar Historial de las notas
    0) Apagar consola
   
    """)
 
 opcion = int(input_numero("Elige una opción: ") ) 

 if opcion == 1:
        
            precio = float(input_numero("Ingrese el valor de su producto: ") )
            IVA = precio*0.12
            sin_IVA = precio - IVA
            print("precio:", precio)
            print("IVA:", IVA)
            print("sin IVA:", sin_IVA)

            cursor = conexion.cursor()
            cursor.execute("INSERT INTO problema3(Precio,IVA,Sin_IVA) VALUES(%s,%s,%s);",(precio,IVA,sin_IVA))
            conexion.commit()
            cursor.close() 

                
 elif opcion == 2:  

            cursor = conexion.cursor()
            SQL = 'SELECT*FROM problema3;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            cursor.close()

 elif opcion == 0:
        break
 else :
    print("Error,Ingrese un número") 