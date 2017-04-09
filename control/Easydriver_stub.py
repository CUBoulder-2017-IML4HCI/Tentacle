#!/usr/bin/python
# -*- coding: utf-8 -*-
# From: https://github.com/davef21370/EasyDriver

"""Stub for testing on non-Pi machines, e.g. on MacBook"""

import time, sys

class Easydriver(object):
    def __init__(self,pin_step=0,delay=0.1,pin_direction=0,pin_ms1=0,pin_ms2=0,pin_ms3=0,pin_sleep=0,pin_enable=0,pin_reset=0,name="Stepper"):
        self.pin_step = pin_step
        self.delay = delay / 2
        self.pin_direction = pin_direction
        self.pin_microstep_1 = pin_ms1
        self.pin_microstep_2 = pin_ms2
        self.pin_microstep_3 = pin_ms3
        self.pin_sleep = pin_sleep
        self.pin_enable = pin_enable
        self.pin_reset = pin_reset
        self.name = name

    def step(self):
        pass

    def set_direction(self,direction):
        pass

    def set_full_step(self):
        pass
        pass
        pass

    def set_half_step(self):
        pass
        pass
        pass

    def set_quarter_step(self):
        pass
        pass
        pass

    def set_eighth_step(self):
        pass
        pass
        pass

    def set_sixteenth_step(self):
        pass
        pass
        pass

    def sleep(self):
        pass

    def wake(self):
        pass

    def disable(self):
        pass

    def enable(self):
        pass

    def reset(self):
        pass
        time.sleep(1)
        pass

    def set_delay(self, delay):
        self.delay = delay / 2

    def finish(self):
        pass