import cgi
import functools
import importlib.util
import inspect
import os
import sys
from http import HTTPStatus


def import_file(fn):
    module_name = os.path.splitext(os.path.basename(fn))[0]
    module_spec = importlib.util.spec_from_file_location(module_name, fn)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    inspect.stack()[1][0].f_globals[module_name] = module


def add_header(key, value):
    print(f'{key.title()}: {value}')


def add_headers(headers):
    for k, v in dict(headers).items():
        add_header(k, v)


def start_response(status=200, mimetype='text/plain', headers=None):
    if not isinstance(status, HTTPStatus):
        try:
            status = HTTPStatus(int(status))
            print(f'Status: {status.value} {status.phrase}')
        except Exception:
            print(f'Status: {status}')
    print(f'Content-Type: {mimetype}')
    if headers:
        add_headers(headers)


def finish_headers():
    print()


def error(msg='', status=400):
    start_response(status)
    finish_headers()
    print(msg)
    sys.exit()


def ensure_method(allowed=['GET']):
    if os.environ['REQUEST_METHOD'] not in allowed:
        error(status=405)


def allowed_methods(allowed=['GET']):
    def helper(f):
        @functools.wraps(f)
        def wrapper(*a, **kw):
            ensure_method(allowed)
            return f(*a, **kw)
        return wrapper
    return helper


def get_query_args():
    fs = cgi.FieldStorage()
    return dict(zip(fs, map(fs.getvalue, fs)))
