#!/usr/bin/python3

import ldap3
import subprocess

SERVER='172.16.112.139'
BASEDN="DC=ad,DC=teste,DC=local"
USER="guilherme.cunha@ad.teste.local"
CURREENTPWD="Vetorial2022"
NEWPWD="Vetorial2023"

SEARCHFILTER='(&(userPrincipalName='+USER+')(objectClass=person))'
USER_DN=""
USER_CN=""

ldap_server = ldap3.Server(SERVER, get_info=ldap3.ALL)
conn = ldap3.Connection(ldap_server, USER, CURREENTPWD, auto_bind=True)


conn.search(search_base = BASEDN,
         search_filter = SEARCHFILTER,
         search_scope = ldap3.SUBTREE,
         attributes = ['cn', 'givenName', 'userPrincipalName'],
         paged_size = 5)

for entry in conn.response:
    if entry.get("dn") and entry.get("attributes"):
        if entry.get("attributes").get("userPrincipalName"):
            if entry.get("attributes").get("userPrincipalName") == USER:
                USER_DN=entry.get("dn")
                USER_CN=entry.get("attributes").get("cn")
print(USER_DN)
print("Found user:", USER_CN)


subprocess.run(["sh", 
                "changepasswd.sh"])