import sys

# Don't check for secrets during tests to appease CI.
if sys.argv[1] == "test":
    try:
        from .secrets import secrets
    except ImportError:
        import app.settings.my_secrets.test as secrets  # noqa
