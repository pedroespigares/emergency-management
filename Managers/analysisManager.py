import os
import sys
sys.path.append(os.path.abspath('..'))

from Clases.analysis import Analysis
from Clases.urgency import Urgency
import sqlite3


class AnalysisManager:
    '''
    Gestiona los objetos de la clase Analysis en la base de datos
    '''

    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def __getAnalysisSets(self, rows):
        '''
        Crea un objeto Analysis a partir registros de la base de datos

        rows = lista registro de la base de datos
        resultado = Análisis(Analysis)
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
            obtainedAnalysis = Analysis(
                self.__connection,
                obtainedUrgency,
                row["petition"],
                row["hemoglobine"],
                row["oxygen"],
            )
            result.add(obtainedAnalysis)
        return result

    def getAnalysisBaseSQL(self):
        '''
        Contiene las consultas de los métodos de colecciones
        de análisis
        resultado = devuelve el contenido de las consultas
        '''

        query = 'SELECT urgency, petition, hemoglobine, '
        query += 'oxygen FROM Analysis '
        return query

    def getAllAnalysis(self):
        '''
        Devuelve una coleccion con todos los objetos tipo Analysis
        de la base de datos.

        resultado = devolvera un conjunto de objetos tipo Analysis
        '''

        query = 'SELECT urgency, petition, hemoglobine, '
        query += 'oxygen FROM Analysis'
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getAnalysisSets(rows)

    def getAnalysisByUrgencies(self, *urgency):
        '''
        Devuelve una coleccion de objetos tipo Analysis según
        sus urgencias.

        urgency = coleccion de urgencias correspondientes a Analysis
        resultado = devolvera un conjunto de objetos tipo Analysis
        '''

        query = self.getAnalysisBaseSQL()
        if len(urgency) > 1:
            query += 'WHERE urgency IN {}'.format(urgency)
        elif len(urgency) == 1:
            query += 'WHERE urgency = {}'.format(urgency[0])
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getAnalysisSets(rows)

    def getAnalysisByUrgency(self, urgency):
        '''
        Devuelve una coleccion de objetos tipo Analysis segun
        parte del episodio de la urgencia

        urgency = contendrá parte del episodio de
        la urgencia de un análisis (str)
        resultado = devolvera un conjunto de objetos tipo Analysis
        '''

        query = self.getAnalysisBaseSQL()
        query += 'WHERE urgency LIKE ?'
        self.__cursor.execute(query, (f'%{urgency}%',))
        rows = self.__cursor.fetchall()
        return self.__getAnalysisSets(rows)

    def getAnalysisByPetition(self, petition):
        '''
        Devuelve una coleccion de objetos tipo Analysis segun su petición

        petition = contendrá parte de la petición de un análisis (str)
        resultado = devolvera un conjunto de objetos tipo Analysis
        '''

        query = self.getAnalysisBaseSQL()
        query += 'WHERE petition LIKE ?'
        self.__cursor.execute(query, (f'%{petition}%',))
        rows = self.__cursor.fetchall()
        return self.__getAnalysisSets(rows)

    def getAnalysisAboveHemoglobineLevel(self, hemoglobine):
        '''
        Devuelve una coleccion de objetos tipo Analysis segun si su
        hemoglobina en sangre es mayor que la pasada como parámetro

        hemoglobine = contendrá un valor de hemoglobina en sangre (str)
        resultado = devolvera un conjunto de objetos tipo Analysis
        '''

        query = self.getAnalysisBaseSQL()
        query += 'WHERE hemoglobine > ?'
        self.__cursor.execute(query, (hemoglobine,))
        rows = self.__cursor.fetchall()
        return self.__getAnalysisSets(rows)

    def getAnalysisBelowHemoglobineLevel(self, hemoglobine):
        '''
        Devuelve una coleccion de objetos tipo Analysis segun si su
        hemoglobina en sangre es menor que la pasada como parámetro

        hemoglobine = contendrá un valor de hemoglobina en sangre (str)
        resultado = devolvera un conjunto de objetos tipo Analysis
        '''

        query = self.getAnalysisBaseSQL()
        query += 'WHERE hemoglobine < ?'
        self.__cursor.execute(query, (hemoglobine,))
        rows = self.__cursor.fetchall()
        return self.__getAnalysisSets(rows)

    def getAnalysisEqualHemoglobineLevel(self, hemoglobine):
        '''
        Devuelve una coleccion de objetos tipo Analysis segun si su
        hemoglobina en sangre es igual que la pasada como parámetro

        hemoglobine = contendrá un valor de hemoglobina en sangre (str)
        resultado = devolvera un conjunto de objetos tipo Analysis
        '''

        query = self.getAnalysisBaseSQL()
        query += 'WHERE hemoglobine = ?'
        self.__cursor.execute(query, (hemoglobine,))
        rows = self.__cursor.fetchall()
        return self.__getAnalysisSets(rows)

    def getAnalysisAboveOxygen(self, oxygen):
        '''
        Devuelve una coleccion de objetos tipo Analysis segun si su oxígeno
        en sangre es mayor que la pasada como parámetro

        oxygen = contendrá un valor de oxígeno en sangre (str)
        resultado = devolvera un conjunto de objetos tipo Analysis
        '''

        query = self.getAnalysisBaseSQL()
        query += 'WHERE oxygen > ?'
        self.__cursor.execute(query, (oxygen,))
        rows = self.__cursor.fetchall()
        return self.__getAnalysisSets(rows)

    def getAnalysisBelowOxygen(self, oxygen):
        '''
        Devuelve una coleccion de objetos tipo Analysis segun si su oxígeno
        en sangre es menor que la pasada como parámetro

        oxygen = contendrá un valor de oxígeno en sangre (str)
        resultado = devolvera un conjunto de objetos tipo Analysis
        '''

        query = self.getAnalysisBaseSQL()
        query += 'WHERE oxygen < ?'
        self.__cursor.execute(query, (oxygen,))
        rows = self.__cursor.fetchall()
        return self.__getAnalysisSets(rows)

    def getAnalysisEqualOxygen(self, oxygen):
        '''
        Devuelve una coleccion de objetos tipo Analysis segun si su oxígeno
        en sangre es igual que la pasada como parámetro

        oxygen = contendrá un valor de oxígeno en sangre (str)
        resultado = devolvera un conjunto de objetos tipo Analysis
        '''

        query = self.getAnalysisBaseSQL()
        query += 'WHERE oxygen = ?'
        self.__cursor.execute(query, (oxygen,))
        rows = self.__cursor.fetchall()
        return self.__getAnalysisSets(rows)

    def deleteAllAnalysisFromUrgency(self, urgencyToDelete):
        '''
        Borra de la base de datos todos los análisis que tengan como
        urgencia el pasado por parámetro
        '''

        query = 'DELETE FROM Analysis WHERE urgency = ?'
        self.__cursor.execute(query, (urgencyToDelete.getEpisode(),))
        self.__connection.commit()
