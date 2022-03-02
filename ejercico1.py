import random 
import psycopg2
import os

try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "12345678",
        dbname = "examen"
    )
    print ("La conexión fue exitosa")
except psycopg2.Error as e:
    print ("Ocurrió un problema con la conexión")
    print ("Verifique los parametros")

print('Juego de dados')
cursor = conexion.cursor()
while True:
    print('''
    Seleccione que desea realizar

    1) Lanzamiento de datos
    2) Partidas anteriores
    3) Salir
    ''')
    try:
        seleccion = int(input('Que opción desea realizar '))
        if seleccion == 1:
                x = random.randint(1,6)
                y = random.randint(1,6)
                suma = x + y 
                print('Cara1', x)
                print('Cara2', y)
                print('El resultado es: ',suma)
                conexion.commit()
                if suma == 7:
                    resultado = ('PERDIO')
                    print(resultado)
                    cursor.execute('INSERT INTO problema1(cara1, cara2, suma, resultado) VALUES(%s,%s,%s,%s);',(x,y,suma,resultado))
                    conexion.commit()
                    break
                elif suma == 8: 
                    resultado = ('GANO')
                    print(resultado)
                    cursor.execute('INSERT INTO problema1(cara1, cara2, suma, resultado) VALUES(%s,%s,%s,%s);',(x,y,suma,resultado))
                    conexion.commit()
                    break
                else:
                    resultado = ('Intente nuevamente')
                    print(resultado)
                    cursor.execute('INSERT INTO problema1(cara1, cara2, suma, resultado) VALUES(%s,%s,%s,%s);',(x,y,suma,resultado))
                    conexion.commit()
        elif seleccion == 2:
            cursor = conexion.cursor()
            SQL = 'SELECT*FROM problema1;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            os.system('pause')
        elif seleccion == 3:
            break
    except ValueError:
        print('El valor no es correcto')
        print('Ingrese un valor correcto')
        os.system('pause')