from database import Database
from patient import Patient
from prettytable import PrettyTable
class Admin:
    def __init__(self):
        self.db = Database()
        ch = 0
        while(ch != '6'):
            print("=" * 50)
            print(" ADMIN DASHBOARD".center(50))
            print("=" * 50)
            print('''Please Select Option:
            1. Add pateint
            2. View All Patients
            3. Search Patients
            4. Update Patients
            5. Delete Patients
            6. Logout
            ''')

            ch = input('Enter Choice:')
            if(ch == '1'):
                res = self.addPatient()
                print(res)
            elif(ch == '2'):
                res = self.showAllPatient()
                print(res)
            elif(ch == '3'):
                patient_id = input('Enter Patient_id: ')
                res = self.searchPatient(patient_id)
                print(res)
            elif(ch == '4'):
                res = self.updPatient()
                print(res) 
            elif(ch == '5'):
                res = self.delPatient()
                print(res)
            elif(ch == '6'):
                print("=" * 50)
                print('Logged Out...'.center(50))
                print('Thank you for Choosing us!'.center(50))
                print("=" * 50)
            else:
                print('Invalid Choice...')


    def addPatient(self):
        # print('Add Patient...')
        patient_id = int(input('Enter Patient Id: '))
        patient_name = input('Enter Patient Name: ')
        age = int(input('Enter Patient Age: '))
        gender = input('Enter gender: ')
        disease  = input('Enter Patient disease: ')
        doctor = input('Enter Patient Doctor: ')
        status = input('Enter Patient Status(Admitted, Discharged, Under Treatment): ')
        phone = input('Enter Phone No.: ')
        admission_date = input('Enter Admission Date (YYYY-MM-DD): ')


        patient = Patient(patient_id,patient_name,age, gender, disease, doctor,status,phone, admission_date)
        res = self.db.addData(patient,'patient')
        return res

    
    def showAllPatient(self):
        res = self.db.showAllPatient('patient')

        table = PrettyTable()
        table.field_names = [
            "Patient ID", "Name", "Age", "Gender", "Disease",
            "Doctor", "Status", "Phone", "Admission Date"
        ]

        if res:
            table.add_rows(res)
            return table
        else:
            return "No patient records found."
    def searchPatient(self, patient_id):
        res = self.db.getData(patient_id,'patient')
        if res:
            table = PrettyTable()
            table.field_names = [
                "Patient ID", "Name", "Age", "Gender", "Disease",
                "Doctor", "Status", "Phone", "Admission Date"
            ]

            table.add_row(res)
            return table

        else:
            return "Patient ID does not exist."

    def updPatient(self):
        patient_id = input('Enter Patient_id: ')
        res = self.db.getData(patient_id,'patient')
    

        if(res):
            print('NOTE: Leave field blank if you do not want to change...')
            patient_name = input(f'Enter Patient Name({res[1]}): ') or res[1]
            age_input = input(f'Enter Patient Age({res[2]}): ')
            age = int(age_input) if age_input.strip() else res[2]
            gender = input(f'Enter gender({res[3]}): ') or res[3]
            disease  = input(f'Enter Patient disease({res[4]}): ') or res[4]
            doctor = input(f'Enter Patient Doctor({res[5]}): ') or res[5]
            status = input(f'Enter Patient Status(Admitted, Discharged, Under Treatment)({res[6]}): ') or res[6]
            phone = input(f'Enter Phone No.({res[7]}): ') or res[7]
            admission_date = input(f'Enter Admission Date (YYYY-MM-DD)({res[8]}): ') or res[8]
            patient = Patient(patient_id,patient_name,age, gender, disease, doctor,status,phone, admission_date)
            res = self.db.updData(patient,'patient')
            return res
        else:
            return 'Patient ID does not exist.'


    def delPatient(self):
        patient_id = input("Enter Patient ID to delete: ")

            # Search for the patient first
        res = self.db.getData(patient_id, 'patient')

        if res:
                # Display patient details
            table = PrettyTable()
            table.field_names = [
                "Patient ID", "Name", "Age", "Gender", "Disease",
                "Doctor", "Status", "Phone", "Admission Date"
            ]
            table.add_row(res)

            print("\nPatient Details:")
            print(table)

            # Ask for confirmation
            confirm = input("Are you sure you want to delete this patient? (yes/no): ")

            if confirm.lower() == 'yes':
                result = self.db.deleteData(patient_id, 'patient')
                return result
            else:
                return "Delete operation cancelled."

        else:
            return "Patient ID does not exist."
            
# cursor = conn.cursor()
if(__name__ == '__main__'):
    Admin()