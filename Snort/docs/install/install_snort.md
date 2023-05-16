# Install Snort on Kali (2023) # 

## Issues ##
 ! Note: 
  snort is no longer available in Kali repositories
 !
  Here are the steps to install snort on Kali:


Step 1) 
-Backup kali's sources.list

```
mv /etc/apt/sources.list /etc/apt/sources.list.bak

```

Step 2)
-Remove updates

```
find /var/lib/apt/lists -type f -exec rm {} \;

```

Step 3)
-Change sources.list content

```
sudo nano /etc/apt/sources.list

```

Step 4)
{If Kali is install on your machine}


Paste content given below

```
deb http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-backports main restricted universe multiverse
deb http://archive.canonical.com/ubuntu focal partner
deb-src http://archive.canonical.com/ubuntu focal partner

```

{If you are using a VM and do not have the ARM repositories in your repo}

```
deb [arch=arm64] http://ports.ubuntu.com/ubuntu-ports focal main restricted universe multiverse
deb [arch=arm64] http://ports.ubuntu.com/ubuntu-ports focal-updates main restricted universe multiverse
deb [arch=arm64] http://ports.ubuntu.com/ubuntu-ports focal-security main restricted universe multiverse
deb [arch=i386,amd64] http://us.archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse
deb [arch=i386,amd64] http://us.archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse
deb [arch=i386,amd64] http://security.ubuntu.com/ubuntu focal-security main restricted universe multiverse

```


Step 5)
-Add the specified public keys 

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 871920D1991BC93C

```

Step 6)
-Update (But, Don't ```upgrade```)

```
sudo apt update

```


Step 7)
-Finally, Install SNORT

```
sudo apt install snort

```
^ This might take a bt of time..


### Disclosure ###

The point in time by which I am typing this, 
I have yet to revert the 'apt files'
and have no idea the reprocutions of these actions.. LoL/KeK


But, to undo the apt list.. 

```

sudo mv /etc/apt/sources.list.bak /etc/apt/sources.list


``` 
 
