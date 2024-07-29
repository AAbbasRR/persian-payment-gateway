from setuptools import setup, find_packages

setup(
    name='persian_payment_gateway',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    description='A package to manage multiple payment gateways',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Abbas Rahimzadeh',
    author_email='arahimzadeh@gmail.com',
    url='https://github.com/yourusername/payment_gateway_package',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
