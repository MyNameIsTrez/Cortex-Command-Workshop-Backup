import json


from python import get_project_path
from python import get_mod_ids, bin_to_zip_copy, download_mods


def main():
	settings_path = get_project_path.get_project_path() / "settings.json"

	with open(settings_path) as f:
		settings = json.load(f)

		mod_ids = get_mod_ids.get_mod_ids(settings)
		download_mods.download_mods(mod_ids, settings)
		bin_to_zip_copy.bin_to_zip_copy(settings)


if __name__ == "__main__":
	main()
