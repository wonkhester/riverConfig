import shutil
from pathlib import Path

class ConfigDeployer:
    def __init__(self, source_subdir="config", target_dir=None):
        script_dir = Path(__file__).resolve().parent
        self.source_dir = (script_dir / ".." / source_subdir).resolve()
        self.target_dir = Path(target_dir or "~/.config").expanduser()

    def deploy(self):
        if not self.source_dir.exists():
            print(f"❌ Source directory not found: {self.source_dir}")
            return

        print(f"📁 Deploying config files from {self.source_dir} to {self.target_dir}")

        for item in self.source_dir.iterdir():
            src = item
            dest = self.target_dir / item.name

            if dest.exists():
                print(f"⚠️  Skipping existing: {dest}")
                continue

            try:
                if src.is_dir():
                    shutil.copytree(src, dest)
                else:
                    shutil.copy2(src, dest)
                print(f"✅ Deployed: {dest}")
            except Exception as e:
                print(f"❌ Failed to copy {src} -> {dest}: {e}")

