# 📝 Markdown to HTML Converter

This is a Python application that allows users to **convert Markdown (`.md`) files into HTML**. The tool can be run via a **console interface**, and optionally includes a **Tkinter GUI**, **SQLite** for storing history, and **logs/reports** using the `logging` and `pandas` modules.

---

## 🚀 Features

### 🔄 Markdown Conversion:
- Accepts `.md` files and converts them to `.html`
- Outputs clean, downloadable HTML files
- Preserves common Markdown syntax (headers, bold, italic, lists, etc.)

### 💬 User Interface:
- Console-based user prompts for file selection and output destination
- Optional GUI using `Tkinter` for selecting files via file dialog

### 🗃️ Optional Enhancements:
- Log conversions using the `logging` module
- Save file conversion history using **SQLite**
- Generate operation reports in tabular format using `pandas`

---

## 💻 Technologies Used

- **Python 3**
- `markdown`: For converting .md content to HTML
- `tkinter`: For file selection and optional GUI
- `sqlite3`: For saving history (optional)
- `pandas`: For reporting (optional)
- `logging`: For tracking operations and errors

---

## 📂 File Structure

📁 Markdown-to-HTML-Converter/
├── main.py # Console-based markdown to HTML converter
├── gui_app.py # GUI version using Tkinter (optional)
├── converter.py # Markdown conversion logic
├── database.py # SQLite interaction (optional)
├── reports/ # Folder to save conversion reports
├── logs/ # Folder for log files
│ └── app.log
├── example.md # Sample markdown file
├── README.md # Project documentation
└── requirements.txt # Required Python packages

yaml
Copy
Edit

---

## 🛠️ How to Run

### 🔹 Console Version:
```bash
python main.py
🔸 GUI Version:
bash
Copy
Edit
python gui_app.py
🧪 Example Usage (Console)
bash
Copy
Edit
Welcome to Markdown to HTML Converter!
Enter the path of your .md file: example.md
File converted successfully! Output saved to: example.html
📊 Optional Database Schema (SQLite)
sql
Copy
Edit
CREATE TABLE conversions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    input_file TEXT,
    output_file TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
📈 Future Improvements
Batch conversion (multiple Markdown files)

Live Markdown preview (in GUI)

Customize HTML output with CSS templates

Add support for uploading .md files via web interface

📄 License
This project is licensed under the MIT License.

✍️ Author
Aaquib Shaikh
GitHub: aaqibshaikh001

