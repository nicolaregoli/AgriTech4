import json
import time
from utils_rabbit import create_connection, declare_queue, safe_json_load

QUEUE_IN = "telemetria.vigneto"
QUEUE_OUT = "comandi.irrigazione"
SOGLIA_UMIDITA = 30.0

def main():
    while True:
        try:
            conn = create_connection()
            ch = conn.channel()

            declare_queue(ch, QUEUE_IN)
            declare_queue(ch, QUEUE_OUT)

            def callback(ch, method, properties, body):
                data = safe_json_load(body)
                if data is None:
                    print("[CTRL] Telemetria non valida, scartata.")
                    ch.basic_ack(method.delivery_tag)
                    return

                print(f"[CTRL] Telemetria ricevuta: {data}")

                # Validazione campi
                if "umidita_suolo" not in data:
                    print("[CTRL] Campo umidita_suolo assente! Ignoro.")
                    ch.basic_ack(method.delivery_tag)
                    return

                umidita = data["umidita_suolo"]

                if umidita < SOGLIA_UMIDITA:
                    cmd = {
                        "azione": "ATTIVA_IRRIGAZIONE",
                        "motivo": f"Umidità {umidita} < {SOGLIA_UMIDITA}",
                        "timestamp": data.get("timestamp"),
                        "vigneto_id": data.get("vigneto_id", "sconosciuto")
                    }

                    payload = json.dumps(cmd)
                    ch.basic_publish(
                        exchange="amq.direct",
                        routing_key=QUEUE_OUT,
                        body=payload,
                        properties=pika.BasicProperties(delivery_mode=2)
                    )
                    print("[CTRL] Comando inviato:", payload)

                ch.basic_ack(method.delivery_tag)

            ch.basic_consume(queue=QUEUE_IN, on_message_callback=callback)
            print("[CTRL] Sistema controllo attivo…")
            ch.start_consuming()

        except Exception as e:
            print("[CTRL] Errore, riavvio…", e)
            time.sleep(3)

if __name__ == "__main__":
    main()