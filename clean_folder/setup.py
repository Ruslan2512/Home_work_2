from setuptools import setup

setup(
    name='clean_folder',
    version='1',
    description='Sort files in directiry',
    url='https://github.com/Ruslan2512/Home_work_2',
    author='Ruslan Sirenko',
    author_email='ruslansirenko25@gmail.com',
    entry_points={'console_scripts': ['clean-folder = clean_folder.sort_files:main']}
)