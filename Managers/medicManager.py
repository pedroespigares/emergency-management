import os
import sys
sys.path.append(os.path.abspath('..'))

import sqlite3
from Clases.medic import Medic


class MedicManager:
    '''
    Gestiona los objetos de la clase Medic en la base de datos
    '''

    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def __getMedicSets(self, rows):
        '''
        Crea un objeto Medic a partir registros de la base de datos

        rows = lista registro de la base de datos
        resultado = Juicio Clínico(Medic)
        '''

        result = set()
        if rows is None:
            return result
        for row in rows:
            obtainedMedic = Medic(
                self.__connection,
                row["NPC"],
                row["name"],
                row["surnames"],
                row["specialty"],
            )
            result.add(obtainedMedic)
        return result

    def getMedicBaseSQL(self):
        '''
        Contiene las consultas de los métodos de colecciones
        de médicos.
        resultado = devuelve el contenido de las consultas
        '''

        query = 'SELECT npc, name, surnames, specialty '
        query += 'FROM Medic '
        return query

    def getAllMedics(self):
        '''
        Devuelve una coleccion con todos los objetos tipo Medic
        de la base de datos.

        resultado = devolvera un conjunto de objetos tipo Medic
        '''

        query = 'SELECT npc, name, surnames, specialty '
        query += 'FROM Medic'
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getMedicSets(rows)

    def getMedicByNPCs(self, *npcs):
        '''
        Devuelve una coleccion de objetos tipo Medic según
        sus NPC.

        npcs = coleccion de npc correspondientes a Medic
        resultado = devolvera un conjunto de objetos tipo Medic
        '''

        query = self.getMedicBaseSQL()
        if len(npcs) > 1:
            query += 'WHERE npc IN {}'.format(npcs)
        elif len(npcs) == 1:
            query += 'WHERE npc = {}'.format(npcs[0])
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getMedicSets(rows)

    def getMedicByNPC(self, npc):
        '''
        Devuelve una coleccion de objetos tipo Medic según
        parte del NPC

        npc = contendrá parte del npc de un médico (str)
        resultado = devolvera un conjunto de objetos tipo Medic
        '''

        query = self.getMedicBaseSQL()
        query += 'WHERE npc LIKE ?'
        self.__cursor.execute(query, (f'%{npc}%',))
        rows = self.__cursor.fetchall()
        return self.__getMedicSets(rows)

    def getMedicByName(self, name):
        '''
        Devuelve una coleccion de objetos tipo Medic segun su nombre

        name = contendrá parte del nombre de un médico (str)
        resultado = devolvera un conjunto de objetos tipo Medic
        '''

        query = self.getMedicBaseSQL()
        query += 'WHERE lower(name) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{name}%',))
        rows = self.__cursor.fetchall()
        return self.__getMedicSets(rows)

    def getMedicBySurnames(self, surnames):
        '''
        Devuelve una coleccion de objetos tipo Medic segun sus apellidos

        surname = contendrá parte del apellido de un Médico (str)
        resultado = devolvera un conjunto de objetos tipo Medic
        '''

        query = self.getMedicBaseSQL()
        query += 'WHERE lower(surnames) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{surnames}%',))
        rows = self.__cursor.fetchall()
        return self.__getMedicSets(rows)

    def getMedicBySpecialty(self, specialty):
        '''
        Devuelve una coleccion de objetos tipo Medic segun su especialidad

        specialty = contendrá parte de la especialidad de un Médico (str)
        resultado = devolvera un conjunto de objetos tipo Medic
        '''

        query = self.getMedicBaseSQL()
        query += 'WHERE lower(specialty) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{specialty}%',))
        rows = self.__cursor.fetchall()
        return self.__getMedicSets(rows)
