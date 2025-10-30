import socket  # Provides low-level networking interface to create TCP/IP connections
import threading  # Enables running multiple threads for handling clients concurrently
import subprocess  # Allows executing system commands like fetching MAC address, uptime
import json  # For converting Python dictionaries to JSON strings and vice versa
from datetime import datetime  # For getting and formatting current date and time

HOST = '0.0.0.0'  # Bind the server to listen on all available network interfaces
PORT = 9999       # The port number the server listens on for client connections

def get_system_info():
    """
    Gathers system information such as MAC address, uptime, and current timestamp.
    """
    try:
        # Run 'cat /sys/class/net/eth0/address' command to get MAC address of Ethernet
        mac_addr_output = subprocess.run(
            ['cat', '/sys/class/net/eth0/address'],
            capture_output=True, text=True, check=True
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        mac_addr_output = "MAC_NOT_FOUND"  # Fallback if command fails

    try:
        # Run 'uptime -p' to get formatted system uptime
        uptime_output = subprocess.run(
            ['uptime', '-p'],
            capture_output=True, text=True, check=True
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        uptime_output = "UPTIME_NOT_FOUND"  # Fallback if command fails

    # Get current date/time in ISO 8601 format
    timestamp = datetime.now().isoformat()

    # Construct a dictionary to hold the info
    info = {
        "device_mac_address": mac_addr_output,
        "timestamp_utc": timestamp,
        "system_uptime": uptime_output
    }
    return info  # Return this dictionary

def handle_client(conn, addr):
    """
    Handles communication with a connected client in a separate thread.
    """
    print(f"[NEW CONNECTION] {addr} connected.")
    with conn:
        while True:
            request = conn.recv(1024).decode('utf-8')  # Receive a request from client
            if not request:
                break  # If no data, client disconnected, exit loop

            print(f"Received request from {addr}: {request}")

            if request == "GET_DATA":
                # If client requests data, get system info, serialize to JSON
                info = get_system_info()
                response = json.dumps(info)
                conn.sendall(response.encode('utf-8'))  # Send JSON response
            else:
                # If unknown request, send error message
                error_msg = "ERROR: Invalid command"
                conn.sendall(error_msg.encode('utf-8'))

    print(f"[CONNECTION CLOSED] {addr} disconnected.")

def start_server():
    """
    Starts the server to accept and handle multiple client connections.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create TCP socket
    server_socket.bind((HOST, PORT))  # Bind socket to host and port
    server_socket.listen()  # Start listening for incoming connections
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    # Infinite loop to accept clients and start a new thread for each
    while True:
        conn, addr = server_socket.accept()  # Accept a client connection
        # Start a new thread with handle_client function for concurrent handling
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()  # Start the server when script runs as main program

