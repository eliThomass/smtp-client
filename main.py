from socket import *

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

sender = '23thomasec@csu.fullerton.edu'
receiever = 'ecthomas05@gmail.com'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

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
rcpttoCommand = f'RCPT TO:<{receiever}>\r\n'
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
subject = 'Subject: ' + input('Subject: ') + '\r\n'
receiver_ = 'To: <' + input('To: ') + '>\r\n'
sender_ = 'From: <' + input('From: ') + '>\r\n'

email = subject + receiver_ + sender_ + msg
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
