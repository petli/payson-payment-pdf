#!/usr/bin/env python3

from setuptools import setup

setup(
    name = 'payson-payment-pdf',
    version = '1.0',
    license = 'MIT',
    description = 'Convert a CSV report of Payson payments into separate PDF files for accounting',
    author = 'Peter Liljenberg',
    author_email = 'peter.liljenberg@gmail.com',
    keywords = 'payson accounting',
    url = 'https://github.com/petli/payson-payment-pdf',

    scripts = [ 'payson2pdf' ],

    install_requires = [
        'fpdf >= 1.7, < 2',
    ]
)
