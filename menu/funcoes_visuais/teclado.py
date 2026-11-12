import os
import select   # só em Linux/macOS
import sys
import time

if os.name == "nt":
    import msvcrt
else:
    import select

def esperar(dt):
    """Pausa 'dt' segundos. Devolve True se o utilizador premiu uma tecla."""
    if os.name == "nt":
        fim = time.time() + dt
        while time.time() < fim:
            if msvcrt.kbhit():
                msvcrt.getwch()
                return True
            time.sleep(0.01)
        return False
    pronto, _, _ = select.select([sys.stdin], [], [], dt)
    if pronto:
        sys.stdin.read(1)
        return True
    return False