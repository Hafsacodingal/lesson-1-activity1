import os

# Create two subject files
with open("math.txt", "w") as f:
    f.write("Math is easy.\nPractice daily.")

with open("science.txt", "w") as f:
    f.write("Science is fun.\nLearn experiments.")

# Count words
with open("math.txt", "r") as f:
    print("Math words:", len(f.read().split()))

with open("science.txt", "r") as f:
    print("Science words:", len(f.read().split()))

# Remove old merged file if it exists
if os.path.exists("study_notes.txt"):
    os.remove("study_notes.txt")

# Merge both files
with open("study_notes.txt", "w") as out:
    with open("math.txt", "r") as f:
        out.write(f.read())
    out.write("\n")
    with open("science.txt", "r") as f:
        out.write(f.read())

print("Files merged successfully!")