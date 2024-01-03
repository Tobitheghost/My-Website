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
    evniron_REAL_n_Remote = f'REAL_IP from REMOTE_ADDR {request.environ.get("HTTP_X_REAL_IP",request.environ.get("REMOTE_ADDR"))}'
    headers_Host = f'HOST HEADERS {request.headers.get("HOST")}'
    headers_X_REAL_IP = f'X_REAL_IP HEADERS {request.headers.get("X_REAL_IP")}'
    headers_FORWARDED_FOR = f'FORWARDED_FOR HEADERS {request.headers.get("X_FORWARDED_FOR")}'
    header_get_all = f'All HEADERS {request.headers.get_all()}'
    logging.warn(visitor_ip)
    logging.warn(user_agent)
    logging.warn(visitor_url)
    logging.warn(evniron_REAL_IP)
    logging.warn(evniron_REAL_n_Remote)
    logging.warn(headers_Host)
    logging.warn(headers_X_REAL_IP)
    logging.warn(headers_FORWARDED_FOR)
    logging.warn(header_get_all)