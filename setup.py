from setuptools import setup, find_packages

setup(
    name='crawler',
    version='0.1.0',
    author='Joe',
    author_email='joseribeiro1017@gmail.com',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'crawler=crawler:main',
        ],
    },
    description='A simple crawler.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
