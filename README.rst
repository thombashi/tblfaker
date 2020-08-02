.. contents:: **tblfaker**
   :backlinks: top
   :depth: 2


Summary
============================================
tblfaker is a Python library to generate fake tabular data.

.. image:: https://badge.fury.io/py/tblfaker.svg
    :target: https://badge.fury.io/py/tblfaker
    :alt: PyPI package version

.. image:: https://img.shields.io/pypi/pyversions/tblfaker.svg
    :target: https://pypi.org/project/tblfaker
    :alt: Supported Python versions

.. image:: https://img.shields.io/travis/thombashi/tblfaker/master.svg?label=Linux/macOS%20CI
    :target: https://travis-ci.org/thombashi/tblfaker
    :alt: Linux/macOS CI status

.. image:: https://img.shields.io/appveyor/ci/thombashi/tblfaker/master.svg?label=Windows%20CI
    :target: https://ci.appveyor.com/project/thombashi/tblfaker/branch/master
    :alt: Windows CI status

.. image:: https://coveralls.io/repos/github/thombashi/tblfaker/badge.svg?branch=master
    :target: https://coveralls.io/github/thombashi/tblfaker?branch=master
    :alt: Test coverage


Usage
============================================

Basic Usage
--------------------------------------------

Generate tabular data at random
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:Sample Code:
    .. code-block:: python

        from tblfaker import TableFaker

        faker = TableFaker()

        print("[1]")
        for row in faker.generate(["name", "address"], rows=4).as_tuple():
            print(row)

        print("\n[2]")
        for row in faker.generate(["name", "address"], rows=4).as_tuple():
            print(row)

:Output:
    .. code-block::

        [1]
        Row(name='Jonathan Hendrix', address='368 Melanie Inlet Suite 890\nLake Stephanie, MT 17441')
        Row(name='Kristina Simmons', address='3867 Perry Alley Suite 957\nLindafurt, FL 12507')
        Row(name='Rebecca Velasquez', address='107 Karla Forges Apt. 925\nEast Jonathan, NC 85462')
        Row(name='Jordan Morris', address='6341 Jessica Walks\nReynoldsshire, MD 05131')

        [2]
        Row(name='Caitlin Bush', address='87380 Barbara Haven Suite 042\nHutchinsonburgh, IA 39544')
        Row(name='Jennifer King', address='39729 Gray Inlet Apt. 693\nPort Peter, AL 80733')
        Row(name='Stephanie Smith', address='256 Emily Street\nCooperhaven, MS 70299')
        Row(name='Nicholas Miller', address='59845 Daniel Ford Suite 729\nDamontown, UT 19811


Reproduce same tabular data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fake tabular data can reproduce by passing the same ``seed`` value to ``TableFaker`` constructor.

:Sample Code:
    .. code-block:: python

        from tblfaker import TableFaker

        seed = 1

        print("[1]")
        faker = TableFaker(seed=seed)
        for row in faker.generate(["name", "address"], rows=4).as_tuple():
            print(row)

        print("\n[2]")
        faker = TableFaker(seed=seed)
        for row in faker.generate(["name", "address"], rows=4).as_tuple():
            print(row)

:Output:
    .. code-block::

        [1]
        Row(name='Ryan Gallagher', address='6317 Mary Light\nSmithview, HI 13900')
        Row(name='Amanda Johnson', address='3608 Samuel Mews Apt. 337\nHousebury, WA 13608')
        Row(name='Willie Heath', address='868 Santiago Grove\nNicolehaven, NJ 05026')
        Row(name='Dr. Jared Ortega', address='517 Rodriguez Divide Suite 570\nWest Melinda, NH 85325')

        [2]
        Row(name='Ryan Gallagher', address='6317 Mary Light\nSmithview, HI 13900')
        Row(name='Amanda Johnson', address='3608 Samuel Mews Apt. 337\nHousebury, WA 13608')
        Row(name='Willie Heath', address='868 Santiago Grove\nNicolehaven, NJ 05026')
        Row(name='Dr. Jared Ortega', address='517 Rodriguez Divide Suite 570\nWest Melinda, NH 85325')


Set locale for fake data
--------------------------------------------
:Sample Code:
    .. code-block:: python

        from tblfaker import TableFaker

        faker = TableFaker(locale="ja_JP")

        for row in faker.generate(["name", "address"], rows=4).as_tuple():
            print(row)

:Output:
    .. code-block::

        Row(name='工藤 健一', address='宮崎県武蔵村山市六番町19丁目15番11号')
        Row(name='井上 聡太郎', address='愛媛県長生郡白子町豊町33丁目7番20号 戸島コート620')
        Row(name='大垣 美加子', address='京都府山武郡芝山町三ノ輪34丁目15番8号 クレスト所野560')
        Row(name='宇野 くみ子', address='宮城県八街市西浅草20丁目24番6号')


Generate data in other data formats
--------------------------------------------

Generate data in dict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:Sample Code:
    .. code-block:: python

        from tblfaker import TableFaker
        import json

        faker = TableFaker(seed=1)

        print(json.dumps(faker.generate(["name", "address"], rows=2, table_name="dict").as_dict(), indent=4))

:Output:
    .. code-block:: json

        {
            "dict": [
                {
                    "name": "Ryan Gallagher",
                    "address": "6317 Mary Light\nSmithview, HI 13900"
                },
                {
                    "name": "Amanda Johnson",
                    "address": "3608 Samuel Mews Apt. 337\nHousebury, WA 13608"
                }
            ]
        }

Generate data in pandas.DataFrame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:Sample Code:
    .. code-block:: python

        from tblfaker import TableFaker

        faker = TableFaker(seed=seed)

        print(faker.generate(["name", "address"], rows=4).as_dataframe())

:Output:
    .. code-block::

                       name                                            address
        0    Ryan Gallagher               6317 Mary Light\nSmithview, HI 13900
        1    Amanda Johnson     3608 Samuel Mews Apt. 337\nHousebury, WA 13608
        2      Willie Heath          868 Santiago Grove\nNicolehaven, NJ 05026
        3  Dr. Jared Ortega  517 Rodriguez Divide Suite 570\nWest Melinda, ...


Installation
============================================
::

    pip install tblfaker


Dependencies
============================================
- Python 3.5+
- `Python package dependencies (automatically installed) <https://github.com/thombashi/tblfaker/network/dependencies>`__
