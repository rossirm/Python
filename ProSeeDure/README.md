# Instalation and configuration Manual

## Requred Hardware
*   Raspberry Pi (2 or 3)
*   HDMI cable
*   Monitor or TV with HDMI input

## Requred Software
*   Raspbian OS
*   ProSEEdure program
*   evince - PDF reader - `sudo apt-get install evince`
*   xbindkeys - `sudo apt-get install xbindkeys && xbindkeys-config`
*   remove mouse cursor - `sudo apt-get install unclutter`

### Set a program to always run in full screen

`sudo leafpad /home/pi/.config/openbox/lxde*.xml`

```xml
<application name="lxterminal">
    <focus>yes</focus> # Ensure that keyboard directly working on the application
    <fullscreen>yes</fullscreen> # Set to always run on full screen
</application>
```

### Hide mouse cursor
```bash
unclutter -display :0 -noevents -grab
```

### Xbindkeys-config
`*` key 
```bash
lxterminal --command 'sh /home/pi/milara/autorun.sh'
```
`/` key
```bash
sudo killall evince lxterminal
```