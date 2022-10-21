import os
import sys
sys.path.append(os.path.abspath('..'))
from Clases.pacient import Pacient


class PacientColection:
    '''
    Gestiona los objetos de la clase Pacient
    '''

    def newPacient(self,
            connection,
            dni,
            history_number=None,
            name=None,
            surnames=None,
            birthday=None,
            nationality=None,
            sex=None,
            social_security=None,
            phone=None,
            address=None,
            history_status=None
        ):
        '''
        Crea un nuevo paciente con los parámetros del
        método como atributos del mismo.
        '''
        created_pacient = Pacient(
            connection,
            dni,
            history_number,
            name, surnames,
            birthday,
            nationality,
            sex,
            social_security,
            phone,
            address,
            history_status
        )

        return created_pacient
