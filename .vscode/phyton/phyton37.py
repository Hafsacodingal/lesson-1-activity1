content = ""
with open("Science_Notes.txt", "r") as f:
    content += "--- Science_Notes.txt ---\n"
    content += f.read() + "\n"
with open("Word Count.txt", "r") as f:
    content += "--- Word Count.txt ---\n"
    content += f.read() + "\n"
with open("all-notes.txt", "w") as out:
    out.write(content)
print("Saved to all-notes.txt")
print()

