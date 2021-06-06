# File_Objects
# Reading another files within python
# We can achieve this using 2 methods

# Open_method [read file]
f = open("test.txt", "r")
print(f.read())
f.close()

# Open_method [write to a file]
f = open("test1.txt", "w")
f.write(
    "Thank You for the support.\n Cyberxploit Hausa"
)  # Try using print(f.name) to get file name
f.close()


# Context_manager [read file]
with open("test.txt", "r") as f:
    file_contents = f.read()
    print(file_contents)


# Context_manager [write to a file by creating a html file]
with open("test3.html", "w") as f:
    f.write(
        "<html>\n<head><title>Cyberxploit.com</title></head>\n<body>\n<p>This is a simple website</p>\n</body>\n</html>"
    )
