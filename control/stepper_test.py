from Stepper import Stepper
import time

stepper_time_interval_seconds = 0.1
# Pin order:             [ENB|MS1|MS2|MS3|RST|SLP|STP|DIR]
stepper_A = Stepper([  4,  7,  6,  5,  0,  0,  3,  2],
    "Stepper A", stepper_time_interval_seconds)
stepper_B = Stepper([ 10, 11, 12, 13,  0,  0,  9,  8],
    "Stepper B", stepper_time_interval_seconds)
stepper_C = Stepper([ 16, 17, 18, 19,  0,  0, 15, 14],
    "Stepper C", stepper_time_interval_seconds)
stepper_D = Stepper([ 22, 23, 24, 25,  0,  0, 21, 20],
    "Stepper D", stepper_time_interval_seconds)
print "Created 4 steppers"

stepper_A.go()
# stepper_B.go()
# stepper_C.go()
# stepper_D.go()

time.sleep(2)  # Sleep 5 seconds

stepper_A.move_to_position(32.0)
print ("Moved goal to 32")


time.sleep(4)  # Sleep 5 seconds

stepper_B.move_to_position(-26.0)
print ("Moved goal to 32")