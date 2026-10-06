INSERT OR IGNORE INTO auth_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
VALUES ('pbkdf2_sha256$1000000$7QD3bB22ahkPz6T0rvJzF5$C46UAsCyKN254AgrKL2YR3BESdQuGX/PsBTbhNI1zDc=', 0, 'cowork_user', '', '', 'cowork_user@cowork.cl', 1, 1, datetime('now'));
