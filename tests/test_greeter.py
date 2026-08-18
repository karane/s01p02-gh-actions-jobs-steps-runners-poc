import pytest

from src.greeter import greet, build_id


def test_greet_returns_message_with_name():
    assert "Hello, Karane!" in greet("Karane")


def test_greet_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("")


def test_build_id_combines_job_and_run_number():
    assert build_id("test", "42") == "test-42"
