from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='diec',
    version='3.0',
    packages=find_packages(),
    license='MIT',
    description='A tool that encodes text and provides a key for decoding!',
    author='Eldritchy',
    author_email='eldritchy.help@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Eldritchyl/diec',
    download_url='https://github.com/Eldritchy/diec/archive/refs/tags/v3.0.tar.gz',
    keywords=['diec', 'encoding', 'decoding'],
    install_requires=[
        'binaryconvert',
    ],
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points='''
        [console_scripts]
        diec-cli=diec.cli:cli
    ''',
)
