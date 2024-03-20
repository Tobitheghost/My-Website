import logging
from flask import request

def req_log():
    logging.basicConfig(
        filename="tobitheghost/utils/site.log",
        filemode="a",
        format={{"forwarded_for": request.headers.get("X_FORWARDED_FOR")},{"real_ip": request.headers.get("X_REAL_IP")},{"host": request.headers.get("HOST")},
                {"request":request.url},{"user_agent": request.user_agent},{"proxy_ip":request.remote_addr},{"date-time":"%(asctime)s"},
                {"line":"%(lineno)d"},{"function":"%(funcName)s"},{"module":"%(module)s"},{"messages":"%(message)s"}},
        level=logging.DEBUG
    )