![banner](images/header.png)

## Actividad 1: El objetivo es crear una cuenta y configurar nuestro equipo con ella

### 1.1.Crear cuenta en github
* Ingresa a la pagina de [https://github.com](https://github.com/)
* Ingresamos nuestros datos en el formulario
!["registro"](images/registro.png)
* Envía los datos del formulario
* Te llegara un email a tu cuenta para confirmar el registro, confírmalo!!

### 1.2.Configura la cuenta que creaste en tu equipo
* Abrimos nuestra terminal de comandos (ctrl+t)
![terminal](images/terminal.png)
* Ingresamos nuestro nombre con el comando:
        git config --global user.name "Juan Galleguillos"
* Ingresamos nuestro mail con el comando:
        git config --global user.email "jgalleguillos@gmail.com"
* Podemos utilizar los comandos sin el ultimo parametro para visualizar la configuración actual.
        git config --global user.name
        git config --global user.email

## Actividad 2: El objetivo es crear nuestro primer repositorio y utilizar los comandos básicos.

### 2.1.Crear carpeta para repositorio e inicializarlo
* Abrimos nuestra terminal de comandos (ctrl+t)
![terminal](images/terminal.png)
* Creamos una carpeta de nombre "mirepo" para nuestro repositorio:
        mkdir mirepo
* Ingresamos a la carpeta e iniciamos nuestro primer repositorio con el siguiente comando:
        cd mirepo
        git init

### 2.2.Estado del repositorio
* Podemos ver en que estado se encuentra nuestro repositorio con el comando:
        git status
* La terminal nos entrega la siguiente información:
![terminal](images/git_status.png)
 - La rama en la cual nos encontramos (master por defecto)
 - Si existen cambios en el repositorio
 - En este caso falta un commit inicial

### 2.3.Confirmación inicial
* Primero tenemos que crear un archivo en el área de trabajo (en nuestro caso sera un programa en python el cual puede ser escrito con cualquier editor)
        vim programa.py
* Creamos un programa básico al ingresarle el siguiente código (área de trabajo):
        #!/usr/bin/env python
        # -*- coding: utf-8 -*-

        print('Hola Mundo!!!')
* Guardamos el archivo "programa.py"
* Si verificamos el estado del repositorio, nos daremos cuenta que git ya reconoció el nuevo archivo:
        git status
![nuevo archivo](images/area_trabajo.png)
* Agregamos nuestro programa al área de preparación con el siguiente comando:
        git add -A
* Podemos verificar nuestros cambios en el repositorio (git nos indica esto con un color diferente):
![area preparacion](images/area_preparacion.png)
* Confirmamos nuestros cambios y se agrega un comentario con el siguiente comando (se confirman los cambios en el repositorio):
        git commit -m "Programa inicial"
* Verificamos el estado de nuestro repositorio:
        git status
* Git nos informa que no hay cambios, ya que estos fueron confirmados:
![primer commit](images/commit_realizado.png)

### 2.4.Confirmaciones realizadas (logs)
* Para ver nuestros commit utilizamos otro comando, el cual se indica a continuación:
        git log
![git log](images/git_log.png)
* La imagen anterior nos indica un listado con los commit realizados (en este caso solo el primero), además, nos entrega información importante como:
  - El código identificador del commit (sha-1)
  - El autor del commit (responsable)
  - La fecha y hora de creación
  - El comentario del commit (descripción concisa)
* Ahora realiza cambios al programa y repite el proceso (la idea es que tengas varios commit, al menos 3)
* Si verificamos los commits del repositorio nos debería salir algo así:
![lista log](images/git_lista_log.png)
* Finalmente como dato extra podemos visualizar los log personalizados para mejorar la lectura con el siguiente comando:
        git log --pretty=oneline
![oneline](images/git_log_oneline.png)
* Puedes ver mas formatos de visualización en la pagina [oficial](https://git-scm.com/docs/pretty-formats).

### 2.5.Muevete entre commits
* Los commit nos permiten movernos entre versiones, para hacer esto, es necesario utilizar el comando:
        git checkout <commit>
* Donde "commit" es el código identificador del commit, el cual es el codigo sha-1 que nos muestra `git log`.
![checkout commit](images/checkout_commit.png)
* A continuación, muévete entre tus commit y verifica el estado del archivo "programa.py"
* Para volver a tu ultimo commit lo puedes realizar con:
        git checkout master
o también con:
        git checkout <commit>
si es que conoces el id (sha-1) de tu ultimo commit.

### 2.6.Crea otras ramas
* Para ver las ramas que tienes y en la que te encuentras actualmente, utiliza:
        git branch
* El comando anterior nos muestra una lista con las ramas existentes y con un asterisco la rama actual (deberíamos tener solo master).
* Puedes crear otras ramas desde una rama inicial, la cual siempre es master, con el comando:
        git branch <nombre>
en nuestro caso le daremos nombre "desarrollo":
        git branch desarrollo
* Si verificamos nuestras ramas:
![ramas](images/ramas.png)

### 2.7.Muevete entre ramas
* Las ramas nos permiten movernos entre dimensiones diferentes, cada rama es independiente de la otra hasta que se fusionan.
* Para movernos entre ramas, utilizamos el mismo comando que el para movernos entre commits, con la diferencia que utilizamos el nombre de la rama y no el id de commit, como se muestra a continuación:
        git checkout <nombre_rama>
* Movámonos a la rama "desarrollo" que creamos:
        git checkout desarrollo
![checkout rama](images/checkout_rama.png)
* Podemos verificar la rama en la que estamos con:
![ramas](images/ramas2.png)
* Realiza nuevas modificaciones en esta rama y realiza los commits correspondientes (al menos 2), debería quedar algo así:
        git log --pretty=online
![log desarrollo](images/log_desarrollo.png)
* Cámbiate a la rama master y verifica que no tiene los commits que creaste en la rama desarrollo:
![log ambas](images/git_logs_ambas.png)

### 2.8.Fusiona las ramas
* Para mover los commits o cambios desde una rama hacia otra tienes que fusionar ramas.
* La fusión funciona desde otra rama hacia la actual, es decir, si nos ubicamos en master, podemos fusionar desde "**desarrollo hacia master**".
* Esto lo realizaremos de la siguiente manera:
        git branch
        git merge desarrollo
![fusion](images/merge_desarrollo.png)
* La fusión nos indica que se modificaron 7 lineas, 6 se agregaron y 1 se elimino.
* Verifica el estado de los commits en ambas ramas y te darás cuenta que ahora ambas ramas tienen los mismos commits, ya que fusionaste.
![images](images/verificar_fusion.png)

## Actividad 3: El objetivo es clonar un proyecto existente y realizar modificaciones en repositorio remoto.

### 3.1.Clona un proyecto existente
* Sal de la carpeta "mirepo", ubícate en la carpeta padre de "mirepo" para clonar un proyecto.
* Dirígete al proyecto [https://github.com/campus-digital/tutorialgit](https://github.com/campus-digital/tutorialgit) y busca el botón clonar:

![images](images/clonar.png)
* Copia la URL y clona con el comando:
        git clone https://github.com/campus-digital/tutorialgit.git
* Nos creara una carpeta llamada "tutorialgit" en donde se encuentra el proyecto clonado, por ende, ingresamos a ella.
* Si ejecutamos `git status` nos reconocerá que estamos en una carpeta de git y nos dará la información correspondiente.
* En la Carpeta python se encuentra el programa "operaciones.py" el cual modificaras colaborativamente, revisa su código.
* Ponte deacuerdo con tus compañeros y selecciona una función a modificar.

### 3.2.Muevete a la rama de tu función
* Muévete a la rama correspondiente a la función que modificaras con el comando:
        git checkout <branch>
* Realiza modificaciones en la función que seleccionaste y realiza los commits que estimes necesarios.

### 3.3.Subir y bajar cambios de repositorio
* Ya conoces los comandos básicos de git para trabajar localmente, sin embargo, para interactuar con un repositorio remoto es necesario conocer algunos mas.
* Para subir tus cambios locales a un repositorio utiliza el comando:
        git push origin <branch>
  - Recuerda que debe ser la misma rama en la que te encuentras y haz realizado modificaciones.
* Ahora cualquier persona puede bajar esos cambios que realizaste en la rama en la que estas.
* Intenta cambiarte de rama y bajar los cambios que realizo otra persona y prueba su funcionamiento.
* Para bajar cambios desde repositorio utiliza el comando:
        git pull origin <branch>
  - Recuerda que debe ser la misma rama en la que te encuentras.

### 3.4.Fusiona los cambios en master
* Fusiona los cambios en master con el comando ya conocido y súbelos al repositorio remoto, con esto quedaran todas las modificaciones en master:
        git checkoutmaster
        git merge <branch>

### 3.5.Verifica que master tiene la ultima versión y sube los cambios
* Ejecuta el programa y verifica que se encuentren los cambios de todas las ramas en master.
* Si tu rama master funciona sin problemas, sube los cambios:
        git push origin master
