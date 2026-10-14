# Montar un Company Brain con Codex

Empieza por un trabajo concreto, su responsable y un resultado verificable. El modelo es una interfaz; memoria, permisos y conexiones deben existir fuera de él.

## Antes de construir

Identifica sistemas fuente, alcance de cada identidad y acciones que necesitan aprobación. Revisa las herramientas existentes antes de crear otra integración. No uses datos privados en demos públicas.

## Primer recorrido

Prepara un caso ficticio. Recupera contexto con fuentes, consulta el dato actual y genera un borrador. Comprueba el resultado con su responsable. Añade escritura solo después de probar autorización, idempotencia, errores y rollback.

## Publicación y cierre

Guarda código, ejecuta tests, revisa secretos y datos privados, publica una revisión inmutable y verifica la URL final. Protege las herramientas internas. Registra qué se publicó y cómo volver atrás.

No basta con que el agente diga que terminó: lee el destino y guarda la evidencia. Si falta una fuente o permiso, registra el bloqueo sin inventar una salida.

Consulta la [arquitectura](../chapters/03-architecture.md) y el [starter kit](../kit/README.md). Los materiales usan CC BY-NC-SA 4.0; revisa la licencia antes del uso comercial.
