import subprocess

import pytest

from hedgehog import __version__


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.parametrize(
    "name",
    [
        "hhdiff",
    ],
)
def test_installed_scripts(name):
    """Test that expected scripts can execute and report correct version."""
    proc = subprocess.run(
        [name, "--version"], check=True, capture_output=True, text=True
    )
    assert name in proc.stdout
    assert __version__ in proc.stdout
