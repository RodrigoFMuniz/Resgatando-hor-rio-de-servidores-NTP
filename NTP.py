import socket, sys, struct, time

#obtendo horário atualizado de servidores remotos

hostname = 'pool.ntp.org'  # Servidor NTP
port = 123
TIME1970 = 2208988800  # 1970-01-01 00:00:00
NTP_QUERY = '\x1b' + 47 * '\0'  # Código para requisição NTP

host = socket.gethostbyname(hostname)  # Obtém IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(NTP_QUERY.encode('ascii'), (host, port))


(buf, addr) = s.recvfrom(1024)

if len(buf) != 48:  # São 12 inteiros: 12 * 4 bytes recebidos
    print("Tamanho errado ", (len(buf), buf))
    sys.exit(1)

secs = struct.unpack("!12I", buf)[10]
secs -= TIME1970
print(time.ctime(int(secs)))