import subprocess
import sys

class PackageInstaller:
    def __init__(self, packages, package_manager="pacman"):
        self.packages = packages
        self.package_manager = package_manager

    def display_packages(self):
        print("The following packages will be installed:\n")
        for pkg in self.packages:
            print(f"  - {pkg}")

    def confirm_installation(self):
        choice = input("\nDo you want to proceed with installation? [y/N]: ").strip().lower()
        return choice in ("y", "yes")

    def install_packages(self):
        try:
            print("\nInstalling packages...\n")
            subprocess.run(["sudo", self.package_manager, "-S"] + self.packages, check=True)
            print("\n✅ All packages installed successfully.")
        except subprocess.CalledProcessError:
            print("\n❌ An error occurred during package installation.")
            sys.exit(1)

    def run(self):
        self.display_packages()
        if self.confirm_installation():
            self.install_packages()
        else:
            print("Installation cancelled.")
            sys.exit(0)

