# Cortex-Command-Workshop-Backup

This repository holds all of Cortex Command's Steam Workshop mods.

This backup was created because it has become impossible to download these mods through Steam, which is most likely the result of a Steam API update which the game won't ever be updated for.

These backed up mods are currently being updated to the [Cortex Command Community Project](https://cortex-command-community.github.io/) version of the game, and once that is done this repository will be deleted.

# Instructions
1. Subscribe to all mods you want to download of a game.
2. Open the `settings.json` file, found at the root of this repository.
	1. `game_id` its value is a number. The number can be found by going to your game's main Steam page and looking at its URL. Example: The game Cortex Command has a URL of `https://store.steampowered.com/app/209670/Cortex_Command/`, so the value of `game_id` should be`209670`.
	2. `vdf_path` its value is a string. `vdf` stands for `Valve Data File`, and the particular `.vdf` you need holds a list of the mods you've subscribed to for your chosen game. Example: My user's ID from my user's profile URL is `https://steamcommunity.com/profiles/76561198101327664/`. I throw that [into this website](https://steamid.io/lookup/) and it tells me my `steamID3` is `[U:1:141061936]`, or in other words `141061936`. I then fill out those `steamID3` and `game_id` values to get my `vdf_path`: `"I:/Program Files (x86)/Steam/userdata/141061936/ugc/209670_subscriptions.vdf"`.
	3. `steamcmd_exe_path` its value is a string. You'll need to download steamcmd [from the wiki](https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_SteamCMD) and unzip it somewhere. You don't need to put it in your regular Steam folder! Just make sure it isn't placed in a protected folder, so the Downloads folder is fine. Example: `"I:/Users/welfj/Downloads/steamcmd/steamcmd.exe"`.
	4. `game_mods_path` its value is a string. This tool downloads the mods into the steamcmd directory in the `game_id` subdirectory. Example: `"I:/Users/welfj/Downloads/steamcmd/steamapps/workshop/content/209670"`
3. `python -m pip install -r requirements.txt`
4. `python main.py`
5. Enter your Username, then your Password and then your Steam guard (two factor authentication) code. This is required because Steam doesn't allow anonymously downloading mods, and you'll also need to own the game on Steam. This may not be needed for all games on Steam, but this program assumes all games do. If you are uncomfortable with entering your sensitive data here I highly recommend reading the Python code; it isn't that much.
