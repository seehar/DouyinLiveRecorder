from dy_live_spider.core.dy_api import get_user_info
from dy_live_spider.util.cookie_utils import auto_get_cookie


def test_get_user_info():
    auto_get_cookie()
    sec_id = "MS4wLjABAAAACiepdzBTSAQmzAeD2Bqwb1irj3A5IYpT0jOYs7_eoaU"
    result = get_user_info(sec_id)
    print(result)
