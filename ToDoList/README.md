# Creating an executable
`set-executionpolicy remotesigned -scope currentuser` if terminal launches with error

`pip install pyinstaller` third party used to create executable files

`py -m PyInstaller --onefile --windowed --clean apps/todoapp/gui.py` windows command to install executable

`streamlit run apps/todoapp-webapp/web.py` Run web app version of TODO