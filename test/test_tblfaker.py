import pytest
from pytablewriter import dumps_tabledata
from tabledata import TableData

from tblfaker import TableFaker

from ._common import print_test_result


dump_opts = {"line_break_handling": "escape"}


class Test_TableFaker_generate:
    @pytest.mark.parametrize(
        ["providers", "rows", "table_name", "expected"],
        [
            [
                ("name", "address"),
                2,
                None,
                TableData(
                    None,
                    ("name", "address"),
                    [
                        ("Ryan Gallagher", "6317 Mary Light\nSmithview, HI 13900"),
                        ("Amanda Johnson", "3608 Samuel Mews Apt. 337\nHousebury, WA 13608"),
                    ],
                ),
            ],
            [
                ("name", "address"),
                2,
                "test",
                TableData(
                    "test",
                    ("name", "address"),
                    [
                        ("Ryan Gallagher", "6317 Mary Light\nSmithview, HI 13900"),
                        ("Amanda Johnson", "3608 Samuel Mews Apt. 337\nHousebury, WA 13608"),
                    ],
                ),
            ],
            [
                ("name", "address"),
                4,
                None,
                TableData(
                    None,
                    ("name", "address"),
                    [
                        ("Ryan Gallagher", "6317 Mary Light\nSmithview, HI 13900"),
                        ("Amanda Johnson", "3608 Samuel Mews Apt. 337\nHousebury, WA 13608"),
                        ("Willie Heath", "868 Santiago Grove\nNicolehaven, NJ 05026"),
                        (
                            "Dr. Jared Ortega",
                            "517 Rodriguez Divide Suite 570\nWest Melinda, NH 85325",
                        ),
                    ],
                ),
            ],
        ],
    )
    def test_normal(self, providers, rows, table_name, expected):
        faker = TableFaker(seed=1)
        out = faker.generate(providers, rows, table_name=table_name)
        out_table = dumps_tabledata(out, **dump_opts)
        expected_table = dumps_tabledata(expected, **dump_opts)

        print_test_result(expected=expected_table, actual=out_table)

        assert expected_table == out_table
        assert out == expected

    def test_normal_specify_header_list(self):
        faker = TableFaker(seed=1)
        providers = ("file_name", "file_path")
        out = faker.generate(providers, 1, table_name="with headers", headers=("input", "output"))
        expected = TableData(
            "with headers", ("input", "output"), [("shake.wav", "/prepare/last.jpeg")]
        )
        out_table = dumps_tabledata(out, **dump_opts)
        expected_table = dumps_tabledata(expected, **dump_opts)

        print_test_result(expected=expected_table, actual=out_table)

        assert expected_table == out_table
        assert out == expected

    def test_normal_locale(self):
        faker = TableFaker(locale="ja_JP", seed=1)
        out = faker.generate(("name", "address"), rows=2)
        expected = TableData(
            None,
            ("name", "address"),
            [("山岸 裕樹", "三重県荒川区明石町14丁目4番16号"), ("村山 拓真", "北海道荒川区白金台15丁目19番4号 コート所野806")],
        )
        out_table = dumps_tabledata(out, **dump_opts)
        expected_table = dumps_tabledata(expected, **dump_opts)

        print_test_result(expected=expected_table, actual=out_table)

        assert expected_table == out_table
        assert out == expected
        assert out != faker.generate(("name", "address"), rows=2)

    def test_normal_random(self):
        faker = TableFaker()
        providers = ("name", "address")
        rows = 16

        for _ in range(3):
            lhs = faker.generate(providers, rows)
            rhs = faker.generate(providers, rows)

            assert lhs.headers == rhs.headers
            assert lhs != rhs

    @pytest.mark.parametrize(
        ["providers", "rows", "expected"],
        [[["invalid provider"], 1, ValueError], [["name"], -1, ValueError]],
    )
    def test_exception(self, providers, rows, expected):
        faker = TableFaker()

        with pytest.raises(expected):
            faker.generate(providers, rows)
