import os
import sys
sys.path.append(os.path.abspath('.'))

import sqlite3
import unittest
from Clases.pacient import Pacient


class PacientTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE Pacient(
                  dni text primary key,
                  history_number int,
                  name text,
                  surnames text,
                  birthday text,
                  nationality text,
                  sex text,
                  social_security text,
                  phone int,
                  address text,
                  history_status text
            )''')

    @classmethod
    def tearDownClass(cls):
        cls.cur.execute('''DROP TABLE Pacient''')
        cls.connection.close()

    def test_constructor_AllParams_Ok(self):
        # Given
        dni = '78589211M'
        history_number = 234562347
        name = 'Pedro'
        surnames = 'Espigares Asenjo'
        birthday = '04/03/2003'
        nationality = 'Española'
        sex = 'H'
        social_security = 'AN 656345345'
        phone = 626366616
        address = 'Avenida Fernando de los Ríos Nº54'
        history_status = 'Activo'

        # When
        myPacient = Pacient(
            PacientTest.connection,
            dni,
            history_number,
            name,
            surnames,
            birthday,
            nationality,
            sex,
            social_security,
            phone,
            address,
            history_status
        )

        # Then
        self.assertIsNotNone(myPacient)
        self.assertIsInstance(myPacient, Pacient)

    def test_constructor_OnlyObligatoryParams_Ok(self):
        # Given
        dni = '12546754G'

        # When
        myPacient = Pacient(
            PacientTest.connection,
            dni
        )

        # Then
        self.assertIsNotNone(myPacient)
        self.assertIsInstance(myPacient, Pacient)

    def test_Save_Ok(self):
        # Given
        dni = '78589211M'
        history_number = 234562347
        name = 'Pedro'
        surnames = 'Espigares Asenjo'
        birthday = '04/03/2003'
        nationality = 'Española'
        sex = 'H'
        social_security = 'AN 656345345'
        phone = 626366616
        address = 'Avenida Fernando de los Ríos Nº54'
        history_status = 'Activo'
        myPacient = Pacient(
            PacientTest.connection,
            dni,
            history_number,
            name,
            surnames,
            birthday,
            nationality,
            sex,
            social_security,
            phone,
            address,
            history_status
        )

        # When
        myPacient.save()

        # Then
        query = 'SELECT dni, name, surnames, birthday, nationality, '
        query += 'sex, social_security, phone, address, history_status '
        query += 'FROM Pacient WHERE dni = ?'
        PacientTest.cur.execute(query, (dni,))
        result = PacientTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['dni'], dni)
        self.assertEqual(result['name'], name)
        self.assertEqual(result['surnames'], surnames)
        self.assertEqual(result['birthday'], birthday)
        self.assertEqual(result['nationality'], nationality)
        self.assertEqual(result['sex'], sex)
        self.assertEqual(result['social_security'], social_security)
        self.assertEqual(result['phone'], phone)
        self.assertEqual(result['address'], address)
        self.assertEqual(result['history_status'], history_status)
        self.cur.execute('DELETE FROM Pacient WHERE dni = ?', (dni,))

    def test_Save_WithSetter_Ok(self):
        # Given
        dni = '78589211M'
        history_number = 234562347
        name = 'Pedro'
        surnames = 'Espigares Asenjo'
        birthday = '04/03/2003'
        nationality = 'Española'
        sex = 'H'
        social_security = 'AN 656345345'
        phone = 626366616
        address = 'Avenida Fernando de los Ríos Nº54'
        history_status = 'Activo'
        myPacient = Pacient(
            PacientTest.connection,
            dni,
            history_number,
            name,
            surnames,
            birthday,
            nationality,
        )

        # When
        myPacient.setSex(sex)
        myPacient.setSocialSecurity(social_security)
        myPacient.setPhone(phone)
        myPacient.setAddress(address)
        myPacient.setStatus(history_status)
        myPacient.save()

        # Then
        query = 'SELECT dni, name, surnames, birthday, nationality, '
        query += 'sex, social_security, phone, address, history_status '
        query += 'FROM Pacient WHERE dni = ?'
        PacientTest.cur.execute(query, (dni,))
        result = PacientTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['dni'], dni)
        self.assertEqual(result['name'], name)
        self.assertEqual(result['surnames'], surnames)
        self.assertEqual(result['birthday'], birthday)
        self.assertEqual(result['nationality'], nationality)
        self.assertEqual(result['sex'], sex)
        self.assertEqual(result['social_security'], social_security)
        self.assertEqual(result['phone'], phone)
        self.assertEqual(result['address'], address)
        self.assertEqual(result['history_status'], history_status)
        self.cur.execute('DELETE FROM Pacient WHERE dni = ?', (dni,))

    def test_Delete_Ok(self):
        # Given
        dni = '78589211M'
        history_number = 234562347
        name = 'Pedro'
        surnames = 'Espigares Asenjo'
        myPacient = Pacient(
            PacientTest.connection,
            dni,
            history_number,
            name,
            surnames
        )
        self.cur.execute('''INSERT INTO Pacient(dni, history_number ,name, surnames)
        VALUES (?,?,?,?)''',
                         (dni,
                          history_number,
                          name,
                          surnames,))

        # When
        myPacient.delete()

        # Then
        PacientTest.cur.execute(
            'SELECT dni FROM Pacient WHERE dni = ?', (dni,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        PacientTest.cur.execute(
            'SELECT history_number FROM Pacient WHERE history_number = ?',
            (history_number,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        PacientTest.cur.execute(
            'SELECT name FROM Pacient WHERE name = ?', (name,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        PacientTest.cur.execute(
            'SELECT surnames FROM Pacient WHERE surnames = ?', (surnames,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])

    def test_update_Ok(self):
        # Given
        dni = '78589211M'
        history_number = 234562347
        name = 'Pedro'
        name2 = 'Sara'
        surnames = 'Espigares Asenjo'
        surnames2 = 'Caro Martín'
        myPacient = Pacient(
            PacientTest.connection,
            dni,
            history_number,
            name,
            surnames
        )
        self.cur.execute('''INSERT INTO Pacient(dni, history_number ,name, surnames)
        VALUES (?,?,?,?)''', (
            dni,
            history_number,
            name,
            surnames,))

        # When
        myPacient.setName(name2)
        myPacient.setSurnames(surnames2)
        myPacient.update()

        # Then
        PacientTest.cur.execute(
            'SELECT dni, name, surnames FROM Pacient WHERE dni = ?', (dni,))
        result = self.cur.fetchone()
        self.assertEqual(result['name'], name2)
        self.assertEqual(result['surnames'], surnames2)
        self.cur.execute('DELETE FROM Pacient WHERE dni = ?', (dni,))

    def test_load_Ok(self):
        dni = '78589211M'
        history_number = 234562347
        name = 'Pedro'
        surnames = 'Espigares Asenjo'
        myPacient = Pacient(
            PacientTest.connection,
            dni
        )
        self.cur.execute('''INSERT INTO Pacient(dni, history_number ,name, surnames)
        VALUES (?,?,?,?)''',
                         (dni,
                          history_number,
                          name,
                          surnames,))

        # When
        myPacient.load()

        # Then
        self.assertEqual(myPacient.getName(), name)
        self.assertEqual(myPacient.getSurnames(), surnames)
        self.cur.execute('DELETE FROM Pacient WHERE dni = ?', (dni,))


if __name__ == '__main__':
    unittest.main()
