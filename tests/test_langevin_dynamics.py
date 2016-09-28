#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_langevin_dynamics
----------------------------------

Tests for `langevin_dynamics` module.
"""
from unittest import TestCase

import os
import sys

import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from langevin_dynamics import langevin_dynamics
from langevin_dynamics import cli
from langevin_dynamics import *


class TestLangevin_dynamics(TestCase):
    

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'langevin_dynamics.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
    
    def test_input_file_exists(self):
            #p=os.getcwd()
            #print (p)
            flag = os.path.exists(langevin_dynamics.Pot_file)
            self.assertTrue(flag)
    
    def test_wrap(self):
        self.assertEqual(0.2, round(langevin_dynamics.wrap(2.2,1),1))
    '''def test_match_table(self):
        self.assertEqual(0.000664,langevin_dynamics.tab_match(0.314))'''
    
    def test_euler_non_langevin_sanity(self):
        dU,force=langevin_dynamics.euler(1.4,0,0)
        self.assertEqual(dU,force)
        
    def test_euler_langevin_sanity(self):
        dU,force=langevin_dynamics.euler(1.4,0,1)
        self.assertNotEqual(dU,force)

        
        

class Test_Input(unittest.TestCase):
        
    def setUp(self):
            pass
    
    def test_euler_input(self):
        self.assertRaises(TypeError,langevin_dynamics.euler,[1.4,0,1.1])
     
            


if __name__ == '__main__':
    sys.exit(unittest.main())
