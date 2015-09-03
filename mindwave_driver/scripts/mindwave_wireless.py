#!/usr/bin/env python

import time

from mindwave_driver.wireless_headset import WirelessHeadset
from mindwave_driver.common import *

headset = WirelessHeadset('/dev/ttyUSB0','7B04', 115200)
#headset = WirelessHeadset(r'\\.\COM17','7B04') # windows r'\\.\COMx'
#headset.echo_raw()

while True:
    if headset.status == Status.STANDBY:
        print 'trying connecting'
        headset.connect()
    elif headset.status == Status.CONNECTED:
        print "quality signal: %s , attention %s , %s meditation " % (headset.signal, headset.attention, headset.meditation)
    else:
        print "status " , headset.status
    time.sleep(0.4)