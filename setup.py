from setuptools import setup, find_packages

setup(
    name='helloworld',
    version='1.0.5.dev1',
    packages=find_packages(),
    url='',
    license='',
    author='Lukas Schmid',
    author_email='lukas.m.schmid@gmail.com',
    description='hello-world rest application',
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
