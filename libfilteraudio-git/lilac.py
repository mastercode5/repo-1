#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
    run_cmd(['git', 'clean', '-dfx'])
    aur_pre_build()

if __name__ == '__main__':
  single_main()
