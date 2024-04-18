from setuptools import setup, find_packages

setup(
    name='convert-us-to-uk',
    version='0.1.3',
    packages=find_packages(),
    include_package_data=True,
    description='A simple utility to convert US spelling to UK spelling.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Oliver Blane',
    author_email='oliverblane72@gmail.com',
    url='https://github.com/oliverblane/convert-us-to-uk/tree/main',
    install_requires=[
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'convert_us_to_uk=convert_us_to_uk.converter:main',
        ],
    },
    
)
