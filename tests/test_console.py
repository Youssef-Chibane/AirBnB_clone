#!/usr/bin/python3

""" test for console"""

import sys
import models
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec


class test_console(unittest.TestCase):
    def setUp(self):
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        sys.stdout = self.backup

    def create(self):
        return HBNBCommand()

    def test_quit(self):
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_show(self):
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(x))

        def test_show_class_name(self):
            console = self.create()
            console.onecmd("create User")
            user_id = self.capt_out.getvalue()
            sys.stdout = self.backup
            self.capt_out.close()
            self.capt_out = StringIO()
            sys.stdout = self.capt_out
            console.onecmd("show")
            x = (self.capt_out.getvalue())
            sys.stdout = self.backup
            self.assertEqual("** class name missing **\n", x)

        def test_show_class_name2(self):
            console = self.create()
            console.onecmd("create User")
            user_id = self.capt_out.getvalue()
            sys.stdout = self.backup
            self.capt_out.close()
            self.capt_out = StringIO()
            sys.stdout = self.capt_out
            console.onecmd("show User")
            x = (self.capt_out.getvalue())
            sys.stdout = self.backup
            self.assertEqual("** instance id missing **\n", x)

        def test_show_no_instance_found(self):
            console = self.create()
            console.onecmd("create User")
            user_id = self.capt_out.getvalue()
            sys.stdout = self.backup
            self.capt_out.close()
            self.capt_out = StringIO()
            sys.stdout = self.capt_out
            console.onecmd("show User " + "124356876")
            x = (self.capt_out.getvalue())
            sys.stdout = self.backup
            self.assertEqual("** no instance found **\n", x)

        def test_create(self):
            console = self.create()
            console.onecmd("create User")
            self.assertTrue(isinstance(self.capt_out.getvalue(), str))

        def test_class_name(self):
            console = self.create()
            console.onecmd("create")
            x = (self.capt_out.getvalue())
            self.assertEqual("** class name missing **\n", x)

        def test_class_name_doest_exist(self):
            console = self.create()
            console.onecmd("create Binita")
            x = (self.capt_out.getvalue())
            self.assertEqual("** class doesn't exist **\n", x)


if __name__ == '__main__':
    unittest.main()
