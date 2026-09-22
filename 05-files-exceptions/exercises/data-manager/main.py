from pathlib import Path


data_dir = Path("data")
backups_dir = data_dir / "backups"
crm_file = data_dir / "crm.json"


data_dir.mkdir(parents=True, exist_ok=True)
backups_dir.mkdir(parents=True, exist_ok=True)


print("Data directory:", data_dir)
print("Data directory exists:", data_dir.exists())
print("Data directory is directory:", data_dir.is_dir())

print()

print("Backups directory:", backups_dir)
print("Backups directory exists:", backups_dir.exists())
print("Backups directory is directory:", backups_dir.is_dir())

print()

print("CRM file:", crm_file)
print("CRM file exists:", crm_file.exists())
print("CRM file is file:", crm_file.is_file())

print()

print("CRM file name:", crm_file.name)
print("CRM file suffix:", crm_file.suffix)
print("CRM file parent:", crm_file.parent)


crm_file.write_text(
    '{"leads": [], "clients": [], "projects": [], "invoices": []}',
    encoding="utf-8"
)

content = crm_file.read_text(encoding="utf-8")
print(content)

for item in data_dir.iterdir():
    print(item)