
import FreeSimpleGUI as sg
import extract_function as ac

# sg.theme("Black")

selectArchivelabel = sg.Text("Select Archive")
input_box = sg.Input()
select_archive_choose_button = sg.FileBrowse("Choose", key="archive")

selectDestlabel = sg.Text("Select Dest Dir")
input_box2 = sg.Input()
select_dest_folder_button = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output = sg.Text(key="Output", text_color="black")

window = sg.Window("Archive Extractor",
                   layout=[[selectArchivelabel, input_box, select_archive_choose_button],
                           [selectDestlabel, input_box2, select_dest_folder_button],
                           [extract_button, output]])

while True:
    event, values = window.read() # Displays the window
    print(event, values)
    archiveFile = values["archive"]
    folder = values["folder"]
    ac.extract(archiveFile, folder)
    window["Output"].update(value="Extraction Complete")

window.close()

