# Montar un Company Brain con Codex

Guía práctica para un fundador o responsable técnico. Revisada el 1 de octubre de 2026 contra Compai v6.2, los aprendizajes de producción de los diez días anteriores y la documentación oficial vigente de Codex.

## La idea correcta

Codex puede construir el sistema y servir como una de sus superficies de trabajo. No debe ser el lugar donde vive la empresa.

La memoria, los permisos, las integraciones, el estado de las tareas y las evidencias tienen que existir fuera del modelo. Así puedes cambiar de modelo, abrir una sesión nueva o trabajar desde otro dispositivo sin perder el sistema.

```text
Fuentes y SaaS
email / documentos / ERP / CRM / ecommerce / finanzas / soporte
                              |
           captura + conectores OAuth gestionados
                              |
                archivo raw + datos estructurados
                              |
                    digestión y memoria
                              |
                          Brain
                              |
          ContextPack + Project Registry + capabilities
                              |
     Codex / asistentes personales / chat / workers / equipo
                              |
                  acción tipada y acotada
                              |
             verificación en el sistema fuente
                              |
           recibo + aprendizaje + recuperación
```

Un agente que responde bien no equivale a un sistema operativo de empresa. La unidad útil es una capacidad que puede leer una fuente, producir o ejecutar algo, comprobarlo y dejar evidencia.

## Qué cambió en esta revisión

Los últimos despliegues añadieron nueve contratos que faltaban en la primera versión de esta guía.

### 1. Codex no es la única superficie

Un asistente personal como Instinct, un bot de Slack o WhatsApp y un worker de fondo pueden usar el mismo Brain. Cada superficie entra por un adaptador tipado y una identidad propia y revocable. Una identidad puede ser equivalente al fundador dentro del Brain sin recibir shell, acceso al host, secretos ni administración global.

El bridge debe exponer operaciones concretas como buscar, leer, escribir, mover, aprender o crear una tarea. No debe entregar una credencial reutilizable al sandbox del asistente. Las mutaciones usan `request_id`, preflight, verificación posterior y una regla de no repetición cuando el resultado queda ambiguo.

### 2. Los MCP de terceros se conectan detrás del MCP central

Fintable es un ejemplo del patrón: el OAuth vive en el servicio central, no en cada chat o portátil. El proxy filtra las herramientas visibles y vuelve a comprobar la autorización en cada llamada. Tener conectado el MCP de la empresa no concede acceso al conector.

Cada integración debe declarar qué roles la ven, qué operaciones pueden ejecutar, cómo se refresca el token, qué Workspaces o cuentas cubre, qué se registra en el ledger y cómo se revoca. Los borrados necesitan confirmación en dos pasos. Una prueba completa incluye lectura, una edición inocua con lectura posterior y una identidad negativa a la que se deniega el acceso.

Separa además `deployed` de `connected`. Un proxy puede pasar sus tests y seguir en `awaiting_oauth_consent` hasta que el propietario elija las cuentas correctas. No declares datos disponibles antes de completar ese E2E.

### 3. Los permisos humanos se asignan por rol y dominio

Las listas de excepciones por persona no escalan. El registro de identidad combina perfiles como Finanzas, Operaciones o AI Lead con dominios de lectura y escritura. Los dominios sensibles siguen separados y los grants a un documento concreto no amplían el dominio completo.

Una persona autenticada no necesita un permiso nuevo para cada acción normal de su puesto. Si el rol autoriza la operación pero no existe una herramienta tipada, el fallo es de implementación de Platform, no una petición de permiso al fundador.

### 4. Los huecos de capacidad tienen su propio broker

El broker distingue `authorization_denied` de `capability_missing`, deduplica incidencias, asigna un responsable, vigila el plazo y avisa solo cuando cambia el estado. La reparación se cierra con una sesión nueva bajo la identidad real de la persona afectada. No basta con que funcione como administrador.

### 5. Los proyectos recurrentes viven en un Project Registry

Cada dashboard, automatización o servicio gestionado registra repositorio canónico, workspace, responsables, documentación principal, instrucciones, fuentes, invariantes, preflight, perfil de runtime, ruta de publicación y rollback. El operador publica un commit inmutable; Platform mantiene red, secretos, almacenamiento, procesos y recuperación.

Una herramienta no está lista solo porque su web y su health endpoint funcionen. Todas las lecturas y mutaciones normales deben estar expuestas como operaciones tipadas y probadas con las identidades que las usarán.

Las altas operativas repetibles, como una nueva tienda o centro, pertenecen a un registro versionado con validación y regeneración. No deberían exigir editar condicionales en varios scripts y dashboards.

### 6. Los jobs conservan el último estado válido

Un timer de producción necesita idempotencia, reintentos limitados, lock, fecha de cobertura, alerta por cambio de estado y recuperación sin publicaciones duplicadas. Si agota los reintentos, conserva la última versión validada y deja el error verificable; no promueve un resultado parcial.

### 7. El índice también es un sistema de producción

La búsqueda léxica sigue siendo el baseline. Si añades embeddings, el mantenimiento debe trabajar por colección, compartir un lock con la actualización, medir el progreso después de cada lote y detectar starvation. Los logs append-only demasiado grandes pueden seguir disponibles para lectura directa sin entrar en el índice semántico.

### 8. Capturar no significa digerir correctamente

La ingesta debe separar carreras de versión, indisponibilidad temporal, fallo permanente y backlog. Una ampliación de alcance invalida el estado de catch-up anterior. Un elemento que falla y después entra correctamente debe reconciliar su dead letter; no puede quedar marcado como fallo para siempre.

### 9. La fuente canónica y el runtime no pueden divergir

El código desplegado, la copia canónica y el registro de capabilities se comparan antes de iniciar el servicio. El source gate debe bloquear una mezcla de versiones. La corrección no es reiniciar hasta que arranque: es reconciliar la fuente, ejecutar tests, desplegar una unidad coherente y repetir el smoke.

## Qué construir en la V1

No empieces creando un agente por departamento. La V1 debe resolver un solo trabajo repetitivo y medible.

Buenos primeros casos:

- preparar respuestas de soporte para revisión humana;
- generar un informe semanal de caja o ventas desde sistemas fuente;
- detectar anomalías en campañas y proponer una acción;
- convertir reuniones en tareas con responsable y fecha;
- conciliar un listado interno sin efectuar pagos ni comunicaciones externas.

El primer caso debe cumplir cinco condiciones:

1. Ocurre con frecuencia.
2. Tiene fuentes identificables.
3. Existe una forma objetiva de comprobar el resultado.
4. Un error es reversible o queda en modo borrador.
5. Hay una persona que decide si el resultado es correcto.

## Lo que necesitas

- Una instalación compatible de Codex. Codex Cloud es útil cuando el desarrollo debe continuar sin depender de un portátil.
- Un repositorio privado para el código, los contratos y las instrucciones de tu implementación.
- Un responsable técnico para APIs, secretos, despliegues y fallos.
- Acceso oficial a una sola fuente para el piloto.
- Un runtime persistente cuando necesites ingesta, un MCP o jobs programados. Un entorno de Codex Cloud ejecuta trabajo en un contenedor asociado a un repositorio; no sustituye una base de datos, un worker permanente ni un servicio de producción.

No compartas claves en prompts, Markdown, documentos ni código. Usa el gestor de secretos del host o del proveedor.

## Usar Compai como referencia

La release pública es material de arquitectura, no un instalador universal:

```bash
git clone https://github.com/usecompai/compound-operations-model.git compai-reference
cd compai-reference
python3 scripts/release_audit.py --repo-root .
```

Lee primero:

1. `chapters/23-operating-layer.md`
2. `chapters/24-context-compiler.md`
3. `chapters/25-capability-registry.md`
4. `chapters/26-human-work-mode.md`
5. `chapters/28-decision-packs-outcome-receipts.md`
6. `kit/README.md`

El repositorio se publica bajo CC BY-NC-SA 4.0. Revisa la licencia antes de reutilizar archivos o derivados en una actividad comercial.

## Repositorio canónico

Crea una implementación privada separada de la referencia:

```text
company-brain/
├── AGENTS.md
├── README.md
├── brain/
│   ├── knowledge/
│   │   ├── company/
│   │   ├── customers/
│   │   ├── finance/
│   │   ├── operations/
│   │   └── projects/
│   ├── memory/
│   ├── tasks/
│   ├── decisions/
│   ├── receipts/
│   └── health/
├── config/
│   ├── architecture-contract.md
│   ├── company.yml
│   ├── source-coverage.yml
│   ├── identities.yml
│   ├── governance.yml
│   ├── capability-registry.yml
│   └── loops/
├── schemas/
│   ├── context-pack.schema.json
│   ├── approved-task.schema.json
│   ├── decision-pack.schema.json
│   ├── outcome-receipt.schema.json
│   └── audit-event.schema.json
├── services/
│   ├── ingest/
│   ├── mcp/
│   └── workers/
├── adapters/
├── skills/
├── tests/
├── scripts/
└── data/
```

Git guarda conocimiento curado, contratos, skills y código. Las transcripciones masivas, adjuntos, bases de datos, caches, tokens y logs sin límite necesitan otro almacenamiento. El Brain conserva el resumen y la referencia a esos artefactos.

## Diez contratos mínimos

### 1. Arquitectura

`config/architecture-contract.md` fija fuentes canónicas, almacenamiento, identidad, método de despliegue, pruebas, rollback y debilidades conocidas.

### 2. Cobertura de fuentes

`config/source-coverage.yml` enumera sistema, cuenta, tipo de contenido, ventana histórica, frecuencia, owner y smoke test. “Tenemos Gmail conectado” no describe qué buzones ni qué mensajes están cubiertos.

### 3. Identidad

Cada persona y cada worker necesitan una identidad distinta. Un proceso desatendido no debe actuar como el fundador ni reutilizar su sesión.

### 4. Capability Registry

Una capability es algo que funciona ahora, no algo descrito en un README. Cada entrada declara fuente, inputs, outputs, permisos, frescura, prueba inocua, verificación, estados terminales, owner y bloqueos. Usa estados explícitos como `ready`, `degraded`, `blocked_auth`, `planned` y `deprecated`.

### 5. ContextPack

Antes de cada trabajo importante, compila solo el contexto necesario para esa identidad y esa tarea. Separa hechos citados, datos operativos leídos en vivo, decisiones previas, incertidumbre, contradicciones y capacidades disponibles.

### 6. Política

Separa cuatro niveles:

- `read`: consultar y analizar;
- `propose`: crear borradores o propuestas;
- `execute`: realizar una acción acotada;
- `administer`: cambiar permisos, runtime o infraestructura.

Un modelo más potente no recibe más autoridad. Las acciones financieras, legales, de RRHH, destructivas o externas empiezan con aprobación humana.

### 7. Outcome Receipt

Una tarea no está cerrada porque el agente diga que terminó. El recibo registra actor, fuentes, frescura, acciones, outputs, versiones, comprobación en el sistema fuente, resultado medible, estado terminal, riesgo residual y siguiente responsable.

### 8. Project Registry y release

Cada proyecto recurrente declara repositorio, workspace, documentación principal, fuentes, invariantes, preflight, identidades autorizadas, runtime, publicación y rollback. La release parte de un commit inmutable y termina con health y evidencia de producción.

### 9. Conectores y OAuth

Cada conector declara propietario del consentimiento, cuentas o Workspaces cubiertos, almacenamiento y rotación del token, roles permitidos, filtros de herramientas, confirmaciones destructivas, ledger y prueba de revocación. La autorización se aplica en `tools/list` y otra vez al ejecutar.

### 10. Operación y recuperación

Índices, ingestas, timers y workers necesitan frescura, locks, reintentos limitados, reconciliación, backup, restore, alertas por cambio de estado y una condición de parada. Un sistema degradado conserva el último estado válido y explica qué falta.

## Configurar Codex

### Codex local

Instala Codex desde la documentación oficial, abre tu repositorio e inicia sesión. Codex carga instrucciones globales y de proyecto desde archivos `AGENTS.md`; mantén las reglas generales cortas y coloca las instrucciones específicas cerca del código al que afectan.

### Codex Cloud

Conecta el repositorio y configura dependencias, scripts y secretos en el entorno cloud. El entorno debe poder reconstruirse desde el repositorio. Los secretos de Codex Cloud solo están disponibles durante la fase de setup, no durante la fase del agente.

### Agents API y entornos propios

La Agents API permite usar el harness gestionado de Codex con sesiones durables, herramientas y MCP. Elige `environment: none` si el agente solo llama herramientas remotas, un sandbox alojado cuando necesita trabajar con archivos aislados o `self_hosted` cuando debe usar tu red y tu software.

Una sesión durable sigue sin ser el Brain de la empresa. La memoria canónica, el estado de los proyectos y los receipts permanecen en tus sistemas. En un entorno propio, aísla cada usuario o workload y usa una clave de executor restringida; la clave general de la aplicación no entra en el sandbox.

### MCP

Cuando exista una primera API o un Brain consultable, expón herramientas tipadas mediante un MCP autenticado. Cada tool debe tener inputs estrechos y devolver evidencia estructurada. Evita una herramienta de shell general para todos los usuarios.

```toml
[mcp_servers.company]
url = "https://mcp.example.com/mcp"
bearer_token_env_var = "COMPANY_MCP_TOKEN"
```

Guarda el token fuera del repositorio. Verifica la conexión con una consulta de identidad, una búsqueda del Brain, una lectura real y un intento prohibido que deba ser rechazado.

Para un MCP remoto, limita también las herramientas anunciadas. Si la superficie solo necesita Brain, no anuncies shell, filesystem, secretos ni conectores operativos. Si un conector usa OAuth de terceros, conserva la credencial detrás del servidor o de un proxy confiable para que el código generado por el agente no pueda leerla.

## Orden de implementación

### Fase 0: discovery

Documenta sistemas, responsables, primer workflow, riesgo, autoridad, fuente de verdad, métrica de éxito y huecos de acceso. No conectes nada todavía.

### Fase 1: Brain y contratos

Crea el árbol del repositorio, `AGENTS.md`, contratos y esquemas. Carga solo empresa, productos, políticas, equipo, definiciones métricas y el procedimiento del primer workflow.

La fase termina cuando una sesión nueva encuentra la información correcta, las afirmaciones importantes citan su fuente, lo obsoleto aparece como obsoleto y no hay secretos ni datos masivos en Git.

### Fase 2: primera fuente en read-only

Construye un adaptador pequeño sobre la API oficial. La salida debe ser paginada, fechada, atribuida y reproducible. Conserva una muestra anonimizada para tests.

### Fase 3: búsqueda y ContextPack

Empieza con Markdown, metadatos y búsqueda léxica. Añade embeddings cuando el volumen o los casos reales lo justifiquen. El índice nunca sustituye al original.

### Fase 4: primer workflow en shadow mode

El workflow produce un borrador o Decision Pack sin cambiar sistemas externos. Cada run termina como `clean_noop`, `approval_required`, `blocked`, `failed` o `success`.

### Fase 5: acción aprobada

Añade una única acción reversible. Relee el estado antes de actuar, verifica después en el sistema fuente y genera el Outcome Receipt.

### Fase 6: runtime persistente

Despliega ingesta y workers con identidad de servicio, secretos gestionados, health, logs con retención, locks, idempotencia, reintentos limitados, alertas por cambio de estado, backup, restore y rollback.

### Fase 7: equipo y superficies adicionales

Añade perfiles por rol y dominio, registra los proyectos recurrentes y conecta una segunda superficie solo después de probar la primera. El smoke mínimo cubre identidad, herramientas visibles, lectura autorizada, mutación permitida, denegación cruzada y receipt. Activa el broker de capacidades cuando exista un owner técnico que pueda reparar herramientas faltantes.

## El primer loop

```text
OBSERVE  leer fuentes frescas y el contexto permitido
CHOOSE   seleccionar como máximo una acción según reglas escritas
ACT      generar un candidato o realizar una acción reversible autorizada
VERIFY   comprobar formato, contenido y efecto en la fuente
RECORD   guardar evidencia, resultado y corrección
STOP     cerrar, pedir aprobación, bloquear o fallar explícitamente
```

La siguiente ejecución solo debe cambiar si existe información nueva. Si no hay feedback nuevo, no es un loop: es una tarea puntual.

## Evals antes de permitir escrituras

Prueba al menos: fuente correcta, cuenta equivocada, vacío legítimo, credencial inválida, paginación incompleta, dato obsoleto, fuentes contradictorias, herramienta visible para el rol correcto, llamada directa denegada al rol incorrecto, `run_id` duplicado, mutación con resultado ambiguo, reinicio a mitad, aprobación ausente, verificación posterior fallida, refresh OAuth, revocación y restauración aislada.

El creador del workflow no debe ser el único juez de los casos sensibles.

## Criterio para añadir agentes

Añade un agente de dominio cuando ya existan conocimiento propio del área, capabilities verificadas, permisos distintos, volumen suficiente, owner humano, evals y límites específicos. Hasta entonces, un solo Codex trabajando con ContextPacks y skills es más sencillo de operar.

## Siguiente paso

Usa el [prompt de bootstrap para Codex](codex-company-brain-bootstrap-prompt.es.md) en un repositorio privado. La primera ejecución hace discovery y deja la implementación pendiente de aprobación.

## Fuentes

- [Compai v6.2](https://github.com/usecompai/compound-operations-model)
- [Agents API](https://developers.openai.com/api/docs/guides/agents-api/overview)
- [Arquitectura de Agents API](https://developers.openai.com/api/docs/guides/agents-api/architecture)
- [Entornos self-hosted](https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted)
- [Conexiones MCP](https://developers.openai.com/api/docs/guides/agents-api/tools/mcp)
- [Seguridad del sandbox](https://developers.openai.com/api/docs/guides/agents-api/environments/security)
- [OpenAI Docs MCP](https://developers.openai.com/learn/docs-mcp)
