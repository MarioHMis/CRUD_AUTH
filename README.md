# 🛡️ CRUD_AUTH – Secure Task Manager

A modern and responsive web app built with Django 5 and Bootstrap 5. This project provides a secure environment for users to manage their personal tasks with full authentication support.

🔗 **Live Demo:** [Visit the site](https://crud-auth-hijd.onrender.com)

## 🚀 Features

- 🔐 Custom user authentication system
- ✅ Full CRUD operations for tasks
- 🌗 Dark and light theme toggle
- 🧠 Only logged-in users can manage their tasks
- ⚙️ Class-Based Views (CBV) with Django
- 📦 PostgreSQL integration
- ☁️ Ready to deploy on Render

## 🛠️ Tech Stack

- **Backend:** Django 5.1
- **Frontend:** Bootstrap 5 + Bootstrap Icons
- **Database:** PostgreSQL
- **Deployment:** Render
- **Environment Management:** Python Decouple

## 🧪 Running Locally

```bash
# 1. Clone the repo
git clone https://github.com/MarioHMis/CRUD_AUTH.git

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add environment variables in .env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url

# 5. Run migrations and start server
python manage.py migrate
python manage.py runserver
```

---

# 🛡️ CRUD_AUTH – Gestor de Tareas Seguro

Una aplicación web moderna y responsiva construida con Django 5 y Bootstrap 5. Este proyecto ofrece un entorno seguro para que los usuarios gestionen sus tareas personales con autenticación completa.

🔗 **Demo en Vivo:** [Visitar sitio](https://crud-auth-hijd.onrender.com)

## 🚀 Funcionalidades

- 🔐 Sistema de autenticación personalizado
- ✅ CRUD completo de tareas
- 🌗 Interruptor de tema claro/oscuro
- 🧠 Solo usuarios autenticados pueden gestionar tareas
- ⚙️ Vistas basadas en clases con Django
- 📦 Integración con PostgreSQL
- ☁️ Listo para desplegar en Render

## 🛠️ Stack Tecnológico

- **Backend:** Django 5.1
- **Frontend:** Bootstrap 5 + Iconos Bootstrap
- **Base de datos:** PostgreSQL
- **Despliegue:** Render
- **Gestión de entorno:** Python Decouple



## 🧪 Ejecutar Localmente

```bash
# 1. Clona el repositorio
git clone https://github.com/MarioHMis/CRUD_AUTH.git

# 2. Crea y activa un entorno virtual
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Crea un archivo .env con:
DEBUG=True
SECRET_KEY=tu-clave-secreta
DATABASE_URL=tu-url-de-bd

# 5. Aplica migraciones y ejecuta el servidor
python manage.py migrate
python manage.py runserver
```
