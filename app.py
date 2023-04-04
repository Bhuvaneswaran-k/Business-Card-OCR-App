import streamlit as st
import easyocr as ocr
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
import re

st.title("Welcome to EasyOCR bussiness card extraction")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
)

# Creating a cursor object
mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS OCRq')
mycursor.execute('USE OCRq')
mycursor.execute('CREATE TABLE IF NOT EXISTS business_cardsq (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),designation VARCHAR(255), company_name VARCHAR(255), email VARCHAR(255),phone VARCHAR(255), website VARCHAR(255), address VARCHAR(255), others VARCHAR(255))')


engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="",
                               db="OCRq"))


name_pattern = re.compile(r"([A-Z][a-z'-]+(?:\s+[A-Z][a-z'-]+)*)")
company_name_pattern = re.compile(r'\b\w+(?=\.com\b)')
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
website_pattern = re.compile(r'(http[s]?:\/\/)?(www\.)?[^\s(["<,>]*\.com[^\s[",><]*')
phone_pattern =re.compile(r'(\+?\d{1,3})?[-\.\s]?\d{3}[-\.\s]?\d{3,4}')
l=[]
name = ''
designation=''
company_name = ''
email = ''
phone=''
website = ''
address = ''
others=''

uploaded_file = st.file_uploader("Upload a business card image", type=["jpg", "jpeg", "png"])
if st.button("Extract Information"):
    if uploaded_file is not None:
        image = uploaded_file.read()
        reader = ocr.Reader(['en'])
        results = reader.readtext(image)
        st.write("Extracted Information:")

        for r in results:
            text = r[1]
            l.append(r[1])
            if email_pattern.search(text):
                email = email_pattern.search(text).group()
            elif website_pattern.search(text):
                website = website_pattern.search(text).group()
            elif re.search(r'^\d+[-\s]?\w*\s\w*\s\w*', text):
                address = text
            elif phone_pattern.search(text):
                phone=text
            else:
                others = text
        name=l[0]
        designation=l[1]
        match=re.search(company_name_pattern,website)
        company_name = match.group()

        insert_query = "INSERT INTO business_cardsq (name,designation, company_name, email,phone, website, address,others) VALUES (%s,%s, %s, %s,%s, %s, %s, %s)"
        mycursor.execute(insert_query, (name, designation, company_name, email,phone, website, address, others))
        mydb.commit()
        disply={"Name":name,"Designation":designation,"company name ":company_name,"Email ":email,"phone":phone,"Website":website,"Address":address,"others":others}
        df=pd.DataFrame([disply])
        st.table(df)

    else:
        st.warning("Please upload a business card image first!")