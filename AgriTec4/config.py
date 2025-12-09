username = "feezkfaa"       # il tuo username
password = "15Ew5gN3dd-RbscHQ30adNoAK1qSVy_e"       # la password
host = "stingray.rmq.cloudamqp.com"
vhost = "feezkfaa"                 # virtual host

AMQP_URL = f"amqps://{username}:{password}@{host}/{vhost}"  # CloudAMQP
# oppure:
#AMQP_URL = "amqp://{username}:{password}@{host}:5672/"  # Docker locale