from config_manager import ConfigManager

class MainMenu:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.username = self.config_manager.get_value('auth', 'username')
        self.password = self.config_manager.get_value('auth', 'password')
        self.schedule_time = self.config_manager.get_value('schedule', 'time')
        self.periodicity = self.config_manager.get_value('schedule', 'periodicity')

    def display_menu(self):
        print("\n Main Menu")
        print("1. Run Scraper")
        print("2. Update Config")
    
    def run_scraper(self):
        print("Running Scraper")
    
    def exit(self):
        print("Exiting")
        exit()

    def run(self):
        if self.username is "" or self.password is "":
            print("Error: Username or password not found in the config file.")
            print("Please update the config file before running the program.")
            self.exit()

        while True:
            self.display_menu()
            choice = input("Enter choice: ")

            if choice == '1':
                self.run_scraper()
            elif choice == '2':
                self.update_config()
            else:
                self.exit()
        


if __name__ == '__main__':
    main_menu = MainMenu()
    main_menu.run()  

