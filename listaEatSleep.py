import threading
import time
import random

mutex = threading.Lock()

barber_sleeping = True
customer_waiting = False

def barber():
    global barber_sleeping, customer_waiting
    while True:
        with mutex:
            if customer_waiting:
                barber_sleeping = False
                print("Barbeiro está acordando e cortando o cabelo do cliente.")
                customer_waiting = False
                time.sleep(random.uniform(1, 3))
                print("Barbeiro terminou de cortar o cabelo do cliente.")
                barber_sleeping = True
            else:
                print("Barbeiro está dormindo.")
        time.sleep(random.uniform(1, 3))

def customer():
    global barber_sleeping, customer_waiting
    while True:
        with mutex:
            if not barber_sleeping:
                print("Cliente está esperando o barbeiro cortar o cabelo.")
                customer_waiting = True
                barber_sleeping = True
            else:
                print("Cliente está cortando o cabelo sozinho.")
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    barber_thread = threading.Thread(target=barber)
    customer_thread = threading.Thread(target=customer)

    barber_thread.start()
    customer_thread.start()

    barber_thread.join()
    customer_thread.join()
