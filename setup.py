from setuptools import setup

setup(name='keg-bot',
      version='0.0.0',
      packages=['keg-bot'],
      entry_points={
          'console_scripts': [
              'keg-bot = keg-bot.__main__:main'
          ]
      }
      )
