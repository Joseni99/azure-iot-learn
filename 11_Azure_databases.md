# Azure Databases

## Introduction to Azure Databases

Here's an organized overview of Databases on Azure:

1. **Purpose-built Azure databases:**
   
   - **Azure Cosmos DB:**
     
     - Fast, serverless distributed NoSQL and SQL database at any scale.
     - Supports open-source PostgreSQL, MongoDB, and Apache Cassandra.
     - Ideal for real-time personalization, global app experiences, peak sales periods, and IoT telemetry streaming data.
   
   - **Azure SQL Database:**
     
     - Flexible, fast, and elastic SQL database for new apps.
     - Grow applications with near-limitless storage capacity and responsive serverless compute.
     - Suitable for high-performance transactional applications, finance, sales order management, and processing streaming data.

2. **Best of open source:**
   
   - **Azure Database for PostgreSQL:** (Single server will be deprecated)
     
     - Fully managed, intelligent, and scalable PostgreSQL database.
     - Perfect for open-source, enterprise app development, digital marketing experiences, e-commerce solutions, finance management apps, and scalable web and mobile apps.
   
   - **Azure Database for MySQL:** (Single server will be deprecated)
     
     - Scalable, open-source MySQL database with high availability and elastic scaling.
     - Great for e-commerce solutions, web and mobile apps, digital customer experiences, finance management apps, and low-latency gaming experiences.
   
   - **Azure Database for MariaDB:** (Will be deprecated)
     
     - Fully managed, community MariaDB database with high availability and elastic scaling.
     - Suited for e-commerce solutions, web and mobile apps, digital customer experiences, and finance management apps.
   
   . **Azure Cache for Redis:**
   
   - Distributed, in-memory, scalable caching solution backed by Redis server.
   - Accelerates application data layer with increased speed and scale, ideal for application caching.

&nbsp;

## Types of Databases

### Relational Databases

Relational databases organize data into structured tables and utilize SQL for querying and manipulation. Azure SQL Database, a fully managed service by Microsoft Azure, streamlines database management with automated tuning, threat detection, and built-in intelligence, offering efficient data management solutions.

### Non Relational Databases

NoSQL databases, such as Azure Cosmos DB, accommodate unstructured data types and support various models like documents, key-value pairs, and graphs. Azure Cosmos DB's global distribution and automatic scaling capabilities empower applications with flexible and high-performance data storage solutions.

## Licensing

There are 2 licensing models:

### Compute Pricing

- **DTU-based purchasing**: In this model, you purchase a certain amount of Database Transaction Units (DTUs) and storage. DTUs represent a blended measure of CPU, memory, and I/O resources. You select a service tier based on your performance requirements, and you are charged based on the performance tier and the amount of storage used. 

- **vCore-based purchasing**: In this model, you choose the number of vCores and the amount of memory and storage required. It offers more granular control over resources compared to the DTU model. You are charged based on the number of vCores, amount of storage used, and the Azure region.

### Storage Pricing:

- **Consumed Storage:** Azure Cosmos DB bills for consumed storage rounded up to the next GB per container/collection/table/graph per region. Consumed storage includes all transactional and analytical data and indexes, and backups.

- **Disk Storage:** Azure Cosmos DB bills for disks provisioned for each node by storage size.

*Not all services are compatible with all pricing models, check the reference in Azure.

## High Availabiliity

Azure databases offer various options for high availability, ensuring that your data remains accessible and reliable even in the face of failures or outages. Here's a breakdown of Azure databases and their high availability features:

1. **Azure SQL Database**: Azure SQL Database is a fully managed relational database service provided by Microsoft on the Azure cloud platform. It offers built-in high availability features such as automatic backups, geo-replication, and automatic failover.
   
   - **Automatic backups**: Azure SQL Database automatically performs backups of your database at regular intervals, ensuring that you can restore your data to a specific point in time in case of data loss or corruption.
   
   - **Geo-replication**: With geo-replication, you can asynchronously replicate your database to different Azure regions. This provides disaster recovery capabilities and enables you to maintain access to your data even if an entire Azure region goes down.
   
   - **Automatic failover**: Azure SQL Database supports automatic failover, where it automatically switches to a secondary replica in the event of a failure in the primary database. This minimizes downtime and ensures continuous availability.

2. **Azure Cosmos DB**: Azure Cosmos DB is a globally distributed, multi-model database service designed for building highly responsive and scalable applications. It offers comprehensive high availability features tailored for distributed systems.
   
   - **Multi-region replication**: Azure Cosmos DB allows you to replicate your data across multiple Azure regions with just a few clicks. This ensures that your data is always available and accessible, even if one or more regions experience failures.
   
   - **Automatic failover**: Azure Cosmos DB automatically detects failures and performs failover to a healthy replica in another region, ensuring continuous availability and minimal downtime.
   
   - **SLA-backed guarantees**: Azure Cosmos DB provides industry-leading SLAs (Service Level Agreements) for availability, consistency, throughput, and latency, giving you confidence in the reliability of your database.

3. **Azure Database for PostgreSQL, MySQL, and MariaDB**: Azure offers managed database services for PostgreSQL, MySQL, and MariaDB, providing high availability features similar to Azure SQL Database.
   
   - **Automated backups**: Like Azure SQL Database, these services offer automated backups to protect your data and enable point-in-time recovery.
   
   - **Geo-replication**: You can configure geo-replication for disaster recovery and improved availability, replicating your database to different Azure regions.
   
   - **Automatic failover**: These services support automatic failover to ensure continuous availability in the event of a failure.
