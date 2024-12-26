from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='diec',
    version='3.2',
    packages=find_packages(),
    license='MIT',
    description='A tool that encodes text and provides a key for decoding!',
    author='VelisCore',
    author_email='velis.help@web.de',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/VelisCore/diec',
    download_url='https://github.com/VelisCore/diec/archive/refs/tags/v3.2.tar.gz',
    keywords=['diec', 'encoding', 'decoding', 'Velis'],
    install_requires=[
        'binaryconvert',
        'argon2',
        'cryptography',
        'click',
    ],
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'diec-cli=diec.cli:cli',
        ],
        'distutils.commands': [
            'diec = diec.cli:main',
        ],
    },
    dependency_links=[
        "https://github.com/VelisCore/diec/packages"
    ],
)
