import mysql.connector


from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# sql = 'create database hospital_db'
# sql = 'drop database HMS' 
sql = 'create table patient(patient_id int,patient_name varchar(100),age int, gender varchar(10),disease varchar(100), doctor varchar(100),status varchar(30),phone varchar(10),admission_date date)'
cursor = conn.cursor()
cursor.execute(sql)
print('Query executed successfully.')