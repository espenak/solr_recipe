from setuptools import setup, find_packages


setup(name = 'solr_recipe',
    description = 'Buildout recipe that installs solr using Maven.',
    license='Apache',
    version = '1.0',
    url = 'http://github.com/espenak/solr_recipe',
    author = 'Espen Angell Kristiansen',
    long_description='See https://github.com/espenak/solr_recipe',
    packages=find_packages(exclude=['ez_setup', 'fabfile']),
    install_requires = ['distribute', 'Django', 'Jinja2'],
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'zc.buildout': [
            'default = solr_recipe.install:InstallSolr'
            ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Framework :: Buildout',
        'Programming Language :: Python'
    ]
)
