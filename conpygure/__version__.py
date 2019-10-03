version_info = (
    0,
    0,
    1,
    # "b2",  # release (b1, rc1, or "" for final or dev)
    # "dev",  # dev or nothing
)

__version__ = ".".join(map(str, version_info[:3])) + ".".join(version_info[3:])