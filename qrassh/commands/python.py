# Copyright (c) 2015 Michel Oosterhof <michel@oosterhof.net>
# All rights reserved.

"""
This module contains the python commnad
"""

from __future__ import division, absolute_import

import getopt

from twisted.python import log

from irassh.shell.honeypot import HoneyPotCommand

commands = {}

class command_python(HoneyPotCommand):
    """
    """
    def version(self):
        ver = 'Python 2.7.11+'
        self.write(ver + '\n')


    def help(self):
        output = (
            'usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...',
            'Options and arguments (and corresponding environment variables):',
            '-B     : don\'t write .py[co] files on import; also PYTHONDONTWRITEBYTECODE=x',
            '-c cmd : program passed in as string (terminates option list)',
            '-d     : debug output from parser; also PYTHONDEBUG=x',
            '-E     : ignore PYTHON* environment variables (such as PYTHONPATH)',
            '-h     : print this help message and exit (also --help)',
            '-i     : inspect interactively after running script; forces a prompt even',
            '         if stdin does not appear to be a terminal; also PYTHONINSPECT=x',
            '-m mod : run library module as a script (terminates option list)',
            '-O     : optimize generated bytecode slightly; also PYTHONOPTIMIZE=x',
            '-OO    : remove doc-strings in addition to the -O optimizations',
            '-R     : use a pseudo-random salt to make hash() values of various types be',
            '         unpredictable between separate invocations of the interpreter, as',
            '         a defense against denial-of-service attacks',
            '-Q arg : division options: -Qold (default), -Qwarn, -Qwarnall, -Qnew',
            '-s     : don\'t add user site directory to sys.path; also PYTHONNOUSERSITE',
            '-S     : don\'t imply \'import site\' on initialization',
            '-t     : issue warnings about inconsistent tab usage (-tt: issue errors)',
            '-u     : unbuffered binary stdout and stderr; also PYTHONUNBUFFERED=x',
            '         see man page for details on internal buffering relating to \'-u\'',
            '-v     : verbose (trace import statements); also PYTHONVERBOSE=x',
            '         can be supplied multiple times to increase verbosity',
            '-V     : print the Python version number and exit (also --version)',
            '-W arg : warning control; arg is action:message:category:module:lineno',
            '         also PYTHONWARNINGS=arg',
            '-x     : skip first line of source, allowing use of non-Unix forms of #!cmd',
            '-3     : warn about Python 3.x incompatibilities that 2to3 cannot trivially fix',
            'file   : program read from script file',
            '-      : program read from stdin (default; interactive mode if a tty)',
            'arg ...: arguments passed to program in sys.argv[1:]',
            '',
            'Other environment variables:',
            'PYTHONSTARTUP: file executed on interactive startup (no default)',
            'PYTHONPATH   : \':\'-separated list of directories prefixed to the',
            '               default module search path.  The result is sys.path.',
            'PYTHONHOME   : alternate <prefix> directory (or <prefix>:<exec_prefix>).',
            '               The default module search path uses <prefix>/pythonX.X.',
            'PYTHONCASEOK : ignore case in \'import\' statements (Windows).',
            'PYTHONIOENCODING: Encoding[:errors] used for stdin/stdout/stderr.',
            'PYTHONHASHSEED: if this variable is set to \'random\', the effect is the same',
            '   as specifying the -R option: a random value is used to seed the hashes of',
            '   str, bytes and datetime objects.  It can also be set to an integer',
            '   in the range [0,4294967295] to get hash values with a predictable seed.'
        )
        for l in output:
            self.write(l + '\n')


    def start(self):
        """
        """
        try:
            opts, args = getopt.gnu_getopt(self.args, 'BdEhiORsStuvVx3c:m:Q:W:', ['help', 'version'])
        except getopt.GetoptError as err:
            self.write("Unknown option: -" +  err.opt + "\n")
            self.write("usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ... \n")
            self.write("Try `python -h' for more information.\n")
            self.exit()
            return

        # Parse options
        for o, a in opts:
            if o in "-V":
                self.version()
                self.exit()
                return
            elif o in "--help":
                self.help()
                self.exit()
                return
            elif o in '-h':
                self.help()
                self.exit()
                return
            elif o in '--version':
                self.version()
                self.exit()
                return

        for value in args:
            sourcefile = self.fs.resolve_path(value, self.protocol.cwd)

            if self.fs.exists(sourcefile):
                self.exit()
            else:

                self.write("python: can't open file '%s': [Errno 2] No such file or directory\n" % (value))
                self.exit()

        if not len(self.args):
            pass


    def lineReceived(self, line):
        """
        """
        log.msg(eventid='irassh.command.input',
                realm='python',
                input=line,
                format='INPUT (%(realm)s): %(input)s')


    def handle_CTRL_D(self):
        """
        """
        self.exit()


commands['/usr/bin/python'] = command_python

# vim: set sw=4 et tw=0:
