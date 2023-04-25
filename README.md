# Welcome to EClothes!
This is a Django and Vue.js based Full Stack App. It utilizes **Vue3, Vuex, VueRouter** on the Front End and **Django 4.1** 



## Installation and Set up

 ## First Clone the repo using the following, type in terminal.
 
	 git clone https://github.com/babaramdev-py/E-Commerce-Web-using-Django-and-VueJS.git
	 
## Activate Python Virtual Environment, all the dependencies of the project are already initialized over here.
 
	cd E-Commerce-Web-using-Django-and-VueJS
	
	source ProjEnv/bin/activate

## Run the following code in terminal to activate the BackEnd.

    python3 manage.py runserver (if using Linux)
    python manage.py runserver (if on MacOS)
    py manage.py runserver (if on Windows)
    
### Should output this to the terminal:
		

    Watching for file changes with StatReloader
    Performing system checks...
    System check identified no issues (0 silenced).
    //Date
    Django version 4.1.3, using settings 'EClothes_Django.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

## To run the front end code, type the following.

    cd eclothes_vue
    // make sure you have npm and node installed
	npm run serve
	
### It should output the following:

    > eclothes_vue@0.1.0 serve
    > vue-cli-service serve
    
     INFO  Starting development server...
    
    
     DONE  Compiled successfully in 6143ms       9:04:55 PM
    
    
      App running at:
      - Local:   http://localhost:8080/ 
      - Network: http://192.168.1.11:8080/
    
      Note that the development build is not optimized.
      To create a production build, run npm run build.
