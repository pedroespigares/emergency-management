import os
import sys
sys.path.append(os.path.abspath('..'))

from Clases.medic import Medic


class MedicColection:
    '''
    Gestiona los objetos de la clase Medic
    '''

    def newMedic(self, connection, npc, name=None,
    surnames=None, specialty=None):
        '''
        Crea un nuevo médico con los parámetros del
        método como atributos del mismo.
        '''
        created_medic = Medic(connection, npc, name, surnames, specialty)

        return created_medic
