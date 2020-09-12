# click_python

Ejemplo de como crear diferentes CLI por medio de la libreria Click https://click.palletsprojects.com/en/7.x/.

Como usar con Docker.

En cualquier OS que se pueda utilizar Makefile (https://opensource.com/article/18/8/what-how-makefile), ejecutar lo siguiente, para construir nuestra imagen docker.

+ make build 

Con nuestra imagen ya genereda, se pueden ejecutar los comandos de la siguiente manera.
 + docker run example_click_python find-character --name="Walter"
 + docker run example_click_python random-character
 + docker run example_click_python random-quote
 + 
 
Para poder realizar cambios al archivo run.py ejecutar lo siguiente.
+ make shell

