## Feodo Tracker   
  https://feodotracker.abuse.ch/blocklist/

### Overview
 Feodo (also known as Cridex or Bugat) is a Trojan used to commit ebanking fraud and steal sensitive information from the victims computer, such as credit card details or credentials.
 Feodo Tracker is tracking four versions of Feodo, and they are labeled by Feodo Tracker as version A, version B, version C and version D
  - Version A: Hosted on compromised webservers running an nginx proxy on port 8080 TCP forwarding all botnet traffic to a tier 2 proxy node.
               Botnet traffic usually directly hits these hosts on port 8080 TCP without using a domain name.
  - Version B: Hosted on servers rented and operated by cybercriminals for the exclusive purpose of hosting a Feodo botnet controller.
               Usually taking advantage of a domain name within ccTLD .ru. Botnet traffic usually hits these domain names using port 80 TCP.
  - Version C: Successor of Feodo, completely different code. Hosted on the same botnet infrastructure as Version A (compromised webservers,
               nginx on port 8080 TCP or port 7779 TCP, no domain names) but using a different URL structure. This Version is also known as Geodo and Emotet.
  - Version D: Successor of Cridex. This version is also known as Dridex
  - Version E: Successor of Geodo / Emotet (Version C) called Heodo. First appeared in March 2017.
 

#### Feodo Tracker IP feeds
 The Feodo Tracker Feodo IP Blocklist contains IP addresses (IPv4) used as C&C communication channel by the Feodo Trojan. 
 This lists contains two types of IP address
  - Feodo C&C servers used by version A, version C and version D of the Feodo Trojan (these IP addresses are usually compromised servers running an nginx daemon on port 8080 TCP or 7779 TCP 
    that is acting as proxy, forwarding all traffic to a tier 2 proxy node)  
  - Feodo C&C servers used by version B which are usually used for the exclusive purpose of hosting a Feodo C&C server. 

Attention: Since Feodo C&C servers associated with version A, version C, version D and version E are usually hosted on compromised servers, 
its likely that you also block/drop legit traffic e.g. towards websites hosted on a certain IP address acting as Feodo C&C for version A, version C and version D.


### Using the Feodo Tracker feed API
 The Feodo Tracker feed API is found on github at

https://github.com/dnif/enrich-feodotracker

#### Getting started with Bambenek Consulting feeds API

1. #####    Login to your Data Store, A10 containers  
   ACCESS DNIF CONTAINER VIA SSH : [Click To Know How](https://dnif.it/docs/guides/tutorials/access-dnif-container-via-ssh.html)
2. #####    Move to the ‘/dnif/<Deployment-key/enrichment_plugin’ folder path.
```
$cd /dnif/CnxxxxxxxxxxxxV8/enrichment_plugin/
```
3. #####   Clone using the following command  
```  
git clone https://github.com/dnif/enrich-feodotracker.git feodotracker
```
### API feed output structure
  | Fields        | Description  |
| ------------- |:-------------:|
| EvtType      | An IP |
| EvtName      | The IOC      |
| IntelRef | Feed Name      |
| IntelRefURL | Feed URL      |
| ThreatType | DNIF Feed Identification Name |      

An example of API feed output
```
{'EvtType': 'IPv4',
'EvtName': '90.244.114.91', 
'AddFields': {
'IntelRef': ['FEODOTRACKER'],
'IntelRefURL': ['https://feodotracker.abuse.ch/blocklist/?download=ipblocklist'], 
'ThreatType': ['Feodo botnet C&C '] }}
```
