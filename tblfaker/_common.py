import inspect
import re
from typing import AbstractSet, Final, Sequence

from faker import Factory


_non_provider_regexp: Final = re.compile("^(add|del|get|set)_[a-z_]+")
_non_provider_methods: Final = (
    "__delattr__",
    "__dir__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__le__",
    "__lt__",
    "__ne__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__str__",
    "__subclasshook__",
    "_Generator__format_token",
    "format",
    "parse",
    "provider",
    "seed",
)


def _get_valid_providers() -> Sequence[str]:
    return tuple(
        method[0]
        for method in inspect.getmembers(Factory.create(), inspect.ismethod)
        if _non_provider_regexp.search(method[0]) is None and method[0] not in _non_provider_methods
    )


_valid_providers: Final = frozenset(_get_valid_providers())
_valid_locals: Final = frozenset(
    [
        "ar_EG",
        "ar_PS",
        "ar_SA",
        "bs_BA",
        "bg_BG",
        "cs_CZ",
        "de_DE",
        "dk_DK",
        "el_GR",
        "en_AU",
        "en_CA",
        "en_GB",
        "en_NZ",
        "en_US",
        "es_ES",
        "es_MX",
        "et_EE",
        "fa_IR",
        "fi_FI",
        "fr_FR",
        "hi_IN",
        "hr_HR",
        "hu_HU",
        "it_IT",
        "ja_JP",
        "ko_KR",
        "lt_LT",
        "lv_LV",
        "ne_NP",
        "nl_NL",
        "no_NO",
        "pl_PL",
        "pt_BR",
        "pt_PT",
        "ro_RO",
        "ru_RU",
        "sl_SI",
        "sv_SE",
        "tr_TR",
        "uk_UA",
        "zh_CN",
        "zh_TW",
        "ka_GE",
    ]
)


def get_providers() -> AbstractSet[str]:
    return _valid_providers


def get_locals() -> AbstractSet[str]:
    return _valid_locals
