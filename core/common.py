import yaml
import CONFIGS

def read_yaml(file_path):
    documents=None
    with open(file_path) as file:
        documents = yaml.full_load(file)

    return documents

def read_template(template_type, template_name, params):
    _search_path = os.path.join(CONFIGS.INPUT_FOLDER,'templates','{}'.format(template_type))
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
