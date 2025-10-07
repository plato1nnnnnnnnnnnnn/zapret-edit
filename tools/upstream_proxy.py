import socket
import threading

# Extremely small upstream proxy stub that accepts CONNECT and GET, logs the request,
# and for CONNECT simply responds with 200 (so downstream sees a connection established),
# for GET — performs a simple HTTP fetch and returns the response.

import select
import sys

HOST = '127.0.0.1'
PORT = 3128

BUFFER = 8192

import urllib.request


def handle_client(conn, addr):
    try:
        data = conn.recv(BUFFER)
        if not data:
            conn.close()
            return
        line = data.split(b"\r\n", 1)[0].decode(errors='ignore')
        print(f"[upstream] Received: {line}")
        if line.startswith('CONNECT'):
            # respond as if successful
            conn.sendall(b"HTTP/1.1 200 Connection established\r\n\r\n")
            # then just relay nothing — keep socket open a bit
            try:
                while True:
                    r, w, x = select.select([conn], [], [], 0.5)
                    if r:
                        d = conn.recv(BUFFER)
                        if not d:
                            break
                        # discard/echo
                        print(f"[upstream] Tunnel data len={len(d)}")
            except Exception:
                pass
        else:
            # naive HTTP GET handling
            try:
                req = data.decode(errors='ignore')
                first_line = req.splitlines()[0]
                parts = first_line.split()
                if len(parts) >= 2 and parts[0] == 'GET':
                    url = parts[1]
                    print(f"[upstream] GET for URL: {url}")
                    try:
                        resp = urllib.request.urlopen(url, timeout=5)
                        body = resp.read()
                        headers = resp.getheaders()
                        status = resp.getcode()
                        status_line = f"HTTP/1.1 {status} OK\r\n"
                        conn.sendall(status_line.encode())
                        for k, v in headers:
                            conn.sendall(f"{k}: {v}\r\n".encode())
                        conn.sendall(b"\r\n")
                        conn.sendall(body)
                    except Exception as e:
                        msg = f"HTTP/1.1 502 Bad Gateway\r\nContent-Length: 0\r\n\r\n"
                        conn.sendall(msg.encode())
                else:
                    conn.sendall(b"HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n")
            except Exception as e:
                conn.sendall(b"HTTP/1.1 500 Internal Server Error\r\nContent-Length: 0\r\n\r\n")
    except Exception as e:
        print(f"[upstream] handler error: {e}")
    finally:
        try:
            conn.close()
        except Exception:
            pass


def serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"[upstream] Listening on {HOST}:{PORT}")
    try:
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            t.start()
    except KeyboardInterrupt:
        s.close()

if __name__ == '__main__':
    serve()
