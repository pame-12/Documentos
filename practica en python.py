'''num1 = int(input('Ingresa el primer numero entero por favor..:'))
num2= int(input('Ingresa el segundo numero entero por favor..:'))
suma = num1+num2
resta = num1-num2
multi = num1*num2
divicion = num1/num2
modulo = num1%num2

print('La suma de tus numeros es:', suma)
print('La resta de tus numeros es:', resta)
print('La multiplicacion de tus numeros es:', multi)
print('La divicio de tus numeros es:', divicion)
print('El modulo de tus numeros es:', modulo)

texto = input('Ingresa un texto por favor:')
print(list(texto))
'''


{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Programación I - Colecciones\n",
    "### Instituto Tecnologicos de las Américas ITLA\n",
    "#### Clase 2024.07.02 & 2024.07.06\n",
    "\n",
    "##### email: gdelarosa@itla.edu.do"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src='Colecciones.png'>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# CONTENIDO\n",
    "\n",
    "Colecciones\n",
    "\n",
    "4.1 Listas\n",
    "\n",
    "4.2 Tuplas\n",
    "\n",
    "4.3 Diccionarios\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Colecciones"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Listas, arreglos y matrices. Una colección de datos en programación almacena 2 o más elementos en un arreglo con distintos números de índex, por lo que nos ayuda a agrupar elementos que tengan algo que ver unos con los otros. Existen cuatro tipos de colecciones de datos en el lenguaje Python:\n",
    "\n",
    "Lista es una colección ordenada y modificable. Permite datos duplicados.\n",
    "\n",
    "Tuple es una colección ordenada e inmutable. Permite datos duplicados.\n",
    "\n",
    "Dictionary es una colección sin orden, modificable e indexada. No permite datos duplicados.\n",
    "\n",
    "Al elegir un tipo de arreglo, es útil comprender las propiedades que cada uno posee. Elegir el tipo adecuado para un conjunto de datos en particular podría significar la retención del significado y aumentar la eficiencia o seguridad del programa."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 4.1 Listas"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Son un poderoso tipo de datos que te permiten crear colecciones de datos igualmente poderosas. Podemos utilizar las listas para recopilar y organizar todo: desde configuración de usuarios hasta información, como diccionarios.\n",
    "\n",
    "Una lista en Python es un tipo de datos nativos construido dentro del lenguaje de programación Python. Estas listas son similares a matrices (o arrays) que se encuentran en otros lenguajes. Sin embargo, en Python se manejan como variables con muchos elementos. Aun así, las listas se consideran un tipo de datos para guardar colecciones de información.\n",
    "\n",
    "Una lista en Python es:\n",
    "\n",
    "1. Ordenada: esto quiere decir que los elementos dentro de ella están indexados y se accede a ellos a través de una locación indexada. \n",
    "\n",
    "2. Editable: los elementos dentro de una lista pueden editarse, añadir nuevos o eliminar los que ya tiene. \n",
    "\n",
    "3. Dinámica: las listas pueden contener diferentes tipos de datos y hasta de objetos. Esto significa que pueden soportar paquetes multidimensionales de datos, como un array o muchos objetos. \n",
    "\n",
    "4. No única: esencialmente, esto quiere decir que la lista puede contener elementos duplicados sin que arroje un error. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### ¿Cómo crear una lista?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Las listas son una colección ordenada y modificable, éstas se declaran entre corchetes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['fresa', 'uva', 'cereza']\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "print(lista_frutas)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Si deseamos obtener acceso a algún elemento en la lista, usaremos la siguiente indicación, colocando el número de índex (recordemos que en programación éstos comienzan en 0) que queremos imprimir entre los corchetes. También podemos pedirle al programa que lea el número de index de forma inversa añadiendo un signo «-» antes del número. Así, -1 se refiere al último elemento, -2 al penúltimo, etc."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "uva\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "print(lista_frutas[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fresa\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "print(lista_frutas[-1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "De igual manera, podemos imprimir un rango de elementos en la lista utilizando dos puntos, de la siguiente manera."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['sandia', 'melon', 'kiwi']\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\", \"sandia\", \"melon\", \"kiwi\", \"toronja\"]\n",
    "'Imprime todo desde el index 2 al 5'\n",
    "print(lista_frutas[2:6])\n",
    "'Imprime todo antes del index 4'\n",
    "print(lista_frutas[:4])\n",
    "'Imprime todo a partir del index 2'\n",
    "print(lista_frutas[2:])\n",
    "'Imprime desde el último hasta 4 después del último index'\n",
    "print(lista_frutas[-4:-1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Funciones para listas\n",
    "##### Cambiar el valor de un elemento"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Para cambiar el valor de un elemento dentro de la lista, haremos referencia al número de índex."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['fresa', 'frambuesa', 'cereza']\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "lista_frutas[1] = \"frambuesa\"\n",
    "print(lista_frutas)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Imprimir todos los elementos de la lista\n",
    "\n",
    "Podemos realizar un loop a través de todos los números de índex, de forma que nos entregue los elementos que ésta contiene."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fresa\n",
      "uva\n",
      "cereza\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "for x in lista_frutas:\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Verificar si un elemento existe\n",
    "\n",
    "Esta función te permite conocer si un cierto elemento está presente en una lista."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sí, 'fresa' se encuentra en la lista de frutas\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "if \"fresa\" in lista_frutas:\n",
    "    print(\"Sí, 'fresa' se encuentra en la lista de frutas\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Longitud del arreglo\n",
    "Para determinar cuántos elementos contiene nuestra lista, utilizaremos la función len()."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "print(len(lista_frutas))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Añadir elementos\n",
    "\n",
    "Además de sustituir, también podemos agregar más elementos a los ya existentes usando el comando append(). Podemos incluso seleccionar el lugar en el que queremos añadir dicho objeto en la lista mediante el método insert().\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['fresa', 'naranja', 'uva', 'cereza', 'mango']\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "\"Simplemente añade un elemento\"\n",
    "lista_frutas.append(\"mango\")\n",
    "\"Añade un elemento en el index 1\"\n",
    "lista_frutas.insert(1, \"naranja\")\n",
    "print(lista_frutas)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Remover elementos\n",
    "\n",
    "Existen varios métodos para remover un elemento de una lista:\n",
    "\n",
    "remove()\n",
    "\n",
    "pop()\n",
    "\n",
    "del\n",
    "\n",
    "clear()\n",
    "\n",
    "A continuación podemos observar su comportamiento.\n",
    "\n",
    "‘La función «remove()» retira un elemento específico’"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['fresa', 'cereza']\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "lista_frutas.remove(\"uva\")\n",
    "print(lista_frutas)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "La función «pop()» retira el número de índex especificado o o el último índex si no se especifica un número."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['fresa', 'uva']\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "lista_frutas.pop()\n",
    "print(lista_frutas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['uva', 'cereza']\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "del lista_frutas[0]\n",
    "print(lista_frutas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "lista_frutas.clear()\n",
    "print(lista_frutas)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Copiar una lista\n",
    "\n",
    "No nos es posible copiar un arreglo simplemente escribiendo lista2 = lista1, ya que lista2 sólo hará referencia a lista1, y cualquier cambio hecho en lista1 será automáticamente hecho también en lista2. A continuación veremos dos métodos para realizar una copia."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['fresa', 'uva', 'cereza']\n",
      "['fresa', 'uva', 'cereza']\n"
     ]
    }
   ],
   "source": [
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "lista2 = lista_frutas.copy()\n",
    "print(lista2)\n",
    "\n",
    "lista_frutas = [\"fresa\", \"uva\", \"cereza\"]\n",
    "lista3 = list(lista_frutas)\n",
    "print(lista3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Unir\n",
    "Hay diferentes formas de unir o concatenar dos o más listas en python, la más sencilla es utilizar el operador «+»"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'c', 1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "lista1 = [\"a\", \"b\" , \"c\"]\n",
    "lista2 = [1, 2, 3]\n",
    "\n",
    "lista3 = lista1 + lista2\n",
    "print(lista3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Otra manera es anexando los elementos de lista2 en la lista1, uno por uno."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'c', 1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "lista1 = [\"a\", \"b\" , \"c\"]\n",
    "lista2 = [1, 2, 3]\n",
    "\n",
    "for x in lista2:\n",
    "  lista1.append(x)\n",
    "\n",
    "print(lista1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Por último ejemplo, está el método extend(), cuyo propósito es añadir los elementos de una lista a la otra."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'c', 1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "lista1 = [\"a\", \"b\" , \"c\"]\n",
    "lista2 = [1, 2, 3]\n",
    "\n",
    "lista1.extend(lista2)\n",
    "print(lista1)   "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Metodo\tDescripción\n",
    "\n",
    "append()\tAñade un elemento al final de la lista\n",
    "\n",
    "clear()\tRemueve todos los elementos de la lista\n",
    "\n",
    "copy()\tEntrega una copoa de la lista\n",
    "\n",
    "count()\tEntrega el número de elementos con un valor específico\n",
    "\n",
    "extend()\tAñade elementos de una lista (o cualquier iterable) al final de la lista actual\n",
    "\n",
    "index()\tEntrega el número de índex del primer elemento con el valor especificado\n",
    "\n",
    "insert()\tAñade un elemento a la posición especificada\n",
    "\n",
    "pop()\tRemueve el elemento de la posición especificada\n",
    "\n",
    "remove()\tRemueve el elemento con el valor especificado\n",
    "\n",
    "reverse()\tInvierte el orden de la lista\n",
    "\n",
    "sort()\tReacomoda la lista"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 4.2 Tuplas"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Un tuple es una colección de datos cuyo orden es inalterable, o sea, son elementos ordenados en una secuencia específica y que posee importancia, los tuples se escriben entre paréntesis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('manzana', 'plátano', 'cereza')\n"
     ]
    }
   ],
   "source": [
    "tuple_frutas = (\"manzana\", \"plátano\", \"cereza\")\n",
    "print(tuple_frutas)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Acceder a los elementos del tuple\n",
    "Podemos acceder a los elementos que lo conforman haciendo referencia al número de índex, de la misma manera que con las listas. Recordemos que éste puede comenzar del primer o último dato utilizando el signo «-«."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "plátano\n",
      "cereza\n"
     ]
    }
   ],
   "source": [
    "tuple_frutas = (\"manzana\", \"plátano\", \"cereza\")\n",
    "print(tuple_frutas[1])\n",
    "print(tuple_frutas[-1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "De nueva cuenta, recordemos que los números de índex siempre comienzan en 0 en programación. Cuando los vemos de forma inversa, el último índex sería -1, el penúltimo -2, etc.\n",
    "\n",
    "De la misma manera, cuando queremos imprimir un cierto rango de datos, los colocaremos entre corchetes de la siguiente manera:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('manzana', 'plátano', 'cereza', 'piña')\n"
     ]
    }
   ],
   "source": [
    "'                   0          1         2        3        4        5       6'\n",
    "tuple_frutas = (\"manzana\", \"plátano\", \"cereza\", \"piña\", \"limón\", \"fresa\", \"uva\")\n",
    "#print(tuple_frutas[2:5])\n",
    "print(tuple_frutas[-7:-3])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Observemos que en el límite [2:5], el índex 2 se incluye pero el 5 no. Esta es una regla que aplica siempre en estos casos."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### ¿Cambiar los valores de un Tuple?\n",
    "Una vez creado, no podemos cambiar sus valores, puesto que este tipo de colección es inalterable, pero hay una forma de llevarlo a cabo. Podemos convertir un tuple a una lista, cambiar la lista, y después regresarla a su tipo original. Veamos cómo se hace."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('manzana', 'kiwi', 'cereza')\n"
     ]
    }
   ],
   "source": [
    "x = (\"manzana\", \"plátano\", \"cereza\")\n",
    "y = list(x)\n",
    "y[1] = \"kiwi\"\n",
    "x = tuple(y)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Si intentáramos cambiar directamente un valor dentro de un tuple, el compilador nos marcará un error. Este tipo de colección no puede ser modificado una vez creado. De igual forma, no podemos eliminar un solo elemento, pero sí podemos eliminar el conjunto completo mediante el comando del."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "lista_frutas = (\"fresa\", \"uva\", \"cereza\")\n",
    "del lista_frutas\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Otra nota a destacar es que si quisiéramos crear un tuple con un solo objeto, debemos agregar una coma aunque no pongamos nada después, ya que de lo contrario el compilador no lo tomará como tal."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Método\tDescripción\n",
    "count()\tEntrega la cantidad de veces que un elemento específico se encuentra en el tuple\n",
    "\n",
    "index()\tBusca en el tuple un valor específico y entrega la posición en la que se encuentra\n",
    "\n",
    "len()\tDetermina la cantidad de elementos en un tuple"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 4.3 Diccionarios"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Un diccionario es una colección sin orden, modificable e indexada,éstos se escriben entre llaves y poseen claves y valores. Esto quiere decir que se tendrán diferentes tipos de valores dentro de una misma categoría,"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Marca': 'Ford', 'Modelo': 'Mustang', 'Año': 1964}\n"
     ]
    }
   ],
   "source": [
    "diccionario = {\n",
    "    \"Marca\" : \"Ford\",\n",
    "    \"Modelo\" : \"Mustang\",\n",
    "    \"Año\" : 1964\n",
    "}\n",
    "print(diccionario)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notemos que se añaden comas entre categorías y dobles puntos para indicar el valor que posee cada una."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Acceder a elementos\n",
    "Podemos acceder a los elementos de un diccionario haciendo referencia al nombre de su categoría clave, dentro de corchetes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mustang\n"
     ]
    }
   ],
   "source": [
    "x = diccionario [\"Modelo\"]\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "También hay un método llamado get() que te otorga el mismo resultado."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mustang\n"
     ]
    }
   ],
   "source": [
    "x = diccionario.get(\"Modelo\")\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "También podemos hacer un ciclo por todos los datos que el diccionario contiene, de manera que se impriman todos sus valores y categorías, de la siguiente manera:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Marca Ford\n",
      "Modelo Mustang\n",
      "Año 1964\n"
     ]
    }
   ],
   "source": [
    "diccionario = {\n",
    "    \"Marca\" : \"Ford\",\n",
    "    \"Modelo\" : \"Mustang\",\n",
    "    \"Año\" : 1964\n",
    "}\n",
    "for x in diccionario:\n",
    "  print(x, diccionario[x])\n",
    "# \"x\" imprime la categoría y \"diccionario[x] imprime el valor\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Otras formas para obtener los datos de un diccionario, son utilizando los métodos values() e items(). En este ejemplo, values() entregará los valores de cada categoría e items() regresará ambos, categoría y valor."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ford\n",
      "Mustang\n",
      "1964\n",
      "Marca Ford\n",
      "Modelo Mustang\n",
      "Año 1964\n"
     ]
    }
   ],
   "source": [
    "diccionario = {\n",
    "    \"Marca\" : \"Ford\",\n",
    "    \"Modelo\" : \"Mustang\",\n",
    "    \"Año\" : 1964\n",
    "}\n",
    "for x in diccionario.values():\n",
    "    print(x)\n",
    "    \n",
    "for x, y in diccionario.items():\n",
    "    print(x, y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Cambiar valores\n",
    "Podemos realizar cambios a los valores específicos de un diccionario haciendo referencia al nombre de su categoría, como veremos en el siguiente ejemplo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Marca': 'Ford', 'Modelo': 'Mustang', 'Año': 1964}\n",
      "{'Marca': 'Ford', 'Modelo': 'Mustang', 'Año': 2020}\n"
     ]
    }
   ],
   "source": [
    "diccionario = {\n",
    "    \"Marca\" : \"Ford\",\n",
    "    \"Modelo\" : \"Mustang\",\n",
    "    \"Año\" : 1964\n",
    "}\n",
    "print(diccionario)\n",
    "diccionario[\"Año\"] = 2020\n",
    "print(diccionario)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "En lo que respecta a los métodos para copiar, eliminar o añadir elementos, obtener la cantidad de objetos presentes o la existencia de alguno en especial, los diccionarios se comportan de manera similar a las otras colecciones que hemos revisado."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Diccionarios Anidados\n",
    "Este tipo de colección nos permite añadir sub-colecciones dentro de ellas, lo cual se conoce como anidar. Esto también sucede en algunos ciclos, que veremos más adelante."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hijo1 {'nombre': 'Dennise', 'año': 2004}\n",
      "hijo2 {'nombre': 'Fernando', 'año': 2007}\n",
      "hijo3 {'nombre': 'Omar', 'año': 2011}\n"
     ]
    }
   ],
   "source": [
    "mifamilia = {\n",
    "  \"hijo1\" : {\n",
    "    \"nombre\" : \"Dennise\",\n",
    "    \"año\" : 2004\n",
    "  },\n",
    "  \"hijo2\" : {\n",
    "    \"nombre\" : \"Fernando\",\n",
    "    \"año\" : 2007\n",
    "  },\n",
    "  \"hijo3\" : {\n",
    "    \"nombre\" : \"Omar\",\n",
    "    \"año\" : 2011\n",
    "  }\n",
    "}\n",
    "for x, y in mifamilia.items():\n",
    "    print(x, y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Método\tDescripción\n",
    "clear()\tRemueve todos los elementos\n",
    "\n",
    "copy()\tEntrega una copia del diccionario\n",
    "\n",
    "fromkeys()\tEntrega un diccionario con la categoría y valor especificados\n",
    "\n",
    "get()\tEntrega el valor de un elemento específico\n",
    "\n",
    "items()\tEntrega una lista conteniendo un tuple para cada par de valores\n",
    "\n",
    "keys()\tEntrega una lista conteniendo las categorías del diccionario\n",
    "\n",
    "pop()\tRemueve un elemento específico\n",
    "\n",
    "popitem()\tRemueve el último par de elementos con una categoría especificada\n",
    "\n",
    "setdefault()\tEntrega el valor de una categoría especificada; si ésta no existe, la inserta con un valor especificado\n",
    "\n",
    "update()\tActualiza el diccionario con la categoría y valores específicos"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
