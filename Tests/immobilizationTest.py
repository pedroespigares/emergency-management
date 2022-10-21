import os
import sys
sys.path.append(os.path.abspath('.'))

import sqlite3
import unittest
from Clases.immobilization import Immobilization
from Clases.urgency import Urgency


class ImmobilizationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE Immobilization(
                  urgency int primary key,
                  type text,
                  place text
            )''')

    @classmethod
    def tearDownClass(cls):
        cls.cur.execute('''DROP TABLE Immobilization''')
        cls.connection.close()

    def test_constructor_AllParams_Ok(self):
        # Given
        myUrgency = Urgency(ImmobilizationTest.connection, None, 108)
        name = 'Parcial'
        place = 'brazo'

        # When
        myImmobilization = Immobilization(
            ImmobilizationTest.connection,
            myUrgency,
            name,
            place
        )

        # Then
        self.assertIsNotNone(myImmobilization)
        self.assertIsInstance(myImmobilization, Immobilization)

    def test_constructor_OnlyObligatoryParams_Ok(self):
        # Given
        myUrgency = Urgency(ImmobilizationTest.connection, None, 108)

        # When
        myImmobilization = Immobilization(
            ImmobilizationTest.connection,
            myUrgency
        )

        # Then
        self.assertIsNotNone(myImmobilization)
        self.assertIsInstance(myImmobilization, Immobilization)

    def test_Save_Ok(self):
        # Given
        myUrgency = Urgency(ImmobilizationTest.connection, None, 108)
        name = 'Parcial'
        place = 'brazo'

        myImmobilization = Immobilization(
            ImmobilizationTest.connection,
            myUrgency,
            name,
            place
        )

        # When
        myImmobilization.save()

        # Then
        query = '''SELECT urgency, type, place
        FROM Immobilization WHERE urgency = ?'''
        ImmobilizationTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = ImmobilizationTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['type'], name)
        self.assertEqual(result['place'], place)
        self.cur.execute(
            'DELETE FROM Immobilization WHERE urgency = ?',
            (myUrgency.getEpisode(),))

    @unittest.expectedFailure
    def test_load_Fail(self):
        # Given
        urgency = 'TestFail'
        myImmobilization = Immobilization(
            ImmobilizationTest.connection,
            urgency,
        )

        # When
        myImmobilization.load()

    def test_Save_WithSetter_Ok(self):
        # Given
        myUrgency = Urgency(ImmobilizationTest.connection, None, 108)
        name = 'Parcial'
        place = 'brazo'

        myImmobilization = Immobilization(
            ImmobilizationTest.connection,
            myUrgency,
        )

        # When
        myImmobilization.setType(name)
        myImmobilization.setPlace(place)
        myImmobilization.save()

        # Then
        query = '''SELECT urgency, type, place
        FROM Immobilization WHERE urgency = ?'''
        ImmobilizationTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = ImmobilizationTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['type'], name)
        self.assertEqual(result['place'], place)
        self.cur.execute(
            'DELETE FROM Immobilization WHERE urgency = ?',
            (myUrgency.getEpisode(),))

    def test_Delete_Ok(self):
        # Given
        myUrgency = Urgency(ImmobilizationTest.connection, None, 108)
        name = 'Parcial'
        place = 'brazo'

        myImmobilization = Immobilization(
            ImmobilizationTest.connection,
            myUrgency,
        )
        self.cur.execute('''INSERT INTO Immobilization(urgency, type, place)
            VALUES (?,?,?)''', (myUrgency.getEpisode(), name, place))

        # When
        myImmobilization.delete()

        # Then
        ImmobilizationTest.cur.execute(
            'SELECT urgency FROM Immobilization WHERE urgency = ?',
            (myUrgency.getEpisode(),))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        ImmobilizationTest.cur.execute(
            'SELECT type FROM Immobilization WHERE type = ?', (name,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        ImmobilizationTest.cur.execute(
            'SELECT place FROM Immobilization WHERE place = ?', (place,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])

    def test_update_Ok(self):
        # Given
        myUrgency = Urgency(ImmobilizationTest.connection, None, 108)
        name = 'Parcial'
        name2 = 'Total'
        place = 'brazo'
        place2 = 'pierna'

        myImmobilization = Immobilization(
            ImmobilizationTest.connection,
            myUrgency,
        )
        self.cur.execute('''INSERT INTO Immobilization(urgency, type, place)
            VALUES (?,?,?)''', (myUrgency.getEpisode(), name, place))

        # When
        myImmobilization.setType(name2)
        myImmobilization.setPlace(place2)
        myImmobilization.update()

        # Then
        query = '''SELECT urgency, type, place
        FROM Immobilization WHERE urgency = ?'''
        ImmobilizationTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = ImmobilizationTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['type'], name2)
        self.assertEqual(result['place'], place2)
        self.cur.execute(
            'DELETE FROM Immobilization WHERE urgency = ?',
            (myUrgency.getEpisode(),))

    def test_load_Ok(self):
        myUrgency = Urgency(ImmobilizationTest.connection, None, 108)
        name = 'Parcial'
        place = 'brazo'

        myImmobilization = Immobilization(
            ImmobilizationTest.connection,
            myUrgency,
        )
        self.cur.execute('''INSERT INTO Immobilization(urgency, type, place)
            VALUES (?,?,?)''', (myUrgency.getEpisode(), name, place))

        # When
        myImmobilization.load()

        # Then
        query = '''SELECT urgency, type, place
        FROM Immobilization WHERE urgency = ?'''
        ImmobilizationTest.cur.execute(query, (myUrgency.getEpisode(),))
        result = ImmobilizationTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['urgency'], myUrgency.getEpisode())
        self.assertEqual(result['type'], name)
        self.assertEqual(result['place'], place)
        self.cur.execute(
            'DELETE FROM Immobilization WHERE urgency = ?',
            (myUrgency.getEpisode(),))


if __name__ == '__main__':
    unittest.main()
