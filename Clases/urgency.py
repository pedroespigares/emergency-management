import sqlite3

from Clases.pacient import Pacient
from Clases.medic import Medic


class Urgency:
    '''
    Representa las urgencias que trabajan
    en servicio de urgencias
    '''

    def __init__(
        self,
        connection,
        pacient,
        episode,
        medic=None,
        status=None,
        entry=None,
        reason=None,
        exploration=None,
        recomendation=None,
        exit=None,
    ):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()
        
        if pacient is not None and not isinstance(pacient, Pacient):
            raise TypeError("El paciente deber pertenecer a la clase Pacient")
        else:
            self.__pacient = pacient

        if medic is not None and not isinstance(medic, Medic):
            raise TypeError("El médico deber pertenecer a la clase Medic")
        else:
            self.__medic = medic

        if not isinstance(episode, int):
            raise TypeError("El episodio debe ser número entero")
        else:
            self.__episode = episode

        self.__status = status
        self.__entry = entry
        self.__reason = reason
        self.__exploration = exploration
        self.__recomendation = recomendation
        self.__exit = exit
        self.__clinicalJudgment = []

    def __str__(self):
        string = f'''\nPaciente: {self.__pacient.getDNI()} - {self.__pacient.getName()} {self.__pacient.getSurnames()}\n'''
        if self.__episode is not None:
            string += f'Episodio: {self.__episode} \n'
        if self.__medic is not None:
            string += f'''Médico: {self.__medic.getNPC()} - {self.__medic.getName()} {self.__medic.getSurnames()}\n'''
        if self.__status is not None:
            string += f'Estado: {self.__status}\n'
        if self.__entry is not None:
            string += f'Entrada: {self.__entry}\n'
        if self.__reason is not None:
            string += f'Motivo: {self.__reason}\n'
        if self.__exploration is not None:
            string += f'Exploración: {self.__exploration}\n'
        if self.__recomendation is not None:
            string += f'Recomendación: {self.__recomendation}\n'
        if self.__exit is not None:
            string += f'Salida: {self.__exit}\n'
        string += f'Juicios Clínicos: \n'
        if self.__clinicalJudgment != []:
            for judgment in self.__clinicalJudgment:
                string += f'- {judgment.getCode()} --> '
                if judgment.getDescription() is not None:
                    string += f'{judgment.getDescription()}\n'
                else:
                        string += '\n'
        string += '----------------------------------------------'
        return string

    def setPacient(self, newPacient):
        self.__pacient = newPacient

    def setMedic(self, newMedic):
        self.__medic = newMedic

    def setStatus(self, newStatu):
        self.__status = newStatu

    def setEntry(self, newEntry):
        self.__entry = newEntry

    def setReason(self, newReason):
        self.__reason = newReason

    def setExploration(self, newExploration):
        self.__exploration = newExploration

    def setRecomendation(self, newRecomendation):
        self.__recomendation = newRecomendation

    def setExit(self, newExit):
        self.__exit = newExit

    def getEpisode(self):
        return self.__episode

    def getStatus(self):
        return self.__status

    def getPacient(self):
        return self.__pacient.getDNI()

    def addClinicalJudgment(self, judgment):
        '''
        Guarda en la lista de de juicios clínicos un juicio clínico
        '''
        self.__clinicalJudgment.append(judgment)

    def save(self):
        '''
        Añade una nuevo urgencia a la base de datos.
        '''

        query = 'INSERT INTO Urgency (episode, pacient, '
        query += 'medic, status, entry, reason, '
        query += 'exploration, recomendation, exit) '
        query += 'VALUES (?, ?, ?, ?, ?, ?, ? ,?, ?)'
        values = (
            self.__episode,
            self.__pacient.getDNI(),
            self.__medic.getNPC(),
            self.__status,
            self.__entry,
            self.__reason,
            self.__exploration,
            self.__recomendation,
            self.__exit,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def load(self):
        '''
        Carga en memoria una urgencia de la base de datos.
        '''

        query = 'SELECT pacient, medic, '
        query += 'status, entry, reason, '
        query += 'exploration, recomendation, exit '
        query += 'FROM Urgency '
        query += 'WHERE episode = ?'
        self.__cursor.execute(query, (self.__episode,))
        self.setAttributes()

    def setAttributes(self):
        '''
        Asigna los atributos del objeto Urgencia tras la carga
        de en memoria del paciente de la base de datos.
        '''
        row = self.__cursor.fetchone()
        self.__pacient = row["pacient"]
        self.__medic = row["medic"]
        self.__status = row["status"]
        self.__entry = row["entry"]
        self.__reason = row["reason"]
        self.__exploration = row["exploration"]
        self.__recomendation = row["recomendation"]
        self.__exit = row["exit"]

    def update(self):
        '''
        Actualiza los datos de un Urgencia existente en la base de datos.
        '''

        query = 'UPDATE Urgency SET pacient = ?, '
        query += 'medic = ?, status = ?, entry = ?, reason = ?, '
        query += 'exploration = ?, recomendation = ?, '
        query += 'exit = ? WHERE episode = ?'
        values = (
            self.__pacient.getDNI(),
            self.__medic.getNPC(),
            self.__status,
            self.__entry,
            self.__reason,
            self.__exploration,
            self.__recomendation,
            self.__exit,
            self.__episode,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def delete(self):
        '''
        Borra un Urgencia existente en la base de datos.
        '''

        query = 'DELETE FROM Urgency WHERE episode = ?'
        self.__cursor.execute(query, (self.__episode,))
        self.__connection.commit()

    def saveUrgencyWithClinicalJudgments(self):
        '''
        Añade a la tabla "References" la relación entre un objeto Urgency
        y uno o varios objetos ClinicalJudgment.
        '''

        if self.__episode is None:
            raise TypeError('El atributo episodio debe tener valor')
        if self.__clinicalJudgment == []:
            raise TypeError('El atributo juicio clínico debe tener valor')
        query = 'INSERT OR REPLACE INTO Reference (urgency, '
        query += 'clinical_judgment) VALUES (?, ?)'
        for judgment in self.__clinicalJudgment:
            self.__cursor.execute(query, (self.__episode, judgment,))
        self.__connection.commit()
