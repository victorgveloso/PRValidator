from setuptools import setup

setup(
    name='prvalidator',
    version='0.1.0',
    packages=['prvalidator'],
    url='',
    license='BSD-3-clauses',
    author='victor',
    author_email='victorgvbh@gmail.com',
    description='Web API to collect and validate Pull Request for my research',
    install_requires=["djangorestframework", "django", "pyyaml", "uritemplate","mysqlclient","python-dotenv","django-environ"]
)
