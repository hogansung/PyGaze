# -*- coding: utf-8 -*-
#
# This file is part of PyGaze - the open-source toolbox for eye tracking
#
#	PyGaze is a Python module for easily creating gaze contingent experiments
#	or other software (as well as non-gaze contingent experiments/software)
#	Copyright (C) 2012-2013  Edwin S. Dalmaijer
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>

from pygaze.py3compat import *
from pygaze import settings
from pygaze._misc.misc import copy_docstr
from pygaze._mouse.basemouse import BaseMouse


class Mouse(BaseMouse):

	"""A mouse for collecting responses"""

	def __init__(self, disptype=settings.DISPTYPE, **args):

		"""
		Initializes the Mouse object.
		
		TODO: docstring.
		"""

		if disptype == 'pygame':
			from pygaze._mouse.pygamemouse import PyGameMouse as Mouse
		elif disptype == 'psychopy':
			from pygaze._mouse.psychopymouse import PsychoPyMouse as Mouse
		elif disptype == 'opensesame':
			from pygaze._mouse.osmouse import OSMouse as Mouse
		else:
			raise Exception('Unexpected disptype : %s' % disptype)
		self.__class__ = Mouse
		self.__class__.__init__(self, **args)
		copy_docstr(BaseMouse, Mouse)
