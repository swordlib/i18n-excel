#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="i18n-excel",
    version="0.1.0",
    description="i18n Excel转换工具 - 在Excel和JSON格式之间转换多语言翻译文件",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl",
    ],
    entry_points={
        'console_scripts': [
            'i18n-excel=i18n_excel.main:main',
        ],
    },
    python_requires='>=3.6',
) 