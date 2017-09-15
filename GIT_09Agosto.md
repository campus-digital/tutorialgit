Leer: <https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell#_git_branching>
## GIT 

Git is a free and **open source distributed version control system** designed to handle everything from small to very large projects with speed and efficiency.

*	**Version control** is a system that records changes to a file or set of files over time so that you can recall specific versions later


## Sistemas de Versionamiento

* **Local Version Control Systems:** 
	* Many people’s version-control method of choice is to copy files into another directory. This approach is very common because it is so simple, but it is also incredibly error prone. It is easy to forget which directory you’re in and accidentally write to the wrong file or copy over files you don’t mean to.
	* Para hacer frente a este problema, Los programadores desarrollaron VCSs locales, that had a simple database that kept all the changes to files under revision control. 
* **Centralized Version Control Systems:**
	* The next major issue that people encounter is that they need to collaborate with developers on other systems. To deal with this problem, Centralized Version Control Systems (CVCSs) were developed. 
	* These systems, such as **CVS, Subversion, and Perforce**, have a single server that contains all the versioned files, and a number of clients that check out files from that central place
* **Distributed Version Control Systems (DVCS):**
	* whenever you have the entire history of the project in a single place, you risk losing everything, this is where Distributed Version Control Systems (DVCSs) step in. .
	* In a DVCS (such as **Git**, **Mercurial**, **Bazaar or Darcs**), clients don’t just check out the latest snapshot of the files: they fully mirror the repository. Thus if any server dies, and these systems were collaborating via it, any of the client repositories can be copied back up to the server to restore it. Every clone is really a full backup of all the data.


Furthermore, many of these systems deal pretty well with having several remote repositories they can work with, **so you can collaborate with different groups of people in different ways simultaneously within the same project**. This allows you to set up several types of workflows **that aren’t possible in centralized systems**, such as hierarchical models.

<https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control#_getting_started>


## Historia
In 2002, the Linux kernel project began using a proprietary DVCS called *BitKeeper*.

In 2005, This prompted the Linux development community (and in particular Linus Torvalds, the creator of Linux) to develop their own tool based on some of the lessons they learned while using BitKeeper. Some of the goals of the new system were as follows:

* Speed
* Simple design
* Strong support for non-linear development (thousands of parallel branches)
* Fully distributed
* Able to handle large projects like the Linux kernel efficiently (speed and data size)



Lanzamiento inicial 7 de abril de 2005 y fue diseñado por Linus Torvalds y se basó en BitKeeper(<https://es.wikipedia.org/wiki/BitKeeper>) y en Monotone (<https://es.wikipedia.org/wiki/Monotone>). 
A diferencia de SCV (Sistema de Control de Versiones) tradicionales que son conectados y centralizados, GIT es distribuido y desconectado lo que lo hace una elección frecuente entre proyectos open-source.


* <https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git>


## Características
 * **Branching and Merging:**
 	* Git allows and encourages you to have multiple local branches that can be entirely independent of each other. The creation, merging, and deletion of those lines of development takes seconds. 
 	* Notably, when you push to a remote repository, you do not have to push all of your branches. You can choose to share just one of your branches, a few of them, or all of them. This tends to free people to try new ideas without worrying about having to plan how and when they are going to merge it in or share it with others. 
 * **Small and Fast**
 	* With Git, nearly all operations are performed locally, giving it a huge speed advantage on centralized systems that constantly have to communicate with a server somewhere
	* Git is **written in C**, reducing the overhead of runtimes associated with higher-level languages. 
 * **Distributed**
 	* This means that instead of doing a "checkout" of the current tip of the source code, you do a "clone" of the entire repository. 
 	* Because of Git's distributed nature and superb branching system, an almost endless number of workflows can be implemented with relative ease. 
 * **Data Assurance**:
 	* The data model that Git uses ensures the **cryptographic integrity** of every bit of your project. Every file and commit is checksummed and retrieved by its **checksum** when checked back out. It's impossible to get anything out of Git other than the exact bits you put in.
 * Staging Area:
 	* Unlike the other systems, Git has something called the **"staging area" or "index"**. This is an intermediate area where commits can be formatted and reviewed before completing the commit. 
 	  ![alt text](images/staging_area.png) 
 	  * One thing that sets Git apart from other tools is that it's possible to quickly stage some of your files and commit them without committing all of the other modified files in your working directory or having to list them on the command line during the commit.
 * Free and Open Source:
 	* The Git project chose to use GPLv2 to guarantee your freedom to share and change free software.

* Referencia: <https://git-scm.com/about>


## Ventajas de Git:
Using Git to power your development workflow presents a few advantages over SVN. 
<ol>
<li> First, it gives every developer their own local copy of the entire project. This isolated environment lets each developer work independently of all other changes to a project—they can add commits to their local repository and completely forget about upstream developments until it's convenient for them.</li>
<li>Second, it gives you access to Git’s robust branching and merging model. Unlike SVN, Git branches are designed to be a fail-safe mechanism for integrating code and sharing changes between repositories.</li>
</ol>

## Repository management services

They are key components of collaborative software development. They enable software developers to manages changes to the source code and related files, create and maintain multiple versions in one <b>central place</b>. 

There are numerous benefits of using them, even if you work in a small team or you are a one man army. Using repository management services enables teams to move faster and preserve efficiency as they scale up.

Entre los que destacan:

* <https://github.com>
* <https://bitbucket.org>
* <https://about.gitlab.com/>
* <https://gogs.io/> (A painless self-hosted Git service.)


Se recomienda utilizar remote repositories 

<https://medium.com/flow-ci/github-vs-bitbucket-vs-gitlab-vs-coding-7cf2b43888a1>
<https://somostechies.com/repositorios-privados-en-git/#.WXs62YrLN7M>
<https://git-scm.com/book/en/v1/Getting-Started-About-Version-Control>
<https://bitbucket.org/product/comparison/bitbucket-vs-github>

## Nomenclatura
* Git Branching: Branching means you diverge from the main line of development and continue to do work without messing with that main line.


## Cómo Trabaja Git

Like Subversion, the Centralized Workflow uses a central repository to serve as the single point-of-entry for all changes to the project. Instead of `trunk`, the default development branch is called `master` and all changes are committed into this branch. This workflow doesn’t require any other branches besides master.


* Developers start by **cloning the central repository**. 
* In their own local copies of the project, they edit files and commit changes as they would with SVN; however, *these new commits are stored locally—they’re completely isolated from the central repository*. This lets developers defer synchronizing upstream until they’re at a convenient break point.
* To publish changes to the official project, developers **“push”** their local master branch to the central repository. This is the equivalent of svn commit, except that it adds all of the local commits that aren’t already in the central master branch.


Before the developer can publish their feature, **they need to fetch the updated central commits and rebase their changes on top of them.** This is like saying, “I want to add my changes to what everyone else has already done.” The result is a perfectly linear history, just like in traditional SVN workflows.


If local changes directly *conflict with upstream commits*, Git will pause the rebasing process and give you a chance to manually resolve the conflicts. The nice thing about Git is that it uses the same git status and git add commands for both generating commits and resolving merge conflicts. This makes it easy for new developers to manage their own merges. Plus, if they get themselves into trouble, Git makes it very easy to abort the entire rebase and try again (or go find help).


## Documentación
* https://git-scm.com/doc 
* Learn Git with Bitbucket Cloud

## Learn Git in your browser for free with Try Git. 
Consola Git de aprendizaje sobre browser

* <https://try.github.io/levels/1/challenges/1>
* <https://git-scm.com/about/>

## Ejemplo de creación de un repositorio en Bitbucket
Ejemplo: <https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud>

### Prerrequisitos

* Tener instalado GIT en el computador (<https://www.atlassian.com/git/tutorials/install-git>)

		MacBook-Pro-de-Cesar:~ cesarvillegascortes$ git --version
				
* Tener una cuenta BitBucket (<https://bitbucket.org/account/signup/>)


### Tareas
* Create a Git repository 
* Copy your Git repository and add files 
* Pull changes from your Git repository on Bitbucket Cloud 
* Use a Git branch to merge a file 

### ¿Por qué BitBucket?
* Flexible deployment models
	* Enjoy flexible deployment models for teams of all sizes and needs. Host it in our cloud or manage it on your servers.
* Unlimited private repositories
	* Get *unlimited private and public repositories* with Bitbucket. 
	* *Bitbucket Cloud is free for small teams of 5*.



* First, someone needs to create the **central repository** on a server.

![alt text](images/central_repository.svg "Clon")

* Everybody **clones the central repository**


![alt text](images/clon_central_repository.svg "Clon")

Next, each developer creates a local copy of the entire project. This is accomplished via the git clone command: (Directorio local repositorio: **path/to/repo.git**)

	git clone ssh://user@host/path/to/repo.git


When you clone a repository, Git automatically adds a shortcut called `origin` that points back to the `“parent”` repository, under the assumption that you'll want to interact with it further on down the road.

## GUI Clients

Git comes with built-in GUI tools for committing (git-gui) and browsing (gitk), but there are several third-party tools for users looking for platform-specific experience. 

* SourceTree (SourceTree is Atlassian's free desktop client for Bitbucket.)
* GitHub Desktop
* TortoiseGit
* ...



## Documentación
* <https://git-scm.com/doc>
* <https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf>
* <http://ndpsoftware.com/git-cheatsheet.html>
