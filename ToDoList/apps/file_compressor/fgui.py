
import FreeSimpleGUI as sg
import zip_creator as zc

selectFilelabel = sg.Text("Select Files to Compress")
input_box = sg.Input()
select_files_choose_button = sg.FilesBrowse("Choose", key="files")

selectDestlabel = sg.Text("Select Destination Folder")
input_box2 = sg.Input()
select_dest_folder_button = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output = sg.Text(key="Output", text_color="black")

window = sg.Window("File Compressor",
                   layout=[[selectFilelabel, input_box, select_files_choose_button],
                           [selectDestlabel, input_box2, select_dest_folder_button],
                           [compress_button, output]])

while True:
    event, values = window.read() # Displays the window
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    zc.make_archive(filepaths, folder)
    window["Output"].update(value="Compression Complete")

window.close()

