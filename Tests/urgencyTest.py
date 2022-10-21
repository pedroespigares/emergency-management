import os
import sys
sys.path.append(os.path.abspath('.'))

import sqlite3
import unittest
from Clases.urgency import Urgency
from Clases.pacient import Pacient
from Clases.medic import Medic


class UrgencyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE Urgency(
                  episode int primary key,
                  pacient text,
                  medic int,
                  status text,
                  entry text,
                  reason text,
                  exploration text,
                  recomendation text,
                  exit text
            )''')

    @classmethod
    def tearDownClass(cls):
        cls.cur.execute('''DROP TABLE Urgency''')
        cls.connection.close()

    def test_constructor_AllParams_Ok(self):
        # Given
        episode = 108
        myPacient = Pacient(UrgencyTest.connection, '78589211M')
        myMedic = Medic(UrgencyTest.connection, 15233)
        status = 'Alta'
        entry = '10/04/2022 20:30'
        reason = 'Sangrado'
        exploration = 'Observación'
        recomendation = 'Gotas'
        urgency_exit = '10/04/2022 21:30'

        # When
        myUrgency = Urgency(
            UrgencyTest.connection,
            myPacient,
            episode,
            myMedic,
            status,
            entry,
            reason,
            exploration,
            recomendation,
            urgency_exit,
        )

        # Then
        self.assertIsNotNone(myUrgency)
        self.assertIsInstance(myUrgency, Urgency)

    def test_constructor_OnlyObligatoryParams_Ok(self):
        # Given
        episode = 108
        myPacient = Pacient(UrgencyTest.connection, '78589211M')

        # When
        myUrgency = Urgency(
            UrgencyTest.connection,
            myPacient,
            episode
        )

        # Then
        self.assertIsNotNone(myUrgency)
        self.assertIsInstance(myUrgency, Urgency)

    def test_Save_Ok(self):
        # Given
        episode = 108
        myPacient = Pacient(UrgencyTest.connection, '78589211M')
        myMedic = Medic(UrgencyTest.connection, 15233)
        status = 'Alta'
        entry = '10/04/2022 20:30'
        reason = 'Sangrado'
        exploration = 'Observación'
        recomendation = 'Gotas'
        urgency_exit = '10/04/2022 21:30'
        myUrgency = Urgency(
            UrgencyTest.connection,
            myPacient,
            episode,
            myMedic,
            status,
            entry,
            reason,
            exploration,
            recomendation,
            urgency_exit,
        )

        # When
        myUrgency.save()

        # Then
        query = 'SELECT episode, pacient, medic, status, entry, '
        query += 'reason, exploration, recomendation, exit '
        query += 'FROM Urgency WHERE episode = ?'
        UrgencyTest.cur.execute(query, (episode,))
        result = UrgencyTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['episode'], episode)
        self.assertEqual(result['pacient'], myPacient.getDNI())
        self.assertEqual(result['medic'], myMedic.getNPC())
        self.assertEqual(result['status'], status)
        self.assertEqual(result['entry'], entry)
        self.assertEqual(result['reason'], reason)
        self.assertEqual(result['exploration'], exploration)
        self.assertEqual(result['recomendation'], recomendation)
        self.assertEqual(result['exit'], urgency_exit)
        self.cur.execute('DELETE FROM Urgency WHERE episode = ?', (episode,))

    def test_Save_WithSetter_Ok(self):
        # Given
        episode = 108
        myPacient = Pacient(UrgencyTest.connection, '78589211M')
        myMedic = Medic(UrgencyTest.connection, 15233)
        status = 'Alta'
        entry = '10/04/2022 20:30'
        reason = 'Sangrado'
        exploration = 'Observación'
        recomendation = 'Gotas'
        urgency_exit = '10/04/2022 21:30'
        myUrgency = Urgency(
            UrgencyTest.connection,
            myPacient,
            episode,
            myMedic,
            status,
            entry
        )

        # When
        myUrgency.setReason('Sangrado')
        myUrgency.setExploration('Observación')
        myUrgency.setRecomendation('Gotas')
        myUrgency.setExit('10/04/2022 21:30')
        myUrgency.save()

        # Then
        query = 'SELECT episode, pacient, medic, status, entry, '
        query += 'reason, exploration, recomendation, exit '
        query += 'FROM Urgency WHERE episode = ?'
        UrgencyTest.cur.execute(query, (episode,))
        result = UrgencyTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['episode'], episode)
        self.assertEqual(result['pacient'], myPacient.getDNI())
        self.assertEqual(result['medic'], myMedic.getNPC())
        self.assertEqual(result['status'], status)
        self.assertEqual(result['entry'], entry)
        self.assertEqual(result['reason'], reason)
        self.assertEqual(result['exploration'], exploration)
        self.assertEqual(result['recomendation'], recomendation)
        self.assertEqual(result['exit'], urgency_exit)
        self.cur.execute('DELETE FROM Urgency WHERE episode = ?', (episode,))

    def test_Delete_Ok(self):
        # Given
        episode = 108
        myPacient = Pacient(UrgencyTest.connection, '78589211M')
        myMedic = Medic(UrgencyTest.connection, 15233)
        status = 'Alta'
        entry = '10/04/2022 20:30'
        reason = 'Sangrado'
        exploration = 'Observación'
        recomendation = 'Gotas'
        urgency_exit = '10/04/2022 21:30'
        myUrgency = Urgency(
            UrgencyTest.connection,
            myPacient,
            episode,
            myMedic,
            status,
            entry,
            reason,
            exploration,
            recomendation,
            urgency_exit
        )
        self.cur.execute('''INSERT INTO Urgency(episode, pacient, medic, status, entry,
            reason, exploration, recomendation, exit)
            VALUES (?,?,?,?,?,?,?,?,?)''',
                         (
                             episode,
                             myPacient.getDNI(),
                             myMedic.getNPC(),
                             status,
                             entry,
                             reason,
                             exploration,
                             recomendation,
                             urgency_exit))

        # When
        myUrgency.delete()

        # Then
        UrgencyTest.cur.execute(
            'SELECT episode FROM Urgency WHERE episode = ?', (episode,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        UrgencyTest.cur.execute(
            'SELECT pacient FROM Urgency WHERE pacient = ?',
            (myPacient.getDNI(),))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        UrgencyTest.cur.execute(
            'SELECT medic FROM Urgency WHERE medic = ?',
            (myMedic.getNPC(),))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        UrgencyTest.cur.execute(
            'SELECT status FROM Urgency WHERE status = ?', (status,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        UrgencyTest.cur.execute(
            'SELECT entry FROM Urgency WHERE entry = ?', (entry,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])

    def test_update_Ok(self):
        # Given
        episode = 108
        myPacient = Pacient(UrgencyTest.connection, '78589211M')
        myMedic = Medic(UrgencyTest.connection, 15233)
        status = 'Alta'
        status2 = 'Ingreso'
        myUrgency = Urgency(
            UrgencyTest.connection,
            myPacient,
            episode,
            myMedic,
            status,
        )
        self.cur.execute('''INSERT INTO Urgency(episode, pacient, medic, status)
            VALUES (?,?,?,?)''',
                         (
                             episode,
                             myPacient.getDNI(),
                             myMedic.getNPC(),
                             status,
                         ))

        # When
        myUrgency.setStatus(status2)
        myUrgency.update()

        # Then
        query = 'SELECT episode, pacient, medic, status, entry, '
        query += 'reason, exploration, recomendation, exit '
        query += 'FROM Urgency WHERE episode = ?'
        UrgencyTest.cur.execute(query, (episode,))
        result = self.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['episode'], episode)
        self.assertEqual(result['pacient'], myPacient.getDNI())
        self.assertEqual(result['medic'], myMedic.getNPC())
        self.assertEqual(result['status'], status2)
        self.cur.execute('DELETE FROM Urgency WHERE episode = ?', (episode,))

    def test_load_Ok(self):
        # Given
        episode = 108
        myPacient = Pacient(UrgencyTest.connection, '78589211M')
        myMedic = Medic(UrgencyTest.connection, 15233)
        status = 'Alta'
        entry = '10/04/2022 20:30'
        reason = 'Sangrado'
        exploration = 'Observación'
        recomendation = 'Gotas'
        urgency_exit = '10/04/2022 21:30'
        myUrgency = Urgency(
            UrgencyTest.connection,
            myPacient,
            episode,
            myMedic
        )
        self.cur.execute('''INSERT INTO Urgency(episode, pacient, medic, status, entry,
            reason, exploration, recomendation, exit)
            VALUES (?,?,?,?,?,?,?,?,?)''',
                         (
                             episode,
                             myPacient.getDNI(),
                             myMedic.getNPC(),
                             status,
                             entry,
                             reason,
                             exploration,
                             recomendation,
                             urgency_exit))

        # When
        myUrgency.load()

        # Then
        query = 'SELECT episode, pacient, medic, status, entry, '
        query += 'reason, exploration, recomendation, exit '
        query += 'FROM Urgency WHERE episode = ?'
        UrgencyTest.cur.execute(query, (episode,))
        result = UrgencyTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['episode'], episode)
        self.assertEqual(result['pacient'], myPacient.getDNI())
        self.assertEqual(result['medic'], myMedic.getNPC())
        self.assertEqual(result['status'], status)
        self.assertEqual(result['entry'], entry)
        self.assertEqual(result['reason'], reason)
        self.assertEqual(result['exploration'], exploration)
        self.assertEqual(result['recomendation'], recomendation)
        self.assertEqual(result['exit'], urgency_exit)
        self.cur.execute('DELETE FROM Urgency WHERE episode = ?', (episode,))


if __name__ == '__main__':
    unittest.main()
