+++
title = "How to query Windows Vista registry with Samba4 regshell"
date = 2009-10-12T15:15:50+00:00
+++
In this example I list the installed software on the Vista machine from a [Debian](http://www.debian.org) Sid with [samba](http://www.samba.org)4 packages.

I'd to enable (with lusrmsgr.msc) and use the Administrator account.

```shell
% regshell --remote=192.168.50.10 -U Administrateur%castorLapon
HKEY_CLASSES_ROOT> predef HKEY_LOCAL_MACHINE
HKEY_LOCAL_MACHINE> cd SOFTWARE
New path is: HKEY_LOCAL_MACHINE\SOFTWARE
HKEY_LOCAL_MACHINE\SOFTWARE> cd Microsoft
New path is: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft> cd Windows
New path is: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows> cd CurrentVersion
New path is: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion> cd Uninstall
New path is: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall> list
K 7-Zip
K AddressBook
K Adobe Flash Player ActiveX
K Bazaar_is1
K Connection Manager
K DirectDrawEx
K DXM_Runtime
K Fontcore
K IE40
K IE4Data
K IE5BAKEX
K IEData
K Microsoft .NET Framework 3.5 Language Pack SP1 - fra
K Microsoft .NET Framework 3.5 SP1
K MobileOptionPack
K Mozilla Firefox (3.5.3)
K MPlayer2
K OCS Inventory Agent
K PuTTY_is1
K SchedulingAgent
K Vim 7.2
K WIC
K {205C6BDD-7B73-42DE-8505-9A093F35A238}
K {26A24AE4-039D-4CA4-87B4-2F83216016FF}
K {3E31821C-7917-367E-938E-E65FC413EA31}
K {89F4137D-6C26-4A84-BDB8-2E5A4BB71E00}
K {CE2CDD62-0124-36CA-84D3-9F4DCF5C5BD9}
K {CE2CDD62-0124-36CA-84D3-9F4DCF5C5BD9}.KB350003
K {CE2CDD62-0124-36CA-84D3-9F4DCF5C5BD9}.KB953595
K {CE2CDD62-0124-36CA-84D3-9F4DCF5C5BD9}.KB958484
K {CE2CDD62-0124-36CA-84D3-9F4DCF5C5BD9}.KB960043
K {CE2CDD62-0124-36CA-84D3-9F4DCF5C5BD9}.KB963707
K {DCE8CD14-FBF5-4464-B9A4-E18E473546C7}
K {F0E12BBA-AD66-4022-A453-A1C8A0C4D570}
K {F18B31E4-E2E3-4F4F-A2C9-BA579D6AF400}
K {FC857AFE-FC36-3C91-BC17-F8E233C21B4B}
```
