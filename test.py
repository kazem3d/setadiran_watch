import unittest
# from send_email import DesireContent


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('start once at startup')

    @classmethod
    def tearDownClass(cls):
        print('start once at end')

    def setUp(self):
        print('start on each test start')
        # obj1 = DesireContent(organization_name='راهداری')
        
    def tearDown(self) -> None:
        print('start on each test end')
        

    def test_sum(self):
        print('fffffffffff')
        self.assertEqual(1+2,3)

    # def test_one(self):
    #     obj1 = DesireContent(organization_name='راهداری')
    #     self.assertEqual(obj1.get_context(), "***")


if __name__ == '__main__':
    unittest.main()
