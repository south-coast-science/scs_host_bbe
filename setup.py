from setuptools import setup, find_packages


with open('requirements.txt') as req_txt:
    required = [line for line in req_txt.read().splitlines() if line]

try:
    import pypandoc
    from os import path
    here = path.abspath(path.dirname(__file__))
    long_description = pypandoc.convert(path.join(here, 'README.md'), 'rst'),
except RuntimeError:
    long_description = ""
except ImportError:
    long_description = ""

setup(
    name='scs_host_bbe',
    version='0.1.1',
    description='Abstractions for Beaglebone based systems',
    author='South Coast Science',
    author_email='contact@southcoastscience.com',
    url='https://github.com/south-coast-science/scs_host_bbe',
    package_dir={'':'src'},
    packages=find_packages('src'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=required,
    platforms=['any'],
    python_requires=">=3.3",
)
   