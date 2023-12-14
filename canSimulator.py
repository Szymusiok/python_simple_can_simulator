import time
from collections import deque
import random

distance_meters = 0  # Initial distance in meters

# Enumeration for CAN message types
class MessageType:
    ODOMETER = "Odometr"
    DOOR_OPEN = "Opening the doors"
    STOP_BUTTON = "STOP button"


# A class that simulates a CAN message
class CANMessage:
    def __init__(self, id, data, message_type):
        self.id = id
        self.data = data
        self.message_type = message_type


# Generator for CAN messages with different probabilities
def generate_can_messages():
    while True:
        random_number = random.random()

        if random_number < 0.7:
            message_type = MessageType.ODOMETER
            message_id = random.randint(0x100, 0x110)
            message_data = [random.randint(0, 255) * 2 for _ in range(8)]

        elif random_number < 0.9:
            message_type = MessageType.STOP_BUTTON
            message_id = random.randint(0x200, 0x210)
            message_data = [random.randint(0, 255) * 2 for _ in range(8)]

        else:
            message_type = MessageType.DOOR_OPEN
            message_id = random.randint(0x300, 0x310)
            message_data = [random.randint(0, 255) * 2 for _ in range(8)]

        yield CANMessage(message_id, message_data, message_type)
        time.sleep(1)


# Queue to store messages
message_queue = deque(maxlen=10)


# Sending a random message to the queue
def send_random_message():
    message = next(message_generator)
    message_queue.append(message)
    print(f"Sent CAN message - Type: {message.message_type}, ID: {message.id}, Data: {message.data}")


# Retrieving a single message from the queue
def receive_message():
    if message_queue:
        received_message = message_queue.popleft()
        print(
            f"Received CAN message - Type: {received_message.message_type}, ID: {received_message.id}, Data: {received_message.data}")
        return received_message
    else:
        print("No messages in the receive queue")
        return None


# Function to handle messages
def handle_message(message):
    global distance_meters

    if message.message_type == MessageType.STOP_BUTTON:
        if random.random() < 0.1:
            return "The stop button has been pressed. Stop."
        else:
            return "The stop button was pressed, but ignored."
    elif message.message_type == MessageType.DOOR_OPEN:
        if random.random() < 0.5:
            return "The doors were opened."
        else:
            return "The doors were not opened."
    elif message.message_type == MessageType.ODOMETER:
        distance_meters += random.randint(100, 500)
        distance_km = distance_meters / 1000
        return f"Distance traveled: {distance_km:.2f} km"
    else:
        return "Incorrect message type."

message_generator = generate_can_messages()
