# from time import sleep
# from Clases.oxygenTherapy import OxygenTherapy
# from Clases.pacient import Pacient
# from Clases.clinicalJudgment import ClinicalJudgment
# from Clases.medic import Medic
# from Clases.urgency import Urgency
# from Clases.actuation import Actuation
# from Clases.analysis import Analysis
# from Clases.transfusion import Transfusion
# from Clases.medication import Medication
# from Clases.radiology import Radiology
# from Clases.immobilization import Immobilization
# from Clases.treatment import Treatment
# from Clases.cpr import Cpr
from Managers.urgencyManager import UrgencyManager
from Managers.pacientManager import PacientManager
# from Managers.clinicalJudgmentManager import ClinicalJudgmentManager
from Managers.analysisManager import AnalysisManager
from Managers.medicManager import MedicManager
# from Managers.analysisManager import AnalysisManager
# from Managers.immobilizationManager import ImmobilizationManager
# from Managers.medicationManager import MedicationManager
# from Managers.oxygenTherapyManager import OxygenTherapyManager
from Managers.radiologyManager import RadiologyManager
# from Managers.transfusionManager import TransfusionManager
# from Managers.treatmentManager import TreatmentManager
import sqlite3


# myConnection = sqlite3.connect('./Urgencias.db')
# owo = UrgencyManager(myConnection)
# ewe = owo.loadUrgencyByFile("./Ficheros/urgency.txt")
# for uwu in ewe:
#     print(uwu)

valor = int(input("Valor: "))
print(valor)