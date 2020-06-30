import setuptools

setuptools.setup(
    name='requires42',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/requires42']
)
