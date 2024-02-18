Azure virtual machines are one of several types of [on-demand, scalable computing resources](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree) that Azure offers. Typically, you choose a virtual machine when you need more control over the computing environment than the other choices offer. This article gives you information about what you should consider before you create a virtual machine, how you create it, and how you manage it.

An Azure virtual machine gives you the flexibility of virtualization without having to buy and maintain the physical hardware that runs it. However, you still need to maintain the virtual machine by performing tasks, such as configuring, patching, and installing the software that runs on it.

## What do I need to think about before creating a virtual machine?

There's always a multitude of design considerations when you build out an application infrastructure in Azure. These aspects of a virtual machine are important to think about before you start:

- The names of your resources
- The location where the resources are stored
- The size of the virtual machine
- The maximum number of virtual machines that can be created
- The operating system that the virtual machine runs
- The configuration of the virtual machine after it starts
- The related resources that the virtual machine needs

# Basics

#### Locations

There are multiple geographical regions around the world where you can create Azure resources. Usually, the region is called **location** when you create a virtual machine. For a virtual machine, the location specifies where the virtual hard disks will be stored.

#### Availability

There are multiple options to manage the availability of your virtual machines in Azure.

- **[Availability Zones](https://learn.microsoft.com/en-us/azure/availability-zones/az-overview)** are physically separated zones within an Azure region. Availability zones guarantee virtual machine connectivity to at least one instance at least 99.99% of the time when you've two or more instances deployed across two or more Availability Zones in the same Azure region.
- **[Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview)** let you create and manage a group of load balanced virtual machines. The number of virtual machine instances can automatically increase or decrease in response to demand or a defined schedule. Scale sets provide high availability to your applications, and allow you to centrally manage, configure, and update many virtual machines. Virtual machines in a scale set can also be deployed into multiple availability zones, a single availability zone, or regionally.

#### Sizes and pricing

The size of the virtual machine that you use is determined by the workload that you want to run. The size that you choose then determines factors such as processing power, memory, storage capacity, and network bandwidth. Azure offers a wide variety of sizes to support many types of uses.

| Type                                                                                           | Sizes                                                                                                                                                                      | Description                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [General purpose](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-general)      | B, Dsv3, Dv3, Dasv4, Dav4, DSv2, Dv2, Av2, Dpdsv5, Dpldsv5, Dpsv5, Dplsv5, Dv4, Dsv4, Ddv4, Ddsv4, Dv5, Dsv5, Ddv5, Ddsv5, Dasv5, Dadsv5, DCasv5, DCadsv5, DCesv5, DCedsv5 | Balanced CPU-to-memory ratio. Ideal for testing and development, small to medium databases, and low to medium traffic web servers.                                                              |
| [Compute optimized](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-compute)    | F, Fs, Fsv2, FX                                                                                                                                                            | High CPU-to-memory ratio. Good for medium traffic web servers, network appliances, batch processes, and application servers.                                                                    |
| [Memory optimized](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-memory)      | Esv3, Ev3, Easv4, Eav4, Epdsv5, Epsv5, Ev4, Esv4, Edv4, Edsv4, Ev5, Esv5, Edv5, Edsv5, Easv5, Eadsv5, Mv2, M, DSv2, Dv2, ECasv5, ECadsv5, ECesv5, ECedsv5                  | High memory-to-CPU ratio. Great for relational database servers, medium to large caches, and in-memory analytics.                                                                               |
| [Storage optimized](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-storage)    | Lsv2, Lsv3, Lasv3                                                                                                                                                          | High disk throughput and IO ideal for Big Data, SQL, NoSQL databases, data warehousing and large transactional databases.                                                                       |
| [GPU](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-gpu)                      | NC, NCv2, NCv3, NCasT4_v3, NC A100 v4, ND, NDv2, NGads V620, NV, NVv3, NVv4, NDasrA100_v4, NDm_A100_v4                                                                     | Specialized virtual machines targeted for heavy graphic rendering and video editing, as well as model training and inferencing (ND) with deep learning. Available with single or multiple GPUs. |
| [High performance compute](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-hpc) | HB, HBv2, HBv3, HBv4, HC, HX                                                                                                                                               | Fastest and most powerful CPU virtual machines with optional high-throughput network interfaces (RDMA).                                                                                         |

Azure charges an hourly price based on the virtual machine’s size and operating system. For partial hours, Azure charges only for the minutes used. Storage is priced and charged separately.

# Disks

Azure Disks are a type of block storage offered by Microsoft Azure, the cloud computing platform. They provide scalable and highly available storage that can be attached to Azure Virtual Machines (VMs) to support various workloads. Here are some key points about Azure Disks:

1. **Disk Encryption:**
   
   - Azure Disks support encryption at rest using Azure Disk Encryption (ADE). This feature helps protect data on the disk by encrypting it with industry-standard encryption algorithms.

2. **Availability:**
   
   - Azure Disks are designed for high availability, and they support availability sets and availability zones. Availability sets and zones ensure that your VMs and disks are distributed across different physical locations to increase fault tolerance.

3. **Snapshot and Backup:**
   
   - Azure Disks support creating snapshots, which are read-only copies of a disk. Snapshots can be used for backup purposes or to create consistent images for VM deployment. Azure Backup is also available for more comprehensive backup and restore capabilities.

4. **Scaling:**
   
   - You can easily scale your Azure Disks by resizing them to meet the changing storage requirements of your applications without downtime.

There is a lot more options and features that covering it in 1 session would be impossible so there is a link if want to learn more.

```
https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview
```

#### Disk type comparison

There are different managed disks types in Azure, so sometimes choosing one it is difficult, here is a cheat-sheet that can help:

![Diagram of a decision tree for managed disk types.](https://learn.microsoft.com/en-us/azure/virtual-machines/media/disks-types/managed-disk-decision-tree.png#lightbox)

|                    | Ultra disk                                                                                                                     | Premium SSD v2                                                                                                    | Premium SSD                                    | Standard SSD                                                   | Standard HDD                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------- | --------------------------------------- |
| Disk type          | SSD                                                                                                                            | SSD                                                                                                               | SSD                                            | SSD                                                            | HDD                                     |
| Scenario           | IO-intensive workloads such as SAP HANA, top tier databases (for example, SQL, Oracle), and other transaction-heavy workloads. | Production and performance-sensitive workloads that consistently require low latency and high IOPS and throughput | Production and performance sensitive workloads | Web servers, lightly used enterprise applications and dev/test | Backup, non-critical, infrequent access |
| Max disk size      | 65,536 GiB                                                                                                                     | 65,536 GiB                                                                                                        | 32,767 GiB                                     | 32,767 GiB                                                     | 32,767 GiB                              |
| Max throughput     | 4,000 MB/s                                                                                                                     | 1,200 MB/s                                                                                                        | 900 MB/s                                       | 750 MB/s                                                       | 500 MB/s                                |
| Max IOPS           | 160,000                                                                                                                        | 80,000                                                                                                            | 20,000                                         | 6,000                                                          | 2,000, 3,000*                           |
| Usable as OS Disk? | No                                                                                                                             | No                                                                                                                | Yes                                            | Yes                                                            | Yes                                     |

# Networking

The networking architecture of Azure VMs is designed to facilitate seamless connectivity while ensuring security and performance. At its core, the architecture includes the following key components:

1. **Virtual Networks (VNets):** VNets serve as the foundational building blocks for Azure VM networking. They provide isolation, segmentation, and control over the communication between VMs within the same VNet.

2. **Subnets:** Within a VNet, subnets allow further segmentation, enabling organizations to group VMs based on functionality, security requirements, or other criteria. Subnets help in efficient network management and resource organization.

3. **Network Security Groups (NSGs):** NSGs act as virtual firewalls, allowing or denying traffic to and from Azure resources. They help control access to VMs, securing the network by defining rules based on source and destination IP addresses, ports, and protocols.

4. **Load Balancers:** Azure Load Balancers distribute incoming network traffic across multiple VMs to ensure high availability and reliability. They play a crucial role in optimizing resource utilization and preventing overloads on specific VMs.

5. 

# Additional Costs

When you create a virtual machine, you're also creating resources that support the virtual machine. These resources come with their own costs that should be considered.

The default resources supporting a virtual machine and how they're billed are detailed in the following table:

| Resource                                                | Description                                                                                                                                                                            |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A virtual Network Interface Card (NIC)                  | For connecting to the virtual network                                                                                                                                                  |
| A private IP address and sometimes a public IP address. | For communication and data exchange on your network and with external networks                                                                                                         |
| OS Disk and possibly separate disks for data.           | It's a best practice to keep your data on a separate disk from your operating system, in case you ever have a VM fail, you can simply detach the data disk, and attach it to a new VM. |
| In some cases, a license for the OS                     | For providing your virtual machine runs to run the OS                                                                                                                                  |
