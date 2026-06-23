# Smart Notes Organizer

# Step 1: Create a sample notes file
file = open("notes.txt", "w")
file.write("Study Python\n")
file.write("Buy groceries\n")
file.write("Meeting at 5 PM\n")
file.write("Study for exam\n")
file.write("Call friend\n")
file.close()

# Step 2: Preview first 15 characters
file = open("notes.txt", "r")
print("Preview:")
print(file.read(15))
file.close()

# Step 3: Read all lines
file = open("notes.txt", "r")
lines = file.readlines()
file.close()

print("\nAll Notes:")
print(lines)

# Step 4: Read line by line
print("\nReading Line by Line:")
file = open("notes.txt", "r")
for line in file:
    print(line.strip())
file.close()

# Step 5: Copy only lines containing "Study"
file = open("notes.txt", "r")
newfile = open("study_notes.txt", "w")

for line in file:
    if "Study" in line:
        newfile.write(line)

file.close()
newfile.close()

print("\nStudy notes copied to study_notes.txt")