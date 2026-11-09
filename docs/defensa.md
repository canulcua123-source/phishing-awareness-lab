# Defensa y mitigaciones

## Para usuarios

- **Permisos del navegador:** trata cámara, micrófono y ubicación como algo que casi
  nunca deberías conceder. Si un sitio desconocido los pide, es bandera roja.
- **Verifica el dominio real**, no el diseño de la página. Mira la barra de
  direcciones completa, no solo el candado (HTTPS ≠ confiable).
- **Desconfía de dominios de túnel** (`*.trycloudflare.com`, `*.ngrok.io`,
  `*.serveo.net`) pidiendo permisos sensibles.
- **Señales clásicas de phishing:** urgencia, premios, amenazas de cierre de cuenta,
  "verifica tu identidad ahora".
- Revisa y revoca permisos en la configuración del navegador periódicamente.

## Para administradores / red

- **Egress filtering:** limita conexiones salientes a puertos no estándar; una
  reverse shell típica llama a algo como el puerto 4444.
- **Monitoreo de DNS/proxy:** alerta sobre resoluciones a dominios de túnel.
- **EDR / detección de procesos:** intérpretes (`python3`) abriendo sockets de red
  salientes hacia IPs externas son sospechosos.
- **Concientización:** campañas internas de simulación de phishing (autorizadas)
  reducen la tasa de clic con el tiempo.

## Para desarrolladores web

- Pide permisos sensibles solo tras una acción explícita del usuario y explica por qué.
- Usa Permissions Policy (cabeceras) para restringir qué orígenes pueden usar cámara
  y geolocalización.
