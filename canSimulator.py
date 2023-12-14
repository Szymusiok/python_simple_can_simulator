import time
from collections import deque
import random

distance_meters = 0  # Initial distance in meters


# Enumeration for CAN message types
class MessageType:
    ODOMETER = "Odometr"
    DOOR_OPEN = "Opening the doors"
    STOP_BUTTON = "STOP button"
    DOOR_CLOSE = "Closing the door"


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

        if random_number < 0.9:
            message_type = MessageType.ODOMETER
            message_id = random.randint(0x100, 0x110)
            message_data = [random.randint(0, 255) * 2 for _ in range(8)]
            yield CANMessage(message_id, message_data, message_type)

        elif random_number < 1:
            message_type = MessageType.STOP_BUTTON
            message_id = random.randint(0x200, 0x210)
            message_data = [random.randint(0, 255) * 2 for _ in range(8)]
            yield CANMessage(message_id, message_data, message_type)


def send_door_open_message():
    message_id = random.randint(0x300, 0x310)
    message_data = [random.randint(0, 255) * 2 for _ in range(8)]
    message = CANMessage(message_id, message_data, MessageType.DOOR_OPEN)
    message_queue.append(message)


def send_door_close_message():
    message_id = random.randint(0x400, 0x410)
    message_data = [random.randint(0, 255) * 2 for _ in range(8)]
    message = CANMessage(message_id, message_data, MessageType.DOOR_CLOSE)
    message_queue.append(message)


# Queue to store messages
message_queue = deque(maxlen=10)


# Sending a random message to the queue
def send_random_message():
    message = next(message_generator)
    message_queue.append(message)


# Retrieving a single message from the queue
def receive_message():
    if message_queue:
        received_message = message_queue.popleft()
        return received_message
    else:
        print("No messages in the receive queue")
        return None


# Function to handle messages
def handle_message(message):
    global distance_meters

    if message.message_type == MessageType.STOP_BUTTON:
        return "The stop button has been pressed. Stop."
    elif message.message_type == MessageType.DOOR_OPEN:
        return "The doors were opened."
    elif message.message_type == MessageType.DOOR_CLOSE:
        if random.random() < 0.9:
            return "The doors were closed."
        else:
            return "The doors were not closed properly."
    elif message.message_type == MessageType.ODOMETER:
        distance_meters += random.randint(100, 500)
        distance_km = distance_meters / 1000
        return f"Distance traveled: {distance_km:.2f} km"
    else:
        return "Incorrect message type."


message_generator = generate_can_messages()
