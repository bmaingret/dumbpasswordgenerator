import unittest

from dumbpasswordgenerator import passwordgenerator

class PasswordGeneratorTtest(unittest.TestCase):

    def setUp(self):
        self.length = 10
        self.generator_0 = passwordgenerator.GenericPasswordGenerator()
        self.generator_a = passwordgenerator.GenericPasswordGenerator(self.length)
        self.generator_1 = passwordgenerator.NumberPasswordGenerator(self.length)

    def test_test(self):
        self.assertEqual(True, True)

    def test_password_length(self):
        self.assertEqual(len(self.generator_0.new_password()), 12)
        self.assertEqual(len(self.generator_a.new_password()), self.length)
        self.assertEqual(len(self.generator_1.new_password(length=5)), 5)
        

    def test_randomness(self):
        self.assertNotEqual(self.generator_a.new_password(), self.generator_a.new_password())
        self.assertNotEqual(self.generator_1.new_password(), self.generator_1.new_password())
    

    def test_old_password(self):
        new_password = self.generator_0.new_password()
        self.assertEqual(new_password, self.generator_0.previous_password())
        

if __name__ == '__main__':
    unittest.main()
