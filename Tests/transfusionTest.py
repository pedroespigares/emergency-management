import os
import sys
sys.path.append(os.path.abspath('.'))

import sqlite3
import unittest
from Clases.transfusion import Transfusion
from Clases.urgency import Urgency


class TransfusionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE Transfusion(
                  urgency int primary key,
                  petition int,
                  blood_group text,
                  IRH text,
                  previous_transfusion text,
                  religion text,
                  informed_consent text
            )''')

    @classmethod
    def tearDownClass(cls):
        cls.cur.execute('''DROP TABLE Transfusion''')
        cls.connection.close()

    def test_constructor_AllParams_Ok(self):
        # Given
        myUrgency = Urgency(TransfusionTest.connection, None, 108)
        petition = 56334
        blood_group = 'B'
        irh = '-'
        previous_transfusion = '1'
        religion = 'Cristiano'
        consent = '1'

        # When
        myTransfusion = Transfusion(
            TransfusionTest.connection,
            myUrgency,
            petition,
            blood_group,
            irh,
            previous_transfusion,
            religion,
            consent
        )

        # Then
        self.assertIsNotNone(myTransfusion)
        self.assertIsInstance(myTransfusion, Transfusion)

    def test_constructor_OnlyObligatoryParams_Ok(self):
        # Given
        myUrgency = Urgency(TransfusionTest.connection, None, 108)
        petition = 56334

        # When
        myTransfusion = Transfusion(
            TransfusionTest.connection,
            myUrgency,
            petition
        )

        # Then
        self.assertIsNotNone(myTransfusion)
        self.assertIsInstance(myTransfusion, Transfusion)

    def test_Save_Ok(self):
        # Given
        myUrgency = Urgency(TransfusionTest.connection, None, 108)
        petition = 56334
        blood_group = 'B'
        irh = '-'
        previous_transfusion = '1'
        religion = 'Cristiano'
        consent = '1'

        myTransfusion = Transfusion(
            TransfusionTest.connection,
            myUrgency,
            petition,
            blood_group,
            irh,
            previous_transfusion,
            religion,
            consent
        )

        # When
        myTransfusion.save()

        # Then
        query = 'SELECT urgency, petition, blood_group, IRH, '
        query += 'previous_transfusion, religion, informed_consent '
        query += 'FROM Transfusion WHERE petition = ?'
        TransfusionTest.cur.execute(query, (petition,))
        result = TransfusionTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['petition'], petition)
        self.assertEqual(result['blood_group'], blood_group)
        self.assertEqual(result['IRH'], irh)
        self.assertEqual(result['previous_transfusion'], previous_transfusion)
        self.assertEqual(result['religion'], religion)
        self.assertEqual(result['informed_consent'], consent)
        self.cur.execute(
            'DELETE FROM Transfusion WHERE petition = ?', (petition,))

    @unittest.expectedFailure
    def test_load_Fail(self):
        # Given
        urgency = 'TestFail'
        petition = '7123'
        myTransfusion = Transfusion(
            TransfusionTest.connection,
            urgency,
            petition
        )

        # When
        myTransfusion.load()

    def test_Save_WithSetter_Ok(self):
        myUrgency = Urgency(TransfusionTest.connection, None, 108)
        petition = 56334
        blood_group = 'B'
        irh = '-'
        previous_transfusion = '1'
        religion = 'Cristiano'
        consent = '1'

        myTransfusion = Transfusion(
            TransfusionTest.connection,
            myUrgency,
            petition
        )

        # When
        myTransfusion.setBloodGroup(blood_group)
        myTransfusion.setIRH(irh)
        myTransfusion.setPreviousTransfusion(previous_transfusion)
        myTransfusion.setReligion(religion)
        myTransfusion.setConsent(consent)
        myTransfusion.save()

        # Then
        query = 'SELECT urgency, petition, blood_group, IRH, '
        query += 'previous_transfusion, religion, informed_consent '
        query += 'FROM Transfusion WHERE petition = ?'
        TransfusionTest.cur.execute(query, (petition,))
        result = TransfusionTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['petition'], petition)
        self.assertEqual(result['blood_group'], blood_group)
        self.assertEqual(result['IRH'], irh)
        self.assertEqual(result['previous_transfusion'], previous_transfusion)
        self.assertEqual(result['religion'], religion)
        self.assertEqual(result['informed_consent'], consent)
        self.cur.execute(
            'DELETE FROM Transfusion WHERE petition = ?', (petition,))

    def test_Delete_Ok(self):
        # Given
        myUrgency = Urgency(TransfusionTest.connection, None, 108)
        petition = 56334
        blood_group = 'B'
        irh = '-'
        previous_transfusion = '1'
        religion = 'Cristiano'
        consent = '1'

        myTransfusion = Transfusion(
            TransfusionTest.connection,
            myUrgency,
            petition,
            blood_group,
            irh,
            previous_transfusion,
            religion,
            consent
        )
        self.cur.execute('''INSERT INTO Transfusion(urgency, petition,
            blood_group, IRH, previous_transfusion, religion, informed_consent)
            VALUES (?,?,?,?,?,?,?)''',
                         (myUrgency.getEpisode(), petition, blood_group, irh,
                          previous_transfusion, religion, consent))

        # When
        myTransfusion.delete()

        # Then
        TransfusionTest.cur.execute(
            'SELECT urgency FROM Transfusion WHERE urgency = ?',
            (myUrgency.getEpisode(),))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        TransfusionTest.cur.execute(
            'SELECT petition FROM Transfusion WHERE petition = ?',
            (petition,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        TransfusionTest.cur.execute(
            'SELECT blood_group FROM Transfusion WHERE blood_group = ?',
            (blood_group,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        TransfusionTest.cur.execute(
            'SELECT irh FROM Transfusion WHERE irh = ?', (irh,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        TransfusionTest.cur.execute('''SELECT previous_transfusion FROM Transfusion
            WHERE previous_transfusion = ?''', (previous_transfusion,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        TransfusionTest.cur.execute(
            'SELECT religion FROM Transfusion WHERE religion = ?', (religion,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        TransfusionTest.cur.execute('''SELECT informed_consent FROM Transfusion
            WHERE informed_consent = ?''', (consent,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])

    def test_update_Ok(self):
        # Given
        myUrgency = Urgency(TransfusionTest.connection, None, 108)
        petition = 56334
        blood_group = 'B'
        blood_group2 = 'A'
        irh = '-'
        irh2 = '+'
        previous_transfusion = '1'
        religion = 'Cristiano'
        consent = '1'

        myTransfusion = Transfusion(
            TransfusionTest.connection,
            myUrgency,
            petition,
            blood_group,
            irh,
            previous_transfusion,
            religion,
            consent
        )
        self.cur.execute('''INSERT INTO Transfusion(urgency, petition,
            blood_group, IRH, previous_transfusion, religion, informed_consent)
            VALUES (?,?,?,?,?,?,?)''',
                         (myUrgency.getEpisode(), petition, blood_group, irh,
                          previous_transfusion, religion, consent))

        # When
        myTransfusion.setBloodGroup(blood_group2)
        myTransfusion.setIRH(irh2)
        myTransfusion.update()

        # Then
        query = 'SELECT urgency, petition, blood_group, IRH, '
        query += 'previous_transfusion, religion, informed_consent '
        query += 'FROM Transfusion WHERE petition = ?'
        TransfusionTest.cur.execute(query, (petition,))
        result = TransfusionTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['petition'], petition)
        self.assertEqual(result['blood_group'], blood_group2)
        self.assertEqual(result['IRH'], irh2)
        self.assertEqual(result['previous_transfusion'], previous_transfusion)
        self.assertEqual(result['religion'], religion)
        self.assertEqual(result['informed_consent'], consent)
        self.cur.execute(
            'DELETE FROM Transfusion WHERE petition = ?', (petition,))

    def test_load_Ok(self):
        myUrgency = Urgency(TransfusionTest.connection, None, 108)
        petition = 56334
        blood_group = 'B'
        irh = '-'
        previous_transfusion = '1'
        religion = 'Cristiano'
        consent = '1'

        myTransfusion = Transfusion(
            TransfusionTest.connection,
            myUrgency,
            petition,
        )
        self.cur.execute('''INSERT INTO Transfusion(urgency, petition,
            blood_group, IRH, previous_transfusion, religion, informed_consent)
            VALUES (?,?,?,?,?,?,?)''',
                         (myUrgency.getEpisode(), petition, blood_group, irh,
                          previous_transfusion, religion, consent))

        # When
        myTransfusion.load()

        # Then
        query = 'SELECT urgency, petition, blood_group, IRH, '
        query += 'previous_transfusion, religion, informed_consent '
        query += 'FROM Transfusion WHERE petition = ?'
        TransfusionTest.cur.execute(query, (petition,))
        result = TransfusionTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['petition'], petition)
        self.assertEqual(result['blood_group'], blood_group)
        self.assertEqual(result['IRH'], irh)
        self.assertEqual(result['previous_transfusion'], previous_transfusion)
        self.assertEqual(result['religion'], religion)
        self.assertEqual(result['informed_consent'], consent)
        self.cur.execute(
            'DELETE FROM Transfusion WHERE petition = ?', (petition,))


if __name__ == '__main__':
    unittest.main()
