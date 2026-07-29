# Manual Operativo: Triaje Automático de Correos y Gestión de Seguimiento

**Proceso:** Clasificación y volcado de correos de clientes  
**Rol objetivo:** Colaborador de Atención al Cliente / Operaciones  

---

## 1. Estrategia de Automatización (Human-in-the-Loop)

### 🔴 ¿Qué SÍ se automatiza?
* **Lectura y parsing:** Extracción rápida de remitente, fecha, asunto y cuerpo del correo.
* **Categorización y Priorización:** Clasificación automática del tipo de petición (`Consulta`, `Pedido`, `Reclamación`, `Desistimiento`) y nivel de urgencia (`Alta`, `Media`, `Baja`).
* **Enrutamiento:** Asignación automática del área/persona responsable según la temática.
* **Deduplicación:** Detección de correos duplicados enviados por un mismo cliente en ventanas cortas de tiempo.
* **Volcado a seguimiento:** Generación automática del consolidado en Excel listo para gestión.

### 🟡 ¿Qué NO se automatiza y por qué?
* **Respuestas a Reclamaciones Graves o Legales:** Todo correo clasificado como `Reclamación` o `Desistimiento` requiere revisión humana antes de enviar compromisos por escrito, para evitar responsabilidades financieras o legales no autorizadas.
* **Mensajes Ambiguos o Incompletos:** Aquellos correos con información insuficiente se marcarán como `Pendiente / Revisión Humana` para que el colaborador contacte al cliente directamente.

---

## 2. Guía Paso a Paso para el Colaborador (SOP)

### Rutina Diaria (Tiempo estimado: 15 minutos):

1. **Ejecutar la herramienta:**
   Cada mañana a primera hora, abre la terminal y ejecuta:
   ```bash
   python ejercicio1/triaje_correos.py
