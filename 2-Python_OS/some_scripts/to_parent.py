#!/usr/bin/env python3

import os

def change_dir_to_parent():
  parent_dir = os.path.dirname(os.getcwd())
  os.chdir(parent_dir)