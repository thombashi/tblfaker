# encoding: utf-8

from __future__ import absolute_import, unicode_literals

from faker import Factory
from tabledata import TableData

from ._common import get_providers


class TableFaker(object):
    def __init__(self, locale=None, seed=None):
        self.__fake = Factory.create(locale)

        if seed:
            self.__fake.seed(seed)

    def generate(self, provider_list, rows, table_name=None, headers=None):
        """Generate fake data as tabular data.

        Args:
            provider_list (list):
                List of provider names to generate a tabular data.
            rows (int):
                Number of rows in the tabular data.
            headers (list):
                List of header names.

        Returns:
            tabledata.TableData: Generated fake tabular data.
        """

        self.__validate_provider(provider_list)

        if rows < 0:
            raise ValueError("invalid rows")

        return TableData(
            table_name,
            headers if headers else provider_list,
            [
                [getattr(self.__fake, faker_name)() for faker_name in provider_list]
                for _row in range(rows)
            ],
        )

    @staticmethod
    def __validate_provider(provider_list):
        if not provider_list:
            raise ValueError("require provider(s)")

        diff = set(provider_list) - get_providers()

        if diff:
            raise ValueError("unknown providers found: {}".format(diff))
