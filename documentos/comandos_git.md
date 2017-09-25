## Actividad

Repositorio Campus Digital en Sitio GitHub: <https://github.com/campus-digital/>

* Abrir Terminal y verificar la instalación.
	
	`$ git --version` 

	*Si no se encuentra instalado git, bajar en: <https://git-scm.com/downloads>*

* Clonar repositorio creado en sitio GitHub

	`$ git clone https://github.com/campus-digital/tutorialgit.git`
	
* Verificar el estatus del repositorio (*Ir a carpeta donde se encuentre repositorio clonado*)
	
	`$ git status`
	
* Seleccionar una rama (branch).

	`$ git checkout master`
	
* Comprobar e incorporar cambios de repositorio remoto en actual rama.

	`git pull origin master`

* Añadir archivo de ejemplo al repositorio

	`$ echo "Incluímos un nuevo archivo al repositorio" >> archivo.txt`

* Verificar el estado de los cambios

	`$ git status`
	
* Añadir cambios al área de preparación (`Staging Area`).

	`$ git add archivo.txt`
	
* Realizar `commit` a los archivos de Staging Area.

	`$ git commit -m "Se añade nuevo archivo al repositorio"`
	
* Subir cambios a rama `master` del repositorio remoto.

	`$ git push origin master`


## Comandos útiles

* Setear la url del repositorio

	`git remote set-url origin git://new.url.here`
	`git remote set-url origin https://github.com/campus-digital/nuevo-repositorio.git`
		
* Añadir otro repositorio.	

	`git remote add [nombre] [url]`

	`git remote add origin https://github.com/campus-digital/nombre-repositorio.git`


