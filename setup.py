from setuptools import setup


setup(
    name='cgi_utils',
    version='0.1.0',
    url='https://github.com/zeevro/cgi_utils',
    download_url='https://github.com/zeevro/cgi_utils/archive/master.zip',
    author='Zeev Rotshtein',
    author_email='zeevro@gmail.com',
    maintainer='Zeev Rotshtein',
    maintainer_email='zeevro@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: Public Domain',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
    ],
    license=None,
    description='A minimal CGI library',
    keywords=[
        'Web',
        'CGI',
    ],
    zip_safe=True,
    py_modules=[
        'cgi_utils',
    ],
)
