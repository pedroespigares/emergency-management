import os
import sys
sys.path.append(os.path.abspath('..'))

import sqlite3
from Clases.transfusion import Transfusion
from Clases.urgency import Urgency


class TransfusionManager:
    '''
    Gestiona los objetos de la clase Transfusion en la base de datos
    '''

    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def __getTransfusionSets(self, rows):
        '''
        Crea un objeto Transfusion a partir registros de la base de datos

        rows = lista registro de la base de datos
        resultado = Transfusión(Transfusion)
        '''

        result = set()
        if rows is None:
            return result
        for row in rows:
            obtainedUrgency = Urgency(
                self.__connection,
                None,
                row["urgency"],
            )
            obtainedTransfusion = Transfusion(
                self.__connection,
                obtainedUrgency,
                row["petition"],
                row["blood_group"],
                row["IRH"],
                row["previous_transfusion"],
                row["religion"],
                row["informed_consent"],
            )
            result.add(obtainedTransfusion)
        return result

    def getTransfusionBaseSQL(self):
        '''
        Contiene las consultas de los métodos de colecciones
        de análisis
        resultado = devuelve el contenido de las consultas
        '''

        query = 'SELECT urgency, petition, blood_group, '
        query += 'IRH, previous_transfusion, '
        query += 'religion, informed_consent '
        query += 'FROM Transfusion '
        return query

    def getAllTransfusion(self):
        '''
        Devuelve una coleccion con todos los objetos tipo Transfusion
        de la base de datos.

        resultado = devolvera un conjunto de objetos tipo Transfusion
        '''

        query = 'SELECT urgency, petition, blood_group, '
        query += 'IRH, previous_transfusion, '
        query += 'religion, informed_consent '
        query += 'FROM Transfusion'
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getTransfusionSets(rows)

    def getTransfusionByUrgencies(self, *urgency):
        '''
        Devuelve una coleccion de objetos tipo Transfusion según
        sus urgencias.

        urgency = coleccion de urgencias correspondientes a Transfusion
        resultado = devolvera un conjunto de objetos tipo Transfusion
        '''

        query = self.getTransfusionBaseSQL()
        if len(urgency) > 1:
            query += 'WHERE urgency IN {}'.format(urgency)
        elif len(urgency) == 1:
            query += 'WHERE urgency = {}'.format(urgency[0])
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getTransfusionSets(rows)

    def getTransfusionByUrgency(self, urgency):
        '''
        Devuelve una coleccion de objetos tipo Transfusion según
        parte del episodio de la urgencia

        urgency = contendrá parte del episodio de la urgencia de
        una transfusión (str)
        resultado = devolvera un conjunto de objetos tipo Transfusion
        '''

        query = self.getTransfusionBaseSQL()
        query += 'WHERE urgency LIKE ?'
        self.__cursor.execute(query, (f'%{urgency}%',))
        rows = self.__cursor.fetchall()
        return self.__getTransfusionSets(rows)

    def getTransfusionByPetition(self, petition):
        '''
        Devuelve una coleccion de objetos tipo Transfusion segun su petición

        petition = contendrá parte de la petición de una transfusión (str)
        resultado = devolvera un conjunto de objetos tipo Transfusion
        '''

        query = self.getTransfusionBaseSQL()
        query += 'WHERE petition LIKE ?'
        self.__cursor.execute(query, (f'%{petition}%',))
        rows = self.__cursor.fetchall()
        return self.__getTransfusionSets(rows)

    def getTransfusionByBloodGroup(self, blood_group):
        '''
        Devuelve una coleccion de objetos tipo Transfusion segun su
        el grupo sanguíneo utilizado.

        blood_group = grupo sanguíneo que puede tener los siguientes valores:
            - A
            - B
            - 0
            - RH
        resultado = devolvera un conjunto de objetos tipo Transfusion
        '''

        query = self.getTransfusionBaseSQL()
        query += 'WHERE pregnancy = ?'
        blood_group = blood_group.strip()
        self.__cursor.execute(query, (blood_group,))
        rows = self.__cursor.fetchall()
        return self.__getTransfusionSets(rows)

    def getTransfusionByIRH(self, irh):
        '''
        Devuelve una coleccion de objetos tipo Transfusion el IRH de la
        transfusión.

        irh = IRH que puede tener los siguientes valores:
            - +
            - -
            - N
        resultado = devolvera un conjunto de objetos tipo Transfusion
        '''

        query = self.getTransfusionBaseSQL()
        query += 'WHERE irh = ?'
        irh = irh.strip()
        self.__cursor.execute(query, (irh,))
        rows = self.__cursor.fetchall()
        return self.__getTransfusionSets(rows)

    def getTransfusionByPreviousTransfusion(self, previous_transfusion):
        '''
        Devuelve una coleccion de objetos tipo Transfusion segun si el paciente
        ha tenido transfusiones previas o no.

        previous_transfusion = (str)
        - 0 --> No
        - 1 --> Sí
        resultado = devolvera un conjunto de objetos tipo Transfusion
        '''

        query = self.getTransfusionBaseSQL()
        query += 'WHERE previous_transfusion = ?'
        previous_transfusion = previous_transfusion.strip()
        self.__cursor.execute(query, (previous_transfusion,))
        rows = self.__cursor.fetchall()
        return self.__getTransfusionSets(rows)

    def getTransfusionByReligion(self, religion):
        '''
        Devuelve una coleccion de objetos tipo Transfusion segun la religión
        del paciente.

        religion = contendrá parte de la religión del paciente (str)
        resultado = devolvera un conjunto de objetos tipo Transfusion
        '''

        query = self.getTransfusionBaseSQL()
        query += 'WHERE lower(religion) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{religion}%',))
        rows = self.__cursor.fetchall()
        return self.__getTransfusionSets(rows)

    def getTransfusionByInformedConsent(self, consent):
        '''
        Devuelve una coleccion de objetos tipo Transfusion segun si el paciente
        ha dado su conocimiento informado o no.

        consent = (str)
        - 0 --> No
        - 1 --> Sí
        resultado = devolvera un conjunto de objetos tipo Transfusion
        '''

        query = self.getTransfusionBaseSQL()
        query += 'WHERE informed_consent = ?'
        consent = consent.strip()
        self.__cursor.execute(query, (consent,))
        rows = self.__cursor.fetchall()
        return self.__getTransfusionSets(rows)

    def deleteAllTransfusionFromUrgency(self, urgencyToDelete):
        '''
        Borra de la base de datos todos las transfusiones que tengan como
        urgencia el pasado por parámetro
        '''

        query = 'DELETE FROM Transfusion WHERE urgency = ?'
        self.__cursor.execute(query, (urgencyToDelete.getEpisode(),))
        self.__connection.commit()
