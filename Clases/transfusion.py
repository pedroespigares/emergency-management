import sqlite3
from Clases.urgency import Urgency


class Transfusion:
    '''
    Representa las transfusiones que se
    realizan en un servicio de urgencias
    '''

    def __init__(
        self,
        connection,
        urgency,
        petition,
        blood_group=None,
        irh=None,
        previous_transfusion=False,
        religion=None,
        informed_consent=True,
    ):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()
        self.__urgency = urgency
        if urgency is not None and not isinstance(self.__urgency, Urgency):
            raise TypeError('''El atributo Urgency debe ser
            un objeto de tipo Urgency''')

        if not isinstance(petition, int):
            raise TypeError("La petición debe ser número entero")
        else:
            self.__petition = petition

        self.__blood_group = blood_group
        self.__irh = irh
        self.__previous_transfusion = previous_transfusion
        self.__religion = religion
        self.__informed_consent = informed_consent

    def __str__(self):
        string = f'\nUrgencia: {self.__urgency.getEpisode()}\n'
        string += f'Petición: {self.__petition}\n'
        if self.__blood_group is not None:
            string += f'Grupo Sanguíneo: {self.__blood_group}\n'
        if self.__irh is not None:
            string += f'IRH: {self.__irh}\n'
        if self.__previous_transfusion is not None:
            if self.__previous_transfusion == 0:
                string += f'Transfusiones previas: No\n'
            elif self.__previous_transfusion == 1:
                string += f'Transfusiones previas: Sí\n'
        if self.__religion is not None:
            string += f'Religión: {self.__religion}\n'
        if self.__informed_consent is not None:
            if self.__informed_consent == 0:
                string += f'Consentimiento informado: No\n\n'
            elif self.__informed_consent == 1:
                string += f'Consentimiento informado: Sí\n\n'
        string += '----------------------------------------------'
        return string

    def setPetition(self, newPetition):
        self.__petition = newPetition

    def setBloodGroup(self, newBlodGroup):
        self.__blood_group = newBlodGroup

    def setIRH(self, newIRH):
        self.__irh = newIRH

    def setPreviousTransfusion(self, newPreviousTransfusion):
        self.__previous_transfusion = newPreviousTransfusion

    def setReligion(self, newReligion):
        self.__religion = newReligion

    def setConsent(self, newConsent):
        self.__informed_consent = newConsent

    def getReligion(self):
        return self.__religion

    def save(self):
        '''
        Añade una nueva tranfusión a la base de datos.
        '''

        query = 'INSERT INTO Transfusion (urgency, petition, '
        query += 'blood_group, IRH, previous_transfusion, '
        query += 'religion, informed_consent) '
        query += 'VALUES (?, ?, ?, ?, ?, ?, ?)'
        values = (
            self.__urgency.getEpisode(),
            self.__petition,
            self.__blood_group,
            self.__irh,
            self.__previous_transfusion,
            self.__religion,
            self.__informed_consent,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def load(self):
        '''
        Carga en memoria una transfusión de la base de datos.
        '''

        query = 'SELECT petition, blood_group, '
        query += 'IRH, previous_transfusion, '
        query += 'religion, informed_consent '
        query += 'FROM Transfusion WHERE urgency = ?'
        self.__cursor.execute(query, (self.__urgency.getEpisode(),))
        row = self.__cursor.fetchone()
        self.__petition = row["petition"]
        self.__blood_group = row["blood_group"]
        self.__irh = row["IRH"]
        self.__previous_transfusion = row["previous_transfusion"]
        self.__religion = row["religion"]
        self.__informed_consent = row["informed_consent"]

    def update(self):
        '''
        Actualiza los datos de una tranfusión existente en la base de datos.
        '''

        query = 'UPDATE Transfusion SET petition = ?, '
        query += 'blood_group = ?, IRH = ?, '
        query += 'previous_transfusion = ?, '
        query += 'religion = ?, '
        query += 'informed_consent = ? '
        query += 'WHERE urgency = ?'
        values = (
            self.__petition,
            self.__blood_group,
            self.__irh,
            self.__previous_transfusion,
            self.__religion,
            self.__informed_consent,
            self.__urgency.getEpisode(),
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def delete(self):
        '''
        Borra una transfusión existente en la base de datos.
        '''

        query = 'DELETE FROM Transfusion WHERE petition = ?'
        self.__cursor.execute(query, (self.__petition,))
        self.__connection.commit()
