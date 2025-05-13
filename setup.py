from setuptools import setup, find_packages

setup(
    name='amazon_sentiment_analysis',
    version='0.1.0',
    description='A sentiment analysis tool for Amazon product reviews using NLP and Flask.',
    author='Athira',
    author_email='athirabs130@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'pandas',
        'numpy',
        'scikit-learn',
    ],
)
