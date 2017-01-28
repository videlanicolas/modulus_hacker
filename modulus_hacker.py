#!/usr/bin/python3
import OpenSSL, Crypto.PublicKey.RSA
from fractions import gcd
from glob import glob

def extract_n(cert):
	pubkey = OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM,OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert).get_pubkey())
	return Crypto.PublicKey.RSA.importKey(pubkey).n

certs = glob("certs/*.pem")
print("There are {0} certificates.".format(str(len(certs))))
print("Searching...")
_certs = certs
for cert in certs:
	_certs.remove(cert)
	with open(cert) as f:
		cert_x509 = f.read()
	print("Certificate: " + cert)
	for _cert in _certs:
		with open(_cert) as f:
			_cert_x509 = f.read()
		if gcd(extract_n(cert_x509),extract_n(_cert_x509)) != 1:
			print("These two certificates used the same prime number!\n{0} {1}\nCommon prime: {2}".format(cert,_cert,gcd(extract_n(cert_x509),extract_n(_cert_x509))))
			with open("result.txt",'a') as f:
				f.write("{0} {1} {2}\n".format(cert,_cert,gcd(extract_n(cert_x509),extract_n(_cert_x509))))
print("End.")
