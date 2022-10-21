import os
import sys
sys.path.append(os.path.abspath('.'))

from Clases.urgency import Urgency
from Clases.cpr import Cpr
import unittest
import sqlite3


class CprTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE Cpr(
                  urgency int primary key,
                  type text
            )''')

    @classmethod
    def tearDownClass(cls):
        cls.cur.execute('''DROP TABLE Cpr''')
        cls.connection.close()

    def test_constructor_AllParams_Ok(self):
        # Given
        myUrgency = Urgency(CprTest.connection, None, 108)
        cpr_type = 'Cardiorespiratioria'

        # When
        myCpr = Cpr(
            CprTest.connection,
            myUrgency,
            cpr_type
        )

        # Then
        self.assertIsNotNone(myCpr)
        self.assertIsInstance(myCpr, Cpr)

    def test_constructor_OnlyObligatoryParams_Ok(self):
        # Given
        myUrgency = Urgency(CprTest.connection, None, 108)

        # When
        myCpr = Cpr(
            CprTest.connection,
            myUrgency
        )

        # Then
        self.assertIsNotNone(myCpr)
        self.assertIsInstance(myCpr, Cpr)

    def test_Save_Ok(self):
        # Given
        myUrgency = Urgency(CprTest.connection, None, 108)
        cpr_type = 'Cardiorespiratioria'

        myCpr = Cpr(
            CprTest.connection,
            myUrgency,
            cpr_type
        )

        # When
        myCpr.save()

        # Then
        query = 'SELECT urgency, type FROM Cpr WHERE urgency = ? '
        CprTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = CprTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['type'], cpr_type)
        self.cur.execute('DELETE FROM Cpr WHERE urgency = ?',
                         (myUrgency.getEpisode(),))

    @unittest.expectedFailure
    def test_load_Fail(self):
        # Given
        urgency = 'TestFail'
        myCpr = Cpr(
            CprTest.connection,
            urgency,
        )

        # When
        myCpr.load()

    def test_Save_WithSetter_Ok(self):
        # Given
        myUrgency = Urgency(CprTest.connection, None, 108)
        cpr_type = 'Cardiorespiratioria'

        myCpr = Cpr(
            CprTest.connection,
            myUrgency
        )

        # When
        myCpr.setType(cpr_type)
        myCpr.save()

        # Then
        query = 'SELECT urgency, type FROM Cpr WHERE urgency = ? '
        CprTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = CprTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['type'], cpr_type)
        self.cur.execute('DELETE FROM Cpr WHERE urgency = ?',
                         (myUrgency.getEpisode(),))

    def test_Delete_Ok(self):
        # Given
        myUrgency = Urgency(CprTest.connection, None, 108)
        cpr_type = 'Cardiorespiratioria'

        myCpr = Cpr(
            CprTest.connection,
            myUrgency,
            cpr_type
        )
        self.cur.execute('''INSERT INTO Cpr(urgency, type)
            VALUES (?,?)''', (myUrgency.getEpisode(), cpr_type))

        # When
        myCpr.delete()

        # Then
        CprTest.cur.execute(
            'SELECT urgency FROM Cpr WHERE urgency = ?',
            (myUrgency.getEpisode(),))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        CprTest.cur.execute('SELECT type FROM Cpr WHERE type = ?', (cpr_type,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])

    def test_update_Ok(self):
        # Given
        myUrgency = Urgency(CprTest.connection, None, 108)
        cpr_type = 'Cardiorespiratioria'
        cpr_type2 = 'Respiratoria'

        myCpr = Cpr(
            CprTest.connection,
            myUrgency,
            cpr_type
        )
        self.cur.execute('''INSERT INTO Cpr(urgency, type)
            VALUES (?,?)''', (myUrgency.getEpisode(), cpr_type))

        # When
        myCpr.setType(cpr_type2)
        myCpr.update()

        # Then
        query = 'SELECT urgency, type FROM Cpr WHERE urgency = ? '
        CprTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = CprTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['type'], cpr_type2)
        self.cur.execute('DELETE FROM Cpr WHERE urgency = ?',
                         (myUrgency.getEpisode(),))

    def test_load_Ok(self):
        myUrgency = Urgency(CprTest.connection, None, 108)
        cpr_type = 'Cardiorespiratioria'

        myCpr = Cpr(
            CprTest.connection,
            myUrgency
        )
        self.cur.execute('''INSERT INTO Cpr(urgency, type)
            VALUES (?,?)''', (myUrgency.getEpisode(), cpr_type))

        # When
        myCpr.load()

        # Then
        query = 'SELECT urgency, type FROM Cpr WHERE urgency = ? '
        CprTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = CprTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['type'], cpr_type)
        self.cur.execute('DELETE FROM Cpr WHERE urgency = ?',
                         (myUrgency.getEpisode(),))


if __name__ == '__main__':
    unittest.main()
