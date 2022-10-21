import os
import sys
sys.path.append(os.path.abspath('..'))

from Clases.clinicalJudgment import ClinicalJudgment


class ClinicalJudgmentColection:
    '''
    Gestiona los objetos de la clase ClinicalJudgment
    '''

    def newPacient(self, connection, code, description=None):
        '''
        Crea un nuevo médico con los parámetros del
        método como atributos del mismo.
        '''
        created_clinicalJudgment = ClinicalJudgment(connection,
        code, description)

        return created_clinicalJudgment
