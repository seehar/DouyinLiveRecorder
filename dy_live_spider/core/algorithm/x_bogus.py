from urllib.parse import urlparse

import execjs

from settings import settings


def generate_request_params(url: str, user_agent: str):
    query = urlparse(url).query
    xbogus = execjs.compile(open(settings.ALGORITHM_DIR / "X-Bogus.js").read()).call(
        "sign", query, user_agent
    )
    return {"param": url + "&X-Bogus=" + xbogus, "X-Bogus": xbogus}
