from cgi import test
from operator import length_hint
import unittest
from user import user

class Testuse(unittest.TestCase):
    
    def setUp(self):
       self.new_user = user("shamim","maloba","306524"),

    def test_init(self):
        self.assertEqual(self.new_user.user_name,"shamim")
        self.asserEqual(self.new_user.password,"306524")
    
    def test_save_user(self):
        self.new_user.save_user_user()
        self.assertEqual(len(user.user_list),1)

    def test_delete_user(self):
       self.new_contact.save_contact()
       test_user = user("Test","user","0798151788",test@user.com)#new contact
       test_user.save_user()

       self.new_user.delete_user() 
       self.assertEqual(len(user.user_list),1)
    if __name__ =='_main_':
        unittest.main()





