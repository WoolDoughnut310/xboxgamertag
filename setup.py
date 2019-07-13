from setuptools import setup

long_description = open('README.md').read()

setup(
	name='xboxgamertag',
	version='1.0',
	description='Python module to get data from www.xboxgamertag.com',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/WoolDoughnut310/xboxgamertag',
	author='J. Nma',
	author_email='wooldoughnutspi@outlook.com',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries',
		'Programming Language :: Python :: 3'
	],
	keywords='xbox-gamertag python3 data',
	py_modules=['xboxgamertag'],
    install_requires=['requests', 'lxml'],
	python_requires='>=3'
)
