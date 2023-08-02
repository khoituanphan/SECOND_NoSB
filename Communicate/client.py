import requests

def start_client():
    server_host = 'https://6690-2402-800-61b1-c632-947f-1569-9696-7ce1.ngrok-free.app'  # Replace with the ngrok HTTPS tunnel URL

    while True:
        message = input("You: ")
        if not message:
            print("Connection closed.")
            break

        # Send the message to the server using HTTPS
        response = requests.post(server_host, data=message, verify=False)  # Use verify=False to ignore SSL certificate verification
        print("Server:", response.text)

if __name__ == "__main__":
    start_client()
