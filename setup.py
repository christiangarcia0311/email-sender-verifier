# Email Sender Verifier Libraryr
# Created by Christian Garcia

# Import Required libraries for setting up packages
from setuptools import setup, find_packages

# Display markdown description in repo/main page 
with open('README.md', 'r', encoding='utf-8') as file:
    description = file.read()

# Set up package, versions and dependencies
setup(
        name='email-sender-verifier',
        version='2.2.0',
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'Verifier = Verifier.__main__:main'
                ]
            },
        author='Christian Garcia',
        author_email='iyaniyan03112003@gmail.com',
        description='Email Verifier is a python library designed for sending One-Time-Passwords (OTP) and performing code verification via email.',
        long_description=description,
        long_description_content_type='text/markdown',
        url='https://github.com/christiangarcia0311/email-sender-verifier',
        license='MIT',
        classifiers= [
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
        )

