"""
besmarts.worker
"""

import sys
import os

from besmarts.core import compute

if __name__ == "__main__":
    ip = '127.0.0.1'
    pt = 55555
    processes = 14
    queue_size = 1
    if len(sys.argv) > 1:
        ip = sys.argv[1]
    if len(sys.argv) > 2:
        pt = int(sys.argv[2])
    if len(sys.argv) > 3:
        processes=int(sys.argv[3])
    if len(sys.argv) > 4:
        queue_size=int(sys.argv[4])

    try:
        compute.compute_remote(ip, pt, processes=processes, queue_size=queue_size)
        print("Exiting normally.")
        sys.exit(0)
    except EOFError:
        sys.exit("Disconnected")
    except ConnectionRefusedError:
        sys.exit("Connection refused.")
    finally:
        os._exit(0)
