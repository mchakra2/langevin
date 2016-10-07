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
        #pass
        self.p = langevin_dynamics.Langevin()

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
           
        self.assertRaises(IOError,self.p.parameters,'random_file_which_should_not_exist.txt')



    def test_potential_file_exists(self):
        self.assertRaises(IOError,self.p.parameters,'./tests/test_input.txt')
        #flag = os.path.exists(self.p.Pot_file)
        #self.assertTrue(flag)
    def test_wrap_positive_val(self):
        self.assertEqual(0.2, round(self.p.wrap(2.2,1),1))
        
    
    def test_force_non_langevin_sanity(self):
        dU,frc=self.p.force(1.4,0,0)
        self.assertEqual(dU,frc)
        
    def test_force_langevin_sanity(self):
        dU,frc=self.p.force(1.4,0,1)
        self.assertNotEqual(dU,frc)


    def test_euler_position(self):
        p,v=self.p.euler(2,1,4)
        pos=round(2+(self.p.dt*1),2)
        self.assertEqual(round(p,2),pos)
        #self.assertTrue( case1 and case2)
        
    def test_euler_vel(self):
        p,v=self.p.euler(2,1,4)
        vel=round(1+(self.p.dt*4/self.p.mass),2)
        self.assertEqual(round(v,2),vel)


    def test_output_file_exists(self):
        self.p.main()
        flag = os.path.exists(self.p.o_file)
        self.assertTrue(flag)

    def test_output_not_empty(self):
        self.p.main()
        flag = os.path.getsize(self.p.o_file)

        self.assertGreater(flag,0)
        
    def test_euler_input(self):
        self.assertRaises(TypeError,self.p.euler,[1.4,0,1.1])



        

class Test_Input(unittest.TestCase):
        
    def setUp(self):
            pass
        
    


class Test_Output(unittest.TestCase):
    def setUp(self):
        pass

 


            


if __name__ == '__main__':
    sys.exit(unittest.main())
