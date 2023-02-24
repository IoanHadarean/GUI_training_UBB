#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Created on 01/25/2022
    Author: Ioan-Dumitru Hadarean """
import argparse

parser = argparse.ArgumentParser(add_help=False, description="Windows to Linux path converter")
parser.add_argument('--source', type=str, metavar='', required=True, help="Source of yaml to convert")
parser.add_argument('--destination', type=str, metavar='', required=True, help="Destination of yaml after "
                                                                               "conversion")
parser.add_argument('-ud', '--use-dirs', action="store_true",
                    help="Use dirs for conversion")
parser.add_argument('-nud', '--not-use-dirs', action="store_false",
                    help="Use dirs for conversion")
parser.add_argument('-l', '--list', nargs='+', required=True, action='store', metavar='', help='Set flag')
parser.set_defaults(feature=True)
# args = parser.parse_args(['-s=C:\\Users\\hadarean', '-d=C:\\Users\\hadarean'])
parser.print_help()


child_parser = argparse.ArgumentParser(parents=[parser])
child_parser.add_argument('-carg', '--child_arg', type=int, metavar='', required=True, help="Child arg")
child_parser.set_defaults(feature=True)
child_args = child_parser.parse_args()


class WindowsPathToLinuxPathConverter:

    def __init__(self, source, destination, use_dirs, *args):
        self.source = source
        self.destination = destination
        self.use_dirs = use_dirs
        self.arg_as_list = args

    def run(self):
        print(self.source, self.destination, self.use_dirs)
        print(self.arg_as_list)


if __name__ == "__main__":
    windows_to_linux_path_converter = WindowsPathToLinuxPathConverter(child_args.source, child_args.destination,
                                                                      child_args.use_dirs, child_args.list)
    windows_to_linux_path_converter.run()
