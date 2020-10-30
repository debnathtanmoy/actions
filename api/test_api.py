import unittest
from patients import Patient
from patientrepository import patientrepositry
from bedsrepository import BedsRepositry


class Test(unittest.TestCase):
    def test_add_beds_repository(self):
        data = {"numberofbeds": "10"}
        numberofbeds = data["numberofbeds"]
        response = BedsRepositry.addBeds(numberofbeds)
        expected = "10 beds are added"
        self.assertEqual(response, expected)

    def test_patient_entry(self):
        data = {"name": "Suresh", "age": "70"}
        patientdetails = Patient(data['name'], data['age'])
        response = patientrepositry.addPatient(patientdetails)
        expected = "Bed number 1 is now occupied by Suresh"
        self.assertEqual(response, expected)

    def test_check_vitals(self):
        response = patientrepositry.patientCheckVitals()
        expected = ''
        self.assertEqual(response, expected)

    def test_discharge_patient(self):
        data = {"bedid": "1"}
        bedid = data["bedid"]
        response = patientrepositry.dischargePatient(bedid)
        # expected = "Patient Suresh is discharged"
        expectedd = ' '
        self.assertEqual(response, expectedd)


if __name__ == '__main__':
    unittest.main()
