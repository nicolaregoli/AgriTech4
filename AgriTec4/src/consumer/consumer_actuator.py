import json
import time
import pika
from src.common.utils_rabbit import create_connection, safe_json_load

QUEUE = "comandi.irrigazione"

def main():
    while True:
        try:
            conn = create_connection("actuator")
            ch = conn.channel()
       
            def callback(ch, method, properties, body):
                data = safe_json_load(body)
                if data is None:
                    print("[ATTUATORE COMANDI] Messaggio comando non valido, scartato.")
                    ch.basic_ack(method.delivery_tag)
                    return

                print("[ATTUATORE COMANDI] Esecuzione comando:", data)
                # simulazione attuatore per esecuzione di comandi
                time.sleep(1)
                print("[ATTUATORE COMANDI] Comando completato.")

                ch.basic_ack(method.delivery_tag)

            ch.basic_consume(queue=QUEUE, on_message_callback=callback)
            print("[ATTUATORE COMANDI] In ascolto…")
            ch.start_consuming()

        except Exception as e:
            print("[ATTUATORE COMANDI] Errore, riavvio…", e)
            time.sleep(3)

if __name__ == "__main__":
    main()