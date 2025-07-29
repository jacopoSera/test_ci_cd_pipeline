"""
Versioning according Semantic Versioning https://semver.org/


"""
MAJOR:str = "0"
MINOR:str = "0"
PATCH:str = "0"

# BUILD come la gestiamo??
build_ver: list = [MAJOR, MINOR, PATCH]

__version__ = ".".join(build_ver)