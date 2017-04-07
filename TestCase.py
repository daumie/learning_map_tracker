from unittest import TestCase
from unittest import mock
from start_screen import start_screen
from progressReport import progress_checker
from marking_function import marking_function
class Learning_map_tracker(TestCase):

    def test_list_of_complete(self):
        output=progress_check()
        self.assertTrue(type(output), (type, 'list'), 'Must return a list')

    
    def test_progress_checker_execution(self,mock):
        progress_checker()
        self.assertTrue(mock.called, 'The function has been called')

    def test_start_screen_execution(self,mock):
        marking_function()
        self.assertTrue(mock.called, 'The function has been called')


    def test_if_progress_int(self):
        output=progress_checker(a)
        self.self.assertEqual(type(output)==int, True , 'The progress checker should return an integer')

    

    
