# Simple Web Stack

- ***What is a server***
A computer or computer program which manages access to a centralized resource or service in a network.

- ***What is the role of the domain name***
Identifies Internet resources, such as computers, networks, and services, with a **text-based label** that is easier to memorize than the numerical addresses used in the Internet protocols

- ***What type of DNS record www is in www.foobar.com***
8.8.8.8

- *** What is the role of the web server***
to store, process, and deliver requested information or webpages to end users

- ***What is the role of the application server***
act as host (or container) for the user's business logic while facilitating access to and performance of the business application.

-  ***What is the role of the database***
To organize a collection of structured information, or data, typically stored electronically in a computer system

- ***What is the server using to communicate with the computer of the user requesting the website***
HyperText Transfer Protocol (HTTP).

![](https://imgur.com/cccfifc)

# Distributed Web Infrastructure
- ***For every additional element, why you are adding it***
1) Load balancer	:	Distributing incoming network traffic across server
2) Second Server	:	Creates a versatile environment by allocating resources between servers

- ***What distribution algorithm your load balancer is configured with and how it works***
HAproxy  algos to balance trafic.

-  ***Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both***
Active-Active	: All servers working.
Active-Passive	: Some servers are active. These server are for backup.

- ***How a database Primary-Replica (Master-Slave) cluster works***
Master	: Read-Write
Slave	  : Read 

- ***What is the difference between the Primary node and the Replica node in regard to the application***
One primary node (PN) – absorbs data and executes pre-computings and computings. One or many replica nodes (RN) – execute computings and respond to end-users' requests to display dashboards.

![](https://imgur.com/a/4Qe0W1D)

# Secured And Monitored Web Infrastructure
- ***For every additional element, why you are adding it***
1) Load balancer	:	Distributing incoming network traffic across server
2) Second Server	:	Creates a versatile environment by allocating resources between servers
3) Firewalls			:	protection against outside cyber attackers
4) SSL certificate	:	keep user data secure, verify ownership of the website,

- ***What are firewalls for***
Blocks unauthorized access to/fro network

- ***Why is the traffic served over HTTPS***
HTTPS ensures that all communications between the user's web browser and a website are completely encrypted

- ***What monitoring is used for***
Monitors the status of the hardware & software

- ***How the monitoring tool is collecting data***
Query per seconds gives information

- ***Explain what to do if you want to monitor your web server QPS***
1: Requests per second (RPS)
2: Uptime.
3: Error rates.
4: Thread count.
5: System-level performance metrics.
6: Average response time (ART)
7: Peak response times (PRT)
8: Security-related metrics.

![](https://imgur.com/a/C8rjdY5)
