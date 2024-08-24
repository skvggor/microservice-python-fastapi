from src.config import Settings

settings = dict(Settings())


def test_config():
    expected_keys = [
        'port',
        'app_name',
        'current_prefix'
    ]

    for key in expected_keys:
        value = settings.get(key)

        assert value and value != ""
