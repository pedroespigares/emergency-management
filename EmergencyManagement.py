import os
import sys
import sqlite3
import syntaxes

CALL_MAIN_PACIENT = '-pacients'
CALL_MAIN_URGENCY = '-urgency'
CALL_MAIN_MEDIC = '-medics'
CALL_MAIN_ACTUATION = '-actuations'


if (len(sys.argv) == 3):
    try:
        program_option = sys.argv[1]
        user_option = sys.argv[2]
    except IndexError:
        syntaxes.show_main_syntax()
    try:
        if program_option == CALL_MAIN_PACIENT:
            os.system(f'python mainPacientes.py {user_option}')

        elif program_option == CALL_MAIN_URGENCY:
            os.system(f'python mainUrgencias.py {user_option}')

        elif program_option == CALL_MAIN_MEDIC:
            os.system(f'python mainMedicos.py {user_option}')

        elif program_option == CALL_MAIN_ACTUATION:
            os.system(f'python mainActuaciones.py {user_option}')
        else:
            syntaxes.show_main_syntax()
    except IndexError:
        syntaxes.show_main_syntax()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido")
    except sqlite3.DatabaseError:
        print('\n\nHay un problema con la base de datos.')

elif(len(sys.argv) >= 5):
    syntaxes.show_main_syntax()
else:
    try:
        program_option = sys.argv[1]
        user_option = sys.argv[2]
        user_value = sys.argv[3]
    except IndexError:
        syntaxes.show_main_syntax()
    try:
        if program_option == CALL_MAIN_PACIENT:
            os.system(f'python mainPacientes.py {user_option} {user_value}')

        elif program_option == CALL_MAIN_URGENCY:
            os.system(f'python mainUrgencias.py {user_option} {user_value}')

        elif program_option == CALL_MAIN_MEDIC:
            os.system(f'python mainMedicos.py {user_option} {user_value}')

        elif program_option == CALL_MAIN_ACTUATION:
            os.system(f'python mainActuaciones.py {user_option} {user_value}')
        else:
            syntaxes.show_main_syntax()
    except IndexError:
        syntaxes.show_main_syntax()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido")
    except sqlite3.DatabaseError:
        print('\n\nHay un problema con la base de datos.')
