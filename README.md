# Files
## Client
* `config.cfg` - client config. Located in `.xonotic/data`
* `hud_luma_xord_v4.cfg` - my HUD config. Located in `.xonotic/data/data`. You can choise it in game settings (Settings -> Game -> HUD -> Enter HUD editor)
## Server
* `server.cfg` - server config which contains all custom settings, [see docs](https://gitlab.com/xonotic/xonotic/-/wikis/basic-server-configuration)
* `xon.conf` - NGINX server config with location, which need for downloading content from server. See [Official docs](https://gitlab.com/xonotic/xonotic/-/wikis/Automatic-map-downloads)
*  `xon-server.service` - systemd service for running server. For convenience to save server logs and autostart on boot. [More about systemd](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
* `rcon_bot directory` - see Chat bot below
# Server description
## Game
Game compiled from source, see [manual](https://gitlab.com/xonotic/xonotic/-/wikis/Repository_Access). Server starts with `-userdir` parameter, which points to custom directory with configs instead of `~/.xonotic`.

Server runs with some custom maps. You can downlodad this from [Google Drive](https://drive.google.com/drive/folders/1Mv4wLkbLW66Y0KtOmgMsdrFpvb_iVS-4?usp=sharing), or find it in unofficial map repos.
## Chat bot
In the rcon_bot directory there is a script written on python3 which sends text from file to game chat. This text contains some tips that may be useful for beginners. Script reads ini config at start where specified host, port, password to server, file with tips (one per line) and interval to send in seconds. Simply config

```
[DEFAULT]
host=localhost
port=2600
password=passwd
text_file=/path/to/tipsntricks.txt
message_interval=300
```

To specify config file use `-c` option. Script uses ONLY DEFAULT section.

IMPORTANT: script loads xrcon module. This module provides posibility to connect to xonotic server. Follow [link](https://pypi.org/project/xrcon/) to see more.

Script also runs with systemd. Option `ExecStartPre=sleep 30` prevents it to run before the xon server gets configured and available. May be I will write handling for this exception. May be =)