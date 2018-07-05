#[virtualenv] Create enviroment

virtualenv -p python3 ImageSearch

#[virtualenv] Activate the env

source bin/activate

#[virtualenv] Deactivate the env

deactivate

#[Start Service]
nameko run service --broker amqp://rabbitmq:rabbitmq@localhost