#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: mafei
@About: loop Servo contral
@Tiem: 10/4/2021

"""

from __future__ import division

import time
import numpy as np
import RPi.GPIO as GPIO
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()


class FloatRange:
    '''
    About:Array reverse iteration
    '''

    def __init__(self, start, end, step=5):
        self.start = start
        self.end = end
        self.step = step

    # Forward iteration
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    # reverse iteration
    def __reversed__(self):
        t = self.start
        while t >= self.end:
            yield t
            t -= self.step


'''

Example for Forward_loop_ControlServo && Reversed_loop_ControlServo:
    Forward_loop_ControlServo(0, 90, 5) ---> 0,5,10...90
    Reversed_loop_ControlServo(90, 0, 5) --->90,85,80...0

'''


def Forward_loop_ControlServo(channel, start, end, interval, freq_sleep, end_sleep):
    for _ in FloatRange(start, end, interval):
        set_servo_angle(channel, _)
        time.sleep(freq_sleep)
    time.sleep(end_sleep)


def Reversed_loop_ControlServo(channel, start, end, interval, freq_sleep, end_sleep):
    for _ in reversed(FloatRange(start, end, interval)):
        set_servo_angle(channel, _)
        time.sleep(freq_sleep)
    time.sleep(end_sleep)

# Helper function to make setting a servo pulse width simpler.


def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)


def set_servo_angle(channel, angle):
    angle = 4096*((angle*11)+500)/20000
    pwm.set_pwm(channel, 0, int(angle))


# Set frequency to 50hz, good for servos.
pwm.set_pwm_freq(50)

print('Moving servo on channel 0, press Ctrl-C to quit...')

################--*--Manipulator attitude--*--#################

if __name__ == '__main__':
	'''
        Run these statements in turn, and you will feel different
    '''

    # Official function
    set_servo_angle(0,90)
	
	time.sleep(0.5)
	
	# Improved function
	Forward_loop_ControlServo(0,90,180,3,0.02,0.3)
