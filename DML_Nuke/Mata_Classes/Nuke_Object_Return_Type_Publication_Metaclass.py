
from . import Data_Storage


########################################################################
class Nuke_Object_Return_Type_Publication(type):
	""""""
	#----------------------------------------------------------------------
	def __new__(mcs, name, bases, dct):
		"""This Is Run Before The Class Is Created. Not An Instance Of The Class But The Creation Of The Class Itself"""
		## Generate The New Class Type And Return It
		NODE_TYPE_RELATION   = dct.pop('NODE_TYPE_RELATION',None)
		RETURN_OVERIDE_CHECK_TYPE = dct.pop('RETURN_OVERIDE_CHECK_TYPE',None)
		
		res = type.__new__(mcs, name, bases, dct)
		Data_Storage.Object_Return_Type_Relations[name]=res
		return res

	#----------------------------------------------------------------------
	def __init__(cls, name, bases, dct):
		return super(Nuke_Object_Return_Type_Publication, cls).__init__(name, bases, dct)

	##----------------------------------------------------------------------
	#def __call__(cls,*args,**kwargs):
		#"""This Is Run Before An Instance Of The Class Created And Allows For The Inspection And Manipulation Of The Values Used To Create The New Instance"""
		## Create The New Class Instance
		#nodeName = kwargs.get("name", kwargs.get("n",None))
		#if nodeName == None and len(args) == 1:
			#nodeName = args[0]
		
		#if nodeName == None or not cmds.objExists(nodeName):
			#if hasattr(cls,"createNode"):
				#nodeName = cls.createNode(*args,**kwargs)
			#elif cls.CREATE_COMMAND != None:
				#nodeName = cls.CREATE_COMMAND(*args,**kwargs)
			#else:
				#if nodeName == None:
					#raise ValueError("no name was given and this class {} has no create function".format(cls.__name__))
				#else:
					#raise LookupError("The input object {} does not exist and this class {} has no create function".format(nodeName, cls.__name__))
			#res = type.__call__(cls,nodeName)
		#else:
			#res = type.__call__(cls,nodeName,**kwargs)
		#return res
