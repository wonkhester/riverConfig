#!/usr/bin/env python3

from package_installer import PackageInstaller
from command_runner import CommandRunner
from shell_setter import ShellSetter
from ohmyzsh_installer import OhMyZshInstaller
from zshrc_builder import ZshrcBuilder
from config_deployer import ConfigDeployer

def main():
    packages = [
        "river",
        "wezterm",
        "git",
        "zsh",
        "nvim",
        "swayidle",
        "swaybg",
        "waybar",
        "wofi",
        "btop",
        "pavucontrol",
        "ttf-nerd-fonts-symbols",
        "noto-fonts-cjk",
    ]

    custom_commands = [
        {
            "name": "wonkhester's custom rivercarro",
            "commands": [
                "mkdir -p ~/.local/bin",
                'curl -L "$(curl -s https://api.github.com/repos/wonkhester/wonkhestersRivercarro/releases/latest | grep browser_download_url | grep rivercarro | cut -d \\" -f 4)" -o ~/.local/bin/rivercarro',
                "chmod +x ~/.local/bin/rivercarro"
            ]
        },
        {
            "name": "Clone Neovim config",
            "commands": [
                "git clone https://github.com/wonkhester/nvimConfig ~/.config/nvim"
            ]
        },
    ]

    print("\n🔹 Step 1: Installing packages...")
    installer = PackageInstaller(packages)
    installer.run()

    print("\n🔹 Step 2: Running custom commands...")
    runner = CommandRunner(custom_commands)
    runner.run()

    print("\n🔹 Step 3: Setting default shell to Zsh...")
    shell_setter = ShellSetter("/bin/zsh")
    shell_setter.set_shell()

    print("\n🔹 Step 4: Installing Oh My Zsh...")
    ohmyzsh = OhMyZshInstaller()
    ohmyzsh.install()

    print("\n🔹 Step 5: Building ~/.zshrc file...")
    builder = ZshrcBuilder()
    builder.add_path("$HOME/.local/bin")
    builder.add_path("/opt/zig-0.14")
    builder.set_theme("")
    builder.set_plugins(["git"])
    builder.append_line("autoload -Uz vcs_info")
    builder.append_line("precmd() { vcs_info }")
    builder.append_line("zstyle ':vcs_info:git:*' formats ' %F{yellow}(%b)%f'")
    builder.append_line("PROMPT='%F{blue}[%n@%m %~]%f${vcs_info_msg_0_} %F{green}$%f '")
    builder.write()

    print("\n🔹 Step 6: Deploying .config files...")
    deployer = ConfigDeployer()
    deployer.deploy()

    print("\n✅ Setup complete.")

if __name__ == "__main__":
    main()

