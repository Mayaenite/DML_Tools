import nuke
from ..Abstract_Nodes import Knob

################################################################################
class Tab_Knob(Knob):
	"""Wrapper class for a nuke Node type"""
	KNOB_TYPE_RELATION        = "Tab_Knob"