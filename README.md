# modulus_hacker
Python script that opens all PEM files in a folder and performs GCD of all the Modulus N of the RSA certificates.

If GCD of any two certificate's N yields something different than 1, then it's one of the prime numbers used by both N.

Store all your collected PEM certificates (with public key) on a directory named 'certs', then run modulus_hacker.py on the same level as certs:

modulus_hacker.py
certs
  |
  --- cert1.pem
  --- cert2.pem
  --- cert3.pem
  ...
  --- certn.pem
