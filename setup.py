from setuptools import setup, find_packages

setup(
    name='data_analysis_project',  # Nome do pacote
    version='0.1',  # Versão inicial
    packages=find_packages(),  # Detecta e inclui todos os pacotes Python no projeto
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'scikit-learn',
        'flask'
    ],  # Dependências do projeto
    entry_points={
        'console_scripts': [
            'data_analysis=src.main:main',
        ],
    },  # Scripts executáveis
    include_package_data=True,  # Inclui outros arquivos especificados no MANIFEST.in
    description='Um projeto de análise de dados em Python',
    author='Felipe Batista dos Santos',
    author_email='felipebs779@gmail.com',
    url='https://github.com/FelipeBatistadosSantos/data_analysis_project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
