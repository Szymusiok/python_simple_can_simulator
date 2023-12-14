# python_simple_can_simulator
A highly simplified CAN interface simulator with 3 types of messages

## Functions description
```
# Enumeration for CAN message types
class MessageType:
    ODOMETER = "Odometr"
    DOOR_OPEN = "Opening the doors"
    STOP_BUTTON = "STOP button"
```
```
# A class that simulates a CAN message
class CANMessage:
    def __init__(self, id, data, message_type):
        self.id = id
        self.data = data
        self.message_type = message_type
```
### !!! When there are more than 10 messages in the queue - the oldest ones are deleted !!!

### send_random_message
  use by: ``` send_random_message() ```
  Generates a random CAN message from a possible 3 types: ODOMETR, DOOR_OPEN, STOP_BUTTON and adds it to the queue.

### receive_message
  use by: ``` received_message = receive_message() ```
  Takes the first message from the queue and returns it

### handle_message
  use by: ``` text = handle_message(received_message) ```
  Returns special text depending on the type of message
  

## Example usage
```
from canSimulator import handle_message, receive_message, send_random_message

for _ in range(5):
    send_random_message()

for _ in range (5):
    received_message = receive_message()
    if received_message:
        print(f"Received CAN message - Type: {received_message.message_type}, ID: {received_message.id}, Data: {received_message.data}")
        tekst = handle_message(received_message)
        print(tekst)
```



