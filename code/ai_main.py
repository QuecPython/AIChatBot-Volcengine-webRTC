import sim
from usr.jobs import scheduler
from usr import pypubsub as pub

import dataCall
import utime as time
import TiktokRTC
import atcmd
import _thread

from machine import Pin

PA = Pin.GPIO39

from machine import ExtInt
from queue import Queue

def key1(args):
    global rtc_queue
    rtc_queue.put(1)

def key2(args):
    global rtc_queue
    rtc_queue.put(2)

def enable_pid2():
    resp = bytearray(50)
    atcmd.sendSync('AT+qicsgp=2,1,3gnet,"","",0\r\n',resp,'',20)
    atcmd.sendSync('at+cgact=1,2\r\n',resp,'',20)

def ai_callback(args):
    global GPIO39
    event = args[0]
    msg = args[1]
    if event == 1:
        print('TIKTOK_RTC_EVENT_START')
        GPIO39.write(1)
    elif event == 2:
        print('TIKTOK_RTC_EVENT_STOP')
        GPIO39.write(0)
    elif event == 3:
        print('TIKTOK_RTC_EVENT_TTS_TEXT {}'.format(msg))
        #call.stopAudioService()
    elif event == 4:
        print('TIKTOK_RTC_EVENT_ASR_TEXT {}'.format(msg))
        #call.stopAudioService()
    elif event == 5:
        print('TIKTOK_RTC_EVENT_ERROR {}'.format(msg))
    else:
        print('TIKTOK_RTC_EVENT UNKNOWN {}'.format(event))

def ai_task():
    global rtc_queue
    global extint1
    global extint2
    global tiktok
    while True:
        lte = dataCall.getInfo(1, 0)
        if lte[2][0] == 1:
            print('lte network normal')
            #pub.publish('update_status', status="ready")
            break
        print('wait lte network normal...')
        pub.publish('update_status', status="connect network")
        time.sleep(3)

    extint1.enable()
    extint2.enable()
    print('ai task running')

    while True:
        data = rtc_queue.get()
        print('rtc_queue key event {}'.format(data))
        if data == 1:
            print('start rtc')
            tiktok.active(True)
        elif data == 2:
            print('stop rtc')
            tiktok.active(False)

if __name__ == "__main__":

    enable_pid2()
    
    # 使能sim卡热插拔
    sim.setSimDet(1, 1)

    # 设置按键中断
    extint1 = ExtInt(ExtInt.GPIO45, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, key1, filter_time=50)
    extint2 = ExtInt(ExtInt.GPIO46, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, key2, filter_time=50)

    rtc_queue = Queue()
    
    # 启动后台任务调度器
    scheduler.start()
    
    print('window show over')

    tiktok = TiktokRTC(300000, ai_callback)
    GPIO39 = Pin(PA, Pin.OUT, Pin.PULL_DISABLE, 0)
    tiktok.config(volume=11)
    print('volume: {}'.format(tiktok.config('volume')))

    _thread.start_new_thread(ai_task, ())


    

