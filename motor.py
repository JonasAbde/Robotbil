# motor.py
from machine import Pin, PWM

# Definer pins for venstre motor (forbundet til IN1, IN2 på L298N)
left_in1 = Pin(16, Pin.OUT)
left_in2 = Pin(17, Pin.OUT)
left_ena = PWM(Pin(20))   # PWM til venstre motor (ENA)
left_ena.freq(1000)

# Definer pins for højre motor (forbundet til IN3, IN4 på L298N)
right_in1 = Pin(18, Pin.OUT)
right_in2 = Pin(19, Pin.OUT)
right_enb = PWM(Pin(21))  # PWM til højre motor (ENB)
right_enb.freq(1000)

def set_speed_left(speed):
    """
    Indstiller hastigheden for venstre motor.
    """
    speed = max(0, min(100, speed))
    duty = int(speed * 65535 / 100)
    left_ena.duty_u16(duty)

def set_speed_right(speed):
    """
    Indstiller hastigheden for højre motor.
    """
    speed = max(0, min(100, speed))
    duty = int(speed * 65535 / 100)
    right_enb.duty_u16(duty)

def move_forward(left_speed, right_speed):
    """
    Kører fremad med individuelle hastigheder for venstre og højre motor.
    """
    # Sæt retning til fremad
    left_in1.high()
    left_in2.low()
    right_in1.high()
    right_in2.low()
    # Sæt hastigheder
    set_speed_left(left_speed)
    set_speed_right(right_speed)

def move_backward(left_speed, right_speed):
    """
    Kører baglæns med individuelle hastigheder for venstre og højre motor.
    """
    # Sæt retning til baglæns
    left_in1.low()
    left_in2.high()
    right_in1.low()
    right_in2.high()
    # Sæt hastigheder
    set_speed_left(left_speed)
    set_speed_right(right_speed)

def stop():
    """
    Stopper begge motorer.
    """
    left_in1.low()
    left_in2.low()
    right_in1.low()
    right_in2.low()
    set_speed_left(0)
    set_speed_right(0)
