# -*- encoding=utf8 -*-
__author__ = "vliavitski"

from airtest.core.api import *
from airtest.core.api import connect_device

auto_setup(__file__)

# dev = connect_device('Android://localhost:5555/R58M800KQTX')
# install("/Users/vliavitski/Documents/belkagames/base.apk")
start_app("com.belkatechnologies.clockmaker")
# time.sleep(20)

def first_test():
    wait(Template(r"tpl1589958867780.png", record_pos=(0.034, 0.499), resolution=(1080, 2340)), 25)

    touch(Template(r"tpl1589958867780.png", record_pos=(0.034, 0.499), resolution=(1080, 2340)))
    wait(Template(r"tpl1589958923586.png", record_pos=(-0.001, 0.453), resolution=(1080, 2340)))
    touch(Template(r"tpl1589958940171.png", record_pos=(0.003, 0.656), resolution=(1080, 2340)))

    time.sleep(15)
    touch(Template(r"tpl1589962326132.png", record_pos=(0.003, 0.012), resolution=(1080, 2340)))
    touch(Template(r"tpl1589962705268.png", record_pos=(0.005, -0.042), resolution=(1080, 2340)))

    time.sleep(10)

    touch(Template(r"tpl1589960777327.png", record_pos=(0.442, 1.007), resolution=(1080, 2340)))
    wait(Template(r"tpl1589960625096.png", record_pos=(0.019, 0.245), resolution=(1080, 2340)))
    touch(Template(r"tpl1589960625096.png", record_pos=(0.019, 0.245), resolution=(1080, 2340)))
    wait(Template(r"tpl1589960635240.png", record_pos=(0.431, -0.718), resolution=(1080, 2340)))

    touch(Template(r"tpl1589960635240.png", record_pos=(0.431, -0.718), resolution=(1080, 2340)))
    sleep(3)
    assert_exists(Template(r"tpl1589961149222.png", record_pos=(0.359, 0.93), resolution=(1080, 2340)), "Please fill in the test point.")

first_test()

