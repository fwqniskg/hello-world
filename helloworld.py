#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import configparser
import logging

try:
    config = configparser.ConfigParser()
    config_dir = str(Path('config').joinpath('cfg.ini'))    
    config.read(config_dir)
    data_dir = config.get('DATA','DATA_DIR')
    data_file = config.get('DATA','DATA_FILE')    
except configparser.NoSectionError:
    print ('Section missing')
    exit()
except:
    print ('Problem with the config file, ¿exists?')
    exit()

print(Path(data_dir, data_file).read_text())