# Impulso Shop V1

Impulso Shop V1 es una plataforma D2C (Direct-to-Consumer) de alto rendimiento, diseñada con una arquitectura modular sobre **Django 5**. El sistema integra capacidades de gestión de catálogo, pedidos y logística en tiempo real utilizando **PostgreSQL**, **Redis**, **Celery** y **Django Channels** para habilitar el seguimiento de envíos en vivo.

---

## 🏗️ Arquitectura y Estructura del Proyecto

El proyecto sigue una estructura de aplicaciones modulares (`apps/`) para garantizar la mantenibilidad y escalabilidad.

```text
/
├── apps/
│   ├── users/        # Gestión de usuarios, perfiles y roles (CLIENT, DRIVER, ADMIN)
│   ├── products/     # Catálogo, categorías, variantes y gestión de inventario
│   ├── orders/       # Carritos de compra y flujo de pedidos
│   └── logistics/    # Gestión de entregas, asignación de drivers y tracking GPS
├── config/           # Configuración centralizada de Django (settings, urls, wsgi/asgi)
└── manage.py
```

---

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python 3.12+
- **Framework Web:** Django 5
- **API:** Django REST Framework (DRF)
- **Base de Datos:** PostgreSQL
- **Tareas Asíncronas:** Celery + Redis
- **Tiempo Real:** Django Channels
- **Desarrollo/CLI:** Gemini CLI

---

## ⚙️ Instrucciones de Instalación y Configuración Local

1.  **Clonar el repositorio:**
    ```bash
    git clone <url-del-repo>
    cd impulso-shop-v1
    ```
2.  **Crear y activar entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```
3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configurar `.env`:**
    Copia el ejemplo y ajusta las variables de entorno:
    ```bash
    cp .env.example .env
    ```
5.  **Correr migraciones:**
    ```bash
    python manage.py migrate
    ```
6.  **Crear superusuario de desarrollo:**
    ```bash
    python create_admin.py
    ```
7.  **Levantar el servidor:**
    ```bash
    python manage.py runserver
    ```

---

## 📡 Endpoints de la API (Documentación API V1)

| Módulo | Endpoint | Métodos |
| :--- | :--- | :--- |
| **Usuarios** | `/api/v1/users/` | GET, POST |
| **Productos** | `/api/v1/products/` | GET |
| **Categorías** | `/api/v1/products/categories/` | GET |
| **Carrito** | `/api/v1/orders/cart/` | GET, POST, DELETE |
| **Órdenes** | `/api/v1/orders/orders/` | GET, POST |
| **Envíos** | `/api/v1/logistics/deliveries/` | GET, PATCH |

---

## 📊 Hoja de Ruta (Roadmap)

- [x] **Fase 1:** Arquitectura Base, Modelos ORM e Infraestructura.
- [x] **Fase 2:** Vistas, API REST y Búsqueda del Catálogo.
- [ ] **Fase 3:** Pasarela de Pagos (Mercado Pago / Stripe) y Webhooks.
- [ ] **Fase 4:** WebSockets, Django Channels y Tracking GPS en Vivo.
- [ ] **Fase 5:** Lealtad Gamificada y Social Commerce (WhatsApp API).

---

## 🔄 Instrucciones de Mantenimiento

> **Nota:** Este archivo `README.md` debe ser actualizado por Gemini CLI tras implementar correcciones o nuevas funcionalidades relevantes para el proyecto.
