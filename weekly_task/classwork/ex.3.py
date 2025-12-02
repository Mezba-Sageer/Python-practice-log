#  Question 3: Identify Hidden and Visible Files
# A file is considered Hidden if its name starts with a dot (.). Otherwise, it is Visible. Print each file name and its type.
# Example Input:
# files = [".env", "main.py", ".gitignore", "README.md", "config.json", ".dockerfile"]
# Expected Output:
# .env - Hidden
# main.py - Visible
# .gitignore - Hidden
# README.md - Visible
# config.json - Visible
# .dockerfile - Hidden

files = [".env", "main.py", ".gitignore", "README.md", "config.json", ".dockerfile"]
for i in files:
    if i.startswith("."):
        print(i,"-","Hidden")
    else:
        print(i,"-","Visible")
