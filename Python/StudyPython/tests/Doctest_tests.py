from nose.tools import *
from StudyPython.Doctest import * 

def test_Doctest():
	#log.debug("logtest")
	assert_equal(square(2),4)
	assert_equal(square(-2),4)

