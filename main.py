from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='frontend')

# Function to recursively read the directory structure
def read_dir_structure(directory):
    structure = []
    for entry in os.scandir(directory):
        if entry.is_dir():
            structure.append({
                "name": entry.name,
                "type": "directory",
                "children": read_dir_structure(entry.path)  # Recursively read directories
            })
        else:
            structure.append({
                "name": entry.name,
                "type": "file"
            })
    return structure

@app.route('/files')
def files():
    dir_path = '.'  # Using the current directory for demonstration; change as needed
    structure = read_dir_structure(dir_path)
    return jsonify(structure)

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
