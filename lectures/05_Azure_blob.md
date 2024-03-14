# Azure Blob Storage

Durability and AvailabilityAzure Blob Storage is a scalable object storage solution provided by Microsoft Azure. It is designed to store and manage large amounts of unstructured data, such as text or binary data, making it suitable for a wide range of applications including backups, media files, documents, and more.

Blob Storage is designed for:

- Serving images or documents directly to a browser.
- Storing files for distributed access.
- Streaming video and audio.
- Writing to log files.
- Storing data for backup and restore, disaster recovery, and archiving.
- Storing data for analysis by an on-premises or Azure-hosted service.

## Service Architecture

Blob Storage offers three types of resources:

- The **storage account**
- A **container** in the storage account
- A **blob** in a container

The following diagram shows the relationship between these resources.

![Diagram showing the relationship between a storage account, containers, and blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/media/storage-blobs-introduction/blob1.png)

### Storage accounts

A storage account provides a unique namespace in Azure for your data. Every object that you store in Azure Storage has an address that includes your unique account name. The combination of the account name and the Blob Storage endpoint forms the base address for the objects in your storage account.

For example, if your storage account is named *mystorageaccount*, then the default endpoint for Blob Storage is:

```
http://mystorageaccount.blob.core.windows.net
```

The following table describes the different types of storage accounts that are supported for Blob Storage:

| Type of storage account | Performance tier | Usage                                                                                                                                                                                         |
| ----------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General-purpose v2      | Standard         | Standard storage account type for blobs, file shares, queues, and tables. Recommended for most scenarios using Blob Storage or one of the other Azure Storage services.                       |
| Block blob              | Premium          | Premium storage account type for block blobs and append blobs. Recommended for scenarios with high transaction rates or that use smaller objects or require consistently low storage latency. |
| Page blob               | Premium          | Premium storage account type for page blobs only.                                                                                                                                             |

### Containers

A container organizes a set of blobs, similar to a directory in a file system. A storage account can include an unlimited number of containers, and a container can store an unlimited number of blobs.

A container name must be a valid DNS name, as it forms part of the unique URI (Uniform resource identifier) used to address the container or its blobs. Follow these rules when naming a container:

- Container names can be between 3 and 63 characters long.
- Container names must start with a letter or number, and can contain only lowercase letters, numbers, and the dash (-) character.
- Two or more consecutive dash characters aren't permitted in container names.

The URI for a container is similar to:

`https://myaccount.blob.core.windows.net/mycontainer`

### Blobs

Azure Storage supports three types of blobs:

- **Block blobs** store text and binary data. Block blobs are made up of blocks of data that can be managed individually. Block blobs can store up to about 190.7 TiB.
- **Append blobs** are made up of blocks like block blobs, but are optimized for append operations. Append blobs are ideal for scenarios such as logging data from virtual machines.
- **Page blobs** store random access files up to 8 TiB in size. Page blobs store virtual hard drive (VHD) files and serve as disks for Azure virtual machines.

## Lifecycle Management Policies and Tiers

Azure Blob Storage allows you to define lifecycle management policies to automatically transition data between these access tiers based on your specified rules. This feature enables cost optimization by moving data to lower-cost storage tiers as it ages or becomes less frequently accessed.

Azure Blob Storage offers the following storage tiers:

1. **Hot Access Tier:**
   
   - **Description:** The hot access tier is optimized for frequent access to your data. It provides lower latency and higher throughput compared to other tiers.
   - **Use Case:** Suitable for data that is accessed regularly or requires quick access.

2. **Cool Access Tier:**
   
   - **Description:** The cool access tier is designed for data that is accessed less frequently, but still requires quick access when needed. It offers lower storage costs compared to the hot tier.
   - **Use Case:** Ideal for data that is accessed less frequently and where slightly higher latency is acceptable.

3. **Archive Access Tier:**
   
   - **Description:** The archive access tier is the most cost-effective option but comes with higher retrieval costs and longer access times. It is suitable for data that is rarely accessed and can tolerate longer access times.
   - **Use Case:** Ideal for long-term storage of data that is seldom accessed and where the lowest storage costs are a priority.

|                                               | **Hot tier**                                                 | **Cool tier**                                                | **Cold tier**                                                | **Archive tier**                                                |
| --------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------------------------- |
| **Availability**                              | 99.9%                                                        | 99%                                                          | 99%                                                          | 99%                                                             |
| **Availability****(RA-GRS reads)**            | 99.99%                                                       | 99.9%                                                        | 99.9%                                                        | 99.9%                                                           |
| **Usage charges**                             | Higher storage costs, but lower access and transaction costs | Lower storage costs, but higher access and transaction costs | Lower storage costs, but higher access and transaction costs | Lowest storage costs, but highest access, and transaction costs |
| **Minimum recommended data retention period** | N/A                                                          | 30 days                                                      | 90 days                                                      | 180 days                                                        |
| **Latency** **(Time to first byte)**          | Milliseconds                                                 | Milliseconds                                                 | Milliseconds                                                 | Hours                                                           |

## Durability and Availability

- **Durability:** Azure Blob Storage ensures high durability by replicating your data across multiple storage nodes and data centers. It uses mechanisms like locally redundant storage (LRS), geo-redundant storage (GRS), and zone-redundant storage (ZRS) to protect against data loss.

- **Availability:** Azure Blob Storage provides high availability by distributing data across multiple servers and geographic regions. This ensures that your data is accessible even in the event of hardware failures or regional outages.

In summary, Azure Blob Storage is a scalable and secure object storage service with features like encryption, lifecycle management, and high durability and availability to meet the needs of various applications and use cases.

## Exercise

### Case Study

Assume you have a storage account in Azure Blob Storage with three types of data, and you want to decide the storage tier for each based on their access patterns.

1. **Frequently Accessed User Profiles (Hot Data):**
   
   - **Access Pattern:** Accessed multiple times throughout the day.
   - **Initial Tier Assignment:** Hot Access Tier.

2. **Monthly Analytics Reports (Cool Data):**
   
   - **Access Pattern:** Accessed frequently in the first week after generation, then infrequently afterwards.
   - **Initial Tier Assignment:** Cool Access Tier.

3. **Archived Backup Files (Archive Data):**
   
   - **Access Pattern:** Rarely accessed, mainly for compliance or disaster recovery.
   - **Initial Tier Assignment:** Archive Access Tier.

### Monitoring

Assume you monitor the access patterns over a month:

- **Frequently Accessed User Profiles:** 10,000 access requests per day.
- **Monthly Analytics Reports:** 1,000 access requests in the first week, then 50 per week afterward.
- **Archived Backup Files:** 10 access requests per month.

### Proposed changes

<details>
<summary>Hidden answer</summary>

1. **Frequently Accessed User Profiles:**
- The access pattern aligns with expectations. No adjustment needed; keep it in the Hot Access Tier.
  
  2. **Monthly Analytics Reports:**

- The initial assignment to the Cool Access Tier is appropriate, given the access patterns. No adjustment needed.
  
  3. **Archived Backup Files:**

- The access pattern is as expected (rarely accessed). Consider transitioning to the Archive Access Tier for cost savings.

**Lifecycle Policies:**

Implement lifecycle management policies to automate tier transitions:

- Move Monthly Analytics Reports from Hot to Cool after 7 days.
- Move Archived Backup Files from Cool to Archive after 30 days.

</details>
