import os

from jinja2 import Environment, FileSystemLoader, select_autoescape

import yaml
import click

class Apperator:
    def __init__(self, crd):
        self.crd = crd

    @property
    def labels(self):
        return {
            'apperator.simone.sh/app-name': self.crd['metadata']['name'],
        }
    @property
    def annotations(self):
        return {
            'apperator.simone.sh/app-name': self.crd['metadata']['name'],
        }

    @property
    def env(self):
        return Environment(
            loader=FileSystemLoader(
                os.path.join(os.path.dirname(__file__), 'templates')
            ),
        )

    def template(self):
        template = self.env.get_template('apperator.jinja')
        return template.render(
            spec=self.crd['spec'],
            annotations=self.annotations,
            labels=self.labels,
            metadata=self.crd['metadata'],
        )


class YamlInput:
    def __init__(self, stream):
        self.stream = stream
        self._yamls = False

    @property
    def manifests(self):
        if not self._yamls:
            self._yamls = [
                x for x in yaml.load_all(self.stream.read())
                if 'apiVersion' in x
                and x['apiVersion'].startswith('apperator.simone.sh')
            ]
        return self._yamls



def f_to_manifests(f):
    yaml_in = click.get_text_stream('stdin') if f == '-' else open(f, 'r')
    yaml_out = YamlInput(yaml_in)

    t = ''
    for crd in yaml_out.manifests:
        App = Apperator(crd)
        t += App.template().replace('\n\n', '\n').replace('\n\n', '\n') + '\n'

    dumped = yaml.dump_all([x for x in yaml.load_all(t)])
    return dumped.encode()
