# Introduction to Cloud Computing

## Cloud Computing and Virtualization

The technology that lies at the core of all cloud operations is virtualization. As illustrated in the image below, virtualization lets you divide the hardware resources of a single physical server into smaller units. That physical server could therefore host multiple virtual machines (VMs) running their own complete operating systems, each with its own memory, storage, and network access.

<p align="center">
  <img title="" src="img/001vm.png" alt="001vm.png" width="550">
</p>

Virtualization’s flexibility makes it possible to provision a virtual server in a matter of seconds, run it for exactly the time your project requires, and then shut it down. The resources released will become instantly available to other workloads.

## Azure services overview

Microsoft Azure offers a wide range of services across various categories, including computing, storage, databases, networking, artificial intelligence (AI), Internet of Things (IoT), analytics, and more. Keep in mind that Azure regularly updates its services, introduces new ones, and may retire or modify existing ones. Here's an overview of some key Azure services:

![](https://www.oreilly.com/api/v2/epubs/9781787124349/files/assets/0be37779-2ac3-4fe6-b8b0-0177c19149f4.jpg)

1. **Azure Virtual Machines (VMs):** Allows you to deploy and manage virtualized Windows and Linux servers in the cloud.

2. **Azure Blob Storage:** Provides scalable object storage for large amounts of unstructured data, such as documents and images.

3. **Azure SQL Database:** A fully managed relational database service with high availability and scalability.

4. **Azure App Service:** A platform for building, deploying, and scaling web apps. It supports multiple programming languages.

5. **Azure Kubernetes Service (AKS):** Simplifies the deployment, management, and scaling of containerized applications using Kubernetes.

6. **Azure Functions:** Enables serverless computing, allowing you to run code in response to events without provisioning or managing servers.

7. **Azure Entra ID:** A cloud-based identity and access management service for securing applications and resources.

8. **Azure Virtual Network:** Allows you to create private, isolated, and securely connected networks in the Azure cloud.

9. **Azure IoT Hub:** A fully managed service for securely connecting, monitoring, and managing IoT devices.

10. **Azure DevOps Services:** Provides a set of development tools for version control, build automation, release management, and more.

## Is Azure secure?

**Q: Why is Azure considered a secure cloud platform?**

**A:** Azure prioritizes security through a multi-layered approach that encompasses physical security, network security, identity and access management, data encryption, and compliance certifications. Microsoft invests heavily in security measures, employs advanced threat intelligence, and regularly updates its security protocols to address emerging threats.

---

**Q: How does Azure ensure the physical security of its data centers?**

**A:** Azure data centers are equipped with state-of-the-art security features, including strict access controls, surveillance systems, and biometric authentication. Only authorized personnel have access to the physical infrastructure, and security measures are implemented 24/7 to safeguard against unauthorized entry or tampering.

---

**Q: What measures does Azure take to protect data during transmission?**

**A:** Azure uses industry-standard encryption protocols to secure data in transit. Data transmitted between users and Azure services is encrypted using protocols like HTTPS, ensuring that even if intercepted, the data remains secure. Additionally, Azure offers Virtual Private Network (VPN) and ExpressRoute options for private, dedicated connections.

---

**Q: How does Azure manage identity and access control?**

**A:** Azure employs robust identity and access management solutions such as Azure Entra ID. Users can implement multi-factor authentication, role-based access control (RBAC), and conditional access policies to control and monitor access to resources, reducing the risk of unauthorized access.

---

**Q: In what ways does Azure protect data at rest within its services?**

**A:** Azure provides built-in encryption for data at rest, ensuring that stored information remains secure. Azure Storage services, databases, and virtual machines all support encryption mechanisms. Customers can also bring their encryption keys or use Azure Key Vault for centralized key management.

---

**Q: How does Azure comply with regulatory standards to ensure data privacy and protection?**

**A:** Azure complies with a wide range of international and industry-specific compliance standards, including ISO 27001, GDPR, HIPAA, and many more. Regular audits and certifications validate Azure's adherence to these standards, providing customers with assurance that their data is handled in accordance with regulatory requirements.

---

**Q: What role does Azure play in helping customers recover from data loss or disasters?**

**A:** Azure offers robust backup and disaster recovery solutions. Services like Azure Backup and Azure Site Recovery enable customers to create comprehensive backup strategies and implement disaster recovery plans. This ensures data availability and minimizes downtime in the event of unexpected incidents.

---

**Q: How can Azure help organizations monitor and respond to security threats in real-time?**

**A:** Azure Security Center provides continuous monitoring of cloud resources and offers advanced threat detection capabilities. It uses machine learning and behavioral analytics to identify and respond to potential security threats, providing insights and recommendations to enhance overall security posture.

---

**Q: Can Azure customers have confidence in the privacy of their data?**

**A:** Yes, Azure is committed to respecting customer privacy. Microsoft's data handling practices prioritize customer control and transparency. Azure's privacy controls, coupled with adherence to strict privacy policies, empower customers to manage their data securely within the Azure environment.

---

Of course there is a caveat here, Azure is as secure also how good practices are implemented by users, here is where the shared responsability model comes in.

The shared responsibility model is a security framework that defines the responsibilities of both cloud service providers and customers in ensuring the security of data and applications in the cloud. In this model, the provider manages security "of" the cloud infrastructure, while the customer is responsible for security "in" the cloud, including data protection, access management, and application security.

Example: In a cloud computing environment, the provider (Azure) is responsible for securing the physical infrastructure, network, and hypervisor, while the customer is responsible for securing their data, configuring access controls, and ensuring the security of applications deployed on the cloud platform.

It will not work if only one of the sides adopts good practices, there is no point in using encryption, securing resources and so on if we simply use an administrator account  with password 1234 without 2FA.
