import os
import sys
sys.path.append(os.path.abspath('..'))

from Managers.analysisManager import AnalysisManager
from Managers.cprManager import CprManager
from Managers.immobilizationManager import ImmobilizationManager
from Managers.medicationManager import MedicationManager
from Managers.oxygenTherapyManager import OxygenTherapyManager
from Managers.radiologyManager import RadiologyManager
from Managers.transfusionManager import TransfusionManager
from Managers.treatmentManager import TreatmentManager

from Colecciones.actuationsColection import ActuationsColection
from Colecciones.urgencyColection import UrgencyColection

from Errores.notbooleanerror import NotBooleanError
import syntaxes

import sqlite3

myConnection = sqlite3.connect('./Urgencias.db')


# Constantes de parámetros para métodos de análisis

SHOW_ALL_ANALYSIS = '-showAllAnalysis'
SEARCH_ANALYSIS_BY_SEVERAL_URGENCY = '-searchAnalysisBySeveralUrgency'
SEARCH_ANALYSIS_BY_URGENCY = '-searchAnalysisByUrgency'
SEARCH_ANALYSIS_BY_PETITION = '-searchAnalysisByPetition'
SEARCH_ANALYSIS_ABOVE_HEMOGLOBINE = '-searchAnalysisAboveHemoglobine'
SEARCH_ANALYSIS_BELOW_HEMOGLOBINE = '-searchAnalysisBelowHemoglobine'
SEARCH_ANALYSIS_EQUAL_HEMOGLOBINE = '-searchAnalysisEqualHemoglobine'
SEARCH_ANALYSIS_ABOVE_OXYGEN = '-searchAnalysisAboveOxygen'
SEARCH_ANALYSIS_BELOW_OXYGEN = '-searchAnalysisBelowOxygen'
SEARCH_ANALYSIS_EQUAL_OXYGEN = '-searchAnalysisEqualOxygen'
ADD_ANALYSIS = '-addAnalysis'
UPDATE_ANALYSIS = '-updateAnalysis'
DELETE_ANALYSIS = '-deleteAnalysis'


# Constantes de parámetros para métodos de cpr

SHOW_ALL_CPR = '-showAllCPR'
SEARCH_CPR_BY_SEVERAL_URGENCY = '-searchCPRBySeveralUrgency'
SEARCH_CRP_BY_URGENCY = '-searchCPRByUrgency'
SEARCH_CRP_BY_TYPE = '-searchCPRByType'
ADD_CPR = '-addCPR'
UPDATE_CPR = '-updateCPR'
DELETE_CPR = '-deleteCPR'

# Constantes de parámetros para métodos de inmobilizaciones

SHOW_ALL_IMMOBILIZATION = '-showAllImmobilizations'
SEARCH_IMMOBILIZATION_BY_SEVERAL_URGENCY = '-searchImmobilizationBySeveralUrgency'
SEARCH_IMMOBILIZATION_BY_URGENCY = '-searchImmobilizationsByUrgency'
SEARCH_IMMOBILIZATION_BY_TYPE = '-searchImmobilizationsByType'
SEARCH_IMMOBILIZATION_BY_PLACE = '-searchImmobilizationsByPlace'
ADD_IMMOBILIZATION = '-addImmobilization'
UPDATE_IMMOBILIZATION = '-updateImmobilization'
DELETE_IMMOBILIZATION = '-deleteImmobilization'

# Constantes de parámetros para métodos de medicaciones

SHOW_ALL_MEDICATION = '-showAllMedications'
SEARCH_MEDICATION_BY_SEVERAL_URGENCY = '-searchMedicationBySeveralUrgency'
SEARCH_MEDICATION_BY_URGENCY = '-searchMedicationByUrgency'
SEARCH_MEDICATION_BY_NAME = '-searchMedicationsByName'
SEARCH_MEDICATION_BY_DOSAGE = '-searchMedicationsByDosage'
ADD_MEDICATION = '-addMedication'
UPDATE_MEDICATION = '-updateMedication'
DELETE_MEDICATION = '-deleteMedication'

# Constantes de parámetros para métodos de oxigenoterapias
SHOW_ALL_OXYGEN_THERAPY = '-showAllOxygenTherapy'
SEARCH_OXYGEN_THERAPY_BY_SEVERAL_URGENCY = '-searchOxygenTherapyBySeveralUrgency'
SEARCH_OXYGEN_THERAPY_BY_URGENCY = '-searchOxygenTherapyByUrgency'
SEARCH_OXYGEN_THERAPY_BY_THERAPY = '-searchOxygenTherapyByTherapy'
ADD_OXYGEN_THERAPY = '-addOxygenTherapy'
UPDATE_OXYGEN_THERAPY = '-updateOxygenTherapy'
DELETE_OXYGEN_THERAPY = '-deleteOxygenTherapy'

# Constantes de parámetros para métodos de radiología

SHOW_ALL_RADIOLOGY = '-showAllRadiology'
SEARCH_RADIOLOGY_BY_SEVERAL_URGENCY = '-searchRadiologyBySeveralUrgency'
SEARCH_RADIOLOGY_BY_URGENCY = '-searchRadiologyByUrgency'
SEARCH_RADIOLOGY_BY_PETITION = '-searchRadiologyByPetition'
SEARCH_RADIOLOGY_BY_PREGNANCY = '-searchRadiologyByPregnancy'
SEARCH_RADIOLOGY_BY_CONTRAST = '-searchRadiologyByContrast'
SEARCH_RADIOLOGY_BY_CONSENT = '-searchRadiologyByConsent'
ADD_RADIOLOGY = '-addRadiology'
UPDATE_RADIOLOGY = '-updateRadiology'
DELETE_RADIOLOGY = '-deleteRadiology'

# Constantes de parámetros para métodos de transfusiones

SHOW_ALL_TRANSFUSION = '-showAllTransfusions'
SEARCH_TRANSFUSION_BY_SEVERAL_URGENCY = '-searchTransfusionBySeveralUrgency'
SEARCH_TRANSFUSION_BY_URGENCY = '-searchTransfusionByUrgency'
SEARCH_TRANSFUSION_BY_PETITION = '-searchTransfusionByPetition'
SEARCH_TRANSFUSION_BY_BLOOD_GROUP = '-searchTransfusionByBloodGroup'
SEARCH_TRANSFUSION_BY_IRH = '-searchTransfusionByIRH'
SEARCH_TRANSFUSION_BY_PREVIOUS_TRANSFUSION = '-searchTransfusionByPreviousTransfusion'
SEARCH_TRANSFUSION_BY_RELIGION = '-searchTransfusionByReligion'
SEARCH_TRANSFUSION_BY_CONSENT = '-searchTransfusionByConsent'
ADD_TRANSFUSION = '-addTransfusion'
UPDATE_TRANSFUSION = '-updateTransfusion'
DELETE_TRANSFUSION = '-deleteTransfusion'

# Constantes de parámetros para métodos de tratamientos

SHOW_ALL_TREATMENTS = '-showAllTreatments'
SEARCH_TREATMENT_BY_SEVERAL_URGENCY = '-searchTreatmentBySeveralUrgency'
SEARCH_TREATMENT_BY_URGENCY = '-searchTreatmentByUrgency'
SEARCH_TREATMENT_BY_TYPE = '-searchTreatmentByType'
SEARCH_TREATMENT_BY_ANTITETANUS = '-searchTreatmentByAntitetanus'
SEARCH_TREATMENT_BY_ANESTHESIA = '-searchTreatmentByAnesthesia'
ADD_TREATMENT = '-addTreatment'
UPDATE_TREATMENT = '-updateTreatment'
DELETE_TREATMENT = '-deleteTreatment'

DELETE_ALL_ACTUATIONS_BY_URGENCY = '-deleteAllByUrgency'


MIN_HEMOGLOBINE_VALUE = 6
MIN_OXYGEN_VALUE = 60


managerAnalysis = AnalysisManager(myConnection)
managerCPR = CprManager(myConnection)
managerImmobilization = ImmobilizationManager(myConnection)
managerMedication = MedicationManager(myConnection)
managerOxygenTherapy = OxygenTherapyManager(myConnection)
managerRadiology = RadiologyManager(myConnection)
managerTransfusion = TransfusionManager(myConnection)
managerTreatment = TreatmentManager(myConnection)
colectionActuations = ActuationsColection()
colectionUrgency = UrgencyColection()

if(len(sys.argv) > 3):
    syntaxes.show_actuation_syntax()
else:
    try:
        user_option = sys.argv[1]
        if user_option == SHOW_ALL_ANALYSIS:
            print("\nMostrando analísis...")
            all_analysis = managerAnalysis.getAllAnalysis()
            for analysis in all_analysis:
                print(analysis)

        elif user_option == SEARCH_ANALYSIS_BY_SEVERAL_URGENCY:
            user_value = sys.argv[2]
            splitted_value = user_value.split(",")
            value_tuple = tuple(splitted_value)
            print("\nMostrando análisis...")
            urgency_analysis = managerAnalysis.getAnalysisByUrgencies(
                *value_tuple)
            for episode in urgency_analysis:
                print(episode)

        elif user_option == SEARCH_ANALYSIS_BY_URGENCY:
            user_value = sys.argv[2]
            print("\nMostrando análisis...")
            urgency_analysis = managerAnalysis.getAnalysisByUrgency(user_value)
            for analysis in urgency_analysis:
                print(analysis)

        elif user_option == SEARCH_ANALYSIS_BY_PETITION:
            user_value = sys.argv[2]
            print("\nMostrando análisis...")
            petition_analysis = managerAnalysis.getAnalysisByPetition(
                user_value)
            for analysis in petition_analysis:
                print(analysis)

        elif user_option == SEARCH_ANALYSIS_ABOVE_HEMOGLOBINE:
            user_value = sys.argv[2]
            print("\nMostrando análisis...")
            above_hemoglobine_analysis = managerAnalysis.getAnalysisAboveHemoglobineLevel(
                user_value)
            for analysis in above_hemoglobine_analysis:
                print(analysis)

        elif user_option == SEARCH_ANALYSIS_BELOW_HEMOGLOBINE:
            user_value = sys.argv[2]
            print("\nMostrando análisis...")
            below_hemoglobine_analysis = managerAnalysis.getAnalysisBelowHemoglobineLevel(
                user_value)
            for analysis in below_hemoglobine_analysis:
                print(analysis)

        elif user_option == SEARCH_ANALYSIS_EQUAL_HEMOGLOBINE:
            user_value = sys.argv[2]
            print("\nMostrando análisis...")
            equal_hemoglobine_analysis = managerAnalysis.getAnalysisEqualHemoglobineLevel(
                user_value)
            for analysis in equal_hemoglobine_analysis:
                print(analysis)

        elif user_option == SEARCH_ANALYSIS_ABOVE_OXYGEN:
            user_value = sys.argv[2]
            print("\nMostrando análisis...")
            above_oxygen_analysis = managerAnalysis.getAnalysisAboveOxygen(
                user_value)
            for analysis in above_oxygen_analysis:
                print(analysis)

        elif user_option == SEARCH_ANALYSIS_BELOW_OXYGEN:
            user_value = sys.argv[2]
            print("\nMostrando análisis...")
            below_oxygen_analysis = managerAnalysis.getAnalysisBelowOxygen(
                user_value)
            for analysis in below_oxygen_analysis:
                print(analysis)

        elif user_option == SEARCH_ANALYSIS_EQUAL_OXYGEN:
            user_value = sys.argv[2]
            print("\nMostrando análisis...")
            equal_oxygen_analysis = managerAnalysis.getAnalysisEqualOxygen(
                user_value)
            for analysis in equal_oxygen_analysis:
                print(analysis)


# -----------------------------------------------------------------------------------------------------------------------------

        elif user_option == SHOW_ALL_CPR:
            print("\nMostrando reanimaciones...")
            all_cpr = managerCPR.getAllCpr()
            for cpr in all_cpr:
                print(cpr)

        elif user_option == SEARCH_CPR_BY_SEVERAL_URGENCY:
            user_value = sys.argv[2]
            splitted_value = user_value.split(",")
            value_tuple = tuple(splitted_value)
            print("\nMostrando reanimaciones...")
            urgency_cpr = managerCPR.getCprByUrgencies(*value_tuple)
            for episode in urgency_cpr:
                print(episode)

        elif user_option == SEARCH_CRP_BY_URGENCY:
            user_value = sys.argv[2]
            print("\nMostrando reanimaciones...")
            urgency_cpr = managerCPR.getCprByUrgency(user_value)
            for cpr in urgency_cpr:
                print(cpr)

        elif user_option == SEARCH_CRP_BY_TYPE:
            user_value = sys.argv[2]
            print("\nMostrando reanimaciones...")
            type_cpr = managerCPR.getCprByType(user_value)
            for cpr in type_cpr:
                print(cpr)


# -----------------------------------------------------------------------------------------------------------------------------

        elif user_option == SHOW_ALL_IMMOBILIZATION:
            print("\nMostrando inmobilizaciones...")
            all_immobilization = managerImmobilization.getAllImmobilization()
            for immobilization in all_immobilization:
                print(immobilization)

        elif user_option == SEARCH_IMMOBILIZATION_BY_SEVERAL_URGENCY:
            user_value = sys.argv[2]
            splitted_value = user_value.split(",")
            value_tuple = tuple(splitted_value)
            print("\nMostrando reanimaciones...")
            urgency_immobilization = managerImmobilization.getImmobilizationByUrgencies(
                *value_tuple)
            for episode in urgency_immobilization:
                print(episode)

        elif user_option == SEARCH_IMMOBILIZATION_BY_URGENCY:
            user_value = sys.argv[2]
            print("\nMostrando inmobilizaciones...")
            urgency_immobilization = managerImmobilization.getImmobilizationByUrgency(
                user_value)
            for immobilization in urgency_immobilization:
                print(immobilization)

        elif user_option == SEARCH_IMMOBILIZATION_BY_TYPE:
            user_value = sys.argv[2]
            print("\nMostrando inmobilizaciones...")
            type_immobilization = managerImmobilization.getImmobilizationByType(
                user_value)
            for immobilization in type_immobilization:
                print(immobilization)

        elif user_option == SEARCH_IMMOBILIZATION_BY_PLACE:
            user_value = sys.argv[2]
            print("\nMostrando inmobilizaciones...")
            place_immobilization = managerImmobilization.getImmobilizationByPlace(
                user_value)
            for immobilization in place_immobilization:
                print(immobilization)


# -----------------------------------------------------------------------------------------------------------------------------

        elif user_option == SHOW_ALL_MEDICATION:
            print("\nMostrando medicaciones...")
            all_medication = managerMedication.getAllMedication()
            for medication in all_medication:
                print(medication)

        elif user_option == SEARCH_MEDICATION_BY_SEVERAL_URGENCY:
            user_value = sys.argv[2]
            splitted_value = user_value.split(",")
            value_tuple = tuple(splitted_value)
            print("\nMostrando medicaciones...")
            urgency_medication = managerMedication.getMedicationByUrgencies(
                *value_tuple)
            for episode in urgency_medication:
                print(episode)

        elif user_option == SEARCH_MEDICATION_BY_URGENCY:
            user_value = sys.argv[2]
            print("\nMostrando medicaciones...")
            urgency_medication = managerMedication.getMedicationByUrgency(
                user_value)
            for medication in urgency_medication:
                print(medication)

        elif user_option == SEARCH_MEDICATION_BY_NAME:
            user_value = sys.argv[2]
            print("\nMostrando medicaciones...")
            name_medication = managerMedication.getMedicationByName(user_value)
            for medication in name_medication:
                print(medication)

        elif user_option == SEARCH_MEDICATION_BY_DOSAGE:
            user_value = sys.argv[2]
            print("\nMostrando medicaciones...")
            dosage_medication = managerMedication.getMedicationByDosage(
                user_value)
            for medication in dosage_medication:
                print(medication)


# -----------------------------------------------------------------------------------------------------------------------------

        elif user_option == SHOW_ALL_OXYGEN_THERAPY:
            print("\nMostrando oxigenoterapias...")
            all_oxygen_therapy = managerOxygenTherapy.getAllOxygenTherapy()
            for oxygen_therapy in all_oxygen_therapy:
                print(oxygen_therapy)

        elif user_option == SEARCH_OXYGEN_THERAPY_BY_SEVERAL_URGENCY:
            user_value = sys.argv[2]
            splitted_value = user_value.split(",")
            value_tuple = tuple(splitted_value)
            print("\nMostrando oxigenoterapias...")
            urgency_oxygen_therapy = managerOxygenTherapy.getOxygenTherapyByUrgencies(
                *value_tuple)
            for episode in urgency_oxygen_therapy:
                print(episode)

        elif user_option == SEARCH_OXYGEN_THERAPY_BY_URGENCY:
            user_value = sys.argv[2]
            print("\nMostrando oxigenoterapias...")
            urgency_oxygen_therapy = managerOxygenTherapy.getOxygenTherapyByUrgency(
                user_value)
            for oxygen_therapy in urgency_oxygen_therapy:
                print(oxygen_therapy)

        elif user_option == SEARCH_OXYGEN_THERAPY_BY_THERAPY:
            user_value = sys.argv[2]
            print("\nMostrando oxigenoterapias...")
            therapy_oxygen_therapy = managerOxygenTherapy.getOxygenTherapyByTherapy(
                user_value)
            for oxygen_therapy in therapy_oxygen_therapy:
                print(oxygen_therapy)


# -----------------------------------------------------------------------------------------------------------------------------

        elif user_option == SHOW_ALL_RADIOLOGY:
            print("\nMostrando radiologías...")
            all_radiology = managerRadiology.getAllRadiology()
            for radiology in all_radiology:
                print(radiology)

        elif user_option == SEARCH_RADIOLOGY_BY_SEVERAL_URGENCY:
            user_value = sys.argv[2]
            splitted_value = user_value.split(",")
            value_tuple = tuple(splitted_value)
            print("\nMostrando radiologías...")
            urgency_radiology = managerRadiology.getRadiologyByUrgencies(
                *value_tuple)
            for episode in urgency_radiology:
                print(episode)

        elif user_option == SEARCH_RADIOLOGY_BY_URGENCY:
            user_value = sys.argv[2]
            print("\nMostrando radiologías...")
            urgency_radiology = managerRadiology.getRadiologyByUrgency(
                user_value)
            for radiology in urgency_radiology:
                print(radiology)

        elif user_option == SEARCH_RADIOLOGY_BY_PETITION:
            user_value = sys.argv[2]
            print("\nMostrando radiologías...")
            petition_radiology = managerRadiology.getRadiologyByPetition(
                user_value)
            for radiology in petition_radiology:
                print(radiology)

        elif user_option == SEARCH_RADIOLOGY_BY_PREGNANCY:
            user_value = sys.argv[2]
            print("\nMostrando radiologías...")
            pregnancy_radiology = managerRadiology.getRadiologyByPregnancy(
                user_value)
            for radiology in pregnancy_radiology:
                print(radiology)

        elif user_option == SEARCH_RADIOLOGY_BY_CONTRAST:
            user_value = sys.argv[2]
            print("\nMostrando radiologías...")
            constrast_radiology = managerRadiology.getRadiologyByConstrast(
                user_value)
            for radiology in constrast_radiology:
                print(radiology)

        elif user_option == SEARCH_RADIOLOGY_BY_CONSENT:
            user_value = sys.argv[2]
            print("\nMostrando radiologías...")
            consent_radiology = managerRadiology.getRadiologyByInformedConsent(
                user_value)
            for radiology in consent_radiology:
                print(radiology)


# -----------------------------------------------------------------------------------------------------------------------------

        elif user_option == SHOW_ALL_TRANSFUSION:
            print("\nMostrando transfusiones...")
            all_transfusion = managerTransfusion.getAllTransfusion()
            for transfusion in all_transfusion:
                print(transfusion)

        elif user_option == SEARCH_TRANSFUSION_BY_SEVERAL_URGENCY:
            user_value = sys.argv[2]
            splitted_value = user_value.split(",")
            value_tuple = tuple(splitted_value)
            print("\nMostrando transfusiones...")
            urgency_transfusion = managerTransfusion.getTransfusionByUrgencies(
                *value_tuple)
            for episode in urgency_transfusion:
                print(episode)

        elif user_option == SEARCH_TRANSFUSION_BY_URGENCY:
            user_value = sys.argv[2]
            print("\nMostrando transfusiones...")
            urgency_transfusion = managerTransfusion.getTransfusionByUrgency(
                user_value)
            for transfusion in urgency_transfusion:
                print(transfusion)

        elif user_option == SEARCH_TRANSFUSION_BY_PETITION:
            user_value = sys.argv[2]
            print("\nMostrando transfusiones...")
            petition_transfusion = managerTransfusion.getTransfusionByPetition(
                user_value)
            for transfusion in petition_transfusion:
                print(transfusion)

        elif user_option == SEARCH_TRANSFUSION_BY_BLOOD_GROUP:
            user_value = sys.argv[2]
            print("\nMostrando transfusiones...")
            blood_group_transfusion = managerTransfusion.getTransfusionByBloodGroup(
                user_value)
            for transfusion in blood_group_transfusion:
                print(transfusion)

        elif user_option == SEARCH_TRANSFUSION_BY_IRH:
            user_value = sys.argv[2]
            print("\nMostrando transfusiones...")
            irh_transfusion = managerTransfusion.getTransfusionByIRH(
                user_value)
            for transfusion in irh_transfusion:
                print(transfusion)

        elif user_option == SEARCH_TRANSFUSION_BY_PREVIOUS_TRANSFUSION:
            user_value = sys.argv[2]
            print("\nMostrando transfusiones...")
            previous_transfusion = managerTransfusion.getTransfusionByPreviousTransfusion(
                user_value)
            for transfusion in previous_transfusion:
                print(transfusion)

        elif user_option == SEARCH_TRANSFUSION_BY_RELIGION:
            user_value = sys.argv[2]
            print("\nMostrando transfusiones...")
            religion_transfusion = managerTransfusion.getTransfusionByReligion(
                user_value)
            for transfusion in religion_transfusion:
                print(transfusion)

        elif user_option == SEARCH_TRANSFUSION_BY_CONSENT:
            user_value = sys.argv[2]
            print("\nMostrando transfusiones...")
            consent_transfusion = managerTransfusion.getTransfusionByInformedConsent(
                user_value)
            for transfusion in consent_transfusion:
                print(transfusion)

# -----------------------------------------------------------------------------------------------------------------------------

        elif user_option == SHOW_ALL_TREATMENTS:
            print("\nMostrando tratamientos...")
            all_treatments = managerTreatment.getAllTreatment()
            for treatment in all_treatments:
                print(treatment)

        elif user_option == SEARCH_TREATMENT_BY_SEVERAL_URGENCY:
            user_value = sys.argv[2]
            splitted_value = user_value.split(",")
            value_tuple = tuple(splitted_value)
            print("\nMostrando tratamientos...")
            urgency_treatments = managerTreatment.getTreatmentByUrgencies(
                *value_tuple)
            for episode in urgency_treatments:
                print(episode)

        elif user_option == SEARCH_TREATMENT_BY_URGENCY:
            user_value = sys.argv[2]
            print("\nMostrando tratamientos...")
            urgency_treatments = managerTreatment.getTreatmentByUrgency(
                user_value)
            for treatment in urgency_treatments:
                print(treatment)

        elif user_option == SEARCH_TREATMENT_BY_TYPE:
            user_value = sys.argv[2]
            print("\nMostrando tratamientos...")
            type_treatments = managerTreatment.getTreatmentByType(user_value)
            for treatment in type_treatments:
                print(treatment)

        elif user_option == SEARCH_TREATMENT_BY_ANTITETANUS:
            user_value = sys.argv[2]
            print("\nMostrando tratamientos...")
            antitetanus_treatments = managerTreatment.getTreatmentByAntitetanus(
                user_value)
            for treatment in antitetanus_treatments:
                print(treatment)

        elif user_option == SEARCH_TREATMENT_BY_ANESTHESIA:
            user_value = sys.argv[2]
            print("\nMostrando tratamientos...")
            anesthesia_treatments = managerTreatment.getTreatmentByAnesthesia(
                user_value)
            for treatment in anesthesia_treatments:
                print(treatment)

        # -----------------------------------------------------------------------------------------------------------------------------

        elif user_option == ADD_ANALYSIS:
            print("Introduzca los datos de la analítica: \n")
            try:
                urgency_option = int(input('\nUrgencia: '))
            except ValueError:
                print("\nEl valor debe ser numérico")

                quit()
            created_urgency_analysis = colectionUrgency.newUrgency(
                myConnection, None, urgency_option)
            try:
                petition_option = int(input('\nPetición: '))
            except ValueError:
                print("\nEl valor debe ser numérico")

                quit()
            if petition_option == '':
                petition_option = None
            try:
                hemoglobine_option = int(
                    input('\nNivel de hemoglobina en sangre: '))
            except ValueError:
                print("\nEl valor debe ser numérico")

                quit()
            if hemoglobine_option == '':
                hemoglobine_option = None
            try:
                oxygen_option = int(input('\nNivel de oxígeno en sangre: '))
            except ValueError:
                print("\nEl valor debe ser numérico")

                quit()
            if oxygen_option == '':
                oxygen_option = None
            created_analysis = colectionActuations.newAnalysis(
                myConnection,
                created_urgency_analysis,
                petition_option,
                hemoglobine_option,
                oxygen_option
            )
            created_analysis.save()
            print("\nAnálisis añadida correctamente")

            if created_analysis.getHemoglobine() < MIN_HEMOGLOBINE_VALUE:
                print("-----------------------------------------------")
                print(
                    "El paciente tiene un nivel demasiado bajo de hemoglobina en sangre")
                print("Se necesita realizarle una transfusión")
                print("-----------------------------------------------")
                print("\nIntroduzca los datos de la transfusión: \n")
                try:
                    petition_option = int(input('\nPetición: '))
                except ValueError:
                    print("\nEl valor debe ser numérico")

                if petition_option == '':
                    petition_option = None
                blood_group_option = input('\nGrupo sanguíneo: ')
                if blood_group_option == '':
                    blood_group_option = None
                irh_option = input('\nIRH: ')
                if irh_option == '':
                    irh_option = None
                try:
                    previous_transfusion_option = int(input(
                        '\nTransfusiones previas (0 - No / 1 - Sí): '))
                except ValueError:
                    print("\nEl valor debe de ser numérico")
                    quit()
                if previous_transfusion_option == '':
                    previous_transfusion_option = None

                elif previous_transfusion_option != 0 and previous_transfusion_option != 1:
                    raise NotBooleanError(previous_transfusion_option)
                religion_option = input('\nReligión: ')
                if religion_option == '':
                    religion_option = None
                try:
                    consent_option = int(
                        input('\nConsentimiento Informado (0 - No / 1- Sí): '))
                except ValueError:
                    print("\nEl valor debe de ser numérico")
                    quit()

                if consent_option == '':
                    consent_option = None

                elif consent_option != 1 and consent_option != 0:
                    raise NotBooleanError(consent_option)

                created_transfusion = colectionActuations.newTransfusion(
                    myConnection,
                    created_urgency_analysis,
                    petition_option,
                    blood_group_option,
                    irh_option,
                    previous_transfusion_option,
                    religion_option,
                    consent_option
                )
                if created_transfusion.getReligion() == 'Testigo de Jehová':
                    print("\n-----------------------------------------------")
                    print("Los testigos de jehová no pueden transferirse sangre")
                    print("Contacte con el juez de guardia")
                    print("-----------------------------------------------\n")
                    quit()
                else:
                    created_transfusion.save()
                    print("\nTranfusión añadida correctamente")

            if created_analysis.getOxygen() < MIN_OXYGEN_VALUE:
                print("-----------------------------------------------")
                print("El paciente tiene un nivel demasiado bajo de oxígeno en sangre")
                print("Se necesita realizarle una oxigenoterapia")
                print("-----------------------------------------------")
                print("\nIntroduzca los datos de la oxigenoterapia: \n")
                therapy_option = input('\nTerapia: ')
                if therapy_option == '':
                    therapy_option = None

                created_oxygen_therapy = colectionActuations.newOxygenTherapy(
                    myConnection,
                    created_urgency_analysis,
                    therapy_option
                )
                created_oxygen_therapy.save()
                print("\nOxigenoterapia añadida correctamente")

        elif user_option == ADD_CPR:
            print("Introduzca los datos de la reanimación: \n")
            try:
                urgency_option = int(input('\nUrgencia: '))
            except ValueError:
                print("\nEl valor debe ser numérico")

            created_urgency_cpr = colectionUrgency.newUrgency(
                myConnection, None, urgency_option)
            type_option = input('\nTipo: ')
            if type_option == '':
                type_option = None
            created_cpr = colectionActuations.newCpr(
                myConnection,
                created_urgency_cpr,
                type_option
            )
            created_cpr.save()
            print("\nReanimación añadida correctamente")

        elif user_option == ADD_IMMOBILIZATION:
            print("Introduzca los datos de la inmobilización: \n")
            try:
                urgency_option = int(input('\nUrgencia: '))
            except ValueError:
                print("\nEl valor debe ser numérico")

                quit()
            created_urgency_immobilization = colectionUrgency.newUrgency(
                myConnection, None, urgency_option)
            type_option = input('\nTipo: ')
            if type_option == '':
                type_option = None
            place_option = input('\nLugar: ')
            if place_option == '':
                place_option = None

            created_immobilization = colectionActuations.newImmobilization(
                myConnection,
                created_urgency_immobilization,
                type_option,
                place_option
            )
            created_immobilization.save()
            print("\nInmobilización añadida correctamente")

        elif user_option == ADD_MEDICATION:
            print("Introduzca los datos de la medicación: \n")
            try:
                urgency_option = int(input('\nUrgencia: '))
            except ValueError:
                print("\nEl valor debe ser numérico")

                quit()
            created_urgency_medication = colectionUrgency.newUrgency(
                myConnection, None, urgency_option)
            name_option = input('\nNombre: ')
            if name_option == '':
                name_option = None
            dosage_option = input('\nDosis: ')
            if dosage_option == '':
                dosage_option = None

            created_medication = colectionActuations.newMedication(
                myConnection,
                created_urgency_medication,
                name_option,
                dosage_option
            )
            created_medication.save()
            print("\nMedicación añadida correctamente")

        elif user_option == ADD_OXYGEN_THERAPY:
            print("Introduzca los datos de la oxigenoterapia: \n")
            try:
                urgency_option = int(input('\nUrgencia: '))
            except ValueError:
                print("\nEl valor debe ser numérico")

                quit()
            created_urgency_oxygen_therapy = colectionUrgency.newUrgency(
                myConnection, None, urgency_option)
            therapy_option = input('\nTerapia: ')
            if therapy_option == '':
                therapy_option = None

            created_oxygen_therapy = colectionActuations.newOxygenTherapy(
                myConnection,
                created_urgency_oxygen_therapy,
                therapy_option
            )
            created_oxygen_therapy.save()
            print("\nOxigenoterapia añadida correctamente")

        elif user_option == ADD_RADIOLOGY:
            print("Introduzca los datos de la radiología: \n")
            try:
                urgency_option = int(input('\nUrgencia: '))
            except ValueError:
                print("\nEl valor debe ser numérico")

                quit()
            created_urgency_radiology = colectionUrgency.newUrgency(
                myConnection, None, urgency_option)

            try:
                petition_option = int(input('\nPetición: '))
            except ValueError:
                print("\nEl valor debe ser numérico")

                quit()

            try:
                pregnancy_option = int(
                    input('\nEmbarazada (0 - No / 1- Sí): '))
            except ValueError:
                print("\nEl valor debe de ser numérico")
                quit()

            if pregnancy_option == '':
                pregnancy_option = None

            elif pregnancy_option != 1 and pregnancy_option != 0:
                raise NotBooleanError(pregnancy_option)

            try:
                contrast_option = int(
                    input('\nUso de constraste (0 - No / 1- Sí): '))
            except ValueError:
                print("\nEl valor debe de ser numérico")
                quit()

            if contrast_option == '':
                contrast_option = None

            elif contrast_option != 1 and contrast_option != 0:
                raise NotBooleanError(consent_option)

            try:
                consent_option = int(
                    input('\nConsentimiento Informado (0 - No / 1- Sí): '))
            except ValueError:
                print("\nEl valor debe de ser numérico")
                quit()

            if consent_option == '':
                consent_option = None

            elif consent_option != 1 and consent_option != 0:
                raise NotBooleanError(consent_option)

            created_radiology = colectionActuations.newRadiology(
                myConnection,
                created_urgency_radiology,
                petition_option,
                pregnancy_option,
                contrast_option,
                consent_option
            )
            created_radiology.save()
            print("\nRadiología añadida correctamente")

        elif user_option == ADD_TRANSFUSION:
            print("Introduzca los datos de la transfusión: \n")
            try:
                urgency_option = int(input('\nUrgencia: '))
            except ValueError:
                print("\nEl valor debe ser numérico")

                quit()
            created_urgency_transfusion = colectionUrgency.newUrgency(
                myConnection, None, urgency_option)
            try:
                petition_option = int(input('\nPetición: '))
            except ValueError:
                print("\nEl valor debe ser numérico")

                quit()
            blood_group_option = input('\nGrupo sanguíneo: ')
            if blood_group_option == '':
                blood_group_option = None
            irh_option = input('\nIRH: ')
            if irh_option == '':
                irh_option = None
            try:
                previous_transfusion_option = input(
                    '\nTransfusiones previas (0 - No / 1 - Sí): ')
            except ValueError:
                print("\nEl valor debe de ser numérico")
                quit()

            if previous_transfusion_option == '':
                previous_transfusion_option = None

            elif previous_transfusion_option != 1 and previous_transfusion_option != 0:
                raise NotBooleanError(previous_transfusion_option)

            religion_option = input('\nReligión: ')
            if religion_option == '':
                religion_option = None
            try:
                consent_option = int(
                    input('\nConsentimiento Informado (0 - No / 1- Sí): '))
            except ValueError:
                print("\nEl valor debe de ser numérico")
                quit()

            if consent_option == '':
                consent_option = None

            elif consent_option != 1 and consent_option != 0:
                raise NotBooleanError(consent_option)

            created_transfusion = colectionActuations.newTransfusion(
                myConnection,
                created_urgency_transfusion,
                petition_option,
                blood_group_option,
                irh_option,
                previous_transfusion_option,
                religion_option,
                consent_option
            )

            if created_transfusion.getReligion() == 'Testigo de Jehová':
                print("\n-----------------------------------------------")
                print("Los testigos de jehová no pueden transferirse sangre")
                print("Contacte con el juez de guardia")
                print("-----------------------------------------------\n")
                quit()
            else:
                created_transfusion.save()
                print("\nTranfusión añadida correctamente")

        elif user_option == ADD_TREATMENT:
            print("Introduzca los datos del tratamiento: \n")
            try:
                urgency_option = int(input('\nUrgencia: '))
            except ValueError:
                print("\nEl valor debe ser numérico")

                quit()
            created_urgency_treatment = colectionUrgency.newUrgency(
                myConnection, None, urgency_option)
            type_option = input('\nTipo: ')
            if type_option == '':
                type_option = None
            try:
                antitetanus_option = int(
                    input('\nVacuna contra el tétanos (0 - No / 1- Sí): '))
            except ValueError:
                print("\nEl valor debe de ser numérico")
                quit()

            if antitetanus_option == '':
                antitetanus_option = None

            elif antitetanus_option != 0 and antitetanus_option != 1:
                raise NotBooleanError(antitetanus_option)

            try:
                anesthesia_option = int(
                    input('\nAnestesia utilizada (0 - No / 1- Sí): '))
            except ValueError:
                print("\nEl valor debe de ser numérico")
                quit()

            if anesthesia_option == '':
                anesthesia_option = None

            elif antitetanus_option != 0 and antitetanus_option != 1:
                raise NotBooleanError(antitetanus_option)

            created_oxygen_therapy = colectionActuations.newTreatment(
                myConnection,
                created_urgency_treatment,
                type_option,
                antitetanus_option,
                anesthesia_option
            )
            created_oxygen_therapy.save()
            print("\nTratamiento añadida correctamente")

# -----------------------------------------------------------------------------------------------------------------------------

        elif user_option == DELETE_ANALYSIS:
            user_value = int(sys.argv[2])
            created_urgency_analysis = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_analysis = colectionActuations.newAnalysis(
                myConnection, created_urgency_analysis, None)
            user_validation = input(
                "\n¿Está seguro de que desea borrar el análisis? (S/N): ")
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando análisis...\n")
                created_analysis.delete()
                print("Análisis eliminado")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")

        elif user_option == DELETE_CPR:
            user_value = int(sys.argv[2])
            created_urgency_cpr = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_cpr = colectionActuations.newCpr(
                myConnection, created_urgency_cpr)
            user_validation = input(
                "\n¿Está seguro de que desea borrar la reanimación? (S/N): ")
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando reanimación...\n")
                created_cpr.delete()
                print("Reanimación eliminada")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")

        elif user_option == DELETE_IMMOBILIZATION:
            user_value = int(sys.argv[2])
            created_urgency_immobilization = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_immobilization = colectionActuations.newImmobilization(
                myConnection, created_urgency_immobilization)
            user_validation = input(
                "\n¿Está seguro de que desea borrar la inmobilización? (S/N): ")
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando inmobilización...\n")
                created_immobilization.delete()
                print("Inmobilización eliminada")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")

        elif user_option == DELETE_MEDICATION:
            user_value = int(sys.argv[2])
            created_urgency_medication = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_immobilization = colectionActuations.newMedication(
                myConnection, created_urgency_medication)
            user_validation = input(
                "\n¿Está seguro de que desea borrar la medicación? (S/N): ")
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando medicación...\n")
                created_medication.delete()
                print("Medicación eliminada")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")

        elif user_option == DELETE_OXYGEN_THERAPY:
            user_value = int(sys.argv[2])
            created_urgency_oxygen_therapy = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_immobilization = colectionActuations.newOxygenTherapy(
                myConnection, created_urgency_oxygen_therapy)
            user_validation = input(
                "\n¿Está seguro de que desea borrar la oxigenoterapia? (S/N): ")
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando oxigenoterapia...\n")
                created_oxygen_therapy.delete()
                print("Oxigenoterapia eliminada")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")

        elif user_option == DELETE_RADIOLOGY:
            user_value = int(sys.argv[2])
            created_urgency_radiology = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_radiology = colectionActuations.newRadiology(
                myConnection, created_urgency_radiology, None)
            user_validation = input(
                "\n¿Está seguro de que desea borrar la radiología? (S/N): ")
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando radiología...\n")
                created_radiology.delete()
                print("\nRadiología eliminada")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")

        elif user_option == DELETE_TRANSFUSION:
            user_value = int(sys.argv[2])
            created_urgency_transfusion = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_transfusion = colectionActuations.newTransfusion(
                myConnection, created_urgency_radiology, None)
            user_validation = input(
                "\n¿Está seguro de que desea borrar la transfusión? (S/N): ")
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando transfusión...\n")
                created_transfusion.delete()
                print("\nTransfusión eliminada")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")

        elif user_option == DELETE_TREATMENT:
            user_value = int(sys.argv[2])
            created_urgency_treatment = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_treatment = colectionActuations.newTreatment(
                myConnection, created_urgency_radiology)
            user_validation = input(
                "\n¿Está seguro de que desea borrar el tratamiento? (S/N): ")
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando tratamiento...\n")
                created_treatment.delete()
                print("Tratamiento eliminada")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")
# -----------------------------------------------------------------------------------------------------------------------------
        elif user_option == UPDATE_ANALYSIS:
            user_value = int(sys.argv[2])
            created_urgency_analysis = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_analysis = colectionActuations.newAnalysis(
                myConnection, created_urgency_analysis, None)

            print("\nPor favor, indique los nuevos valores del análisis: \n")

            try:
                petition_option = int(input('\nPetición: '))
            except ValueError:
                print("\nEl valor debe ser numérico")
            created_analysis.setPetition(petition_option)

            try:
                hemoglobine_option = int(
                    input('\nNivel de hemoglobina en sangre: '))
            except ValueError:
                print("\nEl valor debe ser numérico")
            if hemoglobine_option == '':
                hemoglobine_option = None
            created_analysis.setHemoglobine(hemoglobine_option)


            try:
                oxygen_option = int(input('\nNivel de oxígeno en sangre: '))
            except ValueError:
                print("\nEl valor debe ser numérico")
                quit()
            if oxygen_option == '':
                oxygen_option = None
            created_analysis.setOxygen(oxygen_option)

            created_analysis.update()
            print("\nAnálisis actualizado")

            if created_analysis.getHemoglobine() < MIN_HEMOGLOBINE_VALUE:
                print("-----------------------------------------------")
                print(
                    "El paciente tiene un nivel demasiado bajo de hemoglobina en sangre")
                print("Se necesita realizarle una transfusión")
                print("-----------------------------------------------")
                print("\nIntroduzca los datos de la transfusión: \n")
                try:
                    petition_option = int(input('\nPetición: '))
                except ValueError:
                    print("\nEl valor debe ser numérico")
                    quit()
                blood_group_option = input('\nGrupo sanguíneo: ')
                if blood_group_option == '':
                    blood_group_option = None
                irh_option = input('\nIRH: ')
                if irh_option == '':
                    irh_option = None
                try:
                    previous_transfusion_option = int(input(
                        '\nTransfusiones previas (0 - No / 1 - Sí): '))
                except ValueError:
                    print("\nEl valor debe de ser numérico")
                    quit()

                if previous_transfusion_option == '':
                    previous_transfusion_option = None

                if previous_transfusion_option != 0 and previous_transfusion_option != 0:
                    raise NotBooleanError(previous_transfusion_option)

                religion_option = input('\nReligión: ')
                if religion_option == '':
                    religion_option = None
                try:
                    consent_option = int(
                        input('\nConsentimiento Informado (0 - No / 1- Sí): '))
                    if consent_option == '':
                        consent_option = None
                except ValueError:
                    print("\nEl valor debe de ser numérico")
                    quit()

                if consent_option != 0 and consent_option != 0:
                    raise NotBooleanError(consent_option)

                created_transfusion = colectionActuations.newTransfusion(
                    myConnection,
                    created_urgency_analysis,
                    petition_option,
                    blood_group_option,
                    irh_option,
                    previous_transfusion_option,
                    religion_option,
                    consent_option
                )
                if created_transfusion.getReligion() == 'Testigo de Jehová':
                    print("\n-----------------------------------------------")
                    print("Los testigos de jehová no pueden transferirse sangre")
                    print("Contacte con el juez de guardia")
                    print("-----------------------------------------------\n")
                    quit()
                else:
                    created_transfusion.save()
                    print("\nTranfusión añadida correctamente")

            if int(created_analysis.getOxygen()) < MIN_OXYGEN_VALUE:
                print("-----------------------------------------------")
                print("El paciente tiene un nivel demasiado bajo de oxígeno en sangre")
                print("Se necesita realizarle una oxigenoterapia")
                print("-----------------------------------------------")
                print("\nIntroduzca los datos de la oxigenoterapia: \n")
                therapy_option = input('\nTerapia: ')
                if therapy_option == '':
                    therapy_option = None

                created_oxygen_therapy = colectionActuations.newOxygenTherapy(
                    myConnection,
                    created_urgency_analysis,
                    therapy_option
                )
                created_oxygen_therapy.save()
                print("\nOxigenoterapia añadida correctamente")

        elif user_option == UPDATE_CPR:
            user_value = int(sys.argv[2])
            created_urgency_cpr = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_cpr = colectionActuations.newCpr(
                myConnection, created_urgency_cpr)

            print("\nPor favor, indique los nuevos valores de la reanimación: \n")

            type_option = input('\nTipo: ')
            if type_option == '':
                type_option = None
            created_cpr.setType(type_option)

            created_cpr.update()
            print("\nReanimación actualizada")

        elif user_option == UPDATE_IMMOBILIZATION:
            user_value = int(sys.argv[2])
            created_urgency_immobilization = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_immobilization = colectionActuations.newImmobilization(
                myConnection, created_urgency_immobilization)

            print("\nPor favor, indique los nuevos valores de la inmovilización: \n")

            type_option = input('\nTipo: ')
            if type_option == '':
                type_option = None
            created_immobilization.setType(type_option)

            place_option = input('\nLugar: ')
            if place_option == '':
                place_option = None
            created_immobilization.setPlace(place_option)

            created_immobilization.update()
            print("\nInmovilización actualizada")

        elif user_option == UPDATE_MEDICATION:
            user_value = int(sys.argv[2])
            created_urgency_medication = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_immobilization = colectionActuations.newMedication(
                myConnection, created_urgency_medication)

            print("\nPor favor, indique los nuevos valores de la medicación: \n")

            name_option = input('\nNombre: ')
            if name_option == '':
                name_option = None
            created_medication.setName(name_option)

            dosage_option = input('\nDosis: ')
            if dosage_option == '':
                dosage_option = None
            created_medication.setDosage(dosage_option)

            created_medication.update()
            print("\nMedicación actualizada")

        elif user_option == UPDATE_OXYGEN_THERAPY:
            user_value = int(sys.argv[2])
            created_urgency_oxygen_therapy = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_immobilization = colectionActuations.newOxygenTherapy(
                myConnection, created_urgency_oxygen_therapy)

            print("\nPor favor, indique los nuevos valores de la oxigenoterapia: \n")

            therapy_option = input('\nTerapia: ')
            if therapy_option == '':
                therapy_option = None
            created_oxygen_therapy.setTherapy(therapy_option)

            created_oxygen_therapy.update()
            print("\nOxigenoterapia actualizada")

        elif user_option == UPDATE_RADIOLOGY:
            user_value = int(sys.argv[2])
            created_urgency_radiology = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_radiology = colectionActuations.newRadiology(
                myConnection, created_urgency_radiology, None)

            print("\nPor favor, indique los nuevos valores de la radiología: \n")

            petition_option = int(input('\nPetición: '))
            created_radiology.setPetition(petition_option)

            pregnancy_option = input('\nEmbarazada (0 - No / 1 - Sí): ')
            if pregnancy_option == '':
                pregnancy_option = None
            created_radiology.setPregnancy(pregnancy_option)

            contrast_option = input('\nContraste (0 - No / 1 - Sí): ')
            if contrast_option == '':
                contrast_option = None
            created_radiology.setContrast(contrast_option)

            consent_option = input(
                '\nConsentimiento informado (0 - No / 1 - Sí): ')
            if consent_option == '':
                consent_option = None
            created_radiology.setConsent(consent_option)

            created_radiology.update()
            print("\nRadiología actualizada")

        elif user_option == UPDATE_TRANSFUSION:
            user_value = int(sys.argv[2])
            created_urgency_transfusion = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_transfusion = colectionActuations.newTransfusion(
                myConnection, created_urgency_radiology, None)

            print("\nPor favor, indique los nuevos valores de la transfusión: \n")

            petition_option = int(input('\nPetición: '))
            created_transfusion.setPetition(petition_option)

            blood_group_option = input('\nGrupo Sanguíneo: ')
            if blood_group_option == '':
                blood_group_option = None
            created_transfusion.setBloodGroup(blood_group_option)

            irh_option = input('\nIRH: ')
            if irh_option == '':
                irh_option = None
            created_transfusion.setIRH(irh_option)

            previous_transfusion_option = input(
                '\nTransfusiones previas (0 - No / 1 - Sí): ')
            if previous_transfusion_option == '':
                previous_transfusion_option = None
            created_transfusion.setPreviousTransfusion(
                previous_transfusion_option)

            religion_option = input('\nReligión: ')
            if religion_option == '':
                religion_option = None
            created_transfusion.setReligion(religion_option)

            consent_option = input(
                '\nConsentimiento Informado (0 - No / 1 - Sí): ')
            if consent_option == '':
                consent_option = None
            created_transfusion.setConsent(consent_option)

            if created_transfusion.getReligion() == 'Testigo de Jehová':
                print("-----------------------------------------------")
                print("Los testigos de jehová no pueden transferirse sangre")
                print("Contacte con el juez de guardia")
                print("-----------------------------------------------")
                quit()
            else:
                created_transfusion.update()
                print("\nTransfusión actualizada")

        elif user_option == UPDATE_TREATMENT:
            user_value = int(sys.argv[2])
            created_urgency_treatment = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            created_treatment = colectionActuations.newTreatment(
                myConnection, created_urgency_radiology)

            print("\nPor favor, indique los nuevos valores del tratamiento: \n")

            type_option = input('\nTipo: ')
            if type_option == '':
                type_option = None
            created_treatment.setType(type_option)

            antitetanus_option = input(
                '\nVacuna contra el tétanos (0 - No / 1 - Sí): ')
            if antitetanus_option == '':
                antitetanus_option = None
            created_treatment.setAntitetanus(antitetanus_option)

            anesthesia_option = input('\nAnestesia (0 - No / 1 - Sí): ')
            if anesthesia_option == '':
                anesthesia_option = None
            created_treatment.setAnesthesia(anesthesia_option)

            created_treatment.update()
            print("\nTratamiento actualizado")
# -----------------------------------------------------------------------------------------------------------------------------
        else:
            syntaxes.show_actuation_syntax()
    except IndexError:
        syntaxes.show_actuation_syntax()
    except KeyboardInterrupt:
        print("")
    except sqlite3.DatabaseError:
        print("\n\nHay un problema con la base de datos. Vuelva a intentarlo más adelante")

myConnection.close()
