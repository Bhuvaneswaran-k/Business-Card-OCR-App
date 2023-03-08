# Business-Card-OCR-App
## Introduction:   
This is a simple Streamlit application that allows users to upload an image of a business card and extract its information using easyOCR. The extracted information is then displayed in a clean and organized manner, and can be stored in a SQLite database.

## Requirements:  

Python 3.6+    
Streamlit    
easyOCR   
SQLite    

## Installation:   

1. Install Python from the official website (https://www.python.org/downloads/).
2. Install Streamlit using pip: pip install streamlit.
3. Install easyOCR using pip: pip install easyocr.
4. Install SQLite using the package manager of your operating system or from the official website (https://www.sqlite.org/download.html).

## Usage:

1. Clone this repository or download the source code.
2. Open a terminal or command prompt and navigate to the directory containing the source code.
3. Run the Streamlit application using the command: streamlit run app.py.
4. The application will open in your default web browser.
5. Click on the "Upload Image" button and select an image of a business card.
6. Click on the "Extract Information" button to extract the information from the uploaded image.
7. The extracted information will be displayed in a table below the "Extract Information" button.
8. The extracted information can be stored in a SQLite database by clicking on the "Save Information" button.

## Database:
The application uses a SQLite database to store the extracted information. The database is created automatically when the application is first run. The database file is named "business_cards.db" and is located in the same directory as the application. The database contains a single table named "business_cards" with the following columns:

id (integer, primary key)   
name (text)      
email (text)   
phone (text)   
company (text)   

## Improvements:

1. Improve the OCR accuracy by using a different OCR engine or training the easyOCR model on business card images.
2. Add support for other image formats such as PDF and TIFF.
3. Add support for batch processing of multiple business card images.
4. Improve the user interface by adding more widgets such as checkboxes, dropdowns, and sliders.
5. Add user authentication and authorization to make the application more secure.

## License:
This application is licensed under the MIT License. See the LICENSE file for more information.


