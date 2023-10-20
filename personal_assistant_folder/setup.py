from setuptools import setup, find_packages

setup(name='Jarlis',
      version='0.0.1',
      packages=find_packages(),
      author='pycore17 group 6',
      description='Manage your Address book, Notes list, sort your files',
      entry_points={
          'console_scripts': ['jarlis = personal_assistant_folder.personal_assistant:init']
      }
      )
