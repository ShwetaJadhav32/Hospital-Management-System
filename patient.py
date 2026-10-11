class Patient:
    def __init__(self,patient_id, patient_name, age, gender, disease, doctor, status, phone,admission_date):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.age = age
        self.gender = gender
        self.disease = disease
        self.doctor = doctor
        self.status = status
        self.phone = phone
        self.admission_date = admission_date

    def toTuple(self):
        return( self.patient_id,self.patient_name,self.age, self.gender, self.disease, self.doctor, self.status, self.phone, self.admission_date)


if(__name__ == '__main__'):
    Patient()


