# Guía de trabajo GIT

Ejemplo: <https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud>

## Prerrequisitos

* Tener instalado GIT en el computador (<https://www.atlassian.com/git/tutorials/install-git>)

		$ git --version
		
				
* Tener una cuenta BitBucket (<https://bitbucket.org/account/signup/>)

## Ejercicio
* Create a Git repository 
* Copy your Git repository and add files 
* Pull changes from your Git repository on Bitbucket Cloud 
* Use a Git branch to merge a file 

## Crear Repositorio* Start a new repository or obtain one from an existing URL		$ git init [project-name]
		$ git init repositorio_git
		
		
*Initialized empty Git repository in /Users/cesarvillegascortes/Documents/campusdigital/Pruebas/repositorio_presentacion/repositorio_git/.git/*
		Creates a new local repository with the specified name
		
		$ cd repositorio_git/
		$ git status
		
## Adding & Committing

* Creamos y añadimos un nuevo archivo TXT
		
		echo "Incluímos un nuevo archivo al repositorio" >> archivo.txt

* Verificamos los cambios

		git status
		
* Añadiendo cambios
		
		git add archivo.txt
		
* Mensaje de respuesta (git status)
		
		Changes to be committed:
		(use "git rm --cached <file>..." to unstage)
		new file:   archivo.txt


* Committing

		git commit -m "Se añade nuevo archivo al repositorio"

* History
		
		git log


*commit e23820498c5dd8c92be3150eda5c21fa9a46dcdf*

*Author: César Villegas Cortés <cevillegas@userena.cl>*

*Date:   Thu Aug 10 15:19:33 2017 -0400*

*Se añade nuevo archivo al repositorio*

* Remote Repositories

To push our local repo to the GitHub server we'll need to add a remote repository.

This command takes a remote name and a repository URL, which in your case is 


		git remote add origin https://cesar_universidad@bitbucket.org/cesar_universidad/presentacion_git.git
		
		git push -u origin master
		
		

