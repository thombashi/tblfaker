from typing import Optional, Sequence

from faker import Factory
from tabledata import TableData

from ._common import get_providers


class TableFaker:
    def __init__(self, locale: Optional[str] = None, seed: Optional[int] = None) -> None:
        self.__fake = Factory.create(locale)

        if seed is not None:
            self.__fake.seed(seed)

    def generate(
        self,
        providers: Sequence[str],
        rows: int,
        table_name: Optional[str] = None,
        headers: Optional[Sequence[str]] = None,
        max_workers: Optional[int] = None,
    ) -> TableData:
        """Generate fake data as tabular data.

        Args:
            providers:
                List of provider names to generate a tabular data.
            rows:
                Number of rows in the tabular data.
            headers:
                List of header names.
            max_workers:
                Maximum number of workers to generate table data.
                In default, the same as the total number of CPUs.

        Returns:
            tabledata.TableData: Generated fake tabular data.
        """

        self.__validate_provider(providers)

        if rows < 0:
            raise ValueError("invalid rows")

        return TableData(
            table_name,
            headers if headers else providers,
            [
                [getattr(self.__fake, faker_name)() for faker_name in providers]
                for _row in range(rows)
            ],
            max_workers=max_workers,
        )

    @staticmethod
    def __validate_provider(providers: Sequence[str]) -> None:
        if not providers:
            raise ValueError("require provider(s)")

        diff = set(providers) - get_providers()

        if diff:
            raise ValueError("unknown providers found: {}".format(diff))
