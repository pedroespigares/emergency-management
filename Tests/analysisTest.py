import os
import sys
sys.path.append(os.path.abspath('.'))

import sqlite3
import unittest
from Clases.analysis import Analysis
from Clases.urgency import Urgency


class AnalysisTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE Analysis(
                  urgency int primary key,
                  petition int,
                  hemoglobine int,
                  oxygen int
            )''')

    @classmethod
    def tearDownClass(cls):
        cls.cur.execute('''DROP TABLE Analysis''')
        cls.connection.close()

    def test_constructor_AllParams_Ok(self):
        # Given
        myUrgency = Urgency(AnalysisTest.connection, None, 108)
        petition = 567
        hemoglobine = 14
        oxygen = 100

        # When
        myAnalysis = Analysis(
            AnalysisTest.connection,
            myUrgency,
            petition,
            hemoglobine,
            oxygen
        )

        # Then
        self.assertIsNotNone(myAnalysis)
        self.assertIsInstance(myAnalysis, Analysis)

    def test_constructor_OnlyObligatoryParams_Ok(self):
        # Given
        myUrgency = Urgency(AnalysisTest.connection, None, 108)
        petition = 567

        # When
        myAnalysis = Analysis(
            AnalysisTest.connection,
            myUrgency,
            petition
        )

        # Then
        self.assertIsNotNone(myAnalysis)
        self.assertIsInstance(myAnalysis, Analysis)

    def test_Save_Ok(self):
        # Given
        myUrgency = Urgency(AnalysisTest.connection, None, 108)
        petition = 567
        hemoglobine = 14
        oxygen = 100

        myAnalysis = Analysis(
            AnalysisTest.connection,
            myUrgency,
            petition,
            hemoglobine,
            oxygen
        )

        # When
        myAnalysis.save()

        # Then
        query = 'SELECT urgency, petition, hemoglobine, '
        query += 'oxygen FROM Analysis WHERE petition = ?'
        AnalysisTest.cur.execute(query, (petition,))
        result = AnalysisTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['petition'], petition)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['hemoglobine'], hemoglobine)
        self.assertEqual(result['oxygen'], oxygen)
        self.cur.execute(
            'DELETE FROM Analysis WHERE petition = ?', (petition,))

    @unittest.expectedFailure
    def test_load_Fail(self):
        # Given
        petition = 'TestFail'
        myAnalysis = Analysis(
            AnalysisTest.connection,
            petition,
        )

        # When
        myAnalysis.load()

    def test_Save_WithSetter_Ok(self):
        # Given
        myUrgency = Urgency(AnalysisTest.connection, None, 108)
        petition = 567
        hemoglobine = 14
        oxygen = 100

        myAnalysis = Analysis(
            AnalysisTest.connection,
            myUrgency,
            petition,
        )

        # When
        myAnalysis.setHemoglobine(hemoglobine)
        myAnalysis.setOxygen(oxygen)
        myAnalysis.save()

        # Then
        query = 'SELECT urgency, petition, hemoglobine, '
        query += 'oxygen FROM Analysis WHERE petition = ?'
        AnalysisTest.cur.execute(query, (petition,))
        result = AnalysisTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['petition'], petition)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['hemoglobine'], hemoglobine)
        self.assertEqual(result['oxygen'], oxygen)
        self.cur.execute(
            'DELETE FROM Analysis WHERE petition = ?', (petition,))

    def test_Delete_Ok(self):
        # Given
        myUrgency = Urgency(AnalysisTest.connection, None, 108)
        petition = 567
        hemoglobine = 14
        oxygen = 100

        myAnalysis = Analysis(
            AnalysisTest.connection,
            myUrgency,
            petition
        )
        self.cur.execute('''INSERT INTO Analysis(urgency, petition,
            hemoglobine, oxygen) VALUES (?,?,?,?)''',
                         (myUrgency.getEpisode(),
                          petition,
                          hemoglobine,
                          oxygen))

        # When
        myAnalysis.delete()

        # Then
        AnalysisTest.cur.execute(
            'SELECT petition FROM Analysis WHERE petition = ?', (petition,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        AnalysisTest.cur.execute(
            '''SELECT urgency FROM Analysis
            WHERE urgency = ?''', (myUrgency.getEpisode(),))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        AnalysisTest.cur.execute(
            '''SELECT hemoglobine FROM Analysis
            WHERE hemoglobine = ?''', (hemoglobine,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        AnalysisTest.cur.execute(
            'SELECT oxygen FROM Analysis WHERE oxygen = ?', (oxygen,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])

    def test_update_Ok(self):
        # Given
        myUrgency = Urgency(AnalysisTest.connection, None, 108)
        petition = 567
        hemoglobine = 14
        hemoglobine2 = 15
        oxygen = 100
        oxygen2 = 150

        myAnalysis = Analysis(
            AnalysisTest.connection,
            myUrgency,
            petition
        )
        self.cur.execute('''INSERT INTO Analysis(urgency, petition,
            hemoglobine, oxygen) VALUES (?,?,?,?)''',
                         (myUrgency.getEpisode(),
                          petition,
                          hemoglobine,
                          oxygen))

        # When
        myAnalysis.setHemoglobine(hemoglobine2)
        myAnalysis.setOxygen(oxygen2)
        myAnalysis.update()

        # Then
        query = 'SELECT urgency, petition, hemoglobine, '
        query += 'oxygen FROM Analysis WHERE petition = ?'
        AnalysisTest.cur.execute(query, (petition,))
        result = AnalysisTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['petition'], petition)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['hemoglobine'], hemoglobine2)
        self.assertEqual(result['oxygen'], oxygen2)
        self.cur.execute(
            'DELETE FROM Analysis WHERE petition = ?', (petition,))

    def test_load_Ok(self):
        myUrgency = Urgency(AnalysisTest.connection, None, 108)
        petition = 567
        hemoglobine = 14
        oxygen = 100

        myAnalysis = Analysis(
            AnalysisTest.connection,
            myUrgency,
            petition
        )
        self.cur.execute('''INSERT INTO Analysis(urgency, petition,
            hemoglobine, oxygen) VALUES (?,?,?,?)''',
                         (myUrgency.getEpisode(),
                          petition,
                          hemoglobine,
                          oxygen))

        # When
        myAnalysis.load()

        # Then
        query = 'SELECT urgency, petition, hemoglobine, '
        query += 'oxygen FROM Analysis WHERE petition = ?'
        AnalysisTest.cur.execute(query, (petition,))
        result = AnalysisTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['petition'], petition)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['hemoglobine'], hemoglobine)
        self.assertEqual(result['oxygen'], oxygen)
        self.cur.execute(
            'DELETE FROM Analysis WHERE petition = ?', (petition,))


if __name__ == '__main__':
    unittest.main()
