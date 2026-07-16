# Sistema de Autenticación Seguro

Microservicio de autenticación seguro implementado en FastAPI. El sistema está diseñado para ser seguro, stateless (sin estado) y altamente eficiente.

## Características Principales

- **Protección de Credenciales:** Implementación de hashing de contraseñas utilizando el algoritmo Argon2, reconocido por su resistencia superior contra ataques de fuerza bruta y ataques con hardware especializado (GPUs/ASICs).
- **Gestión de Sesiones:** Manejo de autenticación y autorización mediante JSON Web Tokens (JWTs), permitiendo una arquitectura RESTful verdaderamente sin estado y facilitando la escalabilidad horizontal.
- **Persistencia Segura:** Integración con bases de datos relacionales robustas (PostgreSQL) para el almacenamiento seguro de los usuarios y metadatos.

## Tecnologías Utilizadas

- **Framework Web:** FastAPI (Python)
- **Base de Datos:** PostgreSQL
- **Seguridad:** Argon2 (Hashing), JWT (Tokens de Sesión)

## Estructura del Proyecto
- `app/main.py`: Punto de entrada de la API y rutas principales.
- `app/database.py`: Configuración y conexión con la base de datos.
- `app/models.py`: Modelos y esquemas de datos (ORM).
- `app/schemas.py`: Validaciones de entrada/salida (Pydantic).
