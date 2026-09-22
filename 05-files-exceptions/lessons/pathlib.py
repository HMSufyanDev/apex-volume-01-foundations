# Python gives us a standard library called: pathlib
# Path Object
# path = Path("data")

from pathlib import Path

data_path = Path("data")

print(data_path)
print(type(data_path))

file_path = "data/leads.txt" # old way
file_path = Path("data") / "leads.txt" # new way
# for example
data_dir = Path("data")
leads_file = data_dir / "leads.txt"

# .exists()
from pathlib import Path
data_dir = Path("data")
print(data_dir.exists())

# .is_file()
from pathlib import Path
path = Path("data/crm.json")
print(path.is_file())
# If it exists and is a file: True

# .is_dir()
data_dir = Path("data")
print(data_dir.is_dir())

# .mkdir()
from pathlib import Path
data_dir = Path("data")
data_dir.mkdir() # Create this directory.

# Important: .mkdir() Doesn't Create Parents Automatically
# Means if we are doing something like: backup_dir = Path("data/backups"), 
# and then backup_dir.mkdir(), so it try to create backups folder
# but if our parent folder means data folder also doesnt exist so it will be fail


# parents=True
from pathlib import Path
backup_dir = Path("data/backups")
backup_dir.mkdir(parents=True)
# Now python says: "Create whatever parent directories are missing too."
# Means now if data folder also doesnt exist, so it will create data folder and then in it create backups folder
# Means: Create missing parent directories as necessary.

# exist_ok=True
data_dir = Path("data")
data_dir.mkdir()
# python can raise: FileExistsError, if data already exist
data_dir.mkdir(exist_ok=True)
# means: "Create this directory, but don't complain if it already exists."


# .iterdir()
# data/
# │
# ├── crm.json
# ├── activity.log
# └── backups/
# How can Python see what's inside data/?

from pathlib import Path
data_dir = Path("data")
for item in data_dir.iterdir():
    print(item)
# means: Show me the immediate children of this folder.

# .parent
file_path = Path("data/crm.json")
print(file_path.parent) # data

# .name
file_path = Path("data/crm.json")
print(file_path.name) # crm,json

# .suffix
file_path.suffix # .json

# Reading With pathlib
from pathlib import Path
path = Path("notes.txt")
content = path.read_text(encoding="utf-8")
print(content)
# path.read_text() means: Read the text from this file.


# Writing With pathlib
from pathlib import Path
path = Path("notes.txt")
path.write_text("Hello", encoding="utf-8")

# For append, we dont have append_text
with path.open("a", encoding="utf-8") as file:
    file.write("New activity\n")

# .resolve()
path = Path("data/crm.json")
print(path.resolve()) # C:\Users\Sufyan\Desktop\ProjectAPEX\week5\day2\data\crm.json

