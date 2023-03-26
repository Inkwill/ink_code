from nose.tools import *
from StudyPython import parse

def test_peek_verb():
	s = parse.Sentence("Go home")
	assert_equal(s.peek_verb(), 0)
	s = parse.Sentence("I go to school")
	assert_equal(s.peek_verb(), 1)
	s = parse.Sentence("I need to go")
	assert_equal(s.peek_verb(), 2)
	s = parse.Sentence("Yes")
	assert_equal(s.peek_verb(), None)

def test_peek_subject():
	s = parse.Sentence("Go home")
	assert_equal(s.peek_subject(), None)
	s = parse.Sentence("I go to school")
	assert_equal(s.peek_subject(), 0)
	s = parse.Sentence("The girl I loved is very beuatiful")
	assert_equal(s.peek_subject(), None)

def test_peek_object():
	s = parse.Sentence("Go home")
	assert_equal(s.peek_object(), 1)
	s = parse.Sentence("I go to school")
	assert_equal(s.peek_object(), 2)
	s = parse.Sentence("The girl I loved is very beuatiful")
	assert_equal(s.peek_object(), None)

def test_parse():
	s = parse.Sentence("Go home")
	assert_equal(s.subject[1], 'player')
	assert_equal(s.verb[1], 'Go')
	assert_equal(s.object[1], 'home')
