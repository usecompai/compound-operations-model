# Montar un Company Brain con Codex

Guía práctica para un fundador o responsable técnico. Revisada el 15 de septiembre de 2026 contra Compai v6.2 y la documentación oficial vigente de Codex.

## La idea correcta

Codex puede construir el sistema y servir como una de sus superficies de trabajo. No debe ser el lugar donde vive la empresa.

La memoria, los permisos, las integraciones, el estado de las tareas y las evidencias tienen que existir fuera del modelo. Así puedes cambiar de modelo, abrir una sesión nueva o trabajar desde otro dispositivo sin perder el sistema.

```text
Fuentes de empresa
email / documentos / reuniones / ERP / CRM / ecommerce / soporte
                         |
                 captura determinista
                         |
              archivo raw + datos estructurados
                         |
                 digestión y memoria
                         |
                     Brain
                         |
        ContextPack + capacidades + permisos
                         |
             Codex / personas / agentes
                         |
                acción acotada
                         |
        verificación en el sistema fuente
                         |
             recibo, aprendizaje y cierre
```

Un agente que responde bien no equivale a un sistema operativo de empresa. La unidad útil es una capacidad que puede leer una fuente, producir o ejecutar algo, comprobarlo y dejar evidencia.

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

## Siete contratos mínimos

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

## Configurar Codex

### Codex local

Instala Codex desde la documentación oficial, abre tu repositorio e inicia sesión. Codex carga instrucciones globales y de proyecto desde archivos `AGENTS.md`; mantén las reglas generales cortas y coloca las instrucciones específicas cerca del código al que afectan.

### Codex Cloud

Conecta el repositorio y configura dependencias, scripts y secretos en el entorno cloud. El entorno debe poder reconstruirse desde el repositorio. Los secretos de Codex Cloud solo están disponibles durante la fase de setup, no durante la fase del agente.

### MCP

Cuando exista una primera API o un Brain consultable, expón herramientas tipadas mediante un MCP autenticado. Cada tool debe tener inputs estrechos y devolver evidencia estructurada. Evita una herramienta de shell general para todos los usuarios.

```toml
[mcp_servers.company]
url = "https://mcp.example.com/mcp"
bearer_token_env_var = "COMPANY_MCP_TOKEN"
```

Guarda el token fuera del repositorio. Verifica la conexión con una consulta de identidad, una búsqueda del Brain, una lectura real y un intento prohibido que deba ser rechazado.

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

Prueba al menos: fuente correcta, cuenta equivocada, vacío legítimo, credencial inválida, paginación incompleta, dato obsoleto, fuentes contradictorias, `run_id` duplicado, reinicio a mitad, aprobación ausente, verificación posterior fallida y restauración aislada.

El creador del workflow no debe ser el único juez de los casos sensibles.

## Criterio para añadir agentes

Añade un agente de dominio cuando ya existan conocimiento propio del área, capabilities verificadas, permisos distintos, volumen suficiente, owner humano, evals y límites específicos. Hasta entonces, un solo Codex trabajando con ContextPacks y skills es más sencillo de operar.

## Siguiente paso

Usa el [prompt de bootstrap para Codex](codex-company-brain-bootstrap-prompt.es.md) en un repositorio privado. La primera ejecución hace discovery y deja la implementación pendiente de aprobación.

## Fuentes

- [Compai v6.2](https://github.com/usecompai/compound-operations-model)
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli)
- [Codex Cloud](https://learn.chatgpt.com/docs/environments/cloud-environment)
- [`AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [MCP en Codex](https://learn.chatgpt.com/docs/extend/mcp)
- [Modo no interactivo](https://learn.chatgpt.com/docs/non-interactive-mode)
- [Skills](https://learn.chatgpt.com/docs/build-skills)
