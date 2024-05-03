from setuptools import find_packages, setup

package_name = 'nav_commander'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rmf',
    maintainer_email='ruk.shan@outlook.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'nav_commander = nav_commander.nav_commander:main',
            'csv_data_recorder = nav_commander.csv_data_recorder:main',
            'nav_to_pose = nav_commander.nav_to_pose:main',
        ],
    },
)
