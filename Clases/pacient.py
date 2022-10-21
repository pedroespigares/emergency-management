import sqlite3


class Pacient:
    '''
    Representa los pacientes de un
    servicio de urgencias hospitalaria
    '''

    def __init__(
        self,
        connection,
        dni,
        history_number = None,
        name = None,
        surnames = None,
        birthday = None,
        nationality = None,
        sex = None,
        social_security = None,
        phone = None,
        address = None,
        history_status = None
    ):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()
        self.__dni = dni

        if history_number is not None and not isinstance(history_number, int):
            raise TypeError("El historial debe ser número entero")
        else:
            self.__history_number = history_number

        self.__name = name
        self.__surnames = surnames
        self.__birthday = birthday
        self.__nationality = nationality

        if sex == 'H' or sex == 'M' or sex == 'O' or sex is None:
            self.__sex = sex
        else:
            raise ValueError("El sexo solo puede ser H, M u O")

        self.__social_security = social_security
        self.__phone = phone
        self.__address = address
        self.__history_status = history_status

    def __str__(self):
        string = f'\nDNI: {self.__dni}\n'
        if self.__history_number is not None:
            string += f'Número de historia: {self.__history_number} \n'
        if self.__name is not None:
            string += f'Nombre: {self.__name}\n'
        if self.__surnames is not None:
            string += f'Apellidos: {self.__surnames}\n'
        if self.__birthday is not None:
            string += f'Fecha de nacimiento: {self.__birthday}\n'
        if self.__nationality is not None:
            string += f'Nacionalidad: {self.__nationality}\n'
        if self.__sex is not None:
            string += f'Sexo: {self.__sex}\n'
        if self.__social_security is not None:
            string += f'Seguridad Social: {self.__social_security}\n'
        if self.__phone is not None:
            string += f'Teléfono: {self.__phone}\n'
        if self.__address is not None:
            string += f'Dirección: {self.__address}\n'
        if self.__history_status is not None:
            string += f'Estado de historia: {self.__history_status}\n\n'
        string += '----------------------------------------------'
        return string

    def setHistoryNumber(self, newHistory):
        self.__history_number = newHistory

    def setName(self, newName):
        self.__name = newName

    def setSurnames(self, newSurnames):
        self.__surnames = newSurnames

    def setBirthday(self, newBirthday):
        self.__birthday = newBirthday

    def setNationality(self, newNationality):
        self.__nationality = newNationality

    def setSex(self, newSex):
        self.__sex = newSex

    def setSocialSecurity(self, newSocialSecurity):
        self.__social_security = newSocialSecurity

    def setPhone(self, newPhone):
        self.__phone = newPhone

    def setAddress(self, newAddress):
        self.__address = newAddress

    def setStatus(self, newStatus):
        self.__history_status = newStatus

    def getDNI(self):
        return self.__dni

    def getName(self):
        return self.__name

    def getSurnames(self):
        return self.__surnames

    def save(self):
        '''
        Añade un nuevo paciente a la base de datos.
        '''

        query = 'INSERT INTO Pacient (DNI, history_number, '
        query += 'name, surnames, birthday, nationality, '
        query += 'sex, social_security, phone, '
        query += 'address, history_status) '
        query += 'VALUES (?, ?, ?, ?, ?, ?, ? ,?, '
        query += '?, ?, ?)'
        values = (
            self.__dni,
            self.__history_number,
            self.__name,
            self.__surnames,
            self.__birthday,
            self.__nationality,
            self.__sex,
            self.__social_security,
            self.__phone,
            self.__address,
            self.__history_status,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def load(self):
        '''
        Carga en memoria un paciente de la base de datos.
        '''

        query = 'SELECT history_number, name, surnames, birthday, '
        query += 'nationality, sex, social_security, phone, '
        query += 'address, history_status '
        query += 'FROM Pacient '
        query += 'WHERE DNI = ?'
        self.__cursor.execute(query, (self.__dni,))
        self.setAttributes()

    def setAttributes(self):
        '''
        Asigna los atributos del objeto Paciente tras la carga
        de en memoria del paciente de la base de datos.
        '''
        row = self.__cursor.fetchone()
        self.__history_number = row["history_number"]
        self.__name = row["name"]
        self.__surnames = row["surnames"]
        self.__birthday = row["birthday"]
        self.__nationality = row["nationality"]
        self.__sex = row["sex"]
        self.__social_security = row["social_security"]
        self.__phone = row["phone"]
        self.__address = row["address"]
        self.__history_status = row["history_status"]

    def update(self):
        '''
        Actualiza los datos de un paciente existente en la base de datos.
        '''

        query = 'UPDATE Pacient SET history_number = ?, '
        query += 'name = ?, surnames = ?, birthday = ?, nationality = ?, '
        query += 'sex = ?, social_security = ?, phone = ?, address = ?, '
        query += 'history_status = ? WHERE DNI = ?'
        values = (
            self.__history_number,
            self.__name,
            self.__surnames,
            self.__birthday,
            self.__nationality,
            self.__sex,
            self.__social_security,
            self.__phone,
            self.__address,
            self.__history_status,
            self.__dni,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def delete(self):
        '''
        Borra un paciente existente en la base de datos.
        '''

        query = 'DELETE FROM Pacient WHERE DNI = ?'
        self.__cursor.execute(query, (self.__dni,))
        self.__connection.commit()
