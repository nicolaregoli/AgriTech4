import json
import pika
import time
from pika.exceptions import AMQPConnectionError, ChannelClosedByBroker, StreamLostError
from config import AMQP_URLS

RETRY_DELAY = 3
MAX_RETRIES = 10

def safe_json_load(body):
    """Decodifica JSON robusta: non crasha mai."""
    try:
        return json.loads(body.decode("utf-8"))
    except Exception:
        return None

def create_connection(role: str):
    if role not in AMQP_URLS:
        raise ValueError(f"Ruolo non valido: {role}")

    amqp_url = AMQP_URLS[role]

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            params = pika.URLParameters(amqp_url)
            return pika.BlockingConnection(params)
        except (AMQPConnectionError, StreamLostError):
            print(f"[WARN] Connessione fallita ({attempt}/{MAX_RETRIES}). Ritento...")
            time.sleep(RETRY_DELAY)

    raise RuntimeError("Impossibile connettersi a RabbitMQ.")

def declare_queue(channel, name):
    """Creazione queue durable."""
    channel.queue_declare(queue=name, durable=True)