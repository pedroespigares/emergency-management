import os
import sys
sys.path.append(os.path.abspath('..'))

import sqlite3
from Clases.radiology import Radiology
from Clases.urgency import Urgency


class RadiologyManager:
    '''
    Gestiona los objetos de la clase Radiology en la base de datos
    '''

    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def __getRadiologySets(self, rows):
        '''
        Crea un objeto Radiology a partir registros de la base de datos

        rows = lista registro de la base de datos
        resultado = Análisis(Radiology)
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
            obtainedRadiology = Radiology(
                self.__connection,
                obtainedUrgency,
                row["petition"],
                row["pregnancy"],
                row["contrast"],
                row["informed_consent"],
            )
            result.add(obtainedRadiology)
        return result

    def getRadiologyBaseSQL(self):
        '''
        Contiene las consultas de los métodos de colecciones
        de análisis
        resultado = devuelve el contenido de las consultas
        '''

        query = 'SELECT urgency, petition, pregnancy, '
        query += 'contrast, '
        query += 'informed_consent '
        query += 'FROM Radiology '
        return query

    def getAllRadiology(self):
        '''
        Devuelve una coleccion con todos los objetos tipo Radiology
        de la base de datos.

        resultado = devolvera un conjunto de objetos tipo Radiology
        '''

        query = 'SELECT urgency, petition, pregnancy, '
        query += 'contrast, '
        query += 'informed_consent '
        query += 'FROM Radiology'
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getRadiologySets(rows)

    def getRadiologyByUrgencies(self, *urgency):
        '''
        Devuelve una coleccion de objetos tipo Radiology según
        sus urgencias.

        Urgency = coleccion de urgencias correspondientes a Radiology
        resultado = devolvera un conjunto de objetos tipo Radiology
        '''

        query = self.getRadiologyBaseSQL()
        if len(urgency) > 1:
            query += 'WHERE urgency IN {}'.format(urgency)
        elif len(urgency) == 1:
            query += 'WHERE urgency = {}'.format(urgency[0])
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getRadiologySets(rows)

    def getRadiologyByUrgency(self, urgency):
        '''
        Devuelve una coleccion de objetos tipo Radiology según
        parte del episodio de la urgencia

        urgency = contendrá parte del episodio de la urgencia
        de una radiología (str)
        resultado = devolvera un conjunto de objetos tipo Radiology
        '''

        query = self.getRadiologyBaseSQL()
        query += 'WHERE urgency LIKE ?'
        self.__cursor.execute(query, (f'%{urgency}%',))
        rows = self.__cursor.fetchall()
        return self.__getRadiologySets(rows)

    def getRadiologyByPetition(self, petition):
        '''
        Devuelve una coleccion de objetos tipo Radiology segun su petición

        petition = contendrá parte de la petición de una radiología (str)
        resultado = devolvera un conjunto de objetos tipo Radiology
        '''

        query = self.getRadiologyBaseSQL()
        query += 'WHERE petition LIKE ?'
        self.__cursor.execute(query, (f'%{petition}%',))
        rows = self.__cursor.fetchall()
        return self.__getRadiologySets(rows)

    def getRadiologyByPregnancy(self, pregnancy):
        '''
        Devuelve una coleccion de objetos tipo Radiology segun si está
        embarazadx o no.

        pregnancy = (str)
        - 0 --> No
        - 1 --> Sí
        resultado = devolvera un conjunto de objetos tipo Radiology
        '''

        query = self.getRadiologyBaseSQL()
        query += 'WHERE pregnancy = ?'
        pregnancy = pregnancy.strip()
        self.__cursor.execute(query, (pregnancy,))
        rows = self.__cursor.fetchall()
        return self.__getRadiologySets(rows)

    def getRadiologyByConstrast(self, contrast):
        '''
        Devuelve una coleccion de objetos tipo Radiology segun si se ha
        utilizado contraste o no.

        contrast = (str)
        - 0 --> No
        - 1 --> Sí
        resultado = devolvera un conjunto de objetos tipo Radiology
        '''

        query = self.getRadiologyBaseSQL()
        query += 'WHERE contrast = ?'
        contrast = contrast.strip()
        self.__cursor.execute(query, (contrast,))
        rows = self.__cursor.fetchall()
        return self.__getRadiologySets(rows)

    def getRadiologyByInformedConsent(self, consent):
        '''
        Devuelve una coleccion de objetos tipo Radiology según si el paciente
        ha dado su conocimiento informado o no.

        consent = (str)
        - 0 --> No
        - 1 --> Sí
        resultado = devolvera un conjunto de objetos tipo Radiology
        '''

        query = self.getRadiologyBaseSQL()
        query += 'WHERE informed_consent = ?'
        consent = consent.strip()
        self.__cursor.execute(query, (consent,))
        rows = self.__cursor.fetchall()
        return self.__getRadiologySets(rows)

    def deleteAllRadiologyFromUrgency(self, urgencyToDelete):
        '''
        Borra de la base de datos todos las radiologías que tengan como
        urgencia el pasado por parámetro
        '''

        query = 'DELETE FROM Radiology WHERE urgency = ?'
        self.__cursor.execute(query, (urgencyToDelete.getEpisode(),))
        self.__connection.commit()
