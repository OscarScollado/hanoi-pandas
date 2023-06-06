# hanoi-pandas

Las torres de Hanoi es un puzle donde debes mover una torre de piezas de un sitio a otro, con la condición de poner siempre una pieza más pequeña encima de una más grande y no al revés.

![imagen](https://cdn.kastatic.org/ka-perseus-images/5b5fb2670c9a185b2666637461e40c805fcc9ea5.png)

El programa representa cada pieza con un número; cuanto más grande sea la pieza, más grande será el número que le represente.

Esta representación está hecha gracias a la libería [pandas](https://pandas.pydata.org/pandas-docs/stable/).

El algoritmo usado para resolver el puzle para n piezas es uno recursivo, donde cogemos una torre, le "quitamos" la pieza más grande y resolvemos el mismo puzle con esa subtorre como si la pieza más grande no existiera. Así quitándole pieza a pieza a la torre hasta que llegamos al caso base de una torre de una pieza, y de ahí nos vamos hacia atrás y vamos haciendo el puzle de una torre de una pieza, luego de dos piezas, de tres piezas... Así mover toda la torre con todas las piezas que teníamos originalmente.

Solamente se necesitan tres posiciones para recolocar las piezas. El puzle admite cualquier posición de salida y cualquier posición objetivo de las tres que hay *(incluso si la salida y la meta con las mismas)*.

Las variables del programa con las que se pueden interactuar son: `num_pisos`, `inicio`, `final`:
* `num_pisos`: es el número de piezas que hay
* `inicio`: la posición donde la torre estará al inciar
* `final`: la posición donde se quiere poner la torre
