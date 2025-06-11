from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
import json
import shutil

class CookieManager:
    def __init__(self):
        self.profiles_dir = 'profiles'
        self.drivers = {}
        os.makedirs(self.profiles_dir, exist_ok=True)

    def add_profile(self, name, desc=""):
        if name:
            profile_dir = os.path.join(self.profiles_dir, name)
            # Проверяем существование профиля
            if os.path.exists(profile_dir):
                return False
            
            os.makedirs(profile_dir, exist_ok=True)
            # Сохраняем метаданные профиля
            with open(os.path.join(profile_dir, "profile.json"), "w") as f:
                json.dump({"name": name, "description": desc}, f)
            return True
        return False

    def remove_profile(self, profile_name):
        """Remove profile directory and close associated browser."""
        if not isinstance(profile_name, str):
            return False
            
        profile_dir = os.path.join(self.profiles_dir, profile_name)
        if os.path.exists(profile_dir):
            try:
                shutil.rmtree(profile_dir)
                return True
            except Exception:
                return False
        return False

    def load_profiles(self):
        profiles = []
        if os.path.exists(self.profiles_dir):
            for profile_name in os.listdir(self.profiles_dir):
                profile_path = os.path.join(self.profiles_dir, profile_name)
                if os.path.isdir(profile_path):
                    # Читаем метаданные из JSON
                    try:
                        with open(os.path.join(profile_path, "profile.json"), "r") as f:
                            data = json.load(f)
                            profiles.append((data["name"], data.get("description", "")))
                    except (FileNotFoundError, json.JSONDecodeError):
                        # Если файла нет или он поврежден, используем только имя
                        profiles.append((profile_name, ""))
        return profiles


    def open_browser(self, profile_name):
        """Open Edge browser with the specified profile."""
        try:
            # Check if browser is already open but not responding
            if profile_name in self.drivers:
                try:
                    # Try to get window handles to check if browser is still alive
                    self.drivers[profile_name].window_handles
                except:
                    # Browser is dead, remove it
                    del self.drivers[profile_name]

            # Open new browser if needed
            if profile_name not in self.drivers:
                options = Options()
                
                # Anti-detection settings
                options.add_argument('--disable-blink-features=AutomationControlled')
                options.add_experimental_option('useAutomationExtension', False)
                options.add_experimental_option('excludeSwitches', ['enable-automation'])
                
                # Profile settings
                profile_path = os.path.join(os.path.abspath(self.profiles_dir), profile_name)
                options.add_argument(f'--user-data-dir={profile_path}')
                
                # Additional settings
                options.add_argument('--disable-dev-shm-usage')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                
                service = Service(EdgeChromiumDriverManager().install())
                self.drivers[profile_name] = webdriver.Edge(service=service, options=options)
                return True

            return True
        except Exception as e:
            print(f"Error opening browser: {str(e)}")
            if profile_name in self.drivers:
                del self.drivers[profile_name]
            return False

    def close_browser(self, profile_name=None):
        """Close specific browser or all browsers."""
        if profile_name and profile_name in self.drivers:
            try:
                self.drivers[profile_name].quit()
            except:
                pass
            del self.drivers[profile_name]
        elif profile_name is None:
            for driver in list(self.drivers.values()):
                try:
                    driver.quit()
                except:
                    pass
            self.drivers.clear()

    def __del__(self):
        self.close_browser()