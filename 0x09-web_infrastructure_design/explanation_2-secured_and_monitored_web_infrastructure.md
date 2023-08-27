# Secured and monitored web infrastructure

A three server secured, serve encrypted traffic, and monitored web infrastructure that hosts the website www.foobar.com.

[Whiteboard Screenshot Link](https://photos.app.goo.gl/fvRLvASsrgTfthyB7)

## Specifics about this infrastructure:
### Additional element:
- 3 firewalls
- 1 SSL certificate to serve www.foobar.com over HTTPS
- 3 monitoring clients (data collector for Sumologic or other monitoring services)

### What are firewalls for:
- To secure the network and control incoming/outgoing traffic.
- Ensures cyber protection, by acting as barriers between the internal network and the external network, and blocking unauthorized access, protecting servers from potential threats.

### why is the traffic served over HTTPS:
- To secure data transmitted between users and the website.
- HTTPS encrypts data, preventing eavesdropping and ensuring data integrity.
- Protects users privacy, identity, and data.

### What monitoring is used for:
- To keep track of server performance and detect issues, measure the overall health, and alert the system administrators.
- Collect key metrics data on server health, usage, response time and potential problems.

### How the monitoring tool is collecting data:
- Monitoring clients (data collectors) are installed on each server to gather key metrics data.
- These clients send data to a central monitoring service (like Sumo Logic), enabling analysis and alerts.

### How to monitor my web server QPS:
- To monitor QPS (Queries Per Second) on the web server, the monitoring tool is setup to track incoming requests over time.
- We analyze this data to understand usage patterns and performance thresholds.

## Issues with this Infrastructure:

### Terminating SSL at the load balancer level:
- This issue can limit the ability to inspect encrypted traffic, which might be needed for security analysis at the application level.
- It leave the traffic between the load balancer and the web servers unencrypted.

### Having only one MySQL server capable of accepting writes:
- This issue creates a single point of failure and limits write scalability.
- it is not scalable.

### Having servers with all the same components:
- Identical components might not optimize resource utilization, especially if some servers are more powerful or specialized.
- It can lead to poor performance and also make it difficult to troubleshoot the source of the problem.
