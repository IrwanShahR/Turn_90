maqueenPlusV2.i2c_init()

def on_forever():
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        30)
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        28)
    basic.pause(5000)
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        10)
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        40)
    basic.pause(5000)
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        30)
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        28)
    basic.pause(5000)
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        40)
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        10)
    basic.pause(5000)
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        30)
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        28)
basic.forever(on_forever)
