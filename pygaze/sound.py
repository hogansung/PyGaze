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
from pygaze._sound.basesound import BaseSound


class Sound(BaseSound):

	"""Sound playback"""

	def __init__(self, disptype=settings.DISPTYPE, **args):

		"""
		Initializes the Sound object.
		
		TODO: docstring.
		"""

		if disptype in ('pygame', 'psychopy', 'opensesame'):
			from pygaze._sound.pygamesound import PyGameSound as Sound
		else:
			raise Exception('Unexpected disptype : %s' % disptype)
		self.__class__ = Sound
		self.__class__.__init__(self, **args)
		copy_docstr(BaseSound, Sound)
