<h1>Scripts to allow Server Profile Configuration(SCP) using Redfish & Python</h1>

## Configuring NFS Server to keep CONFIG.XML file

<b>Step-1: Configure NFS Server on your Linux System</b>

```
$cat /etc/exports

/var/nfsshare   *(rw,sync,no_root_squash,no_all_squash)
```


Step-2: Start the NFS service

```
$systemctl restart nfs

```

## Install Python 3.6(directly using YUM or through pip)

```
$yum install python3

```

Step-3: Clone this Repository

```
$git clone https://github.com/ajeetraina/redfish

```
Step-4: Open up export_scp.py file and change IP a/c to your infrastrcuture


There are two entries which are shown below:

```
idrac_ip = "100.98.26.37";

share_ip = "100.98.26.42";
```

Modify iDRAC IP and NFS server IP in the above line.


Step-5: Run the script as shown below:

```
$python export_scp.py
```

This will export the System details onto the NFS share. Based on file_name(for example, in my case it is "R730_myxmlSCP.xml" as entry under export_scp.xml) by now, you must have file dumped onto the /var/nfsshare directory).

Using Docker:

```
$sudo docker run -itd -e IDRAC_IP=100.98.26.37 -e NFS_SERVER=100.98.26.42 -e NFS_SERVER_SHARE=/var/nfsshare -e CONFIG_FILE=config.xml ajeetraina/dell_redfish
```



