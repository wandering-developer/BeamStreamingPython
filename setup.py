import setuptools
REQUIRED_PACKAGES = ['jsonschema','apache_beam[gcp]','google-cloud-bigquery','google-cloud-storage','pymysql']
PACKAGE_NAME = 'com.example.test.pipeline'
PACKAGE_VERSION = '1.0'
setuptools.setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description='Test Beam Project for Pubsub Read',
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
)
