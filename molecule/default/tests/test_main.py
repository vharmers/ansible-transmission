import pytest


def test_installed(host):
    """
    Test if the proper package has been installed.
    """
    package = host.package("transmission-daemon")
    assert package.is_installed


def test_config(host):
    """
    Test if the settings file has the right permissions.
    """
    config = host.file("/etc/transmission-daemon/settings.json")
    assert config.user == "debian-transmission"
    assert config.group == "debian-transmission"
    assert config.mode == 0o600


def test_service(host):
    """
    Test if the service is in the proper state.
    """
    service = host.service("transmission-daemon")
    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize("dir_name", [
    "/var/lib/transmission-daemon/downloads",
    "/var/lib/transmission-daemon/downloads/incomplete",
    "/var/lib/transmission-daemon/watch"
])
def test_dirs_created(host, dir_name):
    """
    Test if the given directory has been created and has
    the right owner.
    """
    dir = host.file(dir_name)
    assert dir.is_directory
    assert dir.user == "debian-transmission"
    assert dir.group == "debian-transmission"


def test_rpc_auth(host):
    """
    Check if RPC authentication is configure correctly.
    """
    path = host.find_command("transmission-remote")
    host.run_expect([0], "{} --auth transmission:test --list".format(path))
