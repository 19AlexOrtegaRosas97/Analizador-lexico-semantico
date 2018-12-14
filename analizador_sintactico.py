from io import open

i = 0

with open("palabritas.txt","r") as fichero:
   
    for linea in fichero:
        bandera=0
        tamano = len(linea)
        linea = linea[0:tamano]
        print(linea, " tiene una cantidad de caracteres de ", len(linea))
        
        if("unsigned" in linea):
            print("unsigned es una palabra reservada para indicar que una variable no tiene signo")
            bandera=1
        if("int" in linea):
            print("palabra reservada para declarar una variable entera")
            bandera=1
        if("long" in linea):
            print("palabra reservada para declarar una variable entera con un rango más amplio")
            bandera=1
        if("float" in linea):
            print("palabra reservada para declarar una variable flotante real")
            bandera=1
        if("short" in linea):
            print("palabra reservada para declarar una variable entera corta")
            bandera=1
        if("bool" in linea):
            print("palabra reservada para declarar una variable del tipo verdadero o falso")
            bandera=1
        if("string" in linea):
            print("palabra reservada para declarar una variable del tipo cadena de texto")
            bandera=1
        if("char" in linea):
            print("palabra reservada para declarar una variable de un solo caracter")
            bandera=1
        if("switch" in linea):
            print("palabra reservada para declarar una estructura selectiva que puede contar con casos y un default")
            bandera=1
        if("case" in linea):
            print("palabra reservada para declarar un caso dentro de la estructura selectiva switch")
            bandera=1
        if("default" in linea):
            print("palabra reservada para indicar un caso por defecto dentro de la estructura selectiva switch")
            bandera=1
        if("break" in linea):
            print("palabra reservada para indicar el rompimiento de una iteración o de un ciclo")
            bandera=1
        if("if" in linea):
            print("palabra reservada de tipo de estructura selectiva donde se debe cumplir una condicion")
            bandera=1
        if("else" in linea):
            print("palabra reservada de tipo de estructura selectiva, debe de ir después de un if")
            bandera=1
        if("do" in linea):
            print("palabra reservada para indicar el comienzo de una estrutura iterativa")
            bandera=1
        if("while" in linea):
            print("palabra reservada del tipo de estructura iterativa que se ejecuta mientras que se cumpla una condición")
            bandera=1
        if("for" in linea):
            print("palabra reservada del tipo de estructura iterativa que ejecuta un numero finito de iteraciones")
            bandera=1
        if("void" in linea):
            print("palabra reservada para indicar que una funcion no devuelve un valor")
            bandera=1
        if("class" in linea):
            print("palabra reservada para indicar una estructura del tipo clase en programación orientada a objetos")
            bandera=1
        if("struct" in linea):
            print("palabra reservada para indicar una estructura con un conjunto de variables dentro")
            bandera=1
        if("cout" in linea):
            print("palabra reservada encargada de mostrar una cadena en la consola")
            bandera=1
        if("cin" in linea):
            print("palabra reservada encargada de recibir un dato por el usuario dentro de la consola")
            bandera=1
        if("include" in linea):
            print("palabra reservada para indicar una librería a incluir")
            bandera=1
        if("catch" in linea):
            print("palabra reservada para evitar que un error detenga la ejecución del programa")
            bandera=1
        if("try" in linea):
            print("palabra reservada para indicar que el programa pruebe una serie de instrucciones a ejecutar")
            bandera=1
        if("not" in linea):
            print("palabra reservada para realizar una negación")
            bandera=1
        if("and" in linea):
            print("palabra reservada para indicar una inclusión")
            bandera=1
        if("xor" in linea):
            print("palabra reservada para indicar la ejecución del algoritmo de xor")
            bandera=1
        if("or" in linea):
            print("palabra reservada para indicar una opcion alternativa a evaluar")
            bandera=1
        if("return" in linea):
            print("palabra reservada para indicar el retorno de un parametro")
            bandera=1
        if("@" in linea):
            print("Caracter aceptado por el compilador")
            bandera=1
        if("}" in linea):
            print("Caracter aceptado por el compilador Delimita el final de un bloque de codigo")
            bandera=1
        if("{" in linea):
            print("Caracter aceptado por el compilador Delimita el inicio de un bloque de codigo")
            bandera=1
        if("]" in linea):
            print("Caracter aceptado por el compilador se utiliza para delimitar el final de un arreglo")
            bandera=1
        if("[" in linea):
            print("Caracter aceptado por el compilador se utiliza para delimitar la apertura de un arreglo")
            bandera=1
        if("#" in linea):
            print("Caracter aceptado por el compilador que se pone antes de la palabra reservada INCLUDE")
            bandera=1
        if("&" in linea):
            print("Caracter aceptado por el compilador sirve para el AND logico (condicional)")
            bandera=1
        if("!" in linea):
            print("Caracter aceptado por el compilador sirve para la negacion")
            bandera=1
        if(")" in linea):
            print("Caracter aceptado por el compilador sirve para llamar una funcion")
            bandera=1
        if("(" in linea):
            print("Caracter aceptado por el compilador sirve para llamar una funcion")
            bandera=1
        if("/" in linea):
            print("Caracter aceptado por el compilador sirve para division entre dos variables o si es doble para comentarios")
            bandera=1
        if("+" in linea):
            print("Caracter aceptado por el compilador sirve para suma entre dos variables")
            bandera=1
        if("-" in linea):
            print("Caracter aceptado por el compilador sirve para resta entre dos variables")
            bandera=1
        if("=" in linea):
            print("Caracter aceptado por el compilador sirve para asignar valos a una varible o si es doble sive como condicional")
            bandera=1
        if("<" in linea):
            print("Caracter aceptado por el compilador comparacion si una variable es menor que otra")
            bandera=1
        if(">" in linea):
            print("Caracter aceptado por el compilador comparacion si una variable es menor que otra")
            bandera=1
        if("*" in linea):
            print("Caracter aceptado por el compilador sirve para multipliccion entre dos variables o para asigar un puntero")
            bandera=1
        if("%" in linea):
            print("Caracter aceptado por el compilador sirve para dar el residuo de una division")
            bandera=1
        if("," in linea):
            print("Caracter aceptado por el compilador sirve para definir un caracter")
            bandera=1
        if(":" in linea):
            print("Caracter aceptado por el compilador")
            bandera=1
        if('"' in linea):
            print("Caracter aceptado por el compilador")
            bandera=1
        if('.' in linea):
            print("Caracter aceptado por el compilador")
            bandera=1
        if(';' in linea):
            print("Caracter aceptado por el compilador terminar una linea de codigo")
            bandera=1
            
        i+=1
    if bandera == 0:
        print("palabra que puede ser usada como identificador")
        
        
fichero.close()
del(fichero)


