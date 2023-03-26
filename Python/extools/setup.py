try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Project-ExcleTools',
	'author':'Ink',
	'url':'URL to get it at.',
	'download_url':'Where to download it.',
	'author_email': 'ink.see@gmail.com',
	'version': '0.1',
	'install_requires':['nose'],
	'packages': ['extools'],
	'scripts':[],
	'name': 'projectname'
}

setup(**config)