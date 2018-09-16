from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import asyncio

from .cmake import Protocol
 
def main ():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        fromfile_prefix_chars='@')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('-W', '--warn', action='append') # uninitialized,unused-vars
    parser.add_argument('-f', action='append')

    trace = parser.add_mutually_exclusive_group()
    trace.add_argument('--trace-expand', action='store_true')
    trace.add_argument('--trace-file', action='append')
    trace.add_argument('--trace', action='store_true')

    subparser = parser.add_subparsers(help='Subcommands')
    configure = subparser.add_parser('configure')
    configure.add_argument('--enable', nargs='*')
    configure.add_argument('--disable', nargs='*')
    configure.add_argument('--with')
    configure.add_argument('--preload', nargs='?')
    # TODO: support .cmake, .yml, .json, .toml, .ini files (code generation, if you will)
    configure.add_argument('--toolchain', nargs='?') 
    metadata = subparser.add_parser('metadata')
    server = subparser.add_parser('server') # cmake -E server --experimental --debug
    script = subparser.add_parser('script') # run cmake -P
    inputs = subparser.add_parser('inputs') # return cmake files included
    tests = subparser.add_parser('tests') # return ctestinfo XXX: Change to 'build-command test' and run ctest?
    cache = subparser.add_parser('cache') # get cache info (possibly set? cache info)
    build = subparser.add_parser('build') # build your project
    run = subparser.add_parser('run') # run cmake -E
  
    metadata.add_argument('--test', help='print ctest info')
    metadata.add_argument('--inputs', help='print cmake inputs')
    metadata.add_argument('--cache', help='print cmake cache contents')

    loop = asyncio.get_event_loop()
    try: _, output = loop.run_until_complete(Protocol(loop))
    except Exception as e: raise SystemExit(str(e))
    else: print(output)
    finally: loop.close()
