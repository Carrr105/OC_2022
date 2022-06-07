# Lenguaje OC2022

#### Proposito

El propósito general de este proyecto es englobar los conocimientos de Computer Science adquiridos a lo largo de la carrera en Ingeniería en Tecnologías Computacionales. Dicho proyecto, tiene como objetivo un entregable final en donde haya sido posible implementar un lenguaje de programación que permita al usuario simular herramientas correspondientes a un lenguaje de computación común, como por ejemplo, la creación de variables simples (int, float, bool), arreglos, matrices, funciones, ciclos, condicionales, entre otros más. Además, se busca implementar funciones más complejas como el manejo de objetos con parámetros y atributos.

***

### Manual de usuario

#### Creación del input

Para poder crear un archivo y ejecutarlo con nuestro lenguaje, es necesario crear un archivo **.txt**, esto puede hacerse desde la terminal con **touch nombre.txt** o haciendo clic derecho y seleccionar **nuevo documento**

#### Estructura básica necesaria

Necesitamos iniciar nuestro programa con el nombre de la misma, por lo cual, haremos uso de la palabra reservada **program** seguida del nombre de nuestro programa y finalizando con un punto y coma ';'

Después necesitamos crear el cuerpo de nuestro programa y este sería colocando **main()** y entre corchetes **{}** nuestro cuerpo
```
program test;

main(){

    write("Hello World");

}
```

#### Creación y asignación de variables

Para poder crear variables, debemos saber que existen distintos tipos, tales como **int, float, char y bool**, estos deben ser escritor en su forma correcta como sería **vars int : myVar;**, en nuestro código quedaría asi:

```
program test;

main(){
    vars int : myVar;
    myVar = 10;
    write("Hello World");

}
```

#### Uso de operadores aritméticos

Para poder realizar **sumas, restas, divisiones y multiplicaciones** podemos hacer uso de los operadores aritméticos, es decir, podemos calcular valores con nuestras variables y constantes, por ejemplo:

```
program test;

main(){
    vars int : myVar;
    vars int : mySecondVar;
    myVar = 5*2;
    mySecondVar = 5 + 20 / 5;
    write("Hello World");

}
```

#### Uso de operadores relacionales y estatutos de condición

En nuestro lenguaje también es posible preguntar si una variable es **mayor, menor, igual o diferente** a otra y también, podemos tomar decisiones de acuerdo a la respuesta **if(condicion)**. Por ejemplo, supongamos que queremos saber si la **variable1 es mayor a la variable2**, en caso de que si sea mayor, imprimiremos "Si es mayor", en caso de que no **(else)** , imprimiremos "No es mayor"

```
program test;

main(){
    vars int : variable1;
    vars int : variable2;

    variable1 = 100;
    variable2 = 20;

    if(variable1 > variable 2){
        write("Si es mayor");
    } else {
        write("No es mayor");
    }
}
```

#### Estatutos de ciclos

Ahora, suponiendo que queremos realizar una acción un N número de veces, ¿Escribiremos N número de veces la misma línea de código, ¡No!.
Para eso nos apoyaremos del estatuto **while()**, este estatuto necesita una **condición** que ira dentro de los paréntesis y al igual que las estructuras que hemos trabajado antes, lo que queremos que ejecute irá entre corchetes **{}**. Suponiendo que queremos imprimir 3 veces "Hola Mundo" lo haremos de la siguiente forma.

```
program test;

main(){
    vars int : variable;
    variable = 1;

    while(variable <= 3){
        write("Hola mundo");
    }
}
```
#### Uso de funciones

Si queremos hacer un pedazo de código para reutilizarlo varias veces, podemos usar las funciones, por ejemplo, suponiendo que siempre queremos sumar dos números y obtener dicha suma, podemos hacer uso de una función. ¿Cómo se hace?, muy sencillo.

```
program test;

function int : sumDos(int uno, int dos){
    return(uno + dos);
}

main(){
    vars int : prueba;
    prueba = sumDos( 1*8+7+1 , 4 ) ;
    write(prueba);
}

```

#### ¿Cómo ejecutar el proyecto?

Para poder ejecutar el proyecto, es necesario tener nuestro **.txt** dentro de la carpeta de **test**, una vez habiendolo colocado ahi, iremos a nuestro archivo **lexyacc.py** y en la línea 1034 colocamos el nombre del archivo que queremos ejecutar. Esto justo despues de **/tests/** y antews de **.txt**

```
archivo = open('./tests/test_funcionsimple.txt','r')
```


Primero ejecutamos en comando **python3 lexyacc.py** y posteriormente el comando **python3 virtualmachine.py**
***

Equipo:

Carlos Gerardo Herrera Cortina - A00821946
Omar Alejandro Balboa Lara - A00825034