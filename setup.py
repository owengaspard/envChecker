from setuptools import find_packages, setup

setup(
    name='envChecker',
    packages=find_packages(include=['envChecker']),
    version='0.2.0',
    description='Compares your .env to .env.example to find anything missing in .env',
    author='Owen Gaspard',
    license='MIT',
    install_requires=['python-dotenv'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)