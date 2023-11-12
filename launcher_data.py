import configparser
import os
import dataclasses
from typing import List


@dataclasses.dataclass
class LauncherData:
    ini_dir: str
    engine_source_dir: str
    engine_build_dir: str
    last_project_dir: str
    load_last_project_on_start: bool
    validate_project_on_load: bool
    validate_project_on_save: bool
    known_project_dirs: List[str]

    def needs_engine_install(self):
        return self.engine_source_dir == "" or self.engine_source_dir == "Null"

    def needs_engine_build(self):
        return self.engine_build_dir == "" or self.engine_build_dir == "Null"

    def has_projects(self):
        return len(self.known_project_dirs) > 0


launcher_ini_file_path = 'launcher.ini'


def validate_ini():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    ini_file_path = os.path.join(current_directory, 'launcher.ini')

    return os.path.exists(ini_file_path)


class CaseSensitiveConfigParser(configparser.ConfigParser):
    def optionxform(self, option: str) -> str:
        return option


def create_default_ini():
    config = CaseSensitiveConfigParser()
    config['EngineData'] = {
        'SourcePath': 'Null',
        'BuildPath': 'Null'
    }

    config['Projects'] = {
        'ProjectPaths': 'Null',
        'LastProjectPath': 'Null'
    }
    config['Settings'] = {
        'LoadLastProjectOnStart': 'False',
        'ValidateProjectOnLoad': 'True',
        'ValidateProjectOnSave': 'True'
    }

    with open(launcher_ini_file_path, 'w') as configfile:
        config.write(configfile)


def load_launcher_data():
    if not validate_ini():
        create_default_ini()

    launcherData = LauncherData("", "", "", "", False, False, False, [])

    config = CaseSensitiveConfigParser()
    config.read(launcher_ini_file_path)

    launcherData.engine_source_dir = config.get('EngineData', 'SourcePath')
    launcherData.engine_build_dir = config.get('EngineData', 'BuildPath')

    projectPaths = config.get('Projects', 'ProjectPaths')
    launcherData.known_project_dirs = projectPaths.split(';') if projectPaths != 'Null' else []

    launcherData.last_project_dir = config.get('Projects', 'LastProjectPath')

    launcherData.load_last_project_on_start = config.getboolean('Settings', 'LoadLastProjectOnStart')
    launcherData.validate_project_on_load = config.getboolean('Settings', 'ValidateProjectOnLoad')
    launcherData.validate_project_on_save = config.getboolean('Settings', 'ValidateProjectOnSave')

    return launcherData
