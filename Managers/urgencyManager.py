import os
import sys
sys.path.append(os.path.abspath('..'))

import sqlite3
from Clases.pacient import Pacient
from Clases.medic import Medic
from Clases.urgency import Urgency


class UrgencyManager:
    '''
    Gestiona los objetos de la clase Urgency en la base de datos
    '''

    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def __getUrgencySets(self, rows):
        '''
        Crea un objeto Urgency a partir registros de la base de datos

        rows = lista registro de la base de datos
        resultado == Urgencia(Urgency)
        '''

        result = set()
        if rows is None:
            return result
        for row in rows:
            obtainedPacient = Pacient(
                self.__connection,
                row["pacient"]
            )
            obtainedPacient.load()
            obtainedMedic = Medic(
                self.__connection,
                row["medic"]
            )
            obtainedMedic.load()
            obtainedUrgency = Urgency(
                self.__connection,
                obtainedPacient,
                row["episode"],
                obtainedMedic,
                row["status"],
                row["entry"],
                row["reason"],
                row["exploration"],
                row["recomendation"],
                row["exit"]
            )
            result.add(obtainedUrgency)
        return result

    def getUrgencyBaseSQL(self):
        '''
        Contiene las consultas de los métodos de colecciones
        de urgencias
        resultado = devuelve el contenepisodeo de las consultas
        '''

        query = 'SELECT episode, pacient, medic, '
        query += 'status, entry, reason, '
        query += 'exploration, recomendation, exit '
        query += 'FROM Urgency '
        return query

    def getAllUrgency(self):
        '''
        Devuelve una coleccion con todos los objetos tipo Urgency
        de la base de datos.

        resultado = devolvera un conjunto de objetos tipo Urgency
        '''

        query = 'SELECT episode, pacient, medic, '
        query += 'status, entry, reason, '
        query += 'exploration, recomendation, exit '
        query += 'FROM Urgency'
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getUrgencySets(rows)

    def getUrgencyByEpisodes(self, *episodes):
        '''
        Devuelve una coleccion de objetos tipo Urgency según
        sus episodios.

        episodes = coleccion de episodes correspondientes a Urgency
        resultado = devolvera un conjunto de objetos tipo Urgency
        '''

        query = self.getUrgencyBaseSQL()
        if len(episodes) > 1:
            query += 'WHERE episode IN {}'.format(episodes)
        elif len(episodes) == 1:
            query += 'WHERE episode = {}'.format(episodes[0])
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getUrgencySets(rows)

    def getUrgencyByEpisode(self, episode):
        '''
        Devuelve una coleccion de objetos tipo Urgency segun el episodio

        pacient = contendrá parte del Episodio de una urgencia (str)
        resultado = devolvera un conjunto de objetos tipo Urgency
        '''

        query = self.getUrgencyBaseSQL()
        query += 'WHERE lower(episode) LIKE lower(?)'
        episode = episode.strip()
        self.__cursor.execute(query, (f'%{episode}%',))
        rows = self.__cursor.fetchall()
        return self.__getUrgencySets(rows)

    def getUrgencyByPacient(self, pacient):
        '''
        Devuelve una coleccion de objetos tipo Urgency segun el paciente

        pacient = contendrá parte del DNI de un paciente (str)
        resultado = devolvera un conjunto de objetos tipo Urgency
        '''

        query = self.getUrgencyBaseSQL()
        query += 'WHERE lower(pacient) LIKE lower(?)'
        pacient = pacient.strip()
        self.__cursor.execute(query, (f'%{pacient}%',))
        rows = self.__cursor.fetchall()
        return self.__getUrgencySets(rows)

    def getUrgencyByMedic(self, medic):
        '''
        Devuelve una coleccion de objetos tipo Urgency segun el medico

        medic = contendrá parte del NPC de un medico (str)
        resultado = devolvera un conjunto de objetos tipo Urgency
        '''

        query = self.getUrgencyBaseSQL()
        query += 'WHERE medic LIKE ?'
        medic = medic.strip()
        self.__cursor.execute(query, (f'%{medic}%',))
        rows = self.__cursor.fetchall()
        return self.__getUrgencySets(rows)

    def getUrgencyByStatus(self, status):
        '''
        Devuelve una coleccion de objetos tipo Urgency segun el estado

        status = contendrá un estado de urgencia:
            - Ingreso
            - Observacion
            - Alta
            - Exitus
        resultado = devolvera un conjunto de objetos tipo Urgency
        '''

        query = self.getUrgencyBaseSQL()
        query += 'WHERE lower(status) = lower(?)'
        status = status.strip()
        self.__cursor.execute(query, (status,))
        rows = self.__cursor.fetchall()
        return self.__getUrgencySets(rows)

    def getUrgencyByEntry(self, entry):
        '''
        Devuelve una coleccion de objetos tipo Urgency
        según el la fecha de entrada

        entry = contendrá parte de la fecha de entrada (str)
        resultado = devolvera un conjunto de objetos tipo Urgency
        '''

        query = self.getUrgencyBaseSQL()
        query += 'WHERE entry LIKE ?'
        entry = entry.strip()
        self.__cursor.execute(query, (f'%{entry}%',))
        rows = self.__cursor.fetchall()
        return self.__getUrgencySets(rows)

    def getUrgencyByReason(self, reason):
        '''
        Devuelve una coleccion de objetos tipo Urgency segun la razón.

        reason = contendrá parte de la razón de entrada (str)
        resultado = devolvera un conjunto de objetos tipo Urgency
        '''

        query = self.getUrgencyBaseSQL()
        query += 'WHERE lower(reason) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{reason}%',))
        rows = self.__cursor.fetchall()
        return self.__getUrgencySets(rows)

    def getUrgencyByExploration(self, exploration):
        '''
        Devuelve una coleccion de objetos tipo Urgency segun la exploración.

        exploration = contendrá parte de la exploración en la urgencia (str)
        resultado = devolvera un conjunto de objetos tipo Urgency
        '''

        query = self.getUrgencyBaseSQL()
        query += 'WHERE lower(exploration) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{exploration}%',))
        rows = self.__cursor.fetchall()
        return self.__getUrgencySets(rows)

    def getUrgencyByRecomendation(self, recomendation):
        '''
        Devuelve una coleccion de objetos tipo Urgency segun la recomendación.

        recomendation = contendrá parte de la recomendación
        en la urgencia (str)
        resultado = devolvera un conjunto de objetos tipo Urgency
        '''

        query = self.getUrgencyBaseSQL()
        query += 'WHERE lower(recomendation) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{recomendation}%',))
        rows = self.__cursor.fetchall()
        return self.__getUrgencySets(rows)

    def getUrgencyByExit(self, exitDate):
        '''
        Devuelve una coleccion de objetos tipo Urgency
        según la fecha de salepisodea.

        exit = contendrá parte de la fecha de salepisodea en la urgencia (str)
        resultado = devolvera un conjunto de objetos tipo Urgency
        '''

        query = self.getUrgencyBaseSQL()
        query += 'WHERE entry LIKE ?'
        exitDate = exitDate.strip()
        self.__cursor.execute(query, (f'%{exitDate}%',))
        rows = self.__cursor.fetchall()
        return self.__getUrgencySets(rows)

    def deleteAllUrgenciesFromPacient(self, pacientToDelete):
        '''
        Borra de la base de datos todos las urgencias que tengan como
        paciente el pasado por parámetro
        '''

        query = 'DELETE FROM Urgency WHERE pacient = ?'
        self.__cursor.execute(query, (pacientToDelete.getDNI(),))
        self.__connection.commit()

    def deleteAllUrgenciesFromDeadPacients(self):
        '''
        Borra de la base de datos todos las urgencias que tengan como
        paciente el pasado por parámetro
        '''

        query = 'DELETE FROM Urgency WHERE pacient IN (SELECT DNI FROM '
        query += 'Pacient WHERE history_status = "Pasivo")'
        self.__cursor.execute(query)
        self.__connection.commit()

    def deleteAllUrgenciesStatusDischarge(self):
        '''
        Borra de la base de datos todos las urgencias que tengan como
        estado dado de alta
        '''
        query = 'DELETE FROM Urgency WHERE status = "Alta"'
        self.__cursor.execute(query)
        self.__connection.commit()

    def deleteAllUrgenciesStatusExitus(self):
        '''
        Borra de la base de datos todos las urgencias que tengan como
        estado dado exitus(fallecido)
        '''
        query = 'DELETE FROM Urgency WHERE status = "Exitus"'
        self.__cursor.execute(query)
        self.__connection.commit()

    def deleteAllUrgenciesStatusHospitalization(self):
        '''
        Borra de la base de datos todos las urgencias que tengan como
        estado dado Ingreso
        '''
        query = 'DELETE FROM Urgency WHERE status = "Ingreso"'
        self.__cursor.execute(query)
        self.__connection.commit()

    def loadUrgencyByFile(self, file):
        '''
        Extrae los datos de cada una de las lineas con contenido del
        archivo de entrada y crea un objeto Pacient por cada línea.

        file = nombre del archivo de entrada (str)
        '''
        with open(file, encoding='utf-8') as file:
            strip_lines = [line.strip() for line in file]
            lines_with_content = [line for line in strip_lines if line]
            result = set()
            for line in lines_with_content:
                data = line.split(",")
                stripped_data = [value.strip() for value in data]
                for i in range(len(stripped_data)):
                    if stripped_data[i] == '':
                        stripped_data[i] = None
                obtainedPacient = Pacient(
                    self.__connection,
                    stripped_data[0],
                )
                obtainedPacient.load()
                obtainedMedic = Medic(
                    self.__connection,
                    int(stripped_data[2]),
                )
                obtainedMedic.load()
                obtainedUrgency = Urgency(
                    self.__connection,
                    obtainedPacient,
                    int(stripped_data[1]),
                    obtainedMedic,
                    stripped_data[3],
                    stripped_data[4],
                    stripped_data[5],
                    stripped_data[6],
                    stripped_data[7],
                    stripped_data[8],
                )
                result.add(obtainedUrgency)
            return result