#=========================================================================
# RegIncr_extra_test
#=========================================================================

import random

from pymtl      import *
from pclib.test import run_test_vector_sim
from RegIncr    import RegIncr

#-------------------------------------------------------------------------
# test_small
#-------------------------------------------------------------------------

def test_small( dump_vcd ):
  run_test_vector_sim( RegIncr(), [
    ('in_   out*'),
    [ 0x00, '?'  ],
    [ 0x03, 0x01 ],
    [ 0x06, 0x04 ],
    [ 0x00, 0x07 ],
  ], dump_vcd )

#-------------------------------------------------------------------------
# test_large
#-------------------------------------------------------------------------

def test_large( dump_vcd ):
  run_test_vector_sim( RegIncr(), [
    ('in_   out*'),
    [ 0xa0, '?'  ],
    [ 0xb3, 0xa1 ],
    [ 0xc6, 0xb4 ],
    [ 0x00, 0xc7 ],
  ], dump_vcd )

# ''' TUTORIAL TASK ''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This test script is incomplete. As part of the tutorial you will add
# another test case to test for overflow. Later you will add a test case
# for random testing.
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#-------------------------------------------------------------------------
# test_overflow
#-------------------------------------------------------------------------

def test_overflow( dump_vcd ):
  run_test_vector_sim( RegIncr(), [
   ('in_ out*'),
  [ 0x00, '?' ],
  [ 0xfe, 0x01 ],
  [ 0xff, 0xff ],
  [ 0x00, 0x00 ],
  ], dump_vcd )

