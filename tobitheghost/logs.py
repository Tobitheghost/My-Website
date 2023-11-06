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
    logging.warn(visitor_ip)
    logging.warn(user_agent)
    logging.warn(visitor_url)
