🟢 DECISIÓN 1 — Separar Frontend y Backend
Contexto

La plataforma necesita:

Interfaz web moderna

API reutilizable

Posibilidad de escalar partes de forma independiente

Decisión

Separar la aplicación en:

Frontend (Next.js)

Backend (FastAPI)

Alternativas consideradas

Monolito (Django + templates)

Backend sirviendo HTML

Por qué NO se eligieron

Acoplan frontend y backend

Dificultan escalado independiente

Menos flexibilidad en despliegues

Consecuencias

✅ Escalado independiente
✅ Mejor CI/CD
❌ Mayor complejidad inicial

🟢 DECISIÓN 2 — FastAPI como Backend
Contexto

Se necesita:

API rápida

Tipado

Documentación automática

Buen rendimiento

Decisión

Usar FastAPI como framework backend.

Alternativas

Flask

Django REST Framework

Razones

Mejor rendimiento

OpenAPI automático

Curva de aprendizaje razonable

Muy usado en microservicios

Consecuencias

✅ Ideal para APIs
❌ Menos batteries-included que Django

🟢 DECISIÓN 3 — Next.js para Frontend
Contexto

Se requiere:

UI moderna

SEO aceptable

Dashboard escalable

Decisión

Usar Next.js + React + Tailwind CSS

Alternativas

React puro

Vue

Angular

Razones

Demanda laboral alta

SSR/SSG

Buen ecosistema

Consecuencias

✅ Diseño moderno
❌ Curva de aprendizaje frontend

🟢 DECISIÓN 4 — Docker como Unidad de Despliegue
Contexto

La aplicación debe:

Ejecutarse igual en cualquier entorno

Facilitar CI/CD

Evitar “en mi máquina sí funciona”

Decisión

Usar Docker para todos los servicios.

Alternativas

Instalación manual

Máquinas virtuales

Razones

Portabilidad

Aislamiento

Estándar industrial

Consecuencias

✅ Reproducibilidad
❌ Overhead inicial

🟢 DECISIÓN 5 — Nginx como Reverse Proxy
Contexto

Se necesita:

HTTPS

Manejo de tráfico

Separación de servicios

Decisión

Usar Nginx en el host como reverse proxy.

Alternativas

Nginx dentro de Docker

Traefik

Razones

Simplicidad

Control directo de certificados

Menor complejidad inicial

Consecuencias

✅ Fácil debugging
❌ Menos automático que Traefik

🟢 DECISIÓN 6 — Background Jobs Separados
Contexto

La app necesita:

Recordatorios cada 48h

Procesos no bloqueantes

Decisión

Crear un worker independiente para jobs.

Alternativas

Cron en el backend

Celery + Redis

Razones

Simplicidad

Aprendizaje gradual

Separación de responsabilidades

Consecuencias

✅ App no se bloquea
❌ Menos robusto que colas distribuidas
