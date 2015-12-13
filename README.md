Timelapse
=========
A Python script to take a series of pictures.

Timelapse is a simple script that takes a series of pictures with a 
USB-connected, gphoto2-compatible camera.

Command-line Arguments
----------------------
    -d, --delay: Time, in seconds, to wait between gphoto2 calls. Note that this
        is not the time between photographs! Rather it is the time paused
        between the end of a gphoto2 call, and the beginning of the next gphoto2
        call. So the time between photographs will be greater than this delay.
        By how much depends on the attached camera.
        
    -e --end: End date and time of the photo session. The argument is a string
        formatted in one of the following ways:
            <year>-<month>-<day> <hour>:<minute>:<second>
            <year>-<month>-<day> <hour>:<minute>
            <month>-<day> <hour>:<minute>:<second>
            <month>-<day> <hour>:<minute>
            <hour>:<minute>:<second>
            <hour>:<minute>
            
    Where:
        <year> is a four-digit year.
        <month> is a two-digit month, with a leading zero if necessary.
        <day> is a two-digit day, with a leading zero if necessary.
        <hour> is a 24-hour clock, two-digit hour, with a leading zero if 
            necessary.
        <minute> is a two-digit minute, with a leading zero if necessary.
        <second> is a two-digit second, with a leading zero if necessary.

Requirements
------------
    * Python 3.x. (Tested with Python 3.5)
    * Gphoto2
    
Copyright and License
---------------------

Copyright 2015, Andrew Lin.
All rights reserved.

This software is released under the BSD 3-clause license. See LICENSE.txt or
https://opensource.org/licenses/BSD-3-Clause for more information
