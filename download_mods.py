import json, getpass, os


steamcmd_exe_path = "i:/Users/welfj/Downloads/steamcmd/steamcmd.exe"

# HAS to be an absolute path in order for +runscript to not look in the dir of steamcmd_exe_path!
download_script_path = "I:\Programming\Cortex-Command-Workshop-Backup\download_script.txt"

game_id = 209670


def main():
	with open("mod_ids.json") as f:
		mod_ids = json.load(f)

		username = input("Username: ")
		password = getpass.getpass("Password: ")
		two_factor = input("Steam guard (two factor authentication) code: ")

		write_download_script_file(mod_ids)

		download_mods(username, password, two_factor)


def write_download_script_file(mod_ids):
	with open(download_script_path, "w") as of:
		of.writelines(get_download_mods_string(mod_ids))
		of.write("\nquit")


def get_download_mods_string(mod_ids):
	download_mod_strings = []

	for mod_id in mod_ids:
		download_mod_strings.append(get_download_mod_string(mod_id))

	return "\n".join(download_mod_strings)


def get_download_mod_string(mod_id):
	return f"workshop_download_item {game_id} {mod_id}"


def download_mods(username, password, two_factor):
	os.system(f"{steamcmd_exe_path} +login {username} {password} {two_factor} +runscript {download_script_path}")


if __name__ == "__main__":
	main()
