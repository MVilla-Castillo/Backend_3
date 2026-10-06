# Cowork

API REST en Django + Django REST Framework para gestionar espacios de trabajo compartido: sedes, salas, clientes y reservas.

## Modelo de datos

| Modelo | Campos | Relación |
|---|---|---|
| Sede | nombre, direccion, ciudad, telefono | 1 sede → N salas |
| Sala | sede, nombre, capacidad, precio_hora, activa | 1 sala → N reservas |
| Cliente | nombre, email (único), telefono, empresa | 1 cliente → N reservas |
| Reserva | cliente, sala, fecha, hora_inicio, hora_fin, estado, creada_en | — |

## Instalación

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Variables de entorno

`config/settings.py` lee el archivo `.env`, por lo que no hay credenciales escritas en el código.

```
DJANGO_SECRET_KEY=...
DJANGO_DEBUG=True
DB_ENGINE=django.db.backends.mysql
DB_NAME=cowork
DB_USER=cowork_user
DB_PASSWORD=...
DB_HOST=localhost
DB_PORT=3306
```

## Base de datos (MySQL 8)

Ejecutar como `root` desde la raíz del proyecto, en este orden (o abrir cada script en MySQL Workbench y ejecutarlo):

| Paso | Comando | Resultado |
|---|---|---|
| 1. Crear BD | `mysql -u root -p -e "source sql/01_crear_bd.sql"` | Base de datos `cowork` (utf8mb4) |
| 2. Crear usuario | `mysql -u root -p -e "source sql/02_crear_usuario.sql"` | Usuario `cowork_user@localhost` |
| 3. Asignar permisos | `mysql -u root -p -e "source sql/03_permisos.sql"` | `GRANT` sobre `cowork.*` |
| 4. Tablas | `python manage.py migrate` | Django crea las tablas conectado como `cowork_user` |

`cowork_user` recibe solo los permisos que Django necesita sobre la base `cowork`: leer y escribir datos (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) y crear o modificar tablas en las migraciones (`CREATE`, `ALTER`, `DROP`, `INDEX`, `REFERENCES`). No tiene acceso a otras bases de datos.

Para entrar a `/admin/`:

```powershell
python manage.py createsuperuser
```

## Ejecución

```powershell
python manage.py runserver
```

| URL | Descripción |
|---|---|
| http://127.0.0.1:8000/ | Bienvenida |
| http://127.0.0.1:8000/admin/ | Administrador |
| http://127.0.0.1:8000/api/ | Raíz de la API |

## Endpoints

| Recurso | Lista / Crear | Detalle / Editar / Eliminar |
|---|---|---|
| Sedes | `/api/sedes/` | `/api/sedes/{id}/` |
| Salas | `/api/salas/` | `/api/salas/{id}/` |
| Clientes | `/api/clientes/` | `/api/clientes/{id}/` |
| Reservas | `/api/reservas/` | `/api/reservas/{id}/` |

| Método | Acción |
|---|---|
| GET | Listar o ver detalle |
| POST | Crear |
| PUT | Reemplazar completo |
| PATCH | Modificar parcial |
| DELETE | Eliminar |

## Ejemplo CRUD

```bash
curl -X POST http://127.0.0.1:8000/api/sedes/ -H "Content-Type: application/json" -d "{\"nombre\":\"Centro\",\"direccion\":\"Av 1\",\"ciudad\":\"Santiago\"}"
curl http://127.0.0.1:8000/api/sedes/1/
curl -X PATCH http://127.0.0.1:8000/api/sedes/1/ -H "Content-Type: application/json" -d "{\"telefono\":\"221234567\"}"
curl -X DELETE http://127.0.0.1:8000/api/sedes/1/
```

## Estructura

```
config/          settings, urls
cowork/          models, serializers, views, urls, admin, migrations
sql/             scripts de base de datos
templates/       páginas 404 y 400
.env             variables de entorno
requirements.txt
```
