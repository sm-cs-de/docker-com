import time
from multiprocessing import shared_memory

shm = shared_memory.SharedMemory(name="ipc_shm", create=True, size=20) # shared memory block of 20 bytes

# to avoid that shm isn't closed/unlinked properly when the container stopped (bevor cleanup happens)
try:
    data = b"Hello from Writer"
    shm.buf[:len(data)] = data
    print("Writer:", data.decode())

    print("Writer waits for some time..")
    time.sleep(30)
finally:
    shm.close()
    shm.unlink()
    del shm        # release reference
    print("Writer cleaned up")