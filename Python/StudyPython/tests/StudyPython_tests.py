from nose.tools import *
from StudyPython.Doctest import * 

def setup():
	print("SETUP!")

def teardown():
	print("TEAR DOWN!")

def test_basic():
	print("I RAN!")
