# -*- coding: utf-8 -*-
# Copyright 2013 Christoph Reiter
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation

import os
import sys

from tests import TestCase, DATA_DIR, skipUnless

from quodlibet.util.path import normalize_path
from quodlibet.util import is_wine
from quodlibet import windows


@skipUnless(os.name == "nt", "Wrong platform")
class TWindows(TestCase):

    def test_dir_funcs(self):
        d = windows.get_personal_dir()
        self.assertTrue(d is None or isinstance(d, unicode))

        d = windows.get_appdate_dir()
        self.assertTrue(d is None or isinstance(d, unicode))

        d = windows.get_desktop_dir()
        self.assertTrue(d is None or isinstance(d, unicode))

        d = windows.get_music_dir()
        self.assertTrue(d is None or isinstance(d, unicode))

        d = windows.get_profile_dir()
        self.assertTrue(d is None or isinstance(d, unicode))

        d = windows.get_links_dir()
        self.assertTrue(d is None or isinstance(d, unicode))

    def test_get_link_target(self):
        path = os.path.join(DATA_DIR, "test.lnk")
        d = windows.get_link_target(path)
        self.assertTrue(isinstance(d, unicode))
        self.assertEqual(
            normalize_path(d), normalize_path(u"C:\Windows\explorer.exe"))

    def test_get_link_target_unicode(self):
        path = os.path.join(DATA_DIR, "test2.lnk")
        d = windows.get_link_target(path)
        self.assertTrue(isinstance(d, unicode))
        if is_wine():
            # wine doesn't support unicode paths here..
            self.assertEqual(os.path.basename(d), u"\xe1??.txt")
        else:
            self.assertEqual(os.path.basename(d), u"\xe1\U00016826.txt")

    def test_get_link_target_non_exist(self):
        with self.assertRaises(WindowsError):
            windows.get_link_target(u"nopenope.lnk")

    def test_environ(self):
        env = windows.WindowsEnviron()
        len_ = len(env)
        env[u"FOO"] = u"bar"
        self.assertEqual(len(env), len_ + 1)
        self.assertEqual(env.get(u"FOO"), u"bar")
        self.assertTrue("FOO" in repr(env))
        self.assertEqual(len(list(env)), len(env))
        del env[u"FOO"]

    def test_environ_ascii(self):
        env = windows.WindowsEnviron()
        env["FOO"] = u"bar"
        env["FOO"]
        del env["FOO"]


@skipUnless(os.name == "nt", "Wrong platform")
class Tget_win32_unicode_argv(TestCase):

    def test_main(self):
        newargv = windows.get_win32_unicode_argv()
        self.assertEqual(len(sys.argv), len(newargv))
        if newargv:
            self.assertTrue(isinstance(newargv[0], unicode))
