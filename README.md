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
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

## Base de datos (SQLite)

Ejecutar desde la raíz del proyecto, en este orden:

| Paso | Comando | Resultado |
|---|---|---|
| 1. Crear BD | `python -c "import sqlite3; sqlite3.connect(':memory:').executescript(open('sql/01_crear_bd.sql').read())"` | `ATTACH DATABASE` crea `db.sqlite3` |
| 2. Tablas | `python manage.py migrate` | Crea las tablas del modelo y de Django |
| 3. Crear usuario | `python -c "import sqlite3; sqlite3.connect('db.sqlite3').executescript(open('sql/02_crear_usuario.sql').read())"` | Usuario `cowork_user` en `auth_user` |
| 4. Asignar permisos | `python -c "import sqlite3; sqlite3.connect('db.sqlite3').executescript(open('sql/03_permisos.sql').read())"` | Permisos add/change/delete/view de los 4 modelos |

SQLite no tiene usuarios ni `GRANT` propios, por lo que el usuario y los permisos se crean en las tablas de autenticación de Django. `cowork_user` (contraseña `cowork_pass_2026`) entra a `/admin/` y solo puede gestionar sedes, salas, clientes y reservas.

Para un administrador completo:

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
