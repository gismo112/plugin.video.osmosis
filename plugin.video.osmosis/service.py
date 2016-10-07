#   Copyright (C) 2016 Jan Gina
#
#
# This file is part of KoStToLib
#
# osmosis is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# osmosis is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with osmosis.  If not, see <http://www.gnu.org/licenses/>.


# -*- coding: utf-8 -*-
import os, re, sys, time
import xbmc, xbmcgui, xbmcaddon, xbmcvfs
from traceback import print_exc
import unicodedata
#import pydevd
#pydevd.settrace(stdoutToServer=True, stderrToServer=True)
import default
import urllib
import collections

vidname = ""
global thelist
thelist = None

x = True
LOG = True
# Plugin Info
ADDON_ID = 'plugin.video.osmosis'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_ID = REAL_SETTINGS.getAddonInfo('id')
ADDON_NAME = REAL_SETTINGS.getAddonInfo('name').decode('utf-8')
ADDON_PATH = REAL_SETTINGS.getAddonInfo('path')
ADDON_SETTINGS = REAL_SETTINGS.getAddonInfo('profile')
ADDON_VERSION = REAL_SETTINGS.getAddonInfo('version')

# PC Settings Info
SETTINGS2_LOC = xbmc.translatePath(os.path.join(ADDON_SETTINGS,'settings2.xml'))
STRM_LOC = REAL_SETTINGS.getSetting('STRM_LOC')
Path_Type = REAL_SETTINGS.getSetting('Path_Type')
Clear_Strms = REAL_SETTINGS.getSetting('Clear_Strms') == 'true'
Automatic_Update = REAL_SETTINGS.getSetting('Automatic_Update')
Automatic_Update_Delay = REAL_SETTINGS.getSetting('Automatic_Update_Delay')
Automatic_Update_Run = REAL_SETTINGS.getSetting('Automatic_Update_Run')
    

    
if __name__ == "__main__":
    def readSettings2(purge=False):
        # try:
        if xbmcvfs.exists(SETTINGS2_LOC):
            fle = open(SETTINGS2_LOC, "r")
            thelist = fle.readlines()
            fle.close()
            return thelist
    
    thelist = readSettings2()
    
    def strm_update():

        for i in range(len(thelist)):
                type ,name, url = ((thelist[i]).strip().split('|', 2))
                xbmc.executebuiltin("Notification(" + "Getting updates for: " + name + " ,Updatig...."+", ,/msgIco.jpg)")
                time.sleep(2) # delays for 2 seconds just to make sure Hodor can read the message   
                default.fillPluginItemsUpdate(url, strm=True, strm_name=name, strm_type=type)
               
                                
        # except Exception,e:
            # log("readSettings2, Failed " + str(e))
        #setProperty('writeSettings2','false')
    strm_update()
    xbmc.executebuiltin("Notification(" + "Done: Your donation is wellcome. Go to: " + name + " ,Updatig...."+" ,,/msgIco.jpg)")

#
# ToDo make a scheduled updater for osmosis
#     monitor = xbmc.Monitor()
#     while x:
#         xbmc.executebuiltin('Notification(Getting updates for: The Flash,500,/script.hellow.world.png)')
#         strm_update()
#         xbmc.executebuiltin('Notification(Done:,500,/script.hellow.world.png)')
#         xbmc.log(" in schleife hello service ist online")
#         # Sleep/wait for abort for 10 seconds
#         if monitor.waitForAbort(5):
#             x = True  # Abort was requested while waiting. We should exit     
#         # Sleep/wait for abort for 10 seconds