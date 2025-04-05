filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for filename in filenames:
    filename = filename.replace('.txt', '')
    print(filename.title())
