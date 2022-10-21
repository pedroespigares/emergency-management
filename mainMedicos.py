import os
import sys
sys.path.append(os.path.abspath('..'))

from Managers.medicManager import MedicManager

from Colecciones.medicColection import MedicColection
import syntaxes

import sqlite3

myConnection = sqlite3.connect('./Urgencias.db')


SHOW_ALL_MEDICS = '-showAll'
SEARCH_BY_NPC = '-searchByNPC'
SEARCH_BY_SEVERAL_NPC = '-searchBySeveralNPC'
SEARCH_BY_NAME = '-searchByName'
SEARCH_BY_SURNAMES = '-searchBySurnames'
SEARCH_BY_SPECIALTY = '-searchBySpecialty'
ADD_MEDIC = '-add'
UPDATE_MEDIC = '-update'
DELETE_MEDIC = '-delete'


managerMedic = MedicManager(myConnection)
colectionMedics = MedicColection()


if(len(sys.argv) > 3):
    syntaxes.show_medic_syntax()
else:
    try:
        user_option = sys.argv[1]
        if user_option == SHOW_ALL_MEDICS:
            print("\nMostrando médicos...")
            all_medics = managerMedic.getAllMedics()
            for medic in all_medics:
                print(medic)

        elif user_option == SEARCH_BY_NPC:
            user_value = int(sys.argv[2])
            print("\nMostrando médicos...")
            npc_medics = managerMedic.getMedicByNPC(user_value)
            for medic in npc_medics:
                print(medic)

        elif user_option == SEARCH_BY_SEVERAL_NPC:
            user_value = sys.argv[2]
            splitted_value = user_value.split(",")
            value_tuple = tuple(splitted_value)
            print("\nMostrando médicos...")
            npc_medics = managerMedic.getMedicByNPCs(*value_tuple)
            for medic in npc_medics:
                print(medic)

        elif user_option == SEARCH_BY_NAME:
            user_value = sys.argv[2]
            print("\nMostrando médicos...")
            name_medics = managerMedic.getMedicByName(user_value)
            for medic in name_medics:
                print(medic)

        elif user_option == SEARCH_BY_SURNAMES:
            user_value = sys.argv[2]
            print("\nMostrando médicos...")
            surnames_medics = managerMedic.getMedicBySurnames(user_value)
            for pacient in surnames_medics:
                print(pacient)

        elif user_option == SEARCH_BY_SPECIALTY:
            user_value = sys.argv[2]
            print("\nMostrando médicos...")
            specialty_medics = managerMedic.getMedicBySpecialty(user_value)
            for medic in specialty_medics:
                print(medic)

        elif user_option == ADD_MEDIC:
            print("Introduzca los datos del médico: \n")
            npc_option = int(input('\nNPC: '))
            npc_option = npc_option.strip()
            name_option = input('\nNombre: ')
            if name_option == '':
                name_option = None
            surnames_option = input('\nApellidos: ')
            if surnames_option == '':
                surnames_option = None
            specialty_option = input('\nEspecialidad: ')
            if specialty_option == '':
                specialty_option = None
            created_medic = colectionMedics.newMedic(
                myConnection,
                npc_option,
                name_option,
                surnames_option,
                specialty_option
            )
            created_medic.save()
            print("\nMédico añadido correctamente")

        elif user_option == UPDATE_MEDIC:
            user_value = int(sys.argv[2])
            created_medic = colectionMedics.newMedic(myConnection, user_value)

            print("\nPor favor, indique los nuevos valores del médico: \n")

            name_option = input('\nNombre: ')
            if name_option == '':
                name_option = None
            created_medic.setName(name_option)

            surnames_option = input('\nApellido: ')
            if surnames_option == '':
                surnames_option = None
            created_medic.setSurnames(surnames_option)

            specialty_option = input('\nEspecialidad: ')
            if specialty_option == '':
                specialty_option = None
            created_medic.setSpecialty(specialty_option)

            created_medic.update()
            print("\nMédico actualizado")

        elif user_option == DELETE_MEDIC:
            user_value = int(sys.argv[2])
            created_medic = colectionMedics.newMedic(myConnection, user_value)
            user_validation = input(
                "\n¿Está seguro de que desea borrar al médico? (S/N): ")
            if user_validation == "S" or user_validation == "s":
                print("\nEliminando medico...\n")
                created_medic.delete()
                print("Médico eliminado")
            if user_validation == "N" or user_validation == "n":
                print("\nOperación cancelada")
        else:
            syntaxes.show_medic_syntax()
    except IndexError:
        syntaxes.show_medic_syntax()
    except KeyboardInterrupt:
        print("")
    except sqlite3.DatabaseError:
        print("\n\nHay un problema con la base de datos. Vuelva a intentarlo más adelante")

myConnection.close()
