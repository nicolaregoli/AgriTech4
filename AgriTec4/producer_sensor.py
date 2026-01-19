import json, time, random
from datetime import datetime, timezone
import pika
from utils_rabbit import create_connection, declare_queue

QUEUE = "telemetria.vigneto"

def generate_data():
    return {
        "vigneto_id": "gubbio_semonte_01",
        "umidita_suolo": round(random.uniform(15, 55), 2),
        "temperatura_aria": round(random.uniform(8, 32), 2),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

def main():
    while True:
        try:
            conn = create_connection("producer")
            ch = conn.channel()
            #declare_queue(ch, QUEUE)

            print("[PRODUCER] Avvio invio dati sensori...")
            while True:
                payload = json.dumps(generate_data())
                ch.basic_publish(
                    exchange="amq.direct",
                    routing_key=QUEUE,
                    body=payload,
                    properties=pika.BasicProperties(delivery_mode=2)
                )
                print(f"[PRODUCER] Inviato: {payload}")
                time.sleep(5)

        except Exception as e:
            print("[PRODUCER] Errore, riavvio…", e)
            time.sleep(3)

if __name__ == "__main__":
    main()