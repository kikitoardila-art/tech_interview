# Akila · Solución Prueba Técnica (Transformación Digital & IA)

**Candidato:** Enrique  
**Cargo:** Líder de Transformación Digital e Inteligencia Artificial  

---

## 🚀 Estructura del Repositorio

```text
.
├── README.md                   <-- Documentación principal
├── requirements.txt            <-- Librerías requeridas
├── apartamentos_akila.csv      <-- Dataset de apartamentos
├── correos_clientes.csv        <-- Dataset de correos
├── ejercicio1/
│   ├── triaje_correos.py       <-- Script de clasificación y volcado
│   └── manual_operativo.md     <-- Manual para el colaborador
└── ejercicio2/
    └── app.py                  <-- Dashboard en Streamlit


Ejercicio 1 — Triaje Automático de Correos y Volcado a Seguimiento
1. Criterios de Automatización vs. Revisión Humana
🔴 Lo que SÍ se Automatiza:
Lectura y Parsing: Extracción de metadatos (fecha, remitente, asunto, contenido).

Categorización Estructurada: Clasificación por Tipo (Reclamación, Pedido, Consulta, Spam) y asignación de Urgencia (Alta, Media, Baja).

Enrutamiento: Asignación automática del área responsable (Servicio al Cliente, Cartera, Obras/Arquitectura).

Deduplicación: Eliminación de registros repetidos enviados por el mismo cliente en ventanas cortas de tiempo.

🟡 Lo que NO se Automatiza (Human-in-the-Loop):
Compromisos Financieros o Legales: Respuestas finales sobre desistimientos, devoluciones de dinero o penalidades contractuales.

Inspecciones de Garantía y Obra: Agendamiento directo de visitas por fallas estructurales o filtraciones (requieren evaluación técnica previa).

Casos Ambiguos o Incompletos: Mensajes con baja certidumbre o sin datos claros del inmueble se derivan a una cola de revisión manual.

2. Ejecución del Script de Triaje
Para procesar el archivo correos_clientes.csv y generar la tabla de seguimiento consolidada en Excel:

Bash
