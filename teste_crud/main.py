# -*- coding: utf-8 -*-

from src.server.instance import server
from src.controllers.movies import *
from werkzeug.utils import cached_property

server.run()