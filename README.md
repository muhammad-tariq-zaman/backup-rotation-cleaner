# backup-rotation-cleaner

Keep the newest N backups per filename prefix and delete older ones.
Dry-run by default — nothing is deleted unless `--apply` is passed.

## How to run

```bash
python3 main.py --dir ./backups --prefix bkp_ --keep 3
python3 main.py --dir ./backups --prefix bkp_ --keep 3 --apply
```

## Example output (sample from test fixture data)

```text
keep: ./backups/bkp_new.zip
keep: ./backups/bkp_mid.zip
would-delete: ./backups/bkp_old.zip
```

Standard library only. No network access.
