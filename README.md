# Files
## Client
* `config.cfg` - client config. Located in `.xonotic/data`
* `hud_luma_xord_v4.cfg` - my HUD config. Located in `.xonotic/data/data`. You can choise it in game settings (Settings -> Game -> HUD -> Enter HUD editor)
## Server
* `server.cfg` - server config which contains all custom settings, [see docs](https://gitlab.com/xonotic/xonotic/-/wikis/basic-server-configuration)
* `xon.conf` - NGINX server config with location, which need for downloading content from server. See [Official docs](https://gitlab.com/xonotic/xonotic/-/wikis/Automatic-map-downloads)
*  `xon-server.service` - systemd service for running server. For convenience to save server logs and autostart on boot. [More about systemd](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
# Server description
Game compiled from source, see [manual](https://gitlab.com/xonotic/xonotic/-/wikis/Repository_Access). Server starts with `-userdir` parameter, which points to custom directory with configs instead of `~/.xonotic`.

Server runs with some custom maps. You can downlodad this from [Google Drive](https://drive.google.com/drive/folders/1Mv4wLkbLW66Y0KtOmgMsdrFpvb_iVS-4?usp=sharing), or find it in unofficial map repos.