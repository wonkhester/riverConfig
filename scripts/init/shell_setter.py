import os
import shutil
import subprocess
import sys

class ShellSetter:
    def __init__(self, shell_path="/bin/zsh"):
        self.shell_path = shell_path

    def is_valid_shell(self):
        """Check if the shell exists in /etc/shells."""
        if not os.path.isfile(self.shell_path):
            print(f"❌ Shell path does not exist: {self.shell_path}")
            return False
        try:
            with open("/etc/shells", "r") as f:
                return self.shell_path in f.read()
        except Exception as e:
            print(f"⚠️ Could not read /etc/shells: {e}")
            return False

    def get_current_shell(self):
        """Return the current user's shell."""
        return os.environ.get("SHELL")

    def set_shell(self):
        """Attempt to set the default shell using chsh."""
        current = self.get_current_shell()
        if current == self.shell_path:
            print(f"✅ Shell already set to {self.shell_path}")
            return True

        if not self.is_valid_shell():
            print(f"❌ {self.shell_path} is not listed in /etc/shells.")
            return False

        print(f"🔧 Changing shell from {current} to {self.shell_path}")
        try:
            subprocess.run(["chsh", "-s", self.shell_path], check=True)
            print("✅ Shell changed successfully. You may need to log out and back in.")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to change shell. Are you running this in a login terminal?")
            return False
        except Exception as e:
            print(f"❌ Error: {e}")
            return False

