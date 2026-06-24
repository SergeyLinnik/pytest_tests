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


def test_sending_mail_3(set_up_module: None) -> None:
    """
    Тест отправки письма #3.
    Использует фикстуру set_up_module (scope="module").
    Фикстура выполняется ОДИН РАЗ для всего модуля.
    """
    print("📧 Письмо #3 отправлено (fixture module)")


def test_sending_mail_4(set_up_module: None) -> None:
    """
    Тест отправки письма #4.
    Использует фикстуру set_up_module (scope="module").
    Фикстура НЕ выполняется повторно, т.к. уже выполнена для модуля.
    """
    print("📧 Письмо #4 отправлено (fixture module)")