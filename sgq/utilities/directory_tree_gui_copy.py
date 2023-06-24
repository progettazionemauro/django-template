import tkinter as tk
import os

def generate_tree():
    directory = entry.get().strip()
    excludes = exclude_entry.get().strip().split(",")  # Splitting exclude directories
    text.delete(1.0, tk.END)  # Clear the text widget

    text.insert(tk.END, f"Directory: {directory}\n\n")
    generate_subtree(directory, excludes, "")

def generate_subtree(directory, excludes, indent):
    for root, dirs, files in os.walk(directory):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if d not in excludes]

        # Print current directory
        text.insert(tk.END, f"{indent}└── {os.path.basename(root)}\n")

        # Print files in current directory
        for file in files:
            text.insert(tk.END, f"{indent}    ├── {file}\n")

        # Recursively generate subtree for subdirectories
        for subdir in dirs:
            generate_subtree(os.path.join(root, subdir), excludes, indent + "    ")

def regenerate_code(directory):
    code = f"""
import tkinter as tk
import os

def generate_tree():
    directory = entry.get().strip()
    excludes = exclude_entry.get().strip().split(",")
    text.delete(1.0, tk.END)
    text.insert(tk.END, f"Directory: {directory}\\n\\n")
    generate_subtree(directory, excludes, "")

def generate_subtree(directory, excludes, indent):
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in excludes]
        text.insert(tk.END, f"{indent}└── {os.path.basename(root)}\\n")
        for file in files:
            text.insert(tk.END, f"{indent}    ├── {file}\\n")
        for subdir in dirs:
            generate_subtree(os.path.join(root, subdir), excludes, indent + "    ")

root = tk.Tk()
root.title("Directory Tree Generator")

label = tk.Label(root, text="Enter a directory path:")
label.pack()

entry = tk.Entry(root)
entry.pack()

exclude_label = tk.Label(root, text="Enter directories to exclude (separated by comma):")
exclude_label.pack()

exclude_entry = tk.Entry(root)
exclude_entry.pack()

button = tk.Button(root, text="Generate Tree", command=generate_tree)
button.pack()

text = tk.Text(root)
text.pack()

regenerate_button = tk.Button(root, text="Regenerate Code", command=lambda: regenerate_code(entry.get().strip()))
regenerate_button.pack()

code_text = tk.Text(root)
code_text.pack()

root.mainloop()
"""

    # Delete existing code in the text widget
    code_text.delete(1.0, tk.END)
    # Insert regenerated code
    code_text.insert(tk.END, code)

root = tk.Tk()
root.title("Directory Tree Generator")

label = tk.Label(root, text="Enter a directory path:")
label.pack()

entry = tk.Entry(root)
entry.pack()

exclude_label = tk.Label(root, text="Enter directories to exclude (separated by comma):")
exclude_label.pack()

exclude_entry = tk.Entry(root)
exclude_entry.pack()

button = tk.Button(root, text="Generate Tree", command=generate_tree)
button.pack()

text = tk.Text(root)
text.pack()

regenerate_button = tk.Button(root, text="Regenerate Code", command=lambda: regenerate_code(entry.get().strip()))
regenerate_button.pack()

