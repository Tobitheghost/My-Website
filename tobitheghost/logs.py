import logging
from flask import request

def req_log():
    logging.basicConfig(
        filename="tobitheghost/utils/site.log",
        filemode="a",
        format="(%(asctime)s) %(funcName)s [On Line %(lineno)d] %(module)s)---->\t%(message)s",
        level=logging.DEBUG,
    )
    visitor_ip = f'Visitor IP {request.remote_addr}'
    user_agent = f'User Agent {request.user_agent}'
    visitor_url = f'Request {request.url}'
    evniron_REAL_IP = f'REAL_IP {request.environ.get("HTTP_X_REAL_IP")}'
    evniron_REAL_n_Remote = f'REAL_IP {request.environ.get("HTTP_X_REAL_IP",request.environ.get("REMOTE_ADDR"))}'
    logging.warn(visitor_ip)
    logging.warn(user_agent)
    logging.warn(visitor_url)
    logging.warn(evniron_REAL_IP)
    logging.warn(evniron_REAL_n_Remote)