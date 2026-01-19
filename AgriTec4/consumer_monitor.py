import json
import time
from utils_rabbit import create_connection, declare_queue, safe_json_load

QUEUE = "telemetria.vigneto"

def process_data(data):
    print(f"[MONITOR] Dato valido: {data}")

    with open("latest.json", "w") as f:
        json.dump(data, f)

def main():
    while True:
        try:
            conn = create_connection("monitor")
            ch = conn.channel()
           # declare_queue(ch, QUEUE)

            def callback(ch, method, properties, body):
                data = safe_json_load(body)
                if data is None:
                    print("[MONITOR] Messaggio malformato, scartato:", body.decode(errors="ignore"))
                    ch.basic_ack(method.delivery_tag)
                    return

                process_data(data)
                ch.basic_ack(method.delivery_tag)

            ch.basic_consume(queue=QUEUE, on_message_callback=callback)
            print("[MONITOR] In ascolto…")
            ch.start_consuming()

        except Exception as e:
            print("[MONITOR] Errore, riavvio…", e)
            time.sleep(3)

if __name__ == "__main__":
    main()