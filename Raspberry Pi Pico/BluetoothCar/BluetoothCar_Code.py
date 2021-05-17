# Libraries
from machine import Pin, PWM, UART
from time import sleep
# Objects
ledTest = Pin(25, Pin.OUT)
bt = UART(1, 9600)
    # Motor A
motor_aa = PWM(Pin(14))
motor_ab = PWM(Pin(15))
motor_aa.freq(50)
motor_ab.freq(50)
    # Motor B
motor_ba = PWM(Pin(17))
motor_bb = PWM(Pin(16))
motor_ba.freq(50)
motor_bb.freq(50)

# Saludo inicial
for i in range(3):
    ledTest.on()
    sleep(0.3)
    ledTest.off()
    sleep(0.3)

# Function
def forWard():  # Hacia delante
    motor_aa.duty_u16(34512)
    motor_ab.duty_u16(0)
    motor_ba.duty_u16(30512)
    motor_bb.duty_u16(0)

def backWard():  # Reversa
    motor_aa.duty_u16(0)
    motor_ab.duty_u16(34512)
    motor_ba.duty_u16(0)
    motor_bb.duty_u16(30512)

def leftWard():
    motor_aa.duty_u16(30512)
    motor_ab.duty_u16(0)
    motor_ba.duty_u16(0)
    motor_bb.duty_u16(20000)

def rightWard():
    motor_aa.duty_u16(0)
    motor_ab.duty_u16(20000)
    motor_ba.duty_u16(30512)
    motor_bb.duty_u16(0)
    

def stop():  # Detenerse
    motor_aa.duty_u16(0)
    motor_ab.duty_u16(0)
    motor_ba.duty_u16(0)
    motor_bb.duty_u16(0)

# Main loop
while True:
    dato = bt.read(1)
    
    if 'w' in dato:
        forWard()
    elif 's' in dato:
        backWard()
    elif 'a' in dato:
        leftWard()
    elif 'd' in dato:
        rightWard()
    elif 'x' in dato:
        stop()

