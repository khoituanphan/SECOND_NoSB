import requests
import os
import time

def create_chat_history_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            pass

def start_server():
    server_host = 'https://6690-2402-800-61b1-c632-947f-1569-9696-7ce1.ngrok-free.app'  # Replace with the ngrok HTTPS tunnel URL

    working_directory = '/path/to/desired/directory'
    os.chdir(working_directory)

    chat_history_file = "chat_history_server.txt"
    create_chat_history_file(chat_history_file)

    while True:
        data = input("You: ")
        if not data:
            print("Connection closed by the client.")
            break
        print("Client:", data)

        # Save the chat message to the file with a timestamp
        message_with_timestamp = "Client: " + data + " (" + time.strftime("%Y-%m-%d %H:%M:%S") + ")\n"
        with open(chat_history_file, "a") as file:
            file.write(message_with_timestamp)

        # Send the response to the client using HTTPS
        response = input("You: ")
        requests.post(server_host, data=response, verify=False)  # Use verify=False to ignore SSL certificate verification

if __name__ == "__main__":
    try:
        import time
        start_server()
    except Exception as e:
        print("Error:", e)
    input("Press Enter to exit...")  # Add this line to keep the console window open for debugging
