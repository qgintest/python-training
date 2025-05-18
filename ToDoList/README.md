# Creating an executable
`set-executionpolicy remotesigned -scope currentuser` if terminal launches with error

`pip install pyinstaller` third party used to create executable files

`py -m PyInstaller --onefile --windowed --clean apps/todoapp/gui.py` windows command to install executable

`streamlit run apps/todoapp-webapp/web.py` Run web app version of TODO

# Deploying web-app steps
1: Make sure Source code is on standalone project, no other files should exist that don't belong

2:`pip freeze > requirements.txt` a file uploaded to the server so it knows all the python libraries
that need to be installed to run web-app correctly

3: `streamlit run web.py`, click on Deploy button

# Deploying to Heroku
Note: Paid service but scalling is available if needed
Its a PaaS, others include; PythonAnywhere, Google App Engine, AWS), better options, focus on coding, less on resource management

Iaas options include; (Digital Ocean, AWS, Google Cloud), better pricing

Notes on web python web frameworks
1. Streamlit: good for small apps, no scalaing, free service
2. Flask: Medium size apps
3. Django: Large apps like news websites, e-learning platforms

Virtual env is good practice for each project but can eat up disk space.
alternative is to use gloabl python interpreter


# Industry standard for prototyping is figma
