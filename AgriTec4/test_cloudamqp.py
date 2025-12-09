import pika

# Inserisci i tuoi dati CloudAMQP
username = "feezkfaa"       # il tuo username
password = "15Ew5gN3dd-RbscHQ30adNoAK1qSVy_e"       # la password
host = "stingray.rmq.cloudamqp.com"
vhost = "feezkfaa"                 # virtual host

# URL di connessione
#amqp_url = f"amqps://{username}:{password}@{host}/{vhost}"
amqp_url= "amqp://guest:guest@localhost:5672/"
params = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Creiamo una coda di test
channel.queue_declare(queue='test_agri2')

# Inviamo un messaggio di prova
channel.basic_publish(
    exchange='',
    routing_key='test_agri',
    body='Hello from CloudAMQP!'
)

print("Messaggio inviato con successo!")

# Chiudiamo la connessione
connection.close()