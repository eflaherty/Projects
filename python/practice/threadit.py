import server
import threading
import time


if '__main__' == __name__:
    s = server.simpleServer()
    t = threading.Thread(target=s.run)

    try:
        print("Starting server - Ctrl-C to stop")
        t.start()

        while True:
            time.sleep(0.25)

    except KeyboardInterrupt:
        print("\nShutting down server....")
        s.stop()
