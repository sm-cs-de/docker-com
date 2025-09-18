import time
from multiprocessing import shared_memory

time.sleep(2)                                           # Wait some time for writer
shm = shared_memory.SharedMemory(name="ipc_shm")        # Attach to shm

data = bytes(shm.buf[:20]).rstrip(b"\x00")              # Read first 20 bytes
print("Reader:", data.decode())

shm.close()
