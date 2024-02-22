from setuptools import setup

package_name = 'simple_communicate'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    py_modules=[
        'simple_communicate.simple_talker',
        'simple_communicate.simple_listener',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='htm2323',
    author_email="",
    maintainer='htm2323',
    maintainer_email="",
    keywords=['ROS', 'ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='TODO: Package description.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker= simple_communicate.simple_talker:main',
            'listener= simple_communicate.simple_listener:main',
        ],
    },
)
