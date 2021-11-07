from setuptools import setup
import mp_database

setup(
    name='mp_database',
    version=mp_database.__version__,
    description='Moon Package for Database(mongodb, mariadb, ...)',
    url='https://github.com/hopelife/mp_database',
    author='Moon Jung Sam',
    author_email='monblue@snu.ac.kr',
    license='MIT',
    packages=['mp_database'],
    # entry_points={'console_scripts': ['mp_database = mp_database.__main__:main']},
    keywords='database',
    # python_requires='>=3.8',  # Python 3.8.6-32 bit
    # install_requires=[ # 패키지 사용을 위해 필요한 추가 설치 패키지
    #     'pymongo',
    # ],
    # zip_safe=False
)
