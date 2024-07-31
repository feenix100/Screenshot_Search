import pywinauto
import mss
import pytesseract
import cv2
import numpy as np
from PIL import Image
import time
import re

#this script takes a screenshot of a browser window basewd on title, then it extracts numbers between 4 and 6 digits, then it writes the numbers to a text file

# pip install pygetwindow pillow pytesseract opencv-python pywinauto pyautogui mss


# Set the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Your\Path\To\Tesseract-OCR\tesseract.exe'  # Update with your path

def capture_window_content(window_title, output_filename):
    app = pywinauto.Application().connect(title_re=window_title)
    window = app.top_window()
    
    if not window:
        raise Exception(f"No window found with title: {window_title}")

    print(f"Found window: {window.window_text()}")

    # Bring the window to the foreground
    window.set_focus()

    # Allow some time for the window to come to the foreground
    time.sleep(2)

    # Capture the entire content of the window
    def capture_scrollable_window():
        with mss.mss() as sct:
            rect = window.rectangle()
            monitor = {
                "left": rect.left,
                "top": rect.top,
                "width": rect.width(),
                "height": rect.height()
            }

            # Get the window's scrollable area
            scroll_height = rect.height()
            y = rect.top
            screenshots = []

            while True:
                screenshot = sct.grab(monitor)
                screenshots.append(screenshot)
                
                # Scroll down
                window.send_keystrokes('{DOWN 10}')  # Scroll down by a small amount
                time.sleep(1)  # Allow some time for scrolling
                
                # Update the monitor rectangle
                monitor['top'] = y
                y += scroll_height

                # Break if the bottom of the scrollable area is reached
                if y >= rect.bottom:
                    break

            # Combine all screenshots into one
            combined_img = Image.new('RGB', (monitor['width'], y - rect.top))
            y_offset = 0
            for img in screenshots:
                img_pil = Image.frombytes('RGB', img.size, img.rgb)
                combined_img.paste(img_pil, (0, y_offset))
                y_offset += img.size[1]

            combined_img.save(output_filename)
            return output_filename

    return capture_scrollable_window()

def extract_numbers_from_image(image_path):
    # Open the image using PIL
    image = Image.open(image_path)
    
    # Convert the image to a numpy array
    img_np = np.array(image)
    
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(gray_img)
    
    return text

def filter_numbers(text):
    # Extract all numbers from the text and filter them based on length
    all_numbers = re.findall(r'\d+', text)
    filtered_numbers = [num for num in all_numbers if 4 <= len(num) <= 6]
    return filtered_numbers

def save_numbers_to_file(numbers, filename):
    with open(filename, 'w') as file:
        file.write(','.join(numbers))

def main():
    window_title = "Part Request Lines To Ship"  # Update with the exact title
    output_filename = 'full_window_screenshot.png'
    
    try:
        # Capture the screenshot of the entire window content
        screenshot_path = capture_window_content(window_title, output_filename)
        
        # Extract text from the screenshot
        text = extract_numbers_from_image(screenshot_path)
        
        # Filter numbers to include only those between 4 and 6 digits
        filtered_numbers = filter_numbers(text)
        
        # Save the filtered numbers to a text file
        save_numbers_to_file(filtered_numbers, 'numbers.txt')
        print("Filtered numbers extracted and saved to numbers.txt")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
