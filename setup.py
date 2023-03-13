from setuptools import setup

setup(
    name='chatgpt_jupyter',
    version='0.1',
    description='Jupyter extension that uses the ChatGPT API to provide helpful suggestions for error messages',
    py_modules=['chatgpt_jupyter'],
    install_requires=[
        'requests',
        'notebook',
    ],
    entry_points={
        'jupyter_server_extension': [
            'chatgpt_jupyter = chatgpt_jupyter:load_jupyter_server_extension',
        ],
    },
)
