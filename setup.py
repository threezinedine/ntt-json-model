from setuptools import setup, find_packages

def load_readme():
    with open('README.md', 'r', encoding='utf-8') as file:
        return file.read()

setup(
    name='ntt-json-model',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        "ntt-signal",
        "ntt-observable-list"
    ],
    author='threezinedine',
    author_email='threezinedine@email.com',
    description='Small library for observation mechanism',
    long_description=load_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/threezinedine/ntt-json-model',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=['json', 'mvvm', 'signal', 'ntt'],
    project_urls={
        'Source': 'https://github.com/threezinedine/ntt-json-model',
        'Tracker': 'https://github.com/threezinedine/ntt-json-model/issues',
    },
)