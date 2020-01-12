import inspect
from typing import AbstractSet, Sequence

from faker import Factory


_non_provider_methods = (
    "__init__",
    "_Generator__format_token",
    "add_provider",
    "format",
    "get_formatter",
    "get_providers",
    "parse",
    "provider",
    "seed",
    "set_formatter",
)


def _get_valid_providers() -> Sequence[str]:
    return tuple(
        method[0]
        for method in inspect.getmembers(Factory.create(), inspect.ismethod)
        if method[0] not in _non_provider_methods
    )


_valid_providers = frozenset(_get_valid_providers())
_valid_locals = frozenset(
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


def get_providers() -> AbstractSet:
    return _valid_providers


def get_locals() -> AbstractSet:
    return _valid_locals
