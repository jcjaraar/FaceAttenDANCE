#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Setup configuration for FaceAttenDANCE.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="faceattendance",
    version="1.0.0",
    author="[Tu Nombre]",
    author_email="[tu@email.com]",
    description="Sistema de reconocimiento facial para control de asistencia en clases de danza",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuusuario/FaceAttenDANCE",
    project_urls={
        "Bug Tracker": "https://github.com/tuusuario/FaceAttenDANCE/issues",
        "Documentation": "https://github.com/tuusuario/FaceAttenDANCE/docs",
        "Source Code": "https://github.com/tuusuario/FaceAttenDANCE",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Education",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=[],  # No top-level modules
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "pylint>=2.8",
            "mypy>=0.900",
        ],
        "opencv": ["opencv-python>=4.5.0"],
        "reports": ["pandas>=1.3.0"],
        "full": ["opencv-python>=4.5.0", "pandas>=1.3.0"],
    },
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "faceattendance=src.ui.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)