from setuptools import setup, find_packages

with open('requirements.in') as f:
    install_requires = [line for line in f if line and line[0] not in '#']

setup(
    name='apperator',
    version='0.0.5',
    url='https://github.com/chauffer/apperator',
    author='Simone Esposito',
    author_email='chaufnet@gmail.com',
    download_url='https://github.com/chauffer/apperator',
    packages=find_packages(),
    install_requires=install_requires,
#    data_files=[('templates', ['apperator/templates/apperator.jinja'])],
    entry_points={'console_scripts': 'apperator=apperator:cli'},
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
    ]
)
