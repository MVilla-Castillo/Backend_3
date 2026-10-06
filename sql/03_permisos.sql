INSERT OR IGNORE INTO auth_user_user_permissions (user_id, permission_id)
SELECT u.id, p.id
FROM auth_user u, auth_permission p
JOIN django_content_type c ON c.id = p.content_type_id
WHERE u.username = 'cowork_user' AND c.app_label = 'cowork';
