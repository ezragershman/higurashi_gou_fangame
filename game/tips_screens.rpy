screen end_oni1():
    imagebutton:
        xalign 0.5
        yalign 0.25
        idle "UI/view_tips.png"
        action Show("oni1_tip"), Hide("end_oni1")
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "UI/save_load.png"
        action QuickSave(message=u'Save complete.', newest=True)
    imagebutton:
        xalign 0.5
        yalign 0.75
        idle "UI/continue.png"
        action Jump("oni1")

screen oni1_tip():
    imagebutton:
        idle "UI/black.png"
        action Show("end_oni1"), Hide("oni1_tip")