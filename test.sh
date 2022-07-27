#!/bin/sh
# user = $1
# senha = $2


sshpass -p Vetorial20 ssh -o ServerAliveInterval=3 -o ServerAliveCountMax=2 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null administrator@172.16.112.139 "powershell"
sshpass -p Vetorial20 ssh -o ServerAliveInterval=3 -o ServerAliveCountMax=2 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null administrator@172.16.112.139 "Import-Module ActiveDirectory"
sshpass -p Vetorial20 ssh -o ServerAliveInterval=3 -o ServerAliveCountMax=2 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null administrator@172.16.112.139 "Get-ADUser -Filter * -SearchScope Subtree –SearchBase “CN=Guilherme Cunha,OU=Vetorial,DC=ad,DC=teste,DC=local” | Ft Name,sAMAccountName"
sshpass -p Vetorial20 ssh -o ServerAliveInterval=3 -o ServerAliveCountMax=2 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null administrator@172.16.112.139 "Exit"
