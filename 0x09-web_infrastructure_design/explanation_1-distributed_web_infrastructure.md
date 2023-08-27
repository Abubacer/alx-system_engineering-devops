# Distributed web infrastructure

A three server web infrastructure that hosts the website www.foobar.com.

[Whiteboard Screenshot Link](https://photos.app.goo.gl/LTVLQYEWhbqiHUqZ9)

## Specifics about this infrastructure:
### Additional element:
- Server 2 a replica of Server 1
- Load Balancer (HAproxy)

### why the Server 2(Replica):
- Acts as a backup for the primary server.
- Ensures redundancy, high availability, and read scalability.

### why the Load-balancer:
- Balances incoming traffic across the servers to avoid overloading one server and ensures high availability.

### What distribution algorithm load balancer is configured with and how it works:
- The load balancer uses Round Robin distribution algorithm, this is a straight forward and dynamic algorithm works by distributing requests equally among available servers according to their weights. also it allows server weights to be adjusted on the go.

### Active-Active or Active-Passive setup:
- The load balancer is enabling an Active-Passive setup, instead ofan active-active setup. in an active-active setup both servers (Primary and Replica) are actively serving requests. If one server fails, the other continues to handle traffic. this setup prevent any single node from getting overloaded and used for load distribution, and high availability. On the other hand, in an Active-Passive setup the primary server serves requests while the other Replica remains inactive. If the Primary fails, the Replica takes over. this setup is used to ensures redundancy and for failover and minimizing downtime.

### How a database Primary-Replica (Master-Slave) cluster works:
- The master-slave is a database architecture divided into a master database and slave databases.
- The slave database serves as the backup and as a replica for the master database. The master database is used for the write operations, while read operations may be spread on multiple slave databases.
- Data is synchronized between the two servers whenever the Primary server executes a write requests.

### What is the difference between the Primary node and the Replica node in regard to the application
- Primary Node (Master): Accepts write operations (inserts, updates, deletes), maintains the most up-to-date data.
- Replica Node (Slave): Copies data from the primary node and can handle read requests. Increases overall performance.

## Issues with this Infrastructure:

### Single Point of Failure (SPOF):
There are multiple SPOF, one example, if the load balancer fails, visitors can't access the website.

### Security:
- This infrastructure lacks a firewall, leaving it vulnerable to unauthorized access and cyber-attacks.
- Data transmission between users and the website is not encrypted, risking data interception and breaches.

### No Monitoring:
- The absence of monitoring tools makes it challenging to identify performance issues or security breaches of this infrastructure.
