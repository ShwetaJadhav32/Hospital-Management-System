# ==========================================
# DATABASE MODULE
# ==========================================
# Purpose:
# This module is responsible for connecting
# the Hospital Management System with MySQL.
#
# Responsibilities:
# 1. Connect to MySQL Database
# 2. Insert Patient Data
# 3. Update Patient Data
# 4. Delete Patient Data
# 5. Retrieve Patient Data
#
# Database credentials are loaded securely
# from the .env file using python-dotenv.
# ==========================================





import mysql.connector
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()


class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            self.cursor = self.conn.cursor(buffered=True)
                                                    ### A buffered cursor fetches the query results into memory, helping prevent this specific unread-result error when another query runs.
        except Exception as e:
            print('Error:', e)


    def addData(self,obj,table_name):
        if table_name != 'patient':
            return "Invalid table name."
        sql = f'insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        values = obj.toTuple()
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            return "Patient added successfully."

        except mysql.connector.IntegrityError:
            self.conn.rollback()
            return "Error: Patient ID already exists."

        except mysql.connector.Error as e:
            self.conn.rollback()
            return f"Database error: {e}"

    def showAllPatient(self, table_name):
        if table_name != 'patient':
            return []
        
        sql = f'select * from {table_name}'
        self.cursor.execute(sql)

        return self.cursor.fetchall()

    def getData(self, patient_id, table_name):
        sql = f'select * from {table_name} where patient_id = %s'
        self.cursor.execute(sql, (patient_id,))
        return self.cursor.fetchone()

    def updData(self, obj, table_name):
        if(table_name == 'patient'):

            sql = f'update {table_name} set patient_name = %s,age = %s, gender = %s, disease = %s, doctor = %s,status = %s, phone = %s, admission_date = %s where patient_id = %s'
            values = (obj.patient_name,obj.age, obj.gender, obj.disease, obj.doctor,obj.status,obj.phone, obj.admission_date,obj.patient_id)
        self.cursor.execute(sql, values)
        self.conn.commit()


        if self.cursor.rowcount == 0:
            return "No patient record updated. Check the patient ID."

        return "Patient data updated successfully."


    def deleteData(self, patient_id, table_name):
        if table_name != 'patient':
            return "Invalid table name."

        sql = "DELETE FROM patient WHERE patient_id = %s"

        try:
            self.cursor.execute(sql, (patient_id,))
            self.conn.commit()

            if self.cursor.rowcount > 0:
                return "Patient deleted successfully."
            else:
                return "Patient ID does not exist."

        except mysql.connector.Error as e:
            self.conn.rollback()
            return f"Database error: {e}"
    
if(__name__ == '__main__'):
    Database()
#     from patient import Patient




        