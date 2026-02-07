# File Organiser

A simple yet powerful Python script that brings order to your chaos by organizing your **Downloads** folder (or any target directory) based on file extensions.

## 🚀 Features

Automatically sorts files into the following categories:
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`
- **Documents**: `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`
- **Videos**: `.mp4`, `.mov`, `.avi`, `.mkv`
- **Music**: `.mp3`, `.wav`, `.flac`
- **Archives**: `.zip`, `.rar`, `.7z`
- **Installers**: `.exe`, `.msi`

## 🛠️ Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/rakeshkumar272/file-organiser.git
    cd file-organiser
    ```

2.  **Run the script:**
    ```bash
    python file.py
    ```

The script will scan your `~/Downloads` folder and move files into subfolders named after their category (e.g., `Downloads/Images`, `Downloads/Documents`).

## ⚙️ Customization

You can easily add new file types or categories by editing the `file_types` dictionary in `file.py`:

```python
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    # Add your own:
    "Code": [".py", ".js", ".html", ".css"],
}
```

## 📋 Requirements

- Python 3.x
- No external dependencies required (uses standard `os` and `shutil` libraries).
