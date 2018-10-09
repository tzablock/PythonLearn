from ftplib import FTP

ftp = FTP("server_ip_or_domain")
ftp.login(user="username",passwd="password")
ftp.cwd("/exact/dir")

def grapFile():
    filename = "somefile.txt"
    localfile = open(filename,"wb")
    ftp.retrbinary("RETR "+filename,localfile.write, 1024)
    ftp.quit()
    localfile.close()

def placeFile():
    filename = "somefile.txt"
    ftp.storbinary("STOR "+filename,open(filename,"rb"))
    ftp.quit()
