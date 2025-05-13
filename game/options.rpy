﻿

define config.name = _("A Feiticeira")


define gui.show_name = True


define config.version = "1.0"


define gui.about = _p("""
""")


define build.name = "AFeiticeira"


define config.has_sound = True
define config.has_music = True
define config.has_voice = True


define config.main_menu_music = "audio/menuSound.mp3"


define config.enter_transition = dissolve
define config.exit_transition = dissolve


define config.intra_transition = dissolve


define config.after_load_transition = None


define config.end_game_transition = None



define config.window = "auto"


define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


default preferences.text_cps = 0

default preferences.afm_time = 15



define config.save_directory = "AFeiticeira-1738764970"



define config.window_icon = "gui/window_icon.png"



init python:



    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)



    build.documentation('*.html')
    build.documentation('*.txt')

