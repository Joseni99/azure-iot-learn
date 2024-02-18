Azure Virtual Network is a service that provides the fundamental building block for your private network in Azure. An instance of the service (a virtual network) enables many types of Azure resources to securely communicate with each other, the internet, and on-premises networks. These Azure resources include virtual machines (VMs).

A virtual network is similar to a traditional network that you'd operate in your own datacenter. But it brings extra benefits of the Azure infrastructure, such as scale, availability, and isolation.

Here is an example of an AVN architecture:

<img src="https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/images/hub-spoke.png#lightbox" title="" alt="Diagram that shows a hub-spoke virtual network topology in Azure with spoke networks connected through the hub or directly." width="627">

## Why use an Azure virtual network?

Key scenarios that you can accomplish with a virtual network include:

- ##### Communication of Azure resources with the internet.
  
  - All resources in a virtual network can communicate outbound with the internet, by default. You can also use a [public IP address](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/virtual-network-public-ip-address), [NAT gateway](https://learn.microsoft.com/en-us/azure/nat-gateway/nat-overview), or [public load balancer](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-overview) to manage your outbound connections. You can communicate inbound with a resource by assigning a public IP address or a public load balancer.
    
    When you're using only an internal standard load balancer, outbound connectivity is not available until you define how you want outbound connections to work with an instance-level public IP address or a public load balancer.

- ##### Communication between Azure resources.
  
  - Azure resources communicate securely with each other in one of the following ways:
    
    - **Virtual network**: You can deploy VMs and other types of Azure resources in a virtual network. Examples of resources include App Service Environments, Azure Kubernetes Service (AKS), and Azure Virtual Machine Scale Sets. 
    
    - **Virtual network service endpoint**: You can extend your virtual network's private address space and the identity of your virtual network to Azure service resources over a direct connection. Examples of resources include Azure Storage accounts and Azure SQL Database. Service endpoints allow you to secure your critical Azure service resources to only a virtual network.
    
    - **Virtual network peering**: You can connect virtual networks to each other by using virtual peering. The resources in either virtual network can then communicate with each other. The virtual networks that you connect can be in the same, or different, Azure regions.

- ##### Communication with on-premises resources.
  
  - You can connect your on-premises computers and networks to a virtual network by using any of the following options:
    
    - **Point-to-site virtual private network (VPN)**: Established between a virtual network and a single computer in your network. Each computer that wants to establish connectivity with a virtual network must configure its connection. This connection type is useful if you're just getting started with Azure, or for developers, because it requires few or no changes to an existing network. The communication between your computer and a virtual network is sent through an encrypted tunnel over the internet. 
    
    - **Site-to-site VPN**: Established between your on-premises VPN device and an Azure VPN gateway that's deployed in a virtual network. This connection type enables any on-premises resource that you authorize to access a virtual network. The communication between your on-premises VPN device and an Azure VPN gateway is sent through an encrypted tunnel over the internet. 
    
    - **Azure ExpressRoute**: Established between your network and Azure, through an ExpressRoute partner. This connection is private. Traffic doesn't go over the internet.

- ##### Filtering of network traffic.
  
  - You can filter network traffic between subnets by using either or both of the following options:
    
    - **Network security groups**: Network security groups and application security groups can contain multiple inbound and outbound security rules. These rules enable you to filter traffic to and from resources by source and destination IP address, port, and protocol. To learn more, see [Network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) and [Application security groups](https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups).
    
    - **Network virtual appliances**: A network virtual appliance is a VM that performs a network function, such as a firewall or WAN optimization. 

- ##### Routing of network traffic.
  
  - Azure routes traffic between subnets, connected virtual networks, on-premises networks, and the internet, by default. You can implement either or both of the following options to override the default routes that Azure creates:
    
    - **Route tables**: You can create [custom route tables](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview#user-defined) that control where traffic is routed to for each subnet.
    
    - **Border gateway protocol (BGP) routes**: If you connect your virtual network to your on-premises network by using an [Azure VPN gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-bgp-overview?toc=/azure/virtual-network/toc.json) or an [ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-routing?toc=/azure/virtual-network/toc.json#dynamic-route-exchange) connection, you can propagate your on-premises BGP routes to your virtual networks.

- ##### Integration with Azure services.
  
  - Integrating Azure services with an Azure virtual network enables private access to the service from virtual machines or compute resources in the virtual network. You can use the following options for this integration:
    
    - Deploy dedicated instances of the service into a virtual network. The services can then be privately accessed within the virtual network and from on-premises networks.
    
    - Use [Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview) to privately access a specific instance of the service from your virtual network and from on-premises networks.
    
    - Access the service over public endpoints by extending a virtual network to the service, through [service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview). Service endpoints allow service resources to be secured to the virtual network.

## Limits

There are limits to the number of Azure resources that you can deploy. Most Azure networking limits are at the maximum values. However, you can [increase certain networking limits](https://learn.microsoft.com/en-us/azure/azure-portal/supportability/networking-quota-requests).

## Virtual networks and availability zones

Virtual networks and subnets span all availability zones in a region. You don't need to divide them by availability zones to accommodate zonal resources. For example, if you configure a zonal VM, you don't have to take into consideration the virtual network when selecting the availability zone for the VM. The same is true for other zonal resources.

### Network design example

In Microsoft Azure, subnet design is an essential aspect of creating a Virtual Network (VNet) to host various resources. Let's consider an example scenario for a company using Azure with different services:

1. **Frontend Web Servers**: Public-facing web servers.
2. **Backend Application Servers**: Running backend services.
3. **Database Servers**: Storing application data.
4. **Management Subnet**: For administrative tools and services.

Here's a basic example:

- **VNet Address Space**: 10.1.0.0/16

- **Frontend Web Servers Subnet**: 10.1.1.0/24
  
  - Usable addresses: 10.1.1.1 to 10.1.1.254

- **Backend Application Servers Subnet**: 10.1.2.0/24
  
  - Usable addresses: 10.1.2.1 to 10.1.2.254

- **Database Servers Subnet**: 10.1.3.0/24
  
  - Usable addresses: 10.1.3.1 to 10.1.3.254

- **Management Subnet**: 10.1.4.0/24
  
  - Usable addresses: 10.1.4.1 to 10.1.4.254

In this example:

- The Frontend Web Servers subnet is exposed to the internet.
- The Backend Application Servers communicate with the Frontend and Database subnets.
- The Database Servers subnet stores sensitive data and communicates with the Backend subnet.
- The Management Subnet is used for administrative tools and services.

Azure provides (NACLs) to control traffic between subnets, providing an additional layer of security in your design. Remember that this is a simplified example, and in a real-world scenario, you might have additional considerations like high availability, scalability, and redundancy.

## Pricing

There's no charge for using Azure Virtual Network. It's free of cost.
