### generacion de procesos hijos en phyton
---

* en primer lugar dentro del main puse dos if para que pudiera ejecutar un codigo u otro segun la variable que sale de platform que nos dice en que sistema
operativo estamos

* en tercer lugar hice una funcion con fork que serviria para linux y otra con process esta serviria para window

* luego utilice un bucle while  en ambos casos despues de un imput con una variable contador para que contara hasta que la variable cumpla el requerimiento 
del while para salir

## window

*en el caso de window creo un hijo con process indicando una funcion hijo para que el hijo la ejcute donde mostrar el mensaje con su pid despues del start que 
es donde lo creara

*una vez echo esto hacer un join pasandole un 0 como parametro ya que queremos que no espere a que el hijo termine para generar el siguiente

*en la funcion hijo ponemos un sleep con 5 pasado como parametro para que espere 5 segundos antes de morir con la funcion exit

## linux

*en el caso de linux utilizaremos el fork para generar los procesos y lo guardamos en la variable con un if veremos si su pid es 0 en ese caso haremos que ejecute
el metodo para el hijo que seria parecido como hicimos en linux
