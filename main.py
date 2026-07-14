""" Write a python progran to build a Smart Notes Organizer using Python file handling. They will create a sample notes file, 
preview file content using read(n),read all lines using readlines(), loop through a file line by line, filter lines with 
conditions, and copy selected lines into a new file. """

print("Smart Note Organizer")
print("=========================")

sampleNotes = [
    "IMPORTANT: Always close files after use\n",
    "TODO: Practice reading text files\n",
    "NOTE: read() reads the entire file\n",
    "IMPORTANT: Handle FileNotFoundError using try-except\n",
    "SKIP: Temporary debug statements\n",
    "NOTE: readline() reads one line at a time\n",
    "TODO: Practice writing to files using write()\n",
    "NOTE: append mode ('a') adds content without deleting existing data\n",
    "IMPORTANT: Use with open() for automatic file closing\n",
    "TODO: Create a simple notes management program\n"
]

file = open("class-notes.txt", "w")
file.writelines(sampleNotes)
file.close()

print("class-notes.txt created")
print()

print("Preview Notes (line(n))")
file = open("class-notes.txt", "r")
p = file.read(30)

print("First 30 Characters")
print(p)
print()

print("Read all lines")
file = open("class-notes.txt", "r")
l = file.readlines()
file.close()

print(f"Total line in file: {len(l)}")

for i in range(len(l)):
    print(i + 1, "=> ", l[i].strip())
print()

print("Loop through file line by line")
file = open("class-notes.txt", "r")

for l in file:
    print("Reading: ", l.strip())
file.close()
print()

print("Filter lines w/ Conditions")
file = open("class-notes.txt", "r")

for l in file:
    if l.startswith("SKIP"):
        print(f"Skipped: {l.strip()}")
    else:
        print(f"Kept: {l.strip()}")
file.close()
print()

print("Copy selected lines to new file")
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()

outputFile = open("organized-notes.txt", "w")

for l in lines:
    if l.startswith("IMPORTANT") or l.startswith("TODO"):
        outputFile.write(l)

outputFile.close()
print("Selected lines copied to organized-notes.txt")
print()

print("Organized File:")
file = open("organized-notes.txt", "r")

for l in file:
    print(l.strip())

file.close()