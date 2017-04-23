# Instalation and configuration Manual

##Requred Hardware
*   Raspberry Pi
*   HDMI cable
*   Monitor or TV
##Requred Software
*   Raspbian OS
*   ProSEEdure program
*   evince - PDF reader - `sudo apt-get install evince`
*   xbindkeys - `sudo apt-get install xbindkeys && xbindkeys-config`
*   remove mouse cursor - `sudo apt-get install unclutter`

# Set a program to always run in full screen

``sudo leafpad /home/pi/.config/openbox/lxde*.xml``

``<application name="lxterminal">``
 `` <focus>yes</focus>  # ensure that keyboard directly working on the application``
 `` <fullscreen>yes</fullscreen>``
``</application>``
####
# Hide mouse cursor
``unclutter -display :0 -noevents -grab``

####

# Xbindkeys-config
```* -> lxterminal --command 'sh /home/pi/milara/autorun.sh'```
```/ -> sudo killall evince lxterminal```
