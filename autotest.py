#! /usr/bin/python
ret_val=' '
import sys
import unittest
sys.path.insert(1,sys.path[0]+'/modules')
sys.path.insert(0,sys.path[0]+'/unittests')
import q
import bbot

class test_bbot(unittest.TestCase):
    def setUp(self):
        self.bbot=bbot('127.0.0.1')
    def test_read_dict(self):
        self.assertEqual(self.bbot.read_dict(),None)
    def test_add_factoid(self):
        self.bbot.add_factoid(('abcdefg','gfedcba'))
        self.assertEqual(self.bbot.query_dict('abcdefg'),'gfedcba')
    def test_del_factoid(self):
        self.bbot.add_factoid(('abc','abc'))
        self.bbot.del_factoid('abc')
        self.assertEqual(self.bbot.query_dict('abc'),None)
    def test_io(self):
        self.bbot.add_factoid(('hi','Hi!'))
        self.bbot.write_dict()
        self.bbot.del_factoid('hi')
        self.bbot.read_dict()
        self.assertEqual(self.bbot.query_dict('hi'),'Hi!')
    def test_main_module(self):
        self.assertEqual(self.bbot.go('aj00200',':aj00200!aj00200@FOSSnet/staff/oper/aj00200 PRIVMSG #bots :?hi','#bots'),None)#Do a quick check to make sure it works
class test_api(unittest.TestCase):
    def test_getHost(self):
        self.assertEqual(api.getHost(':aj00200!aj00200@Fossnet/staff/aj00200 PRIVMSG #bots: hi'),'Fossnet/staff/aj00200','api.getHost() isn\'t returning hosts inside PRIVMSGs')
        self.assertEqual(api.getHost(':aj00200!aj00200@127.0.0.1 NOTICE #bots :Hi!'),'127.0.0.1','api.getHost() isn\'t returning hosts inside NOTICEs')

from BBot import bbot
import api
if __name__ == '__main__':
    unittest.main()

