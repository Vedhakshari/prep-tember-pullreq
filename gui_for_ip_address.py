import socket
import uuid

# Function to get the IP address of the user's computer
def get_ip_address():
    try:
        # Create a socket object
        ip_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Connect to a remote server (doesn't need to be reachable)
        ip_socket.connect(("8.8.8.8", 80))
        
        # Get the local IP address
        ip_address = ip_socket.getsockname()[0]
        
        # Close the socket
        ip_socket.close()
        
        return ip_address
    except Exception as e:
        return "Unable to get IP address"

# Function to get the MAC address of the user's computer
def get_mac_address():
    try:
        # Get the MAC address using uuid library
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        
        # Format the MAC address with colons
        formatted_mac = ":".join([mac[e:e+2] for e in range(0, 11, 2)])
        
        return formatted_mac
    except Exception as e:
        return "Unable to get MAC address"

# Main program
if _name_ == "_main_":
    # Get and print the IP address
    ip_address = get_ip_address()
    print("IP Address:", ip_address)
    
    # Get and print the MAC address
    mac_address = get_mac_address()
    print("MAC Address:", mac_address)
