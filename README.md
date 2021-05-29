# Improvement

A loop is used to slow down the speed control of the steering gear by the official function, so that the steering gear can rotate at the speed you want╰(￣ω￣ｏ)

## How to use

jUST RUN TEH ./examples/ Example.py

You need to pay attention to the following sentences:

```python
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
```
**Parameter interpretation**
    
    - channel: Channel number on board PCA9685  
    - start: The angle of the steering gear at the moment
    - end: The angle at the end of the steering gear rotation you want
    - interval: Sampling frequency from start to end of angular travel
    - freq_sleep: Sampling interval
    - end_sleep: Operating interval of steering gear in different channels
    
    LIKE THIS:
    Forward_loop_ControlServo(0, 90, 5) ---> 0,5,10...90
    Reversed_loop_ControlServo(90, 0, 5) --->90,85,80...0


**For more details, see example.py**


# Here is the official installation method

## Adafruit Python PCA9685
Python code to use the PCA9685 PWM servo/LED controller with a Raspberry Pi or BeagleBone black.

## Installation

To install the library from source (recommended) run the following commands on a Raspberry Pi or other Debian-based OS system:

    sudo apt-get install git build-essential python-dev
    cd ~
    git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
    cd Adafruit_Python_PCA9685
    sudo python setup.py install

Alternatively you can install from pip with:

    sudo pip install adafruit-pca9685

Note that the pip install method **won't** install the example code.
