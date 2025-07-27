# Database Backup Script

This script provides basic functionality to:

1. **Create a backup** of the `todo.sqlite` SQLite database.
2. **Store backups** in the `backups/` directory.
3. **Automatically delete** backups older than 7 days.

---

## Script Location

```
scripts/backup_db.py
```

---

## Requirements

- Python 3.x
- `todo.sqlite` is in root dir

---

## Usage

Run the script from the project root:

```bash
python3 scripts/backup_db.py
```

This will:

- Generate a `.sql` file with a timestamped filename (e.g., `db_backup_2025-07-27-18-34.sql`).
- Place it inside the `backups/` folder.
- Remove any `.sql` files in `backups/` that are older than 7 days.

---

## Testing the Cleanup Logic

To test that older backups are deleted:

1. Create a dummy file in the `backups/` folder:
   ```bash
   touch -d "10 days ago" backups/db_backup_test.sql
   ```

2. Run the script again:
   ```bash
   python3 scripts/backup_db.py
   ```

3. Confirm that `old_backup.sql` has been deleted.

