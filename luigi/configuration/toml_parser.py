# -*- coding: utf-8 -*-
#
# Copyright 2018 Cindicator Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import os.path
import toml

from .base_parser import BaseParser


class LuigiTomlParser(BaseParser):
    NO_DEFAULT = object()
    data = dict()
    _config_paths = [
        '/etc/luigi/luigi.toml',
        'luigi.toml',
        'luigi/base.toml',
        'luigi/local.toml',
    ]

    def read(self, config_paths):
        self.data = dict()
        for path in config_paths:
            if os.path.isfile(path):
                self.data.update(toml.load(path))
        return self.data

    def get(self, section, option, default=NO_DEFAULT, **kwargs):
        try:
            return self.data[section][option]
        except KeyError:
            if default is self.NO_DEFAULT:
                raise
            return default

    def getboolean(self, section, option, default=NO_DEFAULT):
        return self.get(section, option, default)

    def getint(self, section, option, default=NO_DEFAULT):
        return self.get(section, option, default)

    def getfloat(self, section, option, default=NO_DEFAULT):
        return self.get(section, option, default)

    def getintdict(self, section):
        return self.data.get(section, {})

    def set(self, section, option, value=None):
        if section not in self.data:
            self.data[section] = {}
        self.data[section][option] = value
