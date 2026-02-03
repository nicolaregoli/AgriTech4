username = "feezkfaa"       #username
password = "15Ew5gN3dd-RbscHQ30adNoAK1qSVy_e"       # la password
host = "stingray.rmq.cloudamqp.com" #host
vhost = "feezkfaa"     # virtual host


#Docker locale
AMQP_URLS = {
    "producer": f"amqp://producer_user:producer_user@localhost:5672/",
    "monitor":  f"amqp://monitor_user:monitor_user@localhost:5672/",
    "control":  f"amqp://control_user:control_user@localhost:5672/",
    "actuator": f"amqp://actuator_user:actuator_user@localhost:5672/",
}
 # CloudAMQP
AMQPS_URLS = {
    "producer": f"amqps://{username}:{password}@{host}/{vhost}",
    "monitor":  f"amqps://{username}:{password}@{host}/{vhost}",
    "control":  f"amqps://{username}:{password}@{host}/{vhost}",
    "actuator": f"amqps://{username}:{password}@{host}/{vhost}",
}