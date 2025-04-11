
import FreeSimpleGUI as sg

selectFilelabel = sg.Text("Select Files to Compress")
input_box = sg.Input()
select_files_choose_button = sg.FileBrowse("Choose")

selectDestlabel = sg.Text("Select Destination Folder")
input_box2 = sg.Input()
select_dest_folder_button = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout=[[selectFilelabel, input_box, select_files_choose_button],
                           [selectDestlabel, input_box2, select_dest_folder_button],
                           [compress_button]])
window.read() # Displays the window
window.close()

