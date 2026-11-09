# Phishing Awareness Lab

Laboratorio personal de aprendizaje sobre ingeniería social y phishing. El objetivo
de este repo **no es atacar**, sino **entender cómo funcionan estas técnicas para
poder defenderse de ellas**. Todo el trabajo se hizo en un entorno controlado y
aislado (contenedor Docker / máquina de laboratorio), contra equipos propios.

> ⚠️ **Uso educativo.** Ejecutar estas técnicas contra personas o sistemas sin
> autorización explícita es ilegal. Este material documenta prácticas realizadas
> sobre mis propios dispositivos, con fines de formación en ciberseguridad.

## Qué estudié aquí

| Tema | Descripción |
|------|-------------|
| Camera phishing | Cómo una página falsa solicita permisos de cámara/ubicación y por qué los navegadores lo permiten |
| Geolocalización por navegador | Cómo se obtiene IP y GPS vía JavaScript y `navigator.geolocation` |
| Reverse shell básica | Modelo cliente/servidor en Python para entender conexiones remotas (puerto 4444) |

## Lo importante: cómo defenderse

Ver [`docs/defensa.md`](docs/defensa.md). Resumen:

- **Permisos del navegador:** nunca concedas cámara/ubicación a sitios que no
  reconoces. Revisa el candado y el dominio real, no el texto de la página.
- **Enlaces acortados / túneles:** desconfía de URLs tipo `*.trycloudflare.com`,
  `*.ngrok.io` que piden permisos. Un servicio legítimo rara vez usa esos dominios.
- **Señales de phishing:** urgencia, premios, "verifica tu identidad", dominios
  parecidos pero no idénticos al original.
- **Defensa de red:** egress filtering y detección de conexiones salientes a
  puertos no estándar (como 4444) ayudan a frenar reverse shells.

## Estructura

```
.
├── README.md
├── docs/
│   ├── camera-phishing.md   # Cómo funciona la técnica (análisis)
│   └── defensa.md           # Mitigaciones y buenas prácticas
└── src/
    ├── servidor.py          # Reverse shell — lado servidor (educativo)
    └── cliente.py           # Reverse shell — lado cliente (educativo)
```

## Nota sobre datos

Este repo **no contiene** capturas, IPs, coordenadas ni datos de ninguna persona.
El `.gitignore` bloquea explícitamente ese tipo de archivos. Solo se publica
código propio y documentación.
