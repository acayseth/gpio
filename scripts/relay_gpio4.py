import RPi.GPIO as GPIO
import time, os

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

GpioPortRelay = 4

GPIO.setup(GpioPortRelay, GPIO.OUT)

GPIO.output(GpioPortRelay, 0)
os.system("clear")

try:
  print("[try:]")
  GPIO.output(GpioPortRelay, 1)
  print("\t -> Relay[ON], Sleep[3s]")
  time.sleep(3)
  print("\t -> Relay[OFF]")
  GPIO.output(GpioPortRelay, 0)
  print("cleanup")
  GPIO.cleanup()
except:
  print("[except:]")
  GPIO.cleanup()