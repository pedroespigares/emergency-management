import os
import sys
sys.path.append(os.path.abspath('.'))

import sqlite3
import unittest
from Clases.medic import Medic


class MedicTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE Medic(
                  npc int primary key,
                  name text,
                  surnames text,
                  specialty text
            )''')

    @classmethod
    def tearDownClass(cls):
        cls.cur.execute('''DROP TABLE Medic''')
        cls.connection.close()

    def test_constructor_AllParams_Ok(self):
        # Given
        npc = 15233
        name = 'Alicia'
        surnames = 'Delago'
        specialty = 'Neurología'

        # When
        myMedic = Medic(
            MedicTest.connection,
            npc,
            name,
            surnames,
            specialty
        )

        # Then
        self.assertIsNotNone(myMedic)
        self.assertIsInstance(myMedic, Medic)

    def test_constructor_OnlyObligatoryParams_Ok(self):
        # Given
        npc = 15233

        # When
        myMedic = Medic(
            MedicTest.connection,
            npc
        )

        # Then
        self.assertIsNotNone(myMedic)
        self.assertIsInstance(myMedic, Medic)

    def test_Save_Ok(self):
        # Given
        npc = 15233
        name = 'Alicia'
        surnames = 'Delago'
        specialty = 'Neurología'
        myMedic = Medic(
            MedicTest.connection,
            npc,
            name,
            surnames,
            specialty
        )

        # When
        myMedic.save()

        # Then
        query = 'SELECT npc, name, surnames, specialty '
        query += 'FROM Medic WHERE npc = ?'
        MedicTest.cur.execute(query, (npc,))
        result = MedicTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['npc'], npc)
        self.assertEqual(result['name'], name)
        self.assertEqual(result['surnames'], surnames)
        self.assertEqual(result['specialty'], specialty)
        self.cur.execute('DELETE FROM Medic WHERE npc = ?', (npc,))

    @unittest.expectedFailure
    def test_load_Fail(self):
        # Given
        npc = 'FailTest'
        myMedic = Medic(
            MedicTest.connection,
            npc,
        )

        # When
        myMedic.load()

    def test_Save_WithSetter_Ok(self):
        # Given
        npc = 15233
        name = 'Alicia'
        surnames = 'Delago'
        specialty = 'Neurología'
        myMedic = Medic(
            MedicTest.connection, npc,)

        # When
        myMedic.setName(name)
        myMedic.setSurnames(surnames)
        myMedic.setSpecialty(specialty)
        myMedic.save()

        # Then
        query = 'SELECT npc, name, surnames, specialty '
        query += 'FROM Medic WHERE npc = ?'
        MedicTest.cur.execute(query, (npc,))
        result = MedicTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['npc'], npc)
        self.assertEqual(result['name'], name)
        self.assertEqual(result['surnames'], surnames)
        self.assertEqual(result['specialty'], specialty)
        self.cur.execute('DELETE FROM Medic WHERE npc = ?', (npc,))

    def test_Delete_Ok(self):
        # Given
        npc = 15233
        name = 'Alicia'
        surnames = 'Delago'
        specialty = 'Neurología'
        myMedic = Medic(
            MedicTest.connection,
            npc,
            name,
            surnames,
            specialty
        )
        self.cur.execute('''INSERT INTO Medic(npc, name, surnames, specialty)
        VALUES (?,?,?,?)''',
                         (npc,
                          name,
                          surnames,
                          specialty))

        # When
        myMedic.delete()

        # Then
        MedicTest.cur.execute('SELECT npc FROM Medic WHERE npc = ?', (npc,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        MedicTest.cur.execute(
            'SELECT specialty FROM Medic WHERE specialty = ?', (specialty,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        MedicTest.cur.execute('SELECT name FROM Medic WHERE name = ?', (name,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        MedicTest.cur.execute(
            'SELECT surnames FROM Medic WHERE surnames = ?', (surnames,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])

    def test_update_Ok(self):
        # Given
        npc = 15231
        name = 'Alicia'
        name2 = 'Paco'
        surnames = 'Delago'
        surnames2 = 'González'
        specialty = 'Neurología'
        specialty2 = 'Cardiología'
        myMedic = Medic(
            MedicTest.connection,
            npc,
            name,
            surnames,
            specialty
        )
        self.cur.execute('''INSERT INTO Medic(npc, name, surnames, specialty)
        VALUES (?,?,?,?)''', (
            npc,
            name,
            surnames,
            specialty))

        # When
        myMedic.setName(name2)
        myMedic.setSurnames(surnames2)
        myMedic.setSpecialty(specialty2)
        myMedic.update()

        # Then
        MedicTest.cur.execute(
            'SELECT npc, name, surnames, specialty FROM Medic WHERE npc = ?',
            (npc,))
        result = self.cur.fetchone()
        self.assertEqual(result['name'], name2)
        self.assertEqual(result['surnames'], surnames2)
        self.assertEqual(result['specialty'], specialty2)
        self.cur.execute('DELETE FROM Medic WHERE npc = ?', (npc,))

    def test_load_Ok(self):
        npc = 15233
        name = 'Alicia'
        surnames = 'Delago'
        specialty = 'Neurología'
        myMedic = Medic(
            MedicTest.connection,
            npc
        )
        self.cur.execute('''INSERT INTO Medic(npc, name, surnames, specialty)
        VALUES (?,?,?,?)''',
                         (npc,
                          name,
                          surnames,
                          specialty))

        # When
        myMedic.load()

        # Then
        self.assertEqual(myMedic.getName(), name)
        self.assertEqual(myMedic.getSurnames(), surnames)
        self.assertEqual(myMedic.getSpecialty(), specialty)
        self.cur.execute('DELETE FROM Medic WHERE npc = ?', (npc,))


if __name__ == '__main__':
    unittest.main()
