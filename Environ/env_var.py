# Environment variable

# Sometimes there is a need not to display your password in your projects
# Thats because maybe you weren't the only one have access to the code/program
# So instead of saving your code in example1

# Example 1
my_user = "username123"
my_pass = "pass123"

print(my_user)
print(my_pass)


# You do this to avoid the  mistake by Creating an Environment variable
"""
Make sure you are the admin of your computer, if not run as an administrator.
Goto your start button and search for control panel, click on system settings, select systems, by the left hand side, click on advanced systtem settings
under user variables for your user, click on new to add new variable(variable name and variable value).
Repeat the process adding that of the password variable

After that create a python file and write it this waay
"""
import os

my_user = os.environ.get("my_username")
my_pass = os.environ.get("my_password")

print(my_user)
print(my_pass)
