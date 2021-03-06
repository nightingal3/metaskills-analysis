from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='A short description of the project.',
    author='nightingal3',
    license='MIT',
    install_requires=[
        "Click"
    ],
    entry_points={
        "console_scripts": [
            "clean=src.data.clean_metaskills:clean",
            "anonymize=src.data.anonymize_utorid:anonymize"
        ]
    }
)
