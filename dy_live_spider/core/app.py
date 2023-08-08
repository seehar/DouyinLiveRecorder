# coding=utf-8
"""
:author: Lyzen
:date: 2023.04.03
:brief: app主文件
"""

import os
import signal
import sys
import platform

from dy_live_spider.core import version, config, record_manager, monitor
from dy_live_spider.util import logger

# from dy_live_spider.plugin import plugin

# 处理 ctrl+c
stop_all_threads = False


def init():
    # 处理 ctrl+c
    signal.signal(signal.SIGINT, sigint_handler)
    signal.signal(signal.SIGTERM, sigint_handler)

    # plugin.on_open()

    logger.info(f"software started. version: {version}.")
    logger.info(f"platform: {platform.platform()}")
    logger.info(f"python version: {platform.python_version()}")
    if sys.platform == "win32":
        os.system("chcp 65001")

    config.read_configs()
    record_manager.rooms = config.read_rooms()

    # plugin.on_loaded()
    monitor.init()


def sigint_handler(signum, frame):
    global stop_all_threads
    stop_all_threads = True
    logger.exception("catched SIGINT(Ctrl+C) signal")
    # plugin.on_close()
