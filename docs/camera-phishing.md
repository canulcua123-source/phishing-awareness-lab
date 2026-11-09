# Análisis: Camera Phishing

## Idea general

El ataque consiste en una página web atractiva (una "sala de reunión", un video en
vivo, una felicitación) que, al cargar, pide al navegador permiso de **cámara** y/o
**ubicación**. Si la víctima acepta, el sitio:

1. Captura imágenes desde la cámara con `getUserMedia()`.
2. Obtiene coordenadas GPS con `navigator.geolocation.getCurrentPosition()`.
3. Registra la IP pública desde el lado del servidor.
4. Envía todo a un backend (en este lab, scripts PHP) que lo guarda.

## Por qué funciona

- El navegador **sí** permite estas APIs a cualquier sitio HTTPS; la barrera es
  únicamente el clic de "Permitir" del usuario.
- Una buena excusa visual (contexto creíble) hace que el usuario conceda el permiso
  sin pensarlo.
- Los túneles tipo Cloudflare/ngrok dan HTTPS gratis y un dominio con apariencia
  "legítima", que es justo lo que las APIs de cámara requieren.

## Flujo observado en el lab

```
Víctima abre enlace  →  página pide permiso cámara/GPS
        ↓ (acepta)
JS captura foto + coords  →  POST al backend  →  se guarda en servidor
```

## Conclusión

La técnica no explota ninguna vulnerabilidad del navegador: explota **a la persona**.
Por eso la defensa es casi 100% de concientización + higiene de permisos. Ver
[`defensa.md`](defensa.md).
