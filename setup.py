from setuptools import setup, find_packages


setup(
    name="low_voltage",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    #python_requires='>=3.7',
    #install_requires=[
	#'influxdb-client',
	#'paho-mqtt',
	#'pyserial',
    #],
)
