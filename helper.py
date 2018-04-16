#!/usr/bin/env python
# -*- coding: utf-8 -*-  @Author  : bjsasc
__author__ = 'fengshaomin'

import json
import time
import os


def alert(msg):
    return '<script type = "text/javascript"> alert("{}");location.href=""</script>'.format(msg)
