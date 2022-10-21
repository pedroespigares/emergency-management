import os
import sys

sys.path.append(os.path.abspath('..'))

from Managers.pacientManager import PacientManager

from Colecciones.pacientColection import PacientColection
from Managers.urgencyManager import UrgencyManager
import syntaxes

import sqlite3

myConnection = sqlite3.connect('./Urgencias.db')


SHOW_ALL_PACIENTS = '-showAll'
SEARCH_BY_DNI = '-searchByDNI'
SEARCH_BY_SEVERAL_DNI = '-searchBySeveralDNI'
SEARCH_BY_HISTORY = '-searchByHistory'
SEARCH_BY_NAME = '-searchByName'
SEARCH_BY_SURNAMES = '-searchBySurnames'
SEARCH_BY_BIRTHDATE = '-searchByBirthdate'
SEARCH_BY_NACIONALITY = '-searchByNacionality'
SEARCH_BY_SEX = '-searchBySex'
SEARCH_BY_SOCIAL_SECURITY = '-searchBySocialSecurity'
SEARCH_BY_PHONE = '-searchByPhone'
SEARCH_BY_ADDRESS = '-searchByAddress'
SEARCH_BY_STATUS = '-searchByStatus'
LOAD_PACIENT_BY_FILE = '-loadByFile'
ADD_PACIENT = '-add'
UPDATE_PACIENT = '-update'
LOAD_PACIENT_BY_FILE = '-loadByFile'
DELETE_PACIENT = '-delete'
DELETE_DEAD_PACIENTS = '-deleteDeadPacients'


managerPacients = PacientManager(myConnection)
managerUrgency = UrgencyManager(myConnection)
colectionPacients = PacientColection()


if(len(sys.argv) > 3):
    syntaxes.show_pacient_syntax()
else:
    try:
        user_option = sys.argv[1]
        if user_option == SHOW_ALL_PACIENTS:
            print("\nMostrando pacientes...")
            all_pacients = managerPacients.getAllPacients()
            for pacient in all_pacients:
                print(pacient)

        elif user_option == SEARCH_BY_SEVERAL_DNI:
            user_value = sys.argv[2]
            splitted_value = user_value.split(",")
            value_tuple = tuple(splitted_value)
            print("\nMostrando pacientes...")
            dni_pacients = managerPacients.getPacientsByDNIs(*value_tuple)
            for pacient in dni_pacients:
                print(pacient)

        elif user_option == SEARCH_BY_DNI:
            user_value = sys.argv[2]
            print("\nMostrando pacientes...")
            dni_pacients = managerPacients.getPacientByDNI(user_value)
            for pacient in dni_pacients:
                print(pacient)

        elif user_option == SEARCH_BY_HISTORY:
            user_value = int(sys.argv[2])
            print("\nMostrando pacientes...")
            history_pacients = managerPacients.getPacientByHistoryNumber(
                user_value)
            for pacient in history_pacients:
                print(pacient)

        elif user_option == SEARCH_BY_NAME:
            user_value = sys.argv[2]
            print("\nMostrando pacientes...")
            name_pacients = managerPacients.getPacientByName(user_value)
            for pacient in name_pacients:
                print(pacient)

        elif user_option == SEARCH_BY_SURNAMES:
            user_value = sys.argv[2]
            print("\nMostrando pacientes...")
            surnames_pacients = managerPacients.getPacientBySurnames(
                user_value)
            for pacient in surnames_pacients:
                print(pacient)

        elif user_option == SEARCH_BY_BIRTHDATE:
            user_value = sys.argv[2]
            print("\nMostrando pacientes...")
            birthday_pacients = managerPacients.getPacientByBirthday(
                user_value)
            for pacient in birthday_pacients:
                print(pacient)

        elif user_option == SEARCH_BY_NACIONALITY:
            user_value = sys.argv[2]
            print("\nMostrando pacientes...")
            nationality_pacients = managerPacients.getPacientByNationality(
                user_value)
            for pacient in nationality_pacients:
                print(pacient)

        elif user_option == SEARCH_BY_SEX:
            user_value = sys.argv[2]
            print("\nMostrando pacientes...")
            sex_pacients = managerPacients.getPacientBySex(user_value)
            for pacient in sex_pacients:
                print(pacient)

        elif user_option == SEARCH_BY_SOCIAL_SECURITY:
            user_value = sys.argv[2]
            print("\nMostrando pacientes...")
            ss_pacients = managerPacients.getPacientBySocialSecurity(
                user_value)
            for pacient in ss_pacients:
                print(pacient)

        elif user_option == SEARCH_BY_PHONE:
            user_value = sys.argv[2]
            print("\nMostrando pacientes...")
            phone_pacients = managerPacients.getPacientByPhone(user_value)
            for pacient in phone_pacients:
                print(pacient)

        elif user_option == SEARCH_BY_ADDRESS:
            user_value = sys.argv[2]
            print("\nMostrando pacientes...")
            address_pacients = managerPacients.getPacientByAddress(user_value)
            for pacient in address_pacients:
                print(pacient)

        elif user_option == SEARCH_BY_STATUS:
            user_value = sys.argv[2]
            print("\nMostrando pacientes...")
            status_pacients = managerPacients.getPacientByHistoryStatus(
                user_value)
            for pacient in status_pacients:
                print(pacient)

        elif user_option == LOAD_PACIENT_BY_FILE:
            user_value = sys.argv[2]
            print("\nMostrando pacientes...")
            loaded_pacients = managerPacients.loadPacientsByFile(
                user_value)
            for pacient in loaded_pacients:
                print(pacient)
                pacient.save()

        elif user_option == ADD_PACIENT:
            print("Introduzca los datos del paciente: \n")
            dni_option = input('\nDNI: ')
            dni_option = dni_option.strip()
            try:
                history_option = int(input('\nHistoria: '))
            except ValueError:
                print("\nEl valor debe de ser un número")
                quit()
            if history_option == '':
                    history_option = None
            name_option = input('\nNombre: ')
            if name_option == '':
                name_option = None
            surnames_option = input('\nApellidos: ')
            if surnames_option == '':
                surnames_option = None
            birthday_option = input('\nFecha de nacimiento: ')
            birthday_option = birthday_option.strip()
            if birthday_option == '':
                birthday_option = None
            nationality_option = input('\nNacionalidad: ')
            nationality_option = nationality_option.strip()
            if nationality_option == '':
                nationality_option = None
            sex_option = input('\nSexo: ')
            sex_option = sex_option.strip()
            if sex_option == '':
                sex_option = None
            social_security_option = input('\nSeguridad social: ')
            social_security_option = social_security_option.strip()
            if social_security_option == '':
                social_security_option = None
            phone_option = input('\nTeléfono: ')
            phone_option = phone_option.strip()
            if phone_option == '':
                phone_option = None
            address_option = input('\nDirección: ')
            if address_option == '':
                address_option = None
            status_option = input('\nEstado: ')
            if status_option == '':
                status_option = None
            created_pacient = colectionPacients.newPacient(
                myConnection,
                dni_option,
                history_option,
                name_option,
                surnames_option,
                birthday_option,
                nationality_option,
                sex_option,
                social_security_option,
                phone_option,
                address_option,
                status_option,
            )
            created_pacient.save()
            print("\nPaciente añadido correctamente")

        elif user_option == UPDATE_PACIENT:
            user_value = sys.argv[2]
            created_pacient = colectionPacients.newPacient(
                myConnection, user_value)

            print("\nPor favor, indique los nuevos valores del paciente: \n")

            try:
                history_option = int(input('\nHistoria: '))
            except ValueError:
                print("\nEl valor debe ser numérico")
                quit()
            if history_option == '':
                history_option = None
            created_pacient.setHistoryNumber(history_option)

            name_option = input('\nNombre: ')
            if name_option == '':
                name_option = None
            created_pacient.setName(name_option)

            surnames_option = input('\nApellidos: ')
            if surnames_option == '':
                surnames_option = None
            created_pacient.setSurnames(surnames_option)

            birthday_option = input('\nFecha de nacimiento: ')
            if birthday_option == '':
                birthday_option = None
            created_pacient.setBirthday(birthday_option)

            nationality_option = input('\nNacionalidad: ')
            if nationality_option == '':
                nationality_option = None
            created_pacient.setNationality(nationality_option)

            sex_option = input('\nSexo: ')
            if sex_option == '':
                sex_option = None
            created_pacient.setSex(sex_option)

            social_security_option = input('\nSeguridad social: ')
            if social_security_option == '':
                social_security_option = None
            created_pacient.setSocialSecurity(social_security_option)

            phone_option = input('\nTeléfono: ')
            if phone_option == '':
                phone_option = None
            created_pacient.setPhone(phone_option)

            address_option = input('\nDirección: ')
            if address_option == '':
                address_option = None
            created_pacient.setAddress(address_option)

            status_option = input('\nEstado: ')
            if status_option == '':
                status_option = None
            created_pacient.setStatus(status_option)

            created_pacient.update()
            print("\nPaciente actualizado")

        elif user_option == DELETE_PACIENT:
            user_value = sys.argv[2]
            created_pacient = colectionPacients.newPacient(
                myConnection, user_value)
            user_validation = input(
                '''\n¿Está seguro de que desea borrar el paciente?
                 \nSe eliminarán las urgencias relacionadas
                  al mismo (S/N): ''')
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando paciente...\n")
                managerUrgency.deleteAllUrgenciesFromPacient(created_pacient)
                created_pacient.delete()
                print("Paciente eliminado")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")

        elif user_option == DELETE_DEAD_PACIENTS:
            user_validation = input(
                '''\n¿Está seguro de que desea borrar los pacientes fallecidos?
                 \nSe eliminarán las urgencias
                  relacionadas a los mismos (S/N): ''')
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando pacientes fallecidos...")
                managerUrgency.deleteAllUrgenciesFromDeadPacients()
                managerPacients.deleteDeadPacients()
                print("\nPacientes eliminados")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")
        else:
            syntaxes.show_pacient_syntax()
    except IndexError:
        syntaxes.show_pacient_syntax()
    except KeyboardInterrupt:
        print("")
    except sqlite3.DatabaseError:
        print('\n\nHay un problema con la base de datos.')

myConnection.close()
