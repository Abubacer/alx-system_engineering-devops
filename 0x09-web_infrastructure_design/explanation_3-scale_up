# Secured and monitored web infrastructure

Scale up web infrastructure that hosts the website www.foobar.com.

[Whiteboard Screenshot Link](https://photos.app.goo.gl/CY5kJTMmb3vvWETv8)

## Specifics about this infrastructure:
### Additional element:
- 1 load-balancer (HAproxy) configured as cluster with the other one
- Split components (4 web server, 4 application server, 4 database)

### Why Added the load-balancer configured as cluster:
- The load-balancer is configured as a cluster between the servers To distribute traffic effectively.
- It provides redundancy and fault tolerance. If one load balancer fails, the other takes over seamlessly.

### Why Added the 4 Web Servers:
-  To distribute web traffic and increase the capacity to handle incoming requests.
- Ensure efficient handling of HTTP requests and improve response times.

### Why Added the 4 app Servers:
- To distribute dynamic content processing and reduce server load.
- Ensure efficient execution of application logic and improve scalability.

### Why Added the 4 database Servers:
- To distribute data storage and processing for improved performance and redundancy.
- Enhance data availability, reduce the risk of data loss, and increase the capacity to handle database queries.

### Why Added the Firewalls:
- To enhance security by controlling incoming and outgoing traffic for each component.

### Why Added the Monitoring Clients, Data Collectors:
- To monitor the performance and health of each component.
- Adding monitoring clients to each server allows for comprehensive performance monitoring, ensuring that each component is operating optimally.

## Issues with this Infrastructure:

### Complexity:
- As the number of servers and components increases, so does the complexity of the system. This complexity can make setup, maintenance, and troubleshooting more challenging.

### Cost:
-  Adding more servers and redundancy typically comes with increased costs, both in terms of hardware and ongoing operational expenses.

### Monitoring and Maintenance:
- Managing multiple servers and components requires effective monitoring and maintenance processes. Regular updates, patches, and backups are critical.
