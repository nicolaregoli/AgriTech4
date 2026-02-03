import json
import time
import pika
from src.common.utils_rabbit import create_connection, safe_json_load

QUEUE_IN = "telemetria.vigneto"
QUEUE_OUT = "comandi.irrigazione"
SOGLIA_UMIDITA = 30.0

def main():
    while True:
        try:
            conn = create_connection("control")
            ch = conn.channel()

            def callback(ch, method, properties, body):
                data = safe_json_load(body)
                if data is None:
                    print("[CONTROL] Dato Telemetria non valido.")
                    ch.basic_ack(method.delivery_tag)
                    return

                print(f"[CONTROL] Dato Telemetria ricevuto: {data}")

                # Validazione campi
                if "umidita_suolo" not in data:
                    print("[CONTROL] Campo umidita_suolo assente! Ignoro.")
                    ch.basic_ack(method.delivery_tag)
                    return

                umidita = data["umidita_suolo"]

                if umidita < SOGLIA_UMIDITA:
                    cmd = {
                        "azione": "ATTIVA_IRRIGAZIONE",
                        "motivo": f"Umidità {umidita} < {SOGLIA_UMIDITA}",
                        "timestamp": data.get("timestamp"),
                        "vigneto_id": data.get("vigneto_id")
                    }

                    payload = json.dumps(cmd)
                    ch.basic_publish(
                        exchange="amq.direct",
                        routing_key=QUEUE_OUT,
                        body=payload,
                        properties=pika.BasicProperties(delivery_mode=2)
                    )
                    print("[CONTROL] Comando inviato:", payload)

                ch.basic_ack(method.delivery_tag)

            ch.basic_consume(queue=QUEUE_IN, on_message_callback=callback)
            print("[CONTROL] Sistema controllo attivo…")
            ch.start_consuming()

        except Exception as e:
            print("[CONTROL] Errore, riavvio…", e)
            time.sleep(3)

if __name__ == "__main__":
    main()