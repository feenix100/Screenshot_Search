# Screenshot Number Extractor

This Python script captures a screenshot of a specified browser window, extracts numbers between 4 and 6 digits from the screenshot, and writes these numbers to a text file.

## Features

- Captures the content of a specified browser window.
- Extracts text from the screenshot using OCR (Optical Character Recognition).
- Filters extracted text to include only numbers between 4 and 6 digits.
- Saves the filtered numbers to a text file.

## Prerequisites

Install the required packages using pip:
```bash
pip install pygetwindow pillow pytesseract opencv-python pywinauto pyautogui mss
```

Ensure Tesseract OCR is installed and its executable path is set correctly in the script.

## Installation

1. **Install Tesseract OCR**:
   - Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
   - Note the installation path (e.g., `C:\Program Files\Tesseract-OCR\tesseract.exe`).

2. **Set the Tesseract executable path**:
   Update the `tesseract_cmd` variable in the script with your Tesseract installation path.
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your path
   ```

## Usage

1. **Update the window title**:
   Set the `window_title` variable to the exact title of the browser window you want to capture.
   ```python
   window_title = "Part Request Lines To Ship"  # Update with the exact title
   ```

2. **Run the script**:
   Execute the script using Python.
   ```bash
   python find.py
   ```

## Script Overview

### Capture Window Content

The script captures the content of the specified window, scrolling to capture the full content if necessary.

### Extract Numbers from Image

Using Tesseract OCR, the script extracts text from the captured image.

### Filter Numbers

The script filters the extracted text to find numbers between 4 and 6 digits.

### Save Numbers to File

The filtered numbers are saved to a text file named `numbers.txt`.

---

Feel free to customize the script to better suit your needs. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.
