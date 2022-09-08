from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='console_logger',
    version='0.0.9',
    packages=[
        'console_logger',
    ],
    project_urls={
        'Source': 'https://github.com/m1buchnev/console_logger',
    },
    license='MIT License',
    author='Mikhail Buchnev',
    author_email='me@buchnev.page',
    description='Yet another logging package for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='log, logging, logger, console',
    python_requires=">=3.7",
)
