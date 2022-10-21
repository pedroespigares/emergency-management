import os
import sys

sys.path.append(os.path.abspath('..'))

from Managers.urgencyManager import UrgencyManager
import syntaxes

from Colecciones.urgencyColection import UrgencyColection
from Colecciones.pacientColection import PacientColection
from Colecciones.medicColection import MedicColection
from Managers.urgencyManager import UrgencyManager
from Managers.analysisManager import AnalysisManager
from Managers.cprManager import CprManager
from Managers.immobilizationManager import ImmobilizationManager
from Managers.medicationManager import MedicationManager
from Managers.oxygenTherapyManager import OxygenTherapyManager
from Managers.radiologyManager import RadiologyManager
from Managers.transfusionManager import TransfusionManager
from Managers.treatmentManager import TreatmentManager

import sqlite3

myConnection = sqlite3.connect('./Urgencias.db')


SHOW_ALL_URGENCY = '-showAll'
SEARCH_BY_EPISODE = '-searchByEpisode'
SEARCH_BY_SEVERAL_EPISODES = '-searchBySeveralEpisodes'
SEARCH_BY_PACIENT = '-searchByPacient'
SEARCH_BY_MEDIC = '-searchByMedic'
SEARCH_BY_STATUS = '-searchByStatus'
SEARCH_BY_ENTRY = '-searchByEntry'
SEARCH_BY_REASON = '-searchByReason'
SEARCH_BY_EXPLORATION = '-searchByExploration'
SEARCH_BY_RECOMENDATION = '-searchByRecomendation'
SEARCH_BY_EXIT = '-searchByExit'
LOAD_URGENCY_BY_FILE = '-loadByFile'
ADD_URGENCY = '-add'
UPDATE_URGENCY = '-update'
DELETE_URGENCY = '-delete'
DELETE_EXITUS_URGENCY = '-deleteExitus'
DELETE_HOSPITALIZATION_URGENCY = '-deleteHospitalization'
DELETE_DISCHARGE_URGENCY = '-deleteDischarge'


managerUrgency = UrgencyManager(myConnection)
managerAnalysis = AnalysisManager(myConnection)
managerCpr = CprManager(myConnection)
managerImmobilization = ImmobilizationManager(myConnection)
managerMedication = MedicationManager(myConnection)
managerOxygenTherapy = OxygenTherapyManager(myConnection)
managerRadiology = RadiologyManager(myConnection)
managerTransfusion = TransfusionManager(myConnection)
managerTreatment = TreatmentManager(myConnection)
colectionUrgency = UrgencyColection()
colectionPacient = PacientColection()
colectionMedic = MedicColection()


if(len(sys.argv) > 3):
    syntaxes.show_urgency_syntax()
else:
    try:
        user_option = sys.argv[1]
        if user_option == SHOW_ALL_URGENCY:
            print("\nMostrando urgencias...")
            all_urgency = managerUrgency.getAllUrgency()
            for urgency in all_urgency:
                print(urgency)

        elif user_option == SEARCH_BY_SEVERAL_EPISODES:
            user_value = sys.argv[2]
            splitted_value = user_value.split(",")
            value_tuple = tuple(splitted_value)
            print("\nMostrando urgencias...")
            episode_urgency = managerUrgency.getUrgencyByEpisodes(*value_tuple)
            for episode in episode_urgency:
                print(episode)

        elif user_option == SEARCH_BY_EPISODE:
            user_value = int(sys.argv[2])
            print("\nMostrando urgencias...")
            episode_urgency = managerUrgency.getUrgencyByEpisode(user_value)
            for urgency in episode_urgency:
                print(urgency)

        elif user_option == SEARCH_BY_PACIENT:
            user_value = sys.argv[2]
            print("\nMostrando urgencias...")
            pacient_urgency = managerUrgency.getUrgencyByPacient(user_value)
            for urgency in pacient_urgency:
                print(urgency)

        elif user_option == SEARCH_BY_MEDIC:
            user_value = int(sys.argv[2])
            print("\nMostrando urgencias...")
            medic_urgency = managerUrgency.getUrgencyByMedic(user_value)
            for urgency in medic_urgency:
                print(urgency)

        elif user_option == SEARCH_BY_STATUS:
            user_value = sys.argv[2]
            print("\nMostrando urgencias...")
            status_urgency = managerUrgency.getUrgencyByStatus(user_value)
            for urgency in status_urgency:
                print(urgency)

        elif user_option == SEARCH_BY_ENTRY:
            user_value = sys.argv[2]
            print("\nMostrando urgencias...")
            entry_urgency = managerUrgency.getUrgencyByEntry(user_value)
            for urgency in entry_urgency:
                print(urgency)

        elif user_option == SEARCH_BY_REASON:
            user_value = sys.argv[2]
            print("\nMostrando urgencias...")
            reason_urgency = managerUrgency.getUrgencyByReason(user_value)
            for urgency in reason_urgency:
                print(urgency)

        elif user_option == SEARCH_BY_EXPLORATION:
            user_value = sys.argv[2]
            print("\nMostrando urgencias...")
            exploration_urgency = managerUrgency.getUrgencyByExploration(
                user_value)
            for urgency in exploration_urgency:
                print(urgency)

        elif user_option == SEARCH_BY_RECOMENDATION:
            user_value = sys.argv[2]
            print("\nMostrando urgencias...")
            recomendation_urgency = managerUrgency.getUrgencyByRecomendation(
                user_value)
            for urgency in recomendation_urgency:
                print(urgency)

        elif user_option == SEARCH_BY_EXIT:
            user_value = sys.argv[2]
            print("\nMostrando urgencias...")
            exit_urgency = managerUrgency.getUrgencyByExit(user_value)
            for urgency in exit_urgency:
                print(urgency)

        elif user_option == LOAD_URGENCY_BY_FILE:
            user_value = sys.argv[2]
            print("\nMostrando urgencias...")
            loaded_urgency = managerUrgency.loadUrgencyByFile(user_value)
            for urgency in loaded_urgency:
                print(urgency)
                urgency.save()

        elif user_option == ADD_URGENCY:
            print("Introduzca los datos de la urgencia: \n")
            pacient_option = input('\nPaciente: ')
            pacient_option = pacient_option.strip()
            urgency_pacient = colectionPacient.newPacient(
                myConnection, pacient_option)
            urgency_pacient.load()
            episode_option = int(input('\nEpisodio: '))
            episode_option = episode_option.strip()
            if pacient_option == '':
                pacient_option = None
            medic_option = int(input('\nMédico: '))
            if medic_option == '':
                urgency_medic = colectionMedic.newMedic(myConnection, None)
            else:
                urgency_medic = colectionMedic.newMedic(
                    myConnection, medic_option)
            status_option = input('\nEstado: ')
            status_option = status_option.strip()
            if status_option == '':
                status_option = None
            entry_option = input('\nFecha y hora de entrada: ')
            entry_option = entry_option.strip()
            if entry_option == '':
                entry_option = None
            reason_option = input('\nMotivo de consulta: ')
            if reason_option == '':
                reason_option = None
            exploration_option = input('\nExploración: ')
            if exploration_option == '':
                exploration_option = None
            recomendation_option = input('\nRecomendación: ')
            if recomendation_option == '':
                recomendation_option = None
            exit_option = input('\nFecha y hora de salida: ')
            exit_option = exit_option.strip()
            if exit_option == '':
                exit_option = None
            created_urgency = colectionUrgency.newUrgency(
                myConnection,
                urgency_pacient,
                episode_option,
                urgency_medic,
                status_option,
                entry_option,
                reason_option,
                exploration_option,
                recomendation_option,
                exit_option
            )
            clinicalJudgments_option = input(
                '\nIndique los códigos de los juicios clínicos separados por comas: ')
            clinicalJudgments_option_list = list(
                clinicalJudgments_option.split(","))
            for judgment in clinicalJudgments_option_list:
                created_urgency.addClinicalJudgment(judgment)
            created_urgency.save()
            if created_urgency.getStatus() == "Exitus":
                print(
                    "\n-------------------------------------------------------------------------")
                print(
                    "\nEl paciente añadido está fallecido, cambiando su estado en pacientes...")
                print(
                    "\n-------------------------------------------------------------------------")
                urgency_pacient.setStatus("Pasivo")
                urgency_pacient.update()
            created_urgency.saveUrgencyWithClinicalJudgments()
            print("\nUrgencia añadida correctamente")

        elif user_option == UPDATE_URGENCY:
            user_value = int(sys.argv[2])
            update_created_urgency = colectionUrgency.newUrgency(
                myConnection, None, user_value)

            print("\nPor favor, indique los nuevos valores de la urgencia: \n")

            pacient_option = input('\nPaciente: ')
            if pacient_option == '':
                pacient_option = None
            update_created_urgency.setPacient(pacient_option)

            update_urgency_pacient = colectionPacient.newPacient(
                myConnection, pacient_option)
            update_urgency_pacient.load()

            medic_option = int(input('\nMédico: '))
            if medic_option == '':
                medic_option = None
            update_created_urgency.setMedic(medic_option)

            update_urgency_medic = colectionMedic.newMedic(
                myConnection, medic_option)
            update_urgency_medic.load()

            status_option = input('\nEstado: ')
            if status_option == '':
                status_option = None
            update_created_urgency.setStatus(status_option)

            entry_option = input('\nFecha y hora de entrada: ')
            if entry_option == '':
                entry_option = None
            update_created_urgency.setEntry(entry_option)

            reason_option = input('\nMotivo de consulta: ')
            if reason_option == '':
                reason_option = None
            update_created_urgency.setReason(reason_option)

            exploration_option = input('\nExploración: ')
            if exploration_option == '':
                exploration_option = None
            update_created_urgency.setExploration(exploration_option)

            recomendation_option = input('\nRecomendación: ')
            if recomendation_option == '':
                recomendation_option = None
            update_created_urgency.setRecomendation(recomendation_option)

            exit_option = input('\nFecha y hora de salida: ')
            if exit_option == '':
                exit_option = None
            update_created_urgency.setExit(exit_option)

            update_created_urgency.update()
            print("\nUrgencia actualizada correctamente")

            if update_created_urgency.getStatus() == "Exitus":
                print(
                    "\n-------------------------------------------------------------------------")
                print(
                    "\nEl paciente actualizado ha fallecido, cambiando su estado en pacientes...")
                print(
                    "\n-------------------------------------------------------------------------")
                update_urgency_pacient.setStatus("Pasivo")

        elif user_option == DELETE_URGENCY:
            user_value = int(sys.argv[2])
            created_urgency = colectionUrgency.newUrgency(
                myConnection, None, user_value)
            user_validation = input(
                "\n¿Está seguro de que desea borrar la urgencia? \nSe eliminarán todas las actuaciones relacionadas a la misma (S/N): ")
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando urgencia...\n")
                managerAnalysis.deleteAllAnalysisFromUrgency(created_urgency)
                managerCpr.deleteAllCprFromUrgency(created_urgency)
                managerImmobilization.deleteAllImmobilizationFromUrgency(
                    created_urgency)
                managerMedication.deleteAllMedicationFromUrgency(
                    created_urgency)
                managerOxygenTherapy.deleteAllOxygenTherapyFromUrgency(
                    created_urgency)
                managerRadiology.deleteAllRadiologyFromUrgency(created_urgency)
                managerTransfusion.deleteAllTransfusionFromUrgency(
                    created_urgency)
                managerTreatment.deleteAllTreatmentFromUrgency(created_urgency)
                created_urgency.delete()
                print("Urgencia eliminada")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")

        elif user_option == DELETE_DISCHARGE_URGENCY:
            user_validation = input(
                "\n¿Está seguro de que desea borrar las urgencias dadas de alta? (S/N) ")
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando urgencias dadas de alta...")
                managerUrgency.deleteAllUrgenciesStatusDischarge()
                print("\nUrgencias eliminadas")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")

        elif user_option == DELETE_EXITUS_URGENCY:
            user_validation = input(
                "\n¿Está seguro de que desea borrar las urgencias exitus (paciente fallecido)? (S/N) ")
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando urgencias con pacientes fallecidos...")
                managerUrgency.deleteAllUrgenciesStatusExitus()
                print("\nUrgencias eliminadas")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")

        elif user_option == DELETE_HOSPITALIZATION_URGENCY:
            user_validation = input(
                "\n¿Está seguro de que desea borrar las urgencias con pacientes hospitalizados? (S/N) ")
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando urgencias con pacientes hospitalizados...")
                managerUrgency.deleteAllUrgenciesStatusHospitalization()
                print("\nUrgencias eliminadas")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")
        else:
            syntaxes.show_urgency_syntax()
    except IndexError:
        syntaxes.show_urgency_syntax()
    except KeyboardInterrupt:
        print("")
    except sqlite3.DatabaseError:
        print("\n\nHay un problema con la base de datos. Vuelva a intentarlo más adelante")

myConnection.close()
