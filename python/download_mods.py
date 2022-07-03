import getpass, os

from python import get_project_path


def download_mods(mod_ids, settings):
	username = input("Username: ")
	password = getpass.getpass("Password: ")
	two_factor = input("Steam guard (two factor authentication) code: ")

	# Has to be an absolute path in order for +runscript to not look in the dir of steamcmd_exe_path!
	download_script_path = get_project_path.get_project_path() / "python/generated/download_script.txt"

	write_download_script_file(download_script_path, mod_ids, settings)

	execute_download_mods(username, password, two_factor, download_script_path, settings)


def write_download_script_file(download_script_path, mod_ids, settings):
	with open(download_script_path, "w") as of:
		of.writelines(get_download_mods_string(mod_ids, settings))
		of.write("\nquit")


def get_download_mods_string(mod_ids, settings):
	download_mod_strings = []

	for mod_id in mod_ids:
		download_mod_strings.append(get_download_mod_string(mod_id, settings))

	return "\n".join(download_mod_strings)


def get_download_mod_string(mod_id, settings):
	return f"workshop_download_item {settings['game_id']} {mod_id}"


def execute_download_mods(username, password, two_factor, download_script_path, settings):
	os.system(f"{settings['steamcmd_exe_path']} +login {username} {password} {two_factor} +runscript {download_script_path}")
