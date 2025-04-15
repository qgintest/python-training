import zipfile
import pathlib


def extract(archive, destination):
    dest_path = pathlib.Path(destination)
    with zipfile.ZipFile(archive, 'r') as archive:
        archive.extractall(destination)

if __name__ == "__main__":
    extract(archive="archive//compressed.zip", destination="files//")
