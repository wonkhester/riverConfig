import subprocess

class CommandRunner:
    def __init__(self, command_groups):
        """
        command_groups: List of dictionaries with:
        {
            "name": "Group description",
            "commands": ["cmd1", "cmd2", ...]
        }
        """
        self.command_groups = command_groups

    def run(self):
        for group in self.command_groups:
            name = group.get("name", "Unnamed Command Group")
            commands = group.get("commands", [])

            print(f"\n🚀 Running: {name}")
            for cmd in commands:
                print(f"→ {cmd}")
                try:
                    subprocess.run(cmd, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"❌ Command failed: {cmd}\n   ↳ {e}")

