import os
import sys
sys.path.append(os.path.abspath('..'))

import sqlite3
from Clases.clinicalJudgment import ClinicalJudgment


class ClinicalJudgmentManager:
    '''
    Gestiona los objetos de la clase ClinicalJudgment en la base de datos
    '''

    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def __getClinicalJudgmentSets(self, rows):
        '''
        Crea un objeto ClinicalJudgment a partir registros de la base de datos

        rows = lista registro de la base de datos
        resultado = Juicio Clínico(ClinicalJudgment)
        '''

        result = set()
        if rows is None:
            return result
        for row in rows:
            obtainedJudgment = ClinicalJudgment(
                self.__connection,
                row["code"],
                row["description"],
            )
            result.add(obtainedJudgment)
        return result

    def getClinicalJudgmentBaseSQL(self):
        '''
        Contiene las consultas de los métodos de colecciones
        de juicios clínicos
        resultado = devuelve el contencodeo de las consultas
        '''

        query = 'SELECT code, description '
        query += 'FROM Clinical_Judgment '
        return query

    def getAllClinicalJudgment(self):
        '''
        Devuelve una coleccion con todos los objetos tipo ClinicalJudgment
        de la base de datos.

        resultado = devolvera un conjunto de objetos tipo ClinicalJudgment
        '''

        query = 'SELECT code, description '
        query += 'FROM Clinical_Judgment'
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getClinicalJudgmentSets(rows)

    def getClinicalJudgmentByCodes(self, *codes):
        '''
        Devuelve una coleccion de objetos tipo ClinicalJudgment según
        sus códigos.

        codes = coleccion de códigos correspondientes a ClinicalJudgment
        resultado = devolvera un conjunto de objetos tipo ClinicalJudgment
        '''

        query = self.getClinicalJudgmentBaseSQL()
        if len(codes) > 1:
            query += 'WHERE code IN {}'.format(codes)
        elif len(codes) == 1:
            query += 'WHERE code = {}'.format(codes[0])
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getClinicalJudgmentSets(rows)

    def getClinicalJudgmentByCode(self, code):
        '''
        Devuelve una coleccion de objetos tipo ClinicalJudgment segun
        parte del código

        code = contendrá parte del código de un juicio clínico (str)
        resultado = devolvera un conjunto de objetos tipo ClinicalJudgment
        '''

        query = self.getClinicalJudgmentBaseSQL()
        query += 'WHERE code LIKE ?'
        self.__cursor.execute(query, (f'%{code}%',))
        rows = self.__cursor.fetchall()
        return self.__getClinicalJudgmentSets(rows)

    def getClinicalJudgmentByDescription(self, description):
        '''
        Devuelve una coleccion de objetos tipo ClinicalJudgment
        segun su descripción

        medic = contendrá parte de la descripción de un juicio médico (str)
        resultado = devolvera un conjunto de objetos tipo ClinicalJudgment
        '''

        query = self.getClinicalJudgmentBaseSQL()
        query += 'WHERE lower(description) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{description}%',))
        rows = self.__cursor.fetchall()
        return self.__getClinicalJudgmentSets(rows)
