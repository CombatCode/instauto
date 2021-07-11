from instauto.api.structs import Method
import requests
try:
    from typing import Protocol, Dict
except:
    from typing_extensions import Protocol
    from typing_extensions import DefaultDict as Dict


class _request(Protocol):
    def __call__(self, endpoint: str, method: Method, query: dict = None, data: dict = None, headers: Dict[str, str]
    = None, default_headers: bool = None, signed: bool = None) -> requests.Response: ...
