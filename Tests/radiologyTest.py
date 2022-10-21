import os
import sys
sys.path.append(os.path.abspath('.'))

import sqlite3
import unittest
from Clases.radiology import Radiology
from Clases.urgency import Urgency


class RadiologyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE Radiology(
                  urgency int primary key,
                  petition int,
                  pregnancy text,
                  contrast text,
                  informed_consent text
            )''')

    @classmethod
    def tearDownClass(cls):
        cls.cur.execute('''DROP TABLE Radiology''')
        cls.connection.close()

    def test_constructor_AllParams_Ok(self):
        # Given
        myUrgency = Urgency(RadiologyTest.connection, None, 108)
        petition = 56334
        pregnancy = '0'
        contrast = '0'
        consent = '1'

        # When
        myRadiology = Radiology(
            RadiologyTest.connection,
            myUrgency,
            petition,
            pregnancy,
            contrast,
            consent
        )

        # Then
        self.assertIsNotNone(myRadiology)
        self.assertIsInstance(myRadiology, Radiology)

    def test_constructor_OnlyObligatoryParams_Ok(self):
        # Given
        myUrgency = Urgency(RadiologyTest.connection, None, 108)
        petition = 56334

        # When
        myRadiology = Radiology(
            RadiologyTest.connection,
            myUrgency,
            petition
        )

        # Then
        self.assertIsNotNone(myRadiology)
        self.assertIsInstance(myRadiology, Radiology)

    def test_Save_Ok(self):
        # Given
        myUrgency = Urgency(RadiologyTest.connection, None, 108)
        petition = 56334
        pregnancy = '0'
        contrast = '0'
        consent = '1'

        myRadiology = Radiology(
            RadiologyTest.connection,
            myUrgency,
            petition,
            pregnancy,
            contrast,
            consent
        )

        # When
        myRadiology.save()

        # Then
        query = 'SELECT urgency, petition, pregnancy, contrast, '
        query += 'informed_consent FROM Radiology WHERE petition = ? '
        RadiologyTest.cur.execute(query, (petition,))
        result = RadiologyTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['petition'], petition)
        self.assertEqual(result['pregnancy'], pregnancy)
        self.assertEqual(result['contrast'], contrast)
        self.assertEqual(result['informed_consent'], consent)
        self.cur.execute(
            'DELETE FROM Radiology WHERE petition = ?', (petition,))

    @unittest.expectedFailure
    def test_load_Fail(self):
        # Given
        urgency = 'TestFail'
        petition = '7123'
        myRadiology = Radiology(
            RadiologyTest.connection,
            urgency,
            petition
        )

        # When
        myRadiology.load()

    def test_Save_WithSetter_Ok(self):
        myUrgency = Urgency(RadiologyTest.connection, None, 108)
        petition = 56334
        pregnancy = '0'
        contrast = '0'
        consent = '1'

        myRadiology = Radiology(
            RadiologyTest.connection,
            myUrgency,
            petition
        )

        # When
        myRadiology.setPregnancy(pregnancy)
        myRadiology.setContrast(contrast)
        myRadiology.setConsent(consent)
        myRadiology.save()

        # Then
        query = 'SELECT urgency, petition, pregnancy, contrast, '
        query += 'informed_consent FROM Radiology WHERE petition = ? '
        RadiologyTest.cur.execute(query, (petition,))
        result = RadiologyTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['petition'], petition)
        self.assertEqual(result['pregnancy'], pregnancy)
        self.assertEqual(result['contrast'], contrast)
        self.assertEqual(result['informed_consent'], consent)
        self.cur.execute(
            'DELETE FROM Radiology WHERE petition = ?', (petition,))

    def test_Delete_Ok(self):
        # Given
        myUrgency = Urgency(RadiologyTest.connection, None, 108)
        petition = 56334
        pregnancy = '0'
        contrast = '0'
        consent = '1'

        myRadiology = Radiology(
            RadiologyTest.connection,
            myUrgency,
            petition,
            pregnancy,
            contrast,
            consent
        )
        self.cur.execute('''INSERT INTO Radiology(urgency, petition,
            pregnancy, contrast, informed_consent) VALUES (?,?,?,?,?)''',
                         (myUrgency.getEpisode(), petition,
                          pregnancy, contrast, consent))

        # When
        myRadiology.delete()

        # Then
        RadiologyTest.cur.execute(
            'SELECT urgency FROM Radiology WHERE urgency = ?',
            (myUrgency.getEpisode(),))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        RadiologyTest.cur.execute(
            'SELECT petition FROM Radiology WHERE petition = ?', (petition,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        RadiologyTest.cur.execute(
            'SELECT pregnancy FROM Radiology WHERE pregnancy = ?',
            (pregnancy,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        RadiologyTest.cur.execute(
            'SELECT contrast FROM Radiology WHERE contrast = ?', (contrast,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        RadiologyTest.cur.execute(
            '''SELECT informed_consent
            FROM Radiology WHERE informed_consent = ?''',
            (consent,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])

    def test_update_Ok(self):
        # Given
        # Given
        myUrgency = Urgency(RadiologyTest.connection, None, 108)
        petition = 56334
        pregnancy = '0'
        pregnancy2 = '1'
        contrast = '0'
        contrast2 = '1'
        consent = '1'

        myRadiology = Radiology(
            RadiologyTest.connection,
            myUrgency,
            petition,
            pregnancy,
            contrast,
            consent
        )
        self.cur.execute('''INSERT INTO Radiology(urgency, petition,
            pregnancy, contrast, informed_consent) VALUES (?,?,?,?,?)''',
                         (myUrgency.getEpisode(), petition,
                          pregnancy, contrast, consent))

        # When
        myRadiology.setPregnancy(pregnancy2)
        myRadiology.setContrast(contrast2)
        myRadiology.update()

        # Then
        query = 'SELECT urgency, petition, pregnancy, contrast, '
        query += 'informed_consent FROM Radiology WHERE petition = ? '
        RadiologyTest.cur.execute(query, (petition,))
        result = RadiologyTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['petition'], petition)
        self.assertEqual(result['pregnancy'], pregnancy2)
        self.assertEqual(result['contrast'], contrast2)
        self.assertEqual(result['informed_consent'], consent)
        self.cur.execute(
            'DELETE FROM Radiology WHERE petition = ?', (petition,))

    def test_load_Ok(self):
        myUrgency = Urgency(RadiologyTest.connection, None, 108)
        petition = 56334
        pregnancy = '0'
        contrast = '0'
        consent = '1'

        myRadiology = Radiology(
            RadiologyTest.connection,
            myUrgency,
            petition,
        )
        self.cur.execute('''INSERT INTO Radiology(urgency, petition,
            pregnancy, contrast, informed_consent) VALUES (?,?,?,?,?)''',
                         (myUrgency.getEpisode(), petition,
                          pregnancy, contrast, consent))

        # When
        myRadiology.load()

        # Then
        query = 'SELECT urgency, petition, pregnancy, contrast, '
        query += 'informed_consent FROM Radiology WHERE petition = ? '
        RadiologyTest.cur.execute(query, (petition,))
        result = RadiologyTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['petition'], petition)
        self.assertEqual(result['pregnancy'], pregnancy)
        self.assertEqual(result['contrast'], contrast)
        self.assertEqual(result['informed_consent'], consent)
        self.cur.execute(
            'DELETE FROM Radiology WHERE petition = ?', (petition,))


if __name__ == '__main__':
    unittest.main()
