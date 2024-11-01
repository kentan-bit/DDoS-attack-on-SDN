# DDoS Attack on SDN
This project aims to demonstrate a DDoS attack on an SDN. This project serves more on scientific investigation to analyse vulnerabilities of SDN and the impact of cyber-attacks on the network.
This project requires an understanding of OpenFlow, the ONOS controller, the network simulator called Mininet, DDoS penetration testing tools; and using these building blocks to implement a simulator of DDoS attacks against SDNs. 

## Mininet
Mininet version: 2.3.0

1. Install mininet repositories form source
```
$ git clone https://github.com/mininet/mininet
```
2. Install Mininet
```
mininet/util/install.sh -a # to install every dependencies such as Open vSwitch, OpenFlow wireshark and POX.
```
3. Test Mininet after installation
```
sudo mn --switch ovsbr --test pingall
```



## ONOS
Based on [ONOS requirements](https://wiki.onosproject.org/display/ONOS/Requirements) , ONOS requires JAVA 11.
```
$ sudo apt update
$ sudo apt install openjdk-11-jdk
```
Set $JAVA_HOME variable for better performance
```
$ sudo cat >> /etc/environment <<EOL
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
EOL
```
Other software packages that is recommended to be installed includes:
- preffered text editor (gedit, vim, etc.)
- git
- wget
- net-tools

1. Install ONOS and extract the files into /opt/onos
```
$ sudo wget -c https://repo1.maven.org/maven2/org/onosproject/onos-releases/2.7.0/onos-2.7.0.tar.gz
$ sudo tar zxvf onos-2.7.0.tar.gz
```
2. Run ONOS services
```
$ cd /opt/onos/bin
$ sudo /opt/onos/bin/onos-service start
```
3. Configure ssh in another terminal
```
$ mkdir ~/.ssh # if it doesn't exist
$ vim ~/.ssh/config
```
```
HostKeyAlgorithms +ssh-rsa
PubkeyAcceptedKeyTypes +ssh-rsa
```
3. Enter ONOS CLI terminal and activate application
```
$ /opt/onos/bin/onos -l onos
password: rocks

onos> app activate org.onosproject.pipelines.basic
onos> app activate org.onosproject.fwd
onos> app activate org.onosproject.openflow
```

4. Open web browser to log in into GUI
http://localhost:8181/onos/ui
```
username: onos 
password: rocks
```

## Run Mininet with ONOS as Controller
```
$ sudo mn --controller remote,ip=<host ip address> --switch ovs,protocols=OpenFlow14 --custom /path/to/DDoS-attack-on-SDN/sdn_topology.py --topo=project --link tc

mininet> pingall 
```

To properly stop the ONOS service, use this command to avoid complications in the next service run
```
sudo /opt/onos/bin/onos-service stop
```

## DDoS
### DDoS Attack Using hping3 Tool
To simulate a DDoS attack, refer to the DDoS Attack Simulation File.

### DDoS Attack Using Python Script
This script uses [Scapy](https://scapy.readthedocs.io/en/latest/introduction.html), which is a packet manipulation library written in Python. It was originally developed by [brian404](https://scapy.readthedocs.io/en/latest/introduction.html), which initially demonstrates a SYN flood DDoS attack tool to send high volume of SYN packets to a target server. We made some changes in the script to send higher payload and spoof source IP addresses.

To simulate DDoS attack on the SDN, we chose a host to act as server - in this case is h20(IP:10.0.0.20) - and three hosts to act botnet to launch the DDoS script.

1. Open host terminals from mininet CLI
```
mininet> xterm h1 h8 h15
```

2. Launch DDoS attack script with desired parameters towards the targer server in each host terminals. Make sure to use the correct path where the ddos.py script resides in.
```
$ python3 ddos.py 10.0.0.20
```
Usage: python3 ddos.py <target IP|link>
* ```<--port>``` : Specify port number to send the attack packets to. Default is 80
* ```<--threads>``` : Specify the number of threads for the attack
* ```<--method>``` : Either ```scapy``` or ```socket``` to choose the attack method. Default is scapy.

In this case, we are using scapy method to generate the manipulated packets.

## Data Collection
Tools used for monitoring: Sflow-rt, iperf3, Wireshark

1. Sflow-rt
   * Install sflow-rt from source
   ```
   $ sudo wget https://inmon.com/products/sFlow-RT/sflow-rt.tar.gz
   $ tar -xvzf sflow-rt.tar.gz
   ```
   * Install application and start sflow service
   ```
   $ ./sflow-rt/get-app.sh sflow-rt browse-metrics
   $ ./sflow-rt/get-app.sh sflow-rt browse-metrics
   $ ./sflow-rt/get-app.sh sflow-rt mininet-dashboard
   $ ./sflow-rt/start.sh
   ```
   * Open sflow web GUI http://localhost:8008/html
     
2. iperf3
   * Install iperf3
   ```
   $ sudo apt install -y iperf3
   ```
     
3. Wireshark
   * Check if Wireshark has been installed locally. If not, install Wireshark using the following command:
   ```
   $ sudo apt install wireshark
   ```
