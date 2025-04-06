from setuptools import setup, find_packages

setup(
    name='ODEkit',
    version='1.0.0',
    description='A simple Python package for solving and visualizing ODEs in physics education',
    author='Ayush Yadav',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/ODEkit',
    packages=find_packages(),
    install_requires=['numpy', 'scipy', 'matplotlib'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    python_requires='>=3.7',
)
