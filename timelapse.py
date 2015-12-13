#! /usr/bin/env python3
"""
Copyright 2015, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import argparse
import datetime
import io
import shlex
import subprocess
import time


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--delay',
        type=float,
        required=True,
        help='Time to wait between pictures, in seconds.'
    )
    parser.add_argument(
        '-e', '--end',
        default=None,
        help='Date/time to end photo session.'
    )
    args = parser.parse_args()

    if args.end is not None:
        formats = [
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d %H:%M',
            '%m-%d %H:%M:%S',
            '%m-%d %H:%M',
            '%H:%M:%S',
            '%H:%M'
        ]
        try:
            args.end = determine_end_time(args.end, formats)

        except ValueError:
            with io.StringIO(
                'End time must be in one of the following formats:\n'
            ) as msg:
                for f in formats:
                    msg.write('   {}\n'.format(f))
                msg.writelines(
                    [
                        'Where:\n'
                        '   %Y is four-digit year\n'
                        '   %m is a zero-padded month [01..12]\n'
                        '   %d is a zero-padded day [01..31]\n'
                        '   %H is a zero-padded 24-hour clock hour [0..23]\n'
                        '   %M is a zero-padded minute [00..59]\n'
                        '   %S is a zero-padded second [00..59]\n'
                    ]
                )
                err = msg.getvalue()

            parser.error(err)

    else:
        # Danger! Susceptible to the Y3K bug!
        args.end = datetime.datetime(3000, 1, 1)

    return args


def determine_end_time(end, formats):
    # String to datetime.
    for fmt in formats:
        try:
            end_time = datetime.datetime.strptime(end, fmt)

        except ValueError:
            pass

        else:
            break

    else:
        raise ValueError('Bad end time format.')

    # Account for missing date in datetime.
    default_year = 1900
    default_month = 1
    default_day = 1
    today = datetime.datetime.now()

    if end_time.year == default_year:
        # Assume no date.
        new_year = today.year
        new_month = today.month if end_time.month == default_month else None
        new_day = today.day if end_time.day == default_day else None
        end_time = end_time.replace(year=new_year, month=new_month, day=new_day)

    return end_time


def take_photo():
    cmd = 'gphoto2 --capture-image'
    subprocess.check_call(shlex.split(cmd))


def timestamp():
    now = datetime.datetime.now()
    print('Currently {}'.format(now.strftime('%Y-%m-%d %H:%M:%S')))
    return now


def main():
    args = parse_command_line()

    print('Running until {}'.format(args.end.strftime('%Y-%m-%d %H:%M:%S')))
    now = timestamp()
    while now < args.end:
        take_photo()
        time.sleep(args.delay)
        now = timestamp()

if __name__ == '__main__':
    main()
