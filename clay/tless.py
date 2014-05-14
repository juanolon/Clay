import subprocess
import os
from jinja2 import nodes
from jinja2.ext import Extension

LESS_EXTENSION = '.less'

class LessExtension(Extension):
    tags = set(['less'])

    def __init__(self, environment):
        super(LessExtension, self).__init__(environment)

    def compile_less(self, file, caller):
        less_body = caller()

        if file is None or os.path.splitext( file )[1] != LESS_EXTENSION:
            print "File " + file + " not sopported"
            return ""

        if not os.path.isfile( "source" + file ):
            print "No File " + "source" + file + " found"
            return ""

        return self.parse_less(file)

    def parse_less(self, file):
        target_file = os.path.splitext( file )[0] + ".css"
        lessc = subprocess.Popen(['lessc', "-x", "source" + file, "source" + target_file], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

        # TODO: EOF Character is not crossplatform, 125 works for linux need to find what works for windows (probably 26)
        out, err = lessc.communicate(input="")

        # TODO: Handle returned error code from compiler
        if err:
            print out
            return ""
        return "<link href=\""+target_file+"\" rel=\"stylesheet\">"


    def parse(self, parser):
        lineno = parser.stream.next().lineno
        args = [parser.parse_expression()]

        less_body = parser.parse_statements(['name:endless'], drop_needle=True)

        return nodes.CallBlock(self.call_method('compile_less', args), [], [], less_body).set_lineno(lineno)

