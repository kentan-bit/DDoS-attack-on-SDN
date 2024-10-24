# DDoS_attack_on_SDN
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
Java version: OpenJDK 8 (1.8.0),
ONOS version: 2.0.0, Apache Karaf version: 4.2.2, OpenFlow verions: 1.3
1. Install ONOS and extract the files into /opt/onos
```
$ sudo wget -c https://repo1.maven.org/maven2/org/onosproject/onos-releases/2.0.0/onos-2.0.0.tar.gz
$ sudo tar zxvf onos-2.0.0.tar.gz
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


## DDoS
To simulate a DDoS attack, refer to the DDoS Attack Simulation File.


## Monitoring
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
