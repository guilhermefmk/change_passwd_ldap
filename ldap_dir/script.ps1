param($user, $senha)
Start-Process powershell -Verb runAss
Import-Module ActiveDirectory
$Pass = ConvertTo-SecureString $senha -AsPlainText -Force
Set-ADAccountPassword -Identity $user -NewPassword $pass 
exit
