import json
import pika
import time
from pika.exceptions import AMQPConnectionError, ChannelClosedByBroker, StreamLostError
from config import AMQP_URL

RETRY_DELAY = 3
MAX_RETRIES = 10

def safe_json_load(body):
    """Decodifica JSON robusta: non crasha mai."""
    try:
        return json.loads(body.decode("utf-8"))
    except Exception:
        return None

def create_connection():
    """Connessione resiliente con retry."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            params = pika.URLParameters(AMQP_URL)
            return pika.BlockingConnection(params)
        except (AMQPConnectionError, StreamLostError):
            print(f"[ERRORE] Connessione fallita. Tentativo {attempt}/{MAX_RETRIES}. Ritento tra {RETRY_DELAY}s...")
            time.sleep(RETRY_DELAY)
    raise RuntimeError("Impossibile stabilire la connessione con RabbitMQ.")

def declare_queue(channel, name):
    """Creazione queue durable."""
    channel.queue_declare(queue=name, durable=True)