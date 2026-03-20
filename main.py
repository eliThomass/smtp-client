from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com' #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
port = 587 # TLS Port
clientSocket.connect((mailserver, port))
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

receiver = 'e07642704@gmail.com'
sender = 'ecthomas05@gmail.com'
password = input('Enter Google App Password: ')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# ----- Optional 1 (TLS/SSL) ----

# Request STARTTLS from the server
starttlsCommand = 'STARTTLS\r\n'
clientSocket.send(starttlsCommand.encode())
recv_tls = clientSocket.recv(1024).decode()
print(recv_tls)
if recv_tls[:3] != '220':
    print('220 reply not received from server for STARTTLS.')

# Secure the socket using TLS/SSL
context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname=mailserver)

# Send HELO again over the secure connection
clientSocket.send(heloCommand.encode())
recv_helo = clientSocket.recv(1024).decode()
print(recv_helo)

# Send AUTH LOGIN command
clientSocket.send('AUTH LOGIN\r\n'.encode())
recv_auth = clientSocket.recv(1024).decode()
print(recv_auth)

# Send Base64 encoded username
username_b64 = base64.b64encode(sender.encode()).decode() + '\r\n'
clientSocket.send(username_b64.encode())
recv_user = clientSocket.recv(1024).decode()
print(recv_user)

# Send Base64 encoded password
password_b64 = base64.b64encode(password.encode()).decode() + '\r\n'
clientSocket.send(password_b64.encode())
recv_pass = clientSocket.recv(1024).decode()
print(recv_pass)
if recv_pass[:3] != '235':
    print('235 Authentication failed. Check your App Password.')
    raise Exception('Incorrect Password')

# ----- End of Optional 1 -------

# Send MAIL FROM command and print server response.
# Fill in start
mailfromCommand = f'MAIL FROM:<{sender}>\r\n'
clientSocket.send(mailfromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
if recv2[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcpttoCommand = f'RCPT TO:<{receiver}>\r\n'
clientSocket.send(rcpttoCommand.encode())
recv3 = clientSocket.recv(1024).decode()
if recv3[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
if recv4[:3] != '354':
    print('354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
subject_input = input('Subject: ')

# Converted image to base64 
with open('image.jpg', 'rb') as f:
    img_b64 = base64.b64encode(f.read()).decode()

# MIME email for image support for Optional 2
email = (
    f'Subject: {subject_input}\r\n'
    f'To: {receiver}\r\n'
    f'From: {sender}\r\n'
    f'MIME-Version: 1.0\r\n'
    f'Content-Type: multipart/mixed; boundary="B"\r\n\r\n'
    f'--B\r\n'
    f'Content-Type: text/plain\r\n\r\n'
    f'{msg}\r\n\r\n'
    f'--B\r\n'
    f'Content-Type: image/jpeg; name="image.jpg"\r\n'
    f'Content-Transfer-Encoding: base64\r\n'
    f'Content-Disposition: attachment; filename="image.jpg"\r\n\r\n'
    f'{img_b64}\r\n\r\n'
    f'--B--\r\n'
)

clientSocket.send(email.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv6 = clientSocket.recv(1024).decode()
if recv6[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quit_ = 'QUIT\r\n'
clientSocket.send(quit_.encode())
recv7 = clientSocket.recv(1024).decode()
if recv7[:3] != '221':
    print('221 reply not received from server.')
clientSocket.close()
# Fill in end
