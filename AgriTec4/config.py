username = "feezkfaa"       # il tuo username
password = "15Ew5gN3dd-RbscHQ30adNoAK1qSVy_e"       # la password
host = "stingray.rmq.cloudamqp.com"
vhost = "feezkfaa"                 # virtual host

#AMQP_URL = f"amqps://{username}:{password}@{host}/{vhost}"  # CloudAMQP
# oppure:
#AMQP_URL = "amqp://producer_user:producer_user@localhost:5672/"  # Docker locale
AMQP_URLS = {
   # "producer": "amqp://producer_user:producer_user@localhost:5672/",
    "producer" : f"amqps://{username}:{password}@{host}/{vhost}" ,
    "monitor":  "amqp://monitor_user:monitor_user@localhost:5672/",
    "control":  "amqp://control_user:control_user@localhost:5672/",
    "actuator": "amqp://actuator_user:actuator_user@localhost:5672/",
}