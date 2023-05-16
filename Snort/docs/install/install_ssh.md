# SSH Server & Client #

### Requirements ###

You will require a second machine, so if like me, (you don't):
  --termux on your phone it could probably also work..


## Get Started ##

Let's install "openssh-server" on the current machine and "openssh-client"


### This Machine ###

- Install..

```
sudo apt-get install openssh-server

```

- Check Status

```
sudo systemctl status ssh

```


- FireWall Config

```
sudo ufw allow ssh

sudo ufw enable

sudo ufw status

```

- Enable 

```
sudo systemctl enable ssh --now

```

- Launch


```
sudo systemctl start ssh

```



### Other Machine ###

- Install

```
sudo apt-get install openssh-client

```
- Enable

```
sudo systemctl enable ssh --now

```

- login

```
ssh userName@Your-server-name-IP
    -- or --
ssh ec2-user@ec2-aws-ip-here

```







