from unittest import TestCase
import mock
from start_screen import start_screen
from progressReport import progress_checker
from marking_function import marking_function
class Learning_map_tracker(TestCase):

    def test_list_of_complete(self):
        self.assertTrue(progess_check(), [], 'Must return a list')

    def test_start_screen_execution(self,mock):
        start_screen()
        self.assertTrue(mock.called, 'The function has been called')


    def test_if_progress_int(self):
        output=progress_checker(a)
        self.self.assertEqual(output, type(output)==int , 'message')
