import os
import sys
sys.path.append(os.path.abspath('..'))

import sqlite3
from Clases.pacient import Pacient


class PacientManager:
    '''
    Gestiona los objetos de la clase Pacient en la base de datos
    '''

    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def __getPacientSets(self, rows):
        '''
        Crea un objeto Pacient a partir registros de la base de datos

        rows = lista registro de la base de datos
        resultado = Paciente(Pacient)
        '''

        result = set()
        if rows is None:
            return result
        for row in rows:
            obtainedPacient = Pacient(
                self.__connection,
                row["DNI"],
                row["history_number"],
                row["name"],
                row["surnames"],
                row["birthday"],
                row["nationality"],
                row["sex"],
                row["social_security"],
                row["phone"],
                row["address"],
                row["history_status"],
            )
            result.add(obtainedPacient)
        return result

    def getPacientBaseSQL(self):
        '''
        Contiene las consultas de los métodos de colecciones
        de pacientes
        resultado = devuelve el contendnio de las consultas
        '''

        query = 'SELECT DNI, history_number, name, surnames, birthday, '
        query += 'nationality, sex, social_security, phone, '
        query += 'address, history_status '
        query += 'FROM Pacient '
        return query

    def getAllPacients(self):
        '''
        Devuelve una coleccion con todos los objetos tipo Pacient
        de la base de datos.

        resultado = devolvera un conjunto de objetos tipo Pacient
        '''

        query = 'SELECT DNI, history_number, name, surnames, birthday, '
        query += 'nationality, sex, social_security, phone, '
        query += 'address, history_status '
        query += 'FROM Pacient'
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getPacientSets(rows)

    def getPacientsByDNIs(self, *dni):
        '''
        Devuelve una coleccion de objetos tipo Pacient según
        sus dni.

        dni = coleccion de DNIs correspondientes a Pacient
        resultado = devolvera un conjunto de objetos tipo Pacient
        '''

        query = self.getPacientBaseSQL()
        if len(dni) > 1:
            query += 'WHERE dni IN {}'.format(dni)
        elif len(dni) == 1:
            query += 'WHERE dni = {}'.format(dni[0])
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getPacientSets(rows)

    def getPacientByDNI(self, dni):
        '''
        Devuelve una coleccion de objetos tipo Pacient según
        parte del dni.

        dni = parte del DNI correspondiente a Pacient
        resultado = devolvera un conjunto de objetos tipo Pacient
        '''

        query = self.getPacientBaseSQL()
        query += 'WHERE dni LIKE ?'
        dni = dni.strip()
        self.__cursor.execute(query, (f'%{dni}%',))
        rows = self.__cursor.fetchall()
        return self.__getPacientSets(rows)

    def getPacientByHistoryNumber(self, history_number):
        '''
        Devuelve una coleccion de objetos tipo Pacient segun su número
        de historial.

        history_number = contendrá parte del número de
        historial de un paciente (str)
        resultado = devolvera un conjunto de objetos tipo Pacient
        '''

        query = self.getPacientBaseSQL()
        query += 'WHERE history_number LIKE ?' 
        self.__cursor.execute(query, (f'%{history_number}%',))
        rows = self.__cursor.fetchall()
        return self.__getPacientSets(rows)

    def getPacientByName(self, name):
        '''
        Devuelve una coleccion de objetos tipo Pacient segun su nombre

        name = contendrá parte del nombre de un paciente (str)
        resultado = devolvera un conjunto de objetos tipo Pacient
        '''

        query = self.getPacientBaseSQL()
        query += 'WHERE lower(name) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{name}%',))
        rows = self.__cursor.fetchall()
        return self.__getPacientSets(rows)

    def getPacientBySurnames(self, surnames):
        '''
        Devuelve una coleccion de objetos tipo Pacient segun sus apelldnios

        surname = contendrá parte del apellido de un paciente (str)
        resultado = devolvera un conjunto de objetos tipo Pacient
        '''

        query = self.getPacientBaseSQL()
        query += 'WHERE lower(surnames) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{surnames}%',))
        rows = self.__cursor.fetchall()
        return self.__getPacientSets(rows)

    def getPacientByBirthday(self, birthday):
        '''
        Devuelve una coleccion de objetos tipo Pacient según su
        fecha de nacimiento.

        entry = contendrá parte de la fecha de entrada (str)
        resultado = devolvera un conjunto de objetos tipo Pacient
        '''

        query = self.getPacientBaseSQL()
        query += 'WHERE birthday LIKE ?'
        birthday = birthday.strip()
        self.__cursor.execute(query, (f'%{birthday}%',))
        rows = self.__cursor.fetchall()
        return self.__getPacientSets(rows)

    def getPacientByNationality(self, nationality):
        '''
        Devuelve una coleccion de objetos tipo Pacient segun su nacionaldniad.

        nationality = contendrá parte de la nacionaldniad del paciente (str)
        resultado = devolvera un conjunto de objetos tipo Pacient
        '''

        query = self.getPacientBaseSQL()
        query += 'WHERE lower(nationality) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{nationality}%',))
        rows = self.__cursor.fetchall()
        return self.__getPacientSets(rows)

    def getPacientBySex(self, sex):
        '''
        Devuelve una coleccion de objetos tipo Pacient segun su sexo.

        sex = contendrá un sexo:
            - H (Hombre)
            - M (Mujer)
            - O (Otro)
        resultado = devolvera un conjunto de objetos tipo Pacient
        '''

        query = self.getPacientBaseSQL()
        query += 'WHERE sex = ?'
        self.__cursor.execute(query, (sex,))
        rows = self.__cursor.fetchall()
        return self.__getPacientSets(rows)

    def getPacientBySocialSecurity(self, social_security):
        '''
        Devuelve una coleccion de objetos tipo Pacient segun su número de
        seguridad social.

        social_security = contendrá parte del número de la
        seguridad social del paciente (str)
        resultado = devolvera un conjunto de objetos tipo Pacient
        '''

        query = self.getPacientBaseSQL()
        query += 'WHERE social_security LIKE ?'
        self.__cursor.execute(query, (f'%{social_security}%',))
        rows = self.__cursor.fetchall()
        return self.__getPacientSets(rows)

    def getPacientByPhone(self, phone):
        '''
        Devuelve una coleccion de objetos tipo Pacient segun su número de
        teléfono.

        phone = contendrá parte del teléfono del paciente (str)
        resultado = devolvera un conjunto de objetos tipo Pacient
        '''

        query = self.getPacientBaseSQL()
        query += 'WHERE phone LIKE ?'
        self.__cursor.execute(query, (f'%{phone}%',))
        rows = self.__cursor.fetchall()
        return self.__getPacientSets(rows)

    def getPacientByAddress(self, address):
        '''
        Devuelve una coleccion de objetos tipo Pacient segun su dirección.

        address = contendrá parte de la dirección del paciente (str)
        resultado = devolvera un conjunto de objetos tipo Pacient
        '''

        query = self.getPacientBaseSQL()
        query += 'WHERE lower(address) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{address}%',))
        rows = self.__cursor.fetchall()
        return self.__getPacientSets(rows)

    def getPacientByHistoryStatus(self, status):
        '''
        Devuelve una coleccion de objetos tipo Pacient segun el estado
        de su historial.

        status = contendrá un estado:
            - Activo (Hombre)
            - Pasivo (Mujer)
        resultado = devolvera un conjunto de objetos tipo Pacient
        '''

        query = self.getPacientBaseSQL()
        query += 'WHERE lower(history_status) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{status}%',))
        rows = self.__cursor.fetchall()
        return self.__getPacientSets(rows)

    def deleteDeadPacients(self):
        '''
        Borra un paciente existente en la base de datos
        donde su estado clínico sea "pasivo".
        '''

        query = 'DELETE FROM Pacient WHERE history_status = "Pasivo"'
        self.__cursor.execute(query)
        self.__connection.commit()

    def loadPacientsByFile(self, file):
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
                    int(stripped_data[1]),
                    stripped_data[2],
                    stripped_data[3],
                    stripped_data[4],
                    stripped_data[5],
                    stripped_data[6],
                    stripped_data[7],
                    stripped_data[8],
                    stripped_data[9],
                )
                result.add(obtainedPacient)
            return result