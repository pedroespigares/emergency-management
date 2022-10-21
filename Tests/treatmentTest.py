import os
import sys
sys.path.append(os.path.abspath('.'))

import sqlite3
import unittest
from Clases.treatment import Treatment
from Clases.urgency import Urgency


class TreatmentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE Treatment(
                  urgency int primary key,
                  type text,
                  antitetanus text,
                  anesthesia text
            )''')

    @classmethod
    def tearDownClass(cls):
        cls.cur.execute('''DROP TABLE Treatment''')
        cls.connection.close()

    def test_constructor_AllParams_Ok(self):
        # Given
        myUrgency = Urgency(TreatmentTest.connection, None, 108)
        treatment_type = 'Cosura'
        antitetanus = '1'
        anesthesia = '0'

        # When
        myTreatment = Treatment(
            TreatmentTest.connection,
            myUrgency,
            treatment_type,
            antitetanus,
            anesthesia
        )

        # Then
        self.assertIsNotNone(myTreatment)
        self.assertIsInstance(myTreatment, Treatment)

    def test_constructor_OnlyObligatoryParams_Ok(self):
        # Given
        myUrgency = Urgency(TreatmentTest.connection, None, 108)

        # When
        myTreatment = Treatment(
            TreatmentTest.connection,
            myUrgency
        )

        # Then
        self.assertIsNotNone(myTreatment)
        self.assertIsInstance(myTreatment, Treatment)

    def test_Save_Ok(self):
        # Given
        myUrgency = Urgency(TreatmentTest.connection, None, 108)
        treatment_type = 'Cosura'
        antitetanus = '1'
        anesthesia = '0'

        myTreatment = Treatment(
            TreatmentTest.connection,
            myUrgency,
            treatment_type,
            antitetanus,
            anesthesia
        )

        # When
        myTreatment.save()

        # Then
        query = 'SELECT urgency, type, antitetanus, anesthesia '
        query += 'FROM Treatment WHERE urgency = ? '
        TreatmentTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = TreatmentTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['type'], treatment_type)
        self.assertEqual(result['antitetanus'], antitetanus)
        self.assertEqual(result['anesthesia'], anesthesia)
        self.cur.execute(
            'DELETE FROM Treatment WHERE urgency = ?',
            (myUrgency.getEpisode(),))

    @unittest.expectedFailure
    def test_load_Fail(self):
        # Given
        urgency = 'TestFail'
        myTreatment = Treatment(
            TreatmentTest.connection,
            urgency,
        )

        # When
        myTreatment.load()

    def test_Save_WithSetter_Ok(self):
        # Given
        myUrgency = Urgency(TreatmentTest.connection, None, 108)
        treatment_type = 'Cosura'
        antitetanus = '1'
        anesthesia = '0'

        myTreatment = Treatment(
            TreatmentTest.connection,
            myUrgency,
        )

        # When
        myTreatment.setType(treatment_type)
        myTreatment.setAntitetanus(antitetanus)
        myTreatment.setAnesthesia(anesthesia)
        myTreatment.save()

        # Then
        query = 'SELECT urgency, type, antitetanus, anesthesia '
        query += 'FROM Treatment WHERE urgency = ? '
        TreatmentTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = TreatmentTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['type'], treatment_type)
        self.assertEqual(result['antitetanus'], antitetanus)
        self.assertEqual(result['anesthesia'], anesthesia)
        self.cur.execute(
            'DELETE FROM Treatment WHERE urgency = ?',
            (myUrgency.getEpisode(),))

    def test_Delete_Ok(self):
        # Given
        myUrgency = Urgency(TreatmentTest.connection, None, 108)
        treatment_type = 'Cosura'
        antitetanus = '1'
        anesthesia = '0'

        myTreatment = Treatment(
            TreatmentTest.connection,
            myUrgency,
            treatment_type,
            antitetanus,
            anesthesia
        )
        self.cur.execute('''INSERT INTO Treatment(urgency, type, antitetanus,
            anesthesia) VALUES (?,?,?,?)''', (myUrgency.getEpisode(),
                                              treatment_type,
                                              antitetanus, anesthesia))

        # When
        myTreatment.delete()

        # Then
        TreatmentTest.cur.execute(
            'SELECT urgency FROM Treatment WHERE urgency = ?',
            (myUrgency.getEpisode(),))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        TreatmentTest.cur.execute(
            'SELECT type FROM Treatment WHERE type = ?', (treatment_type,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        TreatmentTest.cur.execute(
            'SELECT antitetanus FROM Treatment WHERE antitetanus = ?',
            (antitetanus,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        TreatmentTest.cur.execute(
            'SELECT anesthesia FROM Treatment WHERE anesthesia = ?',
            (anesthesia,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])

    def test_update_Ok(self):
        # Given
        # Given
        myUrgency = Urgency(TreatmentTest.connection, None, 108)
        treatment_type = 'Cosura'
        treatment_type2 = 'Apertura'
        antitetanus = '1'
        antitetanus2 = '0'
        anesthesia = '0'

        myTreatment = Treatment(
            TreatmentTest.connection,
            myUrgency,
            treatment_type,
            antitetanus,
            anesthesia
        )
        self.cur.execute('''INSERT INTO Treatment(urgency, type, antitetanus,
            anesthesia) VALUES (?,?,?,?)''', (myUrgency.getEpisode(),
                                              treatment_type,
                                              antitetanus, anesthesia))

        # When
        myTreatment.setType(treatment_type2)
        myTreatment.setAntitetanus(antitetanus2)
        myTreatment.update()

        # Then
        query = 'SELECT urgency, type, antitetanus, anesthesia '
        query += 'FROM Treatment WHERE urgency = ? '
        TreatmentTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = TreatmentTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['type'], treatment_type2)
        self.assertEqual(result['antitetanus'], antitetanus2)
        self.assertEqual(result['anesthesia'], anesthesia)
        self.cur.execute(
            'DELETE FROM Treatment WHERE urgency = ?',
            (myUrgency.getEpisode(),))

    def test_load_Ok(self):
        myUrgency = Urgency(TreatmentTest.connection, None, 108)
        treatment_type = 'Cosura'
        antitetanus = '1'
        anesthesia = '0'

        myTreatment = Treatment(
            TreatmentTest.connection,
            myUrgency,
        )
        self.cur.execute('''INSERT INTO Treatment(urgency, type, antitetanus,
            anesthesia) VALUES (?,?,?,?)''', (myUrgency.getEpisode(),
                                              treatment_type,
                                              antitetanus, anesthesia))

        # When
        myTreatment.load()

        # Then
        query = 'SELECT urgency, type, antitetanus, anesthesia '
        query += 'FROM Treatment WHERE urgency = ? '
        TreatmentTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = TreatmentTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['type'], treatment_type)
        self.assertEqual(result['antitetanus'], antitetanus)
        self.assertEqual(result['anesthesia'], anesthesia)
        self.cur.execute(
            'DELETE FROM Treatment WHERE urgency = ?',
            (myUrgency.getEpisode(),))


if __name__ == '__main__':
    unittest.main()
