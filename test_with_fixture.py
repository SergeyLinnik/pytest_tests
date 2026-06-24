# -*- coding: utf-8 -*-
"""
Файл с тестами, использующими фикстуры из conftest.py.
"""

import pytest


def test_sending_mail_1(set_up: None) -> None:
    """
    Тест отправки письма #1.
    Использует фикстуру set_up (scope="function").
    Фикстура выполняется перед КАЖДЫМ тестом.
    """
    print("📧 Письмо #1 отправлено (fixture function)")


def test_sending_mail_2(set_up: None) -> None:
    """
    Тест отправки письма #2.
    Использует фикстуру set_up (scope="function").
    Фикстура выполняется перед КАЖДЫМ тестом.
    """
    print("📧 Письмо #2 отправлено (fixture function)")


def test_sending_mail_3(set_up: None, set_up_module: None) -> None:
    """
    Тест отправки письма #3.
    Использует ОБЕ фикстуры: set_up (function) И set_up_module (module).

    Порядок выполнения:
    1. Сначала выполняются фикстуры с scope="function"
    2. Затем фикстуры с scope="module" (если ещё не выполнялись)
    """
    print("📧 Письмо #3 отправлено (fixture function + module)")


def test_sending_mail_4(set_up: None, set_up_module: None) -> None:
    """
    Тест отправки письма #4.
    Использует ОБЕ фикстуры: set_up (function) И set_up_module (module).

    set_up_module НЕ выполняется повторно (уже выполнена для модуля),
    но set_up выполняется снова (для каждого теста).
    """
    print("📧 Письмо #4 отправлено (fixture function + module)")