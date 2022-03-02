import psycopg2

def input_numero(msj=" "):
    numero =0
    while True:
        try:
            numero=int(input(msj))
            break
        except ValueError:
            print("Error, solo se pueden ingrear números")  
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
    Ejercicio 4 Numero primo o compuesto
    
    1) Introduzca un numero
    2) Mostrar Historial de las notas
    0) Apagar consola
   
    """)
 
 opcion = int(input_numero("Elige una opción: ") ) 

 if opcion == 1:
        
            n1=int(input_numero("ingrese un numero:"))
            def evaluar_primo(n1):
                contador=0
                resultado=True
                for i in range(1,n1+1):
                    if (n1%i==0):
                        contador+=1
                    if (contador>2):
                        resultado=False
                        break
                return resultado
            if (evaluar_primo(n1)==True):
                estado="Primo"
                print("El numero es", estado)

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio4(numero,estado) VALUES(%s,%s);",(n1,estado))
                conexion.commit()
                cursor.close()

            if (evaluar_primo(n1)==False):
                estado="Compuesto"
                print("El numero es", estado)
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio4(numero,estado) VALUES(%s,%s);",(n1,estado))
                conexion.commit()
                cursor.close() 
        
                
 elif opcion == 2:  

            cursor = conexion.cursor()
            SQL = 'SELECT*FROM ejercicio4;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            cursor.close()

 elif opcion == 0:
        break
 else :
    print("Error,Ingrese un número")