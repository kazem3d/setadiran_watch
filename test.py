import unittest
from send_email import DesireContent
import shutil

class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('start once at startup')
        

    @classmethod
    def tearDownClass(cls):
        print('start once at end')

    def setUp(self):
        print('start on each test start')
        shutil.copyfile('sqlite.db.test', 'sqlite.db')
        
    def tearDown(self) -> None:
        print('start on each test end')
        

    def test_one(self):
        obj = DesireContent(organization_name='راهداری')
        context = obj.get_context()
        self.assertEqual(len(context.strip().split('\n \n')), 2)

    def test_two(self):
        obj = DesireContent(organization_name='شهرداری')
        context = obj.get_context()
        self.assertEqual(len(context.strip().split('\n \n')), 1)

    def test_title(self):
        obj = DesireContent(title='تابلو')
        context = obj.get_context()
        self.assertEqual(len(context.strip().split('\n \n')), 1)

    def test_title_and_org(self):
        obj = DesireContent(organization_name='راهداری',title='تابلو')
        context = obj.get_context()
        self.assertEqual(len(context.strip().split('\n \n')), 1)

    def test_empty(self):
        obj = DesireContent()
        context = obj.get_context()
        self.assertEqual(len(context.strip().split('\n \n')), 3)

    def test_title_and_org_check_number(self):
        obj = DesireContent(organization_name='راهداری',title='تابلو')
        context = obj.get_context()
        self.assertTrue('1234' in context)

    def test_is_sent(self):
        obj = DesireContent()
        obj.is_sent()
        context = obj.get_context()
        self.assertEqual(len(context), 0)


if __name__ == '__main__':
    unittest.main()
