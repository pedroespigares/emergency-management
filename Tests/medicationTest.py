import os
import sys
sys.path.append(os.path.abspath('.'))

import sqlite3
import unittest
from Clases.medication import Medication
from Clases.urgency import Urgency


class MedicationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE Medication(
                  urgency int primary key,
                  name text,
                  dosage text
            )''')

    @classmethod
    def tearDownClass(cls):
        cls.cur.execute('''DROP TABLE Medication''')
        cls.connection.close()

    def test_constructor_AllParams_Ok(self):
        # Given
        myUrgency = Urgency(MedicationTest.connection, None, 108)
        name = 'Ibuprofeno'
        dosage = 'Cada 8 horas'

        # When
        myMedication = Medication(
            MedicationTest.connection,
            myUrgency,
            name,
            dosage
        )

        # Then
        self.assertIsNotNone(myMedication)
        self.assertIsInstance(myMedication, Medication)

    def test_constructor_OnlyObligatoryParams_Ok(self):
        # Given
        myUrgency = Urgency(MedicationTest.connection, None, 108)

        # When
        myMedication = Medication(
            MedicationTest.connection,
            myUrgency
        )

        # Then
        self.assertIsNotNone(myMedication)
        self.assertIsInstance(myMedication, Medication)

    def test_Save_Ok(self):
        # Given
        myUrgency = Urgency(MedicationTest.connection, None, 108)
        name = 'Ibuprofeno'
        dosage = 'Cada 8 horas'

        myMedication = Medication(
            MedicationTest.connection,
            myUrgency,
            name,
            dosage
        )

        # When
        myMedication.save()

        # Then
        query = '''SELECT urgency, name, dosage
        FROM Medication WHERE urgency = ?'''
        MedicationTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = MedicationTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['name'], name)
        self.assertEqual(result['dosage'], dosage)
        self.cur.execute(
            'DELETE FROM Medication WHERE urgency = ?',
            (myUrgency.getEpisode(),))

    @unittest.expectedFailure
    def test_load_Fail(self):
        # Given
        urgency = 'TestFail'
        myMedication = Medication(
            MedicationTest.connection,
            urgency,
        )

        # When
        myMedication.load()

    def test_Save_WithSetter_Ok(self):
        # Given
        myUrgency = Urgency(MedicationTest.connection, None, 108)
        name = 'Ibuprofeno'
        dosage = 'Cada 8 horas'

        myMedication = Medication(
            MedicationTest.connection,
            myUrgency
        )

        # When
        myMedication.setName(name)
        myMedication.setDosage(dosage)
        myMedication.save()

        # Then
        query = '''SELECT urgency, name, dosage
        FROM Medication WHERE urgency = ?'''
        MedicationTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = MedicationTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['name'], name)
        self.assertEqual(result['dosage'], dosage)
        self.cur.execute(
            'DELETE FROM Medication WHERE urgency = ?',
            (myUrgency.getEpisode(),))

    def test_Delete_Ok(self):
        # Given
        myUrgency = Urgency(MedicationTest.connection, None, 108)
        name = 'Ibuprofeno'
        dosage = 'Cada 8 horas'

        myMedication = Medication(
            MedicationTest.connection,
            myUrgency,
            name,
            dosage
        )
        self.cur.execute('''INSERT INTO Medication(urgency, name, dosage)
            VALUES (?,?,?)''', (myUrgency.getEpisode(), name, dosage))

        # When
        myMedication.delete()

        # Then
        MedicationTest.cur.execute(
            'SELECT urgency FROM Medication WHERE urgency = ?',
            (myUrgency.getEpisode(),))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        MedicationTest.cur.execute(
            'SELECT dosage FROM Medication WHERE dosage = ?', (dosage,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        MedicationTest.cur.execute(
            'SELECT name FROM Medication WHERE name = ?', (name,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])

    def test_update_Ok(self):
        # Given
        # Given
        myUrgency = Urgency(MedicationTest.connection, None, 108)
        name = 'Ibuprofeno'
        name2 = 'Paracetamol'
        dosage = 'Cada 8 horas'

        myMedication = Medication(
            MedicationTest.connection,
            myUrgency,
            name,
            dosage
        )
        self.cur.execute('''INSERT INTO Medication(urgency, name, dosage)
            VALUES (?,?,?)''', (myUrgency.getEpisode(), name, dosage))

        # When
        myMedication.setName(name2)
        myMedication.update()

        # Then
        query = '''SELECT urgency, name, dosage
        FROM Medication WHERE urgency = ?'''
        MedicationTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = MedicationTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['name'], name2)
        self.assertEqual(result['dosage'], dosage)
        self.cur.execute(
            'DELETE FROM Medication WHERE urgency = ?',
            (myUrgency.getEpisode(),))

    def test_load_Ok(self):
        myUrgency = Urgency(MedicationTest.connection, None, 108)
        name = 'Ibuprofeno'
        dosage = 'Cada 8 horas'

        myMedication = Medication(
            MedicationTest.connection,
            myUrgency
        )
        self.cur.execute('''INSERT INTO Medication(urgency, name, dosage)
            VALUES (?,?,?)''', (myUrgency.getEpisode(), name, dosage))

        # When
        myMedication.load()

        # Then
        query = '''SELECT urgency, name, dosage
        FROM Medication WHERE urgency = ?'''
        MedicationTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = MedicationTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['name'], name)
        self.assertEqual(result['dosage'], dosage)
        self.cur.execute(
            'DELETE FROM Medication WHERE urgency = ?',
            (myUrgency.getEpisode(),))


if __name__ == '__main__':
    unittest.main()
