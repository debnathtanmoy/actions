from beds import Beds
from bedsrepository import BedsRepositry
from random import randint


class patientrepositry:
    PatientList = []
    messageForAddingPatient = " "
    message = ""
    messagev = ""

    def addPatient(patient):
        bedID = BedsRepositry.checkVacantBed()
        if bedID == -1:
            messageForAddingPatient = " No Vacant Bed "
        else:
            messageForAddingPatient = "Bed number " + bedID + " is now occupied by " + patient.name
            patient.bedid = bedID
            patientrepositry.PatientList.append(patient)
        return messageForAddingPatient

    def checkSPO(spo2):
        spo2value = int(spo2)
        if spo2value > 95:
            return True
        elif spo2value < 95:
            patientrepositry.messagev = patientrepositry.messagev + " Low SPO2 level"
            return False

    def checkheartbeat(heartbeat):
        heartbeatvalue = int(heartbeat)
        if heartbeatvalue > 100:
            patientrepositry.messagev = patientrepositry.messagev + " High heart beat "
            return False
        elif heartbeatvalue < 60:
            patientrepositry.messagev = patientrepositry.messagev + " Low heart beat "
            return False
        else:
            return True

    def checkBP(bloodpressure):
        bloodpressurevalue = int(bloodpressure)
        if bloodpressurevalue < 80:
            patientrepositry.messagev = patientrepositry.messagev + " Low blood pressure "
            return False
        elif bloodpressurevalue > 120:
            patientrepositry.messagev = patientrepositry.messagev + " High blood pressure "
            return False
        else:
            return True

    def patientstatus(patient):
        patient.heartbeat = str(randint(50, 110))
        patient.bp = str(randint(60, 130))
        patient.spo2 = str(randint(80, 100))

        if patientrepositry.checkheartbeat(patient.heartbeat) & patientrepositry.checkBP(patient.bp) & patientrepositry.checkSPO(patient.spo2):
            patientrepositry.message = patientrepositry.message + " Patient is OK on bed number " + patient.bedid
        else:
            patientrepositry.message = patientrepositry.message + " Check patient on bed number " + patient.bedid + " for following issues" + patientrepositry.messagev + '\n'

    def patientCheckVitals():
        patientrepositry.message = ""
        for patient in patientrepositry.PatientList:
            patientrepositry.messagev = ""
            if patient.bedid != "null":
                patientrepositry.patientstatus(patient)
            else:
                patientrepositry.message = patientrepositry.message + "Patient is not present in ICU"
        return patientrepositry.message

    def resetPatientVitals(id):
        messageReset = "BedId not found"
        for patient in patientrepositry.PatientList:
            if patient.bedid == id:
                patient.spo2 = "null"
                patient.bp = "null"
                patient.heartbeat = "null"
                messageReset = "Patient's Vitals Reset"
                break
        return messageReset

    def dischargePatient(id):
        messageDischargePatient = " "
        for patient in patientrepositry.PatientList:
            if patient.bedid == id:
                patient.bedid = "null"
                patient.spo2 = "null"
                patient.bp = "null"
                patient.heartbeat = "null"
                messageDischargePatient = "Patient " + patient.name + " is discharged"
                BedsRepositry.emptyBed(id)
                break
            else:
                messageDischargePatient = "Bed is not occupied by patient or Bed id does not exist"

        return messageDischargePatient
