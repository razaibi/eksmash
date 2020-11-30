import os
import jinja2
from jinja2 import Environment, FileSystemLoader, Template
import yaml
import config
import errno
import requests
import subprocess
from core.session_manager import Session

session = Session()

def read_docs(params):
    print('{}'.format(params))

def read_template(template_type, template_name, params):
    _search_path = os.path.join('templates','{}'.format(template_type))
    template_loader = jinja2.FileSystemLoader(searchpath=_search_path)
    template_env = jinja2.Environment(loader=template_loader)
    TEMPLATE_FILE = "{}.j2".format(template_name)
    template = template_env.get_template(TEMPLATE_FILE)
    outputText = template.render(params)
    return outputText

def read_template_raw(template_type, template_name):
    _search_path = os.path.join('templates','{}'.format(template_type))
    template_loader = jinja2.FileSystemLoader(searchpath=_search_path)
    template_env = jinja2.Environment(loader=template_loader)
    TEMPLATE_FILE = "{}.j2".format(template_name)
    template = template_env.get_template(TEMPLATE_FILE)
    return template

def render_template(template, params):
    return template.render(params)

def get_injectors(injector_file):
    _injectors = None
    with open(os.path.join(config.INJECTORS_FOLDER,('.').join([injector_file,'yaml']))) as opened_file:
        _injectors = yaml.load(opened_file, Loader=yaml.FullLoader)['injectors']
    return _injectors


def write_to_file(filename, content):
    _file_path = os.path.join('output','{}'.format(filename))
    if not os.path.exists(os.path.dirname(_file_path)):
        try:
            os.makedirs(os.path.dirname(_file_path))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(_file_path, "w+") as f:
        f.write(content)

def append_to_file(filename, content):
    _file_path = os.path.join('output','{}'.format(filename))
    if not os.path.exists(os.path.dirname(_file_path)):
        try:
            os.makedirs(os.path.dirname(_file_path))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(_file_path, "a") as f:
        f.write(content)

def create_directory(directory_name):
    _path = os.path.join('output','{}'.format(directory_name))
    if not os.path.exists(_path):
        try:
            os.makedirs(_path)
        except OSError as exc: # Guard against race condition
            print(exc)
            if exc.errno != errno.EEXIST:
                raise

def call_rest_endpoint(request_data):
    if not bool(request_data['url_params']):
        _rendered_url = render_url(request_data['url'], **request_data['url_params'])
    if request_data['call_type'].lower() == 'post':
        
        req_object = requests.post(
            url=render_url(request_data['url'], **request_data['url_params']),
            headers=request_data['headers'],
            data=request_data['body'],
            params=request_data['query_params']
        )
    if request_data['call_type'].lower() == 'get':
        req_object = requests.get(
            url=render_url(request_data['url'], **request_data['url_params']),
            headers=request_data['headers'],
            data=request_data['body'],
            params=request_data['query_params']
        )
    return req_object

def render_url(url, **kwargs):
    raw_template = Template(url)
    return raw_template.render(kwargs)

def set_bearer_token(request_data, access_token):
    _auth = request_data['headers']['Authorization']
    _raw_bearer_template = Template(_auth)
    request_data['headers']['Authorization'] = _raw_bearer_template.render(
        bearer_token=access_token
    )
    return request_data

def own_script(script_name):
    os.system("chmod +x {}".format(
        os.path.join('output', '{}.sh'.format(script_name))
    ))

def switch_dir(path):
    os.chdir(path)

def invoke_script(path):
    subprocess.call("{}.sh".format(path), shell=True)
    

