import json
import time
from utils_rabbit import create_connection, declare_queue, safe_json_load

QUEUE = "comandi.irrigazione"

def main():
    while True:
        try:
            conn = create_connection()
            ch = conn.channel()
            declare_queue(ch, QUEUE)

            def callback(ch, method, properties, body):
                data = safe_json_load(body)
                if data is None:
                    print("[ATTUATORE] Messaggio comando non valido, scartato.")
                    ch.basic_ack(method.delivery_tag)
                    return

                print("[ATTUATORE] Esecuzione comando:", data)
                # simulazione attuatore
                time.sleep(1)
                print("[ATTUATORE] Comando completato.")

                ch.basic_ack(method.delivery_tag)

            ch.basic_consume(queue=QUEUE, on_message_callback=callback)
            print("[ATTUATORE] In ascolto…")
            ch.start_consuming()

        except Exception as e:
            print("[ATTUATORE] Errore, riavvio…", e)
            time.sleep(3)

if __name__ == "__main__":
    main()