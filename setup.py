from setuptools import setup, find_packages
import os

author_0 = "Juan Carlos Díaz Pérez"
email_0 = "juankidipe@gmail.com"

author_1 = "Iñigo Fernández-Sopeña Hernández"
email_1 = "inigofernandezsopena@gmail.com"

author_2 = "Mattin Peña Galparsoro"
email_2 = "mattinpena@gmail.com"

author_3 = "Daniel Tijeras Casado"
email_3 = "danieltc2608@gmail.com"

author_4 =  "Andrés Velasco Sánchez"
email_4 = "andres.velasco.sanchez.2023@gmail.com"

authors = ", ".join([author_0, author_1, author_2, author_3, author_4])

emails = ", ".join([email_0, email_1, email_2, email_3, email_4])


setup(
    name='base_template_project',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas'

    ],
    author=authors,
    author_email=emails,
    description='A base template for spanish vocals clasiffication',
    python_requires='>=3.7',
)