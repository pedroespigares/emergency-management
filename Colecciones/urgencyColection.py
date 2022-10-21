import os
import sys
sys.path.append(os.path.abspath('..'))

from Clases.urgency import Urgency


class UrgencyColection:
    '''
    Gestiona los objetos de la clase Urgency
    '''

    def newUrgency(self,
            connection,
            pacient,
            episode,
            medic=None,
            status=None,
            entry=None,
            reason=None,
            exploration=None,
            recomendation=None,
            exitDate=None,
    ):
        '''
        Crea una nueva urgencia con los parámetros del
         método como atributos del mismo.
        '''
        created_urgency = Urgency(
            connection,
            pacient,
            episode,
            medic,
            status,
            entry,
            reason,
            exploration,
            recomendation,
            exitDate,
        )

        return created_urgency
