#!/usr/bin/python
# -*- coding: utf8 -*-
# filename: PoliteAlex
# author: alexchen
# date: 2/9/2016
# All copyright reserved to xsunset
# ---------------------------------
import time
import subprocess

from __future__ import absolute_import, division, print_function, \
    with_statement

class PoliteAlex(object):
    last_path = None

    def capture_still_image(self):
        t = time.strftime("%Y%m%d_%H%M%S")
        path = "imgs/%s" % t
        popen = subprocess.Popen(['raspstill','-o',path])
        ret = popen.communicate()
        return path

    def is_screen_changed(self):
        pass

    def is_somebody_in_picture(self):
        pass

    def recognize_with_facepp(self, path):

        rst = api.recognition.identify(group_name = 'test', url = TARGET_IMAGE)
        print('recognition result', rst)
        print '=' * 60
        print 'The person with highest confidence:', \
                rst['face'][0]['candidate'][0]['person_name']

    def is_master_in_picture(self):
        pass

    def is_only_one_stranger_in_picture(self):
        pass

    def is_master_with_stranger(self):
        pass

    def welcom_master_with_stranger(self):
        pass

    def welcome_master(self):
        pass

    def yield_at_stranger(self):
        pass

    def run_forever(self):
        while True:
            path = self.capture_still_image()
            changed = self.is_screen_changed(path, last_path)
            if not changed:
                # Sleep
                continue
            sb = self.is_somebody_in_picture(path)
            if not sb:
                # Sleep
                continue

            ret = self.recognize_with_facepp(path)
            if self.is_master_with_stranger():
                self.welcom_master_with_stranger()
            elif self.is_master_in_picture():
                self.welcome_master()
            elif self.is_only_one_stranger_in_picture():
                self.yield_at_stranger()


if __name__ == "__main__":
    alex = PoliteAlex()
    alex.run_forever()
