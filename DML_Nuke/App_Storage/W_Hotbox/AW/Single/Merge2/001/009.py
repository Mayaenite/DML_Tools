#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: divide
#
#----------------------------------------------------------------------------------------------------------

for nod in nuke.selectedNodes():
    knb = nod.knob("operation")
    knb.setValue("divide")