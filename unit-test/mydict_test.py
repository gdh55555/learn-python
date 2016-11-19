#!/usr/bin/python  
#-*- coding:utf-8 -*-  
__author__ = "goodhe"

#=====================================

#File Name: up-down.py
#Mail: gdhe55555@gmail.com  
#Created Time: 2016-11-19 19:12:57

#=====================================

import unittest
from mydict import Dict

class TestDict(unittest.TestCase):
    
    def test_init(self):
        d = Dict(a=1, b ="test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d["key"]

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        print("setUp...")

    def tearDown(self):
        print("tearDown")
