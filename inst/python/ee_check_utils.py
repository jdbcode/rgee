#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Check Selenium drivers and download geckodriver for linux, mac and windows.

>>> ee_check_drivers_py(driverdir,display_in_browser=True)
>>> chromedriver_linux(directory,vr)
>>> chromedriver_win(directory,vr)
>>> chromedriver_mac(directory,vr)

These functions are using in R/ee_check.R
"""
from __future__ import print_function

import os
import zipfile
import tarfile
import urllib
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

def ee_check_drivers_py(driverdir, display_in_browser=True):
    """Check if selenium works in their system

    Args:
        driverdir (str): geckodriver path
        display_in_broswer (bool): If it is True, Chrome browser will display it.

    Returns:
        Bool : If it is True means that no existing execution errors

    Examples:
        >>> driverdir = '/home/aybarpc01/.config/earthengine/aybar1994/'
        >>> ee_check_drivers_py(driverdir, display_in_browser=True)
    """
    options = Options()
    options.add_argument('-headless')
    authorization_url = 'https://www.google.com/'
    if os.name == 'nt':
        path_driver = os.path.join(driverdir, 'chromedriver.exe')
        if display_in_browser:
            try:
                driver = Chrome(executable_path=path_driver)
            except:
                return False
        else:
            try:
                driver = Chrome(executable_path=path_driver,
                                chrome_options=options)
            except:
                return False
    else:
        path_driver = os.path.join(driverdir, 'chromedriver')
        if display_in_browser:
            try:
                driver = Chrome(executable_path=path_driver)
            except:
                return False
        else:
            try:
                driver = Chrome(executable_path=path_driver,
                                chrome_options=options)
            except:
                return False
    driver.get(authorization_url)
    driver.quit()
    return True

def download_chromedriver(directory,operating_system, version):
    """Download geckodriver driver for linux

    Args:
        directory (str): name where the downloaded file is saved.
        vr (float): geckodriver version

    Returns:
        None

    Examples:
        >>> operating_system = 'macos'
        >>> driverdir = '/home/aybarpc01/.config/earthengine/aybar1994/'
        >>> download_chromedriver(driverdir, operating_system, version='76.0.3809.126')
    """
    if operating_system == 'windows':
        drivername = 'chromedriver.exe'
        operating_system = 'win32'
    elif operating_system == 'linux':
        drivername = 'chromedriver'
        operating_system = 'linux64'
    elif operating_system == 'macos':
        drivername = 'chromedriver'
        operating_system = 'mac64'
    else:
        raise Exception('OS not sopported')
    file_to_download = "https://chromedriver.storage.googleapis.com/%s/chromedriver_%s.zip" % (version, operating_system)
    chromedriver_fullname = "%s/chromedriver.zip" % directory
    urllib.request.urlretrieve(file_to_download, chromedriver_fullname)
    if operating_system=='linux64':
        with zipfile.ZipFile(chromedriver_fullname) as file:
            file.extract(drivername, directory)
        os.chmod(directory+drivername, 0o775)
    else:
        with zipfile.ZipFile(chromedriver_fullname) as file:
            file.extract(drivername, directory)
    os.remove(chromedriver_fullname)
    return True