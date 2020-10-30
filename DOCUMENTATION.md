# Alert To Care

**This project implements a service that receives measurements from devices that monitor patients.
It includes patient data, name, age, spo2, BloodPressure and HeartBeat and their bed ID.**

## Segment 1: API
API is executed by running api.py file.
It includes the following method:
Method | Route | Function
------------ | ------------- | -------------
POST | /addBeds | Adding the no of beds
POST | /patient | Adding the name and age of Patient 
GET | /alertonpatientstatus | Retrieves the vitals status of a patient
POST | /resetPatientStatus | Resets Patient's Vitals Status
POST | /dischargePatient | Discharges patient and maked the bed vacant


## Segment 2: GUI
The User Interface follows this lineup order.

GUI incorporates a main menu which consists of the followings options:
Menu Option | Path
------------ | -------------
Home | /home
Patient Data | /patientdata  
Discharge Patient | /dischargepatient
Alert Status | /alertstatus
Reset Alert | /resetalert

**Home page is also the welcome screen & consists of buttons with direct access links to:**
   1. Bed Configuration
       -> Route: /configuration
   1. Patient
       -> Route: /patient
