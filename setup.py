import setuptools

setuptools.setup(
        name = 'jetan',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        install_requires=[
                'tqdm',
                'pyyaml',
            ],
        entry_points = {
            'console_scripts':[
                'jetan = jetan.cli.jetan:main',
                ]},)

