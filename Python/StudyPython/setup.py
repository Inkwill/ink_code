try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project of study python',
	'author':'Ink',
	'url':'URL to get it at.',
	'download_url':'Where to download it.',
	'author_email': 'ink.see@gmail.com',
	'version': '0.1',
	'install_requires':['nose'],
	'packages': ['StudyPython'],
	'scripts':[],
	'name': 'studypython'
}

setup(**config)
