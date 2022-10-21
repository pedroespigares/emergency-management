import os
import sys
sys.path.append(os.path.abspath('.'))

from Clases.clinicalJudgment import ClinicalJudgment
import unittest
import sqlite3


class ClinicalJudgmentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE Clinical_Judgment(
                  code text primary key,
                  description text
            )''')

    @classmethod
    def tearDownClass(cls):
        cls.cur.execute('''DROP TABLE Clinical_Judgment''')
        cls.connection.close()

    def test_constructor_AllParams_Ok(self):
        # Given
        code = '802.11'
        description = 'Fractura de clavícula abierta'

        # When
        myClinicalJudgment = ClinicalJudgment(
            ClinicalJudgmentTest.connection,
            code,
            description,
        )

        # Then
        self.assertIsNotNone(myClinicalJudgment)
        self.assertIsInstance(myClinicalJudgment, ClinicalJudgment)

    def test_constructor_OnlyObligatoryParams_Ok(self):
        # Given
        code = '802.11'

        # When
        myClinicalJudgment = ClinicalJudgment(
            ClinicalJudgmentTest.connection,
            code
        )

        # Then
        self.assertIsNotNone(myClinicalJudgment)
        self.assertIsInstance(myClinicalJudgment, ClinicalJudgment)

    def test_Save_Ok(self):
        # Given
        code = '802.11'
        description = 'Fractura de clavícula abierta'
        myClinicalJudgment = ClinicalJudgment(
            ClinicalJudgmentTest.connection,
            code,
            description
        )

        # When
        myClinicalJudgment.save()

        # Then
        query = 'SELECT code, description '
        query += 'FROM Clinical_Judgment WHERE code = ?'
        ClinicalJudgmentTest.cur.execute(query, (code,))
        result = ClinicalJudgmentTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['code'], code)
        self.assertEqual(result['description'], description)
        self.cur.execute(
            'DELETE FROM Clinical_Judgment WHERE code = ?', (code,))

    @unittest.expectedFailure
    def test_load_Fail(self):
        # Given
        code = 123412
        myClinicalJudgment = ClinicalJudgment(
            ClinicalJudgmentTest.connection,
            code,
        )

        # When
        myClinicalJudgment.load()

    def test_Save_WithSetter_Ok(self):
        # Given
        code = '802.11'
        description = 'Fractura de clavícula abierta'

        myClinicalJudgment = ClinicalJudgment(
            ClinicalJudgmentTest.connection,
            code,)

        # When
        myClinicalJudgment.setDescription(description)
        myClinicalJudgment.save()

        # Then
        query = 'SELECT code, description '
        query += 'FROM Clinical_Judgment WHERE code = ?'
        ClinicalJudgmentTest.cur.execute(query, (code,))
        result = ClinicalJudgmentTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['code'], code)
        self.assertEqual(result['description'], description)
        self.cur.execute(
            'DELETE FROM Clinical_Judgment WHERE code = ?', (code,))

    def test_Delete_Ok(self):
        # Given
        code = '802.11'
        description = 'Fractura de clavícula abierta'

        myClinicalJudgment = ClinicalJudgment(
            ClinicalJudgmentTest.connection,
            code,)
        self.cur.execute('''INSERT INTO Clinical_Judgment(code, description)
        VALUES (?,?)''',
                         (code,
                          description))

        # When
        myClinicalJudgment.delete()

        # Then
        ClinicalJudgmentTest.cur.execute(
            'SELECT code FROM Clinical_Judgment WHERE code = ?', (code,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        ClinicalJudgmentTest.cur.execute(
            '''SELECT description FROM Clinical_Judgment
            WHERE description = ?''', (description,))
        result = self.cur.fetchall()
        self.assertEqual(result, [])

    def test_update_Ok(self):
        # Given
        code = '802.11'
        description = 'Fractura de clavícula abierta'
        description2 = 'Sangrado de oído'
        myClinicalJudgment = ClinicalJudgment(
            ClinicalJudgmentTest.connection,
            code,
            description
        )
        self.cur.execute('''INSERT INTO Clinical_Judgment(code, description)
        VALUES (?,?)''', (
            code,
            description))

        # When
        myClinicalJudgment.setDescription(description2)
        myClinicalJudgment.update()

        # Then
        ClinicalJudgmentTest.cur.execute(
            '''SELECT code, description FROM
            Clinical_Judgment WHERE code = ?''', (code,))
        result = self.cur.fetchone()
        self.assertEqual(result['description'], description2)
        self.cur.execute(
            'DELETE FROM Clinical_Judgment WHERE code = ?', (code,))

    def test_load_Ok(self):
        code = '802.11'
        description = 'Fractura de clavícula abierta'
        myClinicalJudgment = ClinicalJudgment(
            ClinicalJudgmentTest.connection,
            code
        )
        self.cur.execute('''INSERT INTO Clinical_Judgment(code, description)
        VALUES (?,?)''',
                         (code,
                          description))

        # When
        myClinicalJudgment.load()

        # Then
        self.assertEqual(myClinicalJudgment.getDescription(), description)
        self.cur.execute(
            'DELETE FROM Clinical_Judgment WHERE code = ?', (code,))


if __name__ == '__main__':
    unittest.main()
