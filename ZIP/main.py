import zipfile

zip_dina = zipfile.ZipFile("files.zip", "w")

zip_dina.write("image.png")
zip_dina.write("test.txt")
zip_dina.write("read.py")
zip_dina.close()

"""
You can do the same thing using context managers. by
"""
with zipfile.ZipFile("files.zip", "w") as zip_dina:
    zip_dina.write("image.png")
    zip_dina.write("test.txt")
    zip_dina.write("read.py")

"""
To extract the zip files, yoou can use do the following
"""

with zipfile.ZipFile("files.zip", "r") as zip_dina:
    zip_dina.extract("image.png")
    zip_dina.extract("test.txt")
    zip_dina.extract("read.py")
    # Or you can extract all at the same time
    zip_dina.extractall()
