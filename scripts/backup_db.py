import os
import sqlite3
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(__file__)
BACKUP_DIR = os.path.join(BASE_DIR, '..', 'backups')
DB_PATH = os.path.join(BASE_DIR, '..', 'todo.sqlite')
RETENTION_DAYS = 7


def create_backup() -> None:
    """Create a timestamped SQL dump of the SQLite database."""
    os.makedirs(BACKUP_DIR, exist_ok=True)

    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M')
    backup_name = f'db_backup_{timestamp}.sql'
    backup_path = os.path.join(BACKUP_DIR, backup_name)

    with sqlite3.connect(DB_PATH) as conn, open(backup_path, 'w', encoding='utf-8') as f:
        for line in conn.iterdump():
            f.write(f'{line}\n')

    print(f'Backup created: {backup_name}')


def cleanup_old_backups() -> None:
    """Delete backup files older than the retention period."""
    cutoff = datetime.now() - timedelta(days=RETENTION_DAYS)

    for filename in os.listdir(BACKUP_DIR):
        if not filename.startswith('db_backup_') or not filename.endswith('.sql'):
            continue

        path = os.path.join(BACKUP_DIR, filename)
        file_time = datetime.fromtimestamp(os.path.getmtime(path))

        if file_time < cutoff:
            os.remove(path)
            print(f'Deleted old backup: {filename}')


if __name__ == '__main__':
    create_backup()
    cleanup_old_backups()

