from setuptools import find_packages, setup

package_name = 'alan_py'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ogrenci',
    maintainer_email='ogrenci@example.com',
    description='RectangleArea sunucu ve istemci',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'server = alan_py.area_server:main',
            'client = alan_py.area_client:main',
        ],
    },
)
