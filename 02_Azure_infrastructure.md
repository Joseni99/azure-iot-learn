# Azure Infrastructure

Azure is structured into **regions**, defined as geographic areas housing one or more **availability zones**. These regions are intricately interconnected through the **Microsoft Network**, hostinga robust and expansive computing environment.

## Microsoft Global Networks

Microsoft owns and operates one of the largest backbone networks in the world. This global and sophisticated architecture, spanning more than 165,000 miles, connects our datacenters and customers.

Every day, customers around the world connect and pass trillions of requests to Microsoft Azure, Bing, Dynamics 365, Microsoft 365, XBox, and many others. Regardless of type, customers expect instant reliability and responsiveness from our services.

The [Microsoft global network](https://azure.microsoft.com/global-infrastructure/global-network/) (WAN) is a central part of delivering a great cloud experience. The global network connects our Microsoft [data centers](https://azure.microsoft.com/global-infrastructure/) across 61 Azure regions with a large mesh of edge-nodes strategically placed around the world. The Microsoft global network offers both the availability, capacity, and the flexibility to meet any demand.

![Diagram of Microsoft global network.](https://learn.microsoft.com/en-us/azure/networking/media/microsoft-global-network/microsoft-global-wan.png)

&nbsp;

## Azure Regions

Azure regions are geographical areas containing one or more data centers that are connected through a low-latency network. Microsoft Azure, the cloud computing platform provided by Microsoft, is distributed globally across multiple regions to ensure high availability, fault tolerance, and scalability for its services. Each Azure region is designed to be independent of other regions, providing isolation in terms of data residency, compliance, and disaster recovery.

Here are key aspects of Azure regions:

1. **Geographical Distribution:**
   
   - Azure regions are spread across the world to cater to the diverse needs of customers and comply with regional regulations regarding data residency and compliance.
   - Microsoft strategically selects locations for regions based on factors like proximity to customers, data sovereignty requirements, and geopolitical considerations.

2. **Availability Zones:**
   
   - Each Azure region is typically divided into multiple Availability Zones, which are essentially separate data centers within the region.
   - Availability Zones are designed to provide redundancy and resiliency, ensuring that if one zone experiences an outage, the others can continue to operate independently.

3. **Data Centers:**
   
   - Within each region, there are multiple data centers that house the physical infrastructure, including servers, storage, and networking equipment.
   - These data centers are equipped with advanced security measures, backup power supplies, and environmental controls to ensure the safety and integrity of the hosted services.

4. **Network Connectivity:**
   
   - Azure regions are connected through Microsoft's global network infrastructure. This network is designed to provide low-latency, high-bandwidth connectivity between regions, ensuring fast and reliable data transfer.

5. **Service Availability:**
   
   - Azure services are deployed in individual regions, and users can deploy their applications and resources in the region of their choice.
   - Microsoft aims to provide high availability for its services by distributing them across multiple regions and Availability Zones.

6. **Data Residency and Compliance:**
   
   - Azure regions enable users to store their data in specific geographic locations, helping them comply with data residency requirements and regulations in different regions.
   - Microsoft provides a wide range of compliance certifications and adheres to industry-standard security and privacy practices.

7. **Disaster Recovery:**
   
   - The geographic distribution of Azure regions facilitates disaster recovery planning. Users can replicate their applications and data across regions to ensure business continuity in case of a regional outage.

8. **Expanding Footprint:**
   
   - Microsoft continues to expand its Azure footprint by adding new regions globally. This expansion allows customers to deploy their services closer to end-users and comply with specific regional requirements.

Feel free to visit an interactive map of Azure Datacenters:

```
https://datacenters.microsoft.com/globe/explore
```

&nbsp;

## Azure Availability Zones

Many Azure regions provide *availability zones*, which are separated groups of datacenters within a region. Availability zones are close enough to have low-latency connections to other availability zones. They're connected by a high-performance network with a round-trip latency of less than 2ms. However, availability zones are far enough apart to reduce the likelihood that more than one will be affected by local outages or weather. Availability zones have independent power, cooling, and networking infrastructure. They're designed so that if one zone experiences an outage, then regional services, capacity, and high availability are supported by the remaining zones. They help your data stay synchronized and accessible when things go wrong.

Datacenter locations are selected by using rigorous vulnerability risk assessment criteria. This process identifies all significant datacenter-specific risks and considers shared risks between availability zones.

The following diagram shows several example Azure regions. Regions 1 and 2 support availability zones.

<img title="" src="https://learn.microsoft.com/en-us/azure/reliability/media/regions-availability-zones.png" alt="Screenshot of physically separate availability zone locations within an Azure region." width="659">
