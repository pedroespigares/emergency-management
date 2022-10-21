import sqlite3
from Clases.urgency import Urgency


class Radiology:
    '''
    Representa las radiologías que se
    realizan en un servicio de urgencias
    '''

    def __init__(
        self,
        connection,
        urgency,
        petition,
        pregnancy=False,
        contrast=False,
        informed_consent=True
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

        self.__pregnancy = pregnancy
        self.__contrast = contrast
        self.__informed_consent = informed_consent
       

    def __str__(self):
        string = f'\nUrgencia: {self.__urgency.getEpisode()}\n'
        string += f'Petición: {self.__petition}\n'
        if self.__pregnancy is not None:
            if self.__pregnancy == 0:
                string += f'Embarazo: No\n'
            elif self.__pregnancy == 1:
                string += f'Embarazo: Sí\n'
        if self.__contrast is not None:
            if self.__contrast == 0:
                string += f'Contraste: No\n'
            elif self.__contrast == 1:
                string += f'Contraste: Sí\n'
        if self.__informed_consent is not None:
            if self.__informed_consent == 0:
                string += f'Consentimiento informado: No\n\n'
            if self.__informed_consent == 1:
                string += f'Consentimiento informado: Sí\n\n'
        string += '----------------------------------------------'
        return string

    def setPetition(self, newPetition):
        self.__petition = newPetition

    def setPregnancy(self, newPregnancy):
        self.__pregnancy = newPregnancy

    def setContrast(self, newContrast):
        self.__contrast = newContrast

    def setConsent(self, newConsent):
        self.__informed_consent = newConsent

    def save(self):
        '''
        Añade una nueva radiología a la base de datos.
        '''

        query = 'INSERT INTO Radiology '
        query += '(urgency, petition, '
        query += 'pregnancy, contrast, '
        query += 'informed_consent) '
        query += 'VALUES (?, ?, ?, ?, ?)'
        values = (
            self.__urgency.getEpisode(),
            self.__petition,
            self.__pregnancy,
            self.__contrast,
            self.__informed_consent,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def load(self):
        '''
        Carga en memoria una oxigenoterapia de la base de datos.
        '''

        query = 'SELECT petition, pregnancy, '
        query += 'contrast, '
        query += 'informed_consent '
        query += 'FROM Radiology '
        query += 'WHERE urgency = ?'
        self.__cursor.execute(query, (self.__urgency.getEpisode(),))
        row = self.__cursor.fetchone()
        self.__petition = row["petition"]
        self.__pregnancy = row["pregnancy"]
        self.__contrast = row["contrast"]
        self.__informed_consent = row["informed_consent"]

    def update(self):
        '''
        Actualiza los datos de una radiología existente en la base de datos.
        '''

        query = 'UPDATE Radiology '
        query += 'SET petition = ?, '
        query += 'pregnancy = ?, '
        query += 'contrast = ?, '
        query += 'informed_consent = ? '
        query += 'WHERE urgency = ?'
        values = (
            self.__petition,
            self.__pregnancy,
            self.__contrast,
            self.__informed_consent,
            self.__urgency.getEpisode(),
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def delete(self):
        '''
        Borra una oxigenoterapia existente en la base de datos.
        '''

        query = 'DELETE FROM Radiology WHERE petition = ?'
        self.__cursor.execute(query, (self.__petition,))
        self.__connection.commit()
