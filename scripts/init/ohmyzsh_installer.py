import os
import subprocess
from pathlib import Path

class OhMyZshInstaller:
    def __init__(self, user_home=None):
        self.home = Path(user_home) if user_home else Path.home()
        self.ohmyzsh_dir = self.home / ".oh-my-zsh"
        self.install_url = "https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh"

    def is_installed(self):
        return self.ohmyzsh_dir.exists()

    def install(self):
        if self.is_installed():
            print("✅ Oh My Zsh is already installed.")
            return

        print("⬇️ Installing Oh My Zsh...")
        try:
            subprocess.run(
                ["sh", "-c", f"curl -fsSL {self.install_url} | bash"],
                check=True
            )
            print("✅ Oh My Zsh installed.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Installation failed: {e}")

