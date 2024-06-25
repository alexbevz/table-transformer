from setuptools import setup, find_packages


def get_requirements() -> list[str]:
    with open('detr/requirements.txt', 'r') as f:
        return [line for line in f.readlines() if not line.startswith('git')]


setup(
    name='table-transformer',
    version='0.1',
    description='Convert the tables at image to the structure tables',
    packages=['detr', 'src', 'scripts'],  # find_packages(),
    author_email='as-bivz@yandex.ru',
    zip_safe=False,
    install_requires=get_requirements(),#.extend('git+https://github.com/cocodataset/panopticapi.git#egg=panopticapi'),
    python_requires='>=3.8',
    package_dir={'table-transformer': 'table-transformer'},
)
