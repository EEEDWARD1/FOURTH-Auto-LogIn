from configparser import ConfigParser

class ConfigManager:
    def __init__(self, file_path='config.ini'):
        self.config = ConfigParser()
        self.file_path = file_path
        self.config.read(self.file_path)
    
    def get_value(self, section, key):
        # Return the value of the key in the section
        try:
            return self.config[section][key]
        except KeyError:
            print(f"Error: '{section}' or '{key}' not found in the config file.")
            return None
    
    def set_value(self, section, key, value):
        #Set a value in the config file and save the changes.
        if section in self.config:
            if key in self.config[section]:
                self.config[section][key] = value
                with open(self.file_path, 'w') as configfile:
                    self.config.write(configfile)
        print(f"Updated {key} in {section}")
