import socket
import time
import json


# --- TODO: Configure these values --- #
SERVER_IP = '192.168.127.10'  # The IP address of your RDK-X5
SERVER_PORT = 9999
REQUEST_MESSAGE = "GET_DATA"  # The message your server expects
# --- END OF TODO --- #


def run_client():
    while True:
        print("-" * 30)
        print(f"Attempting to connect to {SERVER_IP}:{SERVER_PORT}...")
        try:
            # 1. Create and use a socket object
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                # 2. Connect to the server
                sock.connect((SERVER_IP, SERVER_PORT))
                print("Connected to the server.")

                # 3. Send the request message
                sock.sendall(REQUEST_MESSAGE.encode('utf-8'))

                # 4. Receive the response (up to 4096 bytes)
                response = sock.recv(4096).decode('utf-8')

                # 5. Parse the JSON response into a dictionary
                data = json.loads(response)

                # 6. Print the received data in a friendly format
                print("Received data from server:")
                for key, value in data.items():
                    print(f"  {key}: {value}")

        except ConnectionRefusedError:
            print("Connection failed. Is the server running?")
        except json.JSONDecodeError:
            print("Failed to decode JSON from server response.")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for 60 seconds before the next request
        print("\nWaiting for 60 seconds...")
        time.sleep(60)


if __name__ == "__main__":
    run_client()

