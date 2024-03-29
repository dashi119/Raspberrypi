import webiopi
import time
import pigpio

def getServoDutyForWebIOPi(val):
    val_min = 0.0
    val_max = 1.0
    servo_min =  35000
    servo_max = 100000

    duty = int((servo_max-servo_min)*(val-val_min)/(val_max-val_min) + servo_min)
    return duty

pi = pigpio.pi()
pi.set_mode(18, pigpio.OUTPUT)
pi.hardware_PWM(18, 50, getServoDutyForWebIOPi(0.5))

# デバッグ出力を有効に
webiopi.setDebug()

# GPIOライブラリの取得
GPIO = webiopi.GPIO

PWM1  = 25
PWM2  = 24
PWM3  = 23
PWM4  = 22

# WebIOPiの起動時に呼ばれる関数
def setup():
    webiopi.debug("Script with macros - Setup")
    # GPIOのセットアップ
    GPIO.setFunction(PWM1, GPIO.PWM)
    GPIO.setFunction(PWM2, GPIO.PWM)
    GPIO.setFunction(PWM3, GPIO.PWM)
    GPIO.setFunction(PWM4, GPIO.PWM)
    # 初期のデューティー比を0%に（静止状態）
    GPIO.pwmWrite(PWM1, 0)
    GPIO.pwmWrite(PWM2, 0)
    GPIO.pwmWrite(PWM3, 0)
    GPIO.pwmWrite(PWM4, 0)

# WebIOPiにより繰り返される関数
def loop():
    webiopi.sleep(5)

# WebIOPi終了時に呼ばれる関数
def destroy():
    webiopi.debug("Script with macros - Destroy")
    # GPIO関数のリセット（入力にセットすることで行う）
    GPIO.setFunction(PWM1, GPIO.IN)
    GPIO.setFunction(PWM2, GPIO.IN)
    GPIO.setFunction(PWM3, GPIO.IN)
    GPIO.setFunction(PWM4, GPIO.IN)
    pi.stop()

# 4つのPWMにデューティー比をまとめてセットするためのマクロ
# commandIDは、iOSのSafariでPOSTがキャッシュされることへの対策
@webiopi.macro
def pwm4Write(duty1, duty2, duty3, duty4, commandID):
    GPIO.pwmWrite(PWM1, float(duty1))
    GPIO.pwmWrite(PWM2, float(duty2))
    GPIO.pwmWrite(PWM3, float(duty3))
    GPIO.pwmWrite(PWM4, float(duty4))

@webiopi.macro
def setHwPWM(duty, commandID):
    pi.hardware_PWM(18, 50, getServoDutyForWebIOPi(float(duty)))
