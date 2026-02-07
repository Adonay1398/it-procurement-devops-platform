# It-procurement-devops-platform
##  📌 Descripción
Plataforma web para automatizar el proceso de solicitudes de compras de equipos,
diseñada como un proyecto de aprendizaje enfocado en prácticas DevOps reales.

El objetivo principal del proyecto es construir,desplegar y operar una 
una aplicacion en un entorno productivo utilizando buenas prácticas
de infraestructura,automatización, seguridad y observabilidad.

---

##  🎯 Objeticos del proyecto
 - Diseñar una arquitectura productiva
 - Automatizar despliegues con CI/CD
 - Aplicar Docker y Docker Compose
 - Implementar monitoreso y alertar
 - Gestionar seguridad básica en producción

---

##  🧱 Arquitectura 

flowchart TD
 User[Usuarios]
 Browser[Navegador Web]
 
 Browser --> |HTTPS| Nginx[Nginx Reverse Proxy]
 
 Nginx --> Frontend[Frontend - Next.js]
 Nginx --> Backend[Backend API - FastAPI]
 
 Backend --> DB[(PostgreSQL)]
 Backend --> Worker[Background Jobs / Cron]

 subgraph Server["Ubuntu Server"]
    Nginx
    Frontend
    Backend
    DB
    Worker
  end

---

## 🛠️ Tecnologías
- Backend: FastAPI (Python)
- Frontend: Next.js + Tailwind CSS
- Base de datos: PostgreSQL
- Contenedores: Docker & Docker Compose
- Reverse Proxy: Nginx
- CI/CD: GitHub Actions
- Monitoreo: Prometheus & Grafana
- Seguridad: HTTPS (Let's Encrypt), UFW
---
## 🚧 Estado del Proyecto

🔄  En desarrollo - Etapa 1: Arquitectura y preparacion del entorno


