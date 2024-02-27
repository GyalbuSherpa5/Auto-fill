from setuptools import setup, find_packages

setup(
    name="auto_fill_don",
    version="0.3",
    packages=find_packages(),
    install_requires=[
        'pyperclip>=1.8.2',
        'pycryptodome>=3.20.0',
    ],
    python_requires=">=3.12.2",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        # Add other supported Python versions if applicable
    ],
    entry_points={
        "console_scripts": [
            "auto_fill_don = auto_fill_don:autofill",
            "save = auto_fill_don:add_entry",
            "load = auto_fill_don:retrieve_passwords"
        ]
    }
)
