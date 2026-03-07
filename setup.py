from setuptools import setup

setup(
    name="task-cli",
    version="0.1",
    py_modules=["app"], # Nombre de tu archivo sin el .py
    entry_points={
        'console_scripts': [
            'task-cli=app:main', # comando=archivo:función_a_ejecutar
        ],
    },
)