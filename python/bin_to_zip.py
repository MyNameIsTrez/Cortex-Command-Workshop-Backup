import os, shutil

from pathlib import Path


game_mods_path = Path("I:/Users/welfj/Downloads/steamcmd/steamapps/workshop/content/209670")

zip_output_directory = Path("./output_zips")


def main():
	for mod_bin_parent_dir_name in os.listdir(game_mods_path):
		mod_bin_parent_dir_path = game_mods_path / mod_bin_parent_dir_name

		# There's always a single .bin in mod_bin_parent_dir_name, but the name will be unknown
		for mod_bin_file_name in os.listdir(mod_bin_parent_dir_path):
			mod_bin_path = mod_bin_parent_dir_path / mod_bin_file_name
			mod_zip_path = (zip_output_directory / mod_bin_file_name).with_suffix(".zip")

			shutil.copyfile(mod_bin_path, mod_zip_path)


if __name__ == "__main__":
	main()
