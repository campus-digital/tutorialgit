## Comandos Básicos de git

* Abrir Terminal y verificar la instalación.
	
	`$ git --version` 

	*Si no se encuentra instalado git, bajar en: <https://git-scm.com/downloads>*

* Clonar repositorio creado en sitio GitHub

	`$ git clone https://github.com/nombre_cuenta/nombre_repositorio.git`
	
* Verificar el estado del repositorio (*Ir a carpeta donde se encuentre repositorio clonado*)
	
	`$ git status`
	
* Ver ramas (branch)

	`$ git branch`

* Seleccionar una rama.

	`$ git checkout nombre_rama`
	
* Comprobar e incorporar cambios de repositorio remoto en actual rama.

	`$ git pull origin nombre_rama`
	
* Añadir cambios al área de preparación (`Staging Area`).

	`$ git add nombre_archivo.txt`
	
* Realizar `commit` a los archivos de Staging Area.

	`$ git commit -m "comentario de la confirmación en repositorio"`
	
* Mezclar cambios desde una rama hacia la rama actual.

	`$ git merge nombre_rama`

* Eliminar rama local

	`$ git branch -D nombre_rama`

* Eliminar rama remota

	`$ git push origin nombre_rama --delete`

* Subir cambios a rama `master` del repositorio remoto.

	`$ git push origin nombre_rama`
