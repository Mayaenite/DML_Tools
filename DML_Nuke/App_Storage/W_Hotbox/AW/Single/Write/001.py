#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: File Output Display
#
#----------------------------------------------------------------------------------------------------------

for n in nuke.selectedNodes():
    n.selectOnly()
    text_node = nuke.createNode("Text",'message "[value [value input.name].file]" xjustify left yjustify baseline size 20 box "0 0 0 0" translate "0 50" Transform 1')