from nose.tools import *
from StudyPython import lexicon

def test_directions():
	assert_equal(lexicon.scan("north"), [('direction', 'north')])
	result = lexicon.scan("north south East")
	assert_equal(result, [('direction', 'north'),('direction', 'south'),('direction', 'East')])

def test_verbs():
	assert_equal(lexicon.scan("go"), [('verb','go')])
	result = lexicon.scan("Go kill eat")
	assert_equal(result, [('verb', 'Go'),('verb', 'kill'),('verb', 'eat')])

def test_stops():
	assert_equal(lexicon.scan("The"), [('stop','The')])
	result = lexicon.scan("the in OF")
	assert_equal(result, [('stop', 'the'),('stop', 'in'),('stop', 'OF')])

def test_nouns():
	assert_equal(lexicon.scan("bear"), [('noun','bear')])
	result = lexicon.scan("home I")
	assert_equal(result, [('noun', 'home'),('noun', 'I')])

def test_numbers():
	assert_equal(lexicon.scan("1234"), [('number','1234')])
	result = lexicon.scan("3 91234 3.14")
	assert_equal(result, [('number', '3'),('number', '91234'),('number', '3.14')])

def test_errors():
	assert_equal(lexicon.scan("ASDFADFASDF"), [('error','ASDFADFASDF')])
	result = lexicon.scan("bear IAS princess")
	assert_equal(result, [('noun', 'bear'),('error', 'IAS'),('noun', 'princess')])


