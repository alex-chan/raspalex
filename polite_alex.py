#!/usr/bin/python
# -*- coding: utf8 -*-
# filename: PoliteAlex
# author: alexchen
# date: 2/9/2016
# All copyright reserved to xsunset
# ---------------------------------
from __future__ import absolute_import, division, print_function, \
    with_statement

import time
import subprocess
from facepp import API, File
import pygame


API_KEY = '2d0df4c56a364d82eed3d1a238950ffb'
API_SECRET = 'QovGDvkrsfOjY_ncbvT7ItprS6Af7gZZ'
api = API(API_KEY, API_SECRET)



class PoliteAlex(object):
    last_path = None
    def __init__(self):
        pygame.mixer.init()


    def capture_still_image(self):
        # return "imgs/test1.jpg"
        t = time.strftime("%Y%m%d_%H%M%S")
        path = "imgs/%s" % t
        popen = subprocess.Popen(['raspstill','-w','200','-h','200','-o',path])
        ret = popen.communicate()
        return path

    def is_screen_changed(self, new_path, old_path):
        return True

    def is_somebody_in_picture(self, path):
        return True

    def recognize_with_facepp(self, path):

        # rst = api.recognition.identify(group_name = 'test', url = TARGET_IMAGE)
        rst = api.recognition.identify(group_name = 'piface', img = File(path))
        print('recognition result', rst)
        print('=' * 60)
        if len(rst['face']) > 0 and len(rst['face'][0]['candidate']) > 0:
            print('The person with highest confidence:', \
                rst['face'][0]['candidate'][0]['person_name'])
        return rst

    def is_master_in_picture(self, regn):
        if len(rst['face']) > 0:
            if len(rst['face'][0]['candidate']) > 0:
                return rst['face'][0]['candidate'][0]['person_name'] == 'Sunset'

        return False

    def is_only_one_stranger_in_picture(self, regn):
        return False

    def is_master_with_stranger(self, regn):
        return False

    def welcom_master_with_stranger(self):
        pass

    def welcome_master(self):
        pygame.mixer.music.load("res/welcomeback_master.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

    def yield_at_stranger(self):
        pass

    def run_forever(self):
        while True:
            path = self.capture_still_image()
            changed = self.is_screen_changed(path, self.last_path)
            if not changed:
                # Sleep
                continue
            sb = self.is_somebody_in_picture(path)
            if not sb:
                # Sleep
                continue

            ret = self.recognize_with_facepp(path)
            if self.is_master_with_stranger(ret):
                self.welcom_master_with_stranger()
            elif self.is_master_in_picture(ret):
                self.welcome_master()
            elif self.is_only_one_stranger_in_picture(ret):
                self.yield_at_stranger()


if __name__ == "__main__":
    alex = PoliteAlex()
    alex.run_forever()
