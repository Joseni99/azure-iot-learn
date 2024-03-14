# Azure Resources and Identity

## Azure Resource Hierarchy

Before proceeding further, it is essential to have a basic understanding of the Azure resource hierarchy. This involves gaining a foundational understanding of how different resources are organized and interconnected within the Azure environment.

But first some definitions of basic concepts:

**Azure Active Directory:** Is Microsoft's cloud-based identity and access management service. Azure Active Directory is designed to help organizations manage and secure user identities and access to applications and resources in the cloud. Nowadays is renamed to Azure Entra ID.

<p align="center">
<img title="" src="img/30_resources.png" alt="30_resources.png" width="383">
</p>

1. **Management Groups**

At the top level of the hierarchy are **management groups**. Management groups provide a way to manage access, policies, and compliance for multiple subscriptions. They help in organizing subscriptions based on organizational structure or business divisions. Policies can be applied at the management group level to enforce governance standards across multiple subscriptions. A management group tree can support up to six levels of depth however this limit doesn’t include root or subscription level.

2. **Subscriptions**

Below management groups are **subscriptions**, which represent an agreement with Microsoft to use Azure services. Subscriptions are used to organize and manage resources such as virtual machines, databases, and storage accounts. Organizations often have multiple subscriptions to separate environments like development, testing, and production.

3. **Resource Groups**

Within a subscription, resources are organized into **resource groups**. A resource group is a logical container for resources, and it helps in managing and organizing resources based on their lifecycle, ownership, or environment. Resources within a resource group share the same lifecycle and are deployed, updated, and deleted together.

4. **Resources**

At the lowest level of the hierarchy are individual **resources**. These are the actual services or components you deploy, such as virtual machines, databases, storage accounts, etc. Resources are always associated with a resource group.

&nbsp;

In our case, if we access the management groups:

<p align="center">
<img title="" src="img/31_resourceg.png" alt="31_resourceg.png" width="645">
</p>

We can check that there is the tenant root group, which in turn is assigned to our Azure for Students subscription containing the credits we will utilize for conducting our laboratory.

Each Microsoft Entra tenant is given a single top-level management group called the root management group. This root management group is built into the hierarchy to have all management groups and subscriptions fold up to it. This group allows global policies and Azure role assignments to be applied at the directory level.

&nbsp;

## Identity and Access Management

### Understanding Azure Entra ID

Azure Active Directory or now the Azure Entra ID (AEI) is a cloud-based identity and access management service that enables access resources. Example resources include Microsoft 365, the Azure portal, and thousands of other SaaS applications. The capabilties related to Entra ID are extensive, ranging from permission delegation to user and domain management, encompassing various business aplications aspects. However, in this practice, our primary focus will be on access control through RBAC (Role-Based Access Control), where we will provide a detailed explanation of RBAC. 

First we need to differentiate between authentication and authorization, these are fundamental concepts in the realm of security, each serving a distinct purpose in safeguarding information and resources, complementing the identity and the access management parts.

### Authentification and Authorization

- **Authentication:** Authentication is the initial step in the security process and it is closely related to Identity, designed to confirm the legitimacy of a user, system, or entity. Various methods are employed for authentication, including traditional approaches such as passwords, or the more robust multi-factor authentication systems. The aim is to establish a reliable mechanism to validate and confirm the identity of individuals or entities seeking access.
  
  E.g. When you sucessfully login in an account, such as an email. This is a successful authetification example.

- **Authorization:** Authorization comes into play once authentication has successfully verified the identity of a user or system. While authentication confirms who the user is, authorization dictates what that authenticated user is allowed to do within the system (Access Management). This entails defining access rights, permissions, and privileges based on the user's role or specific attributes. Access control policies, roles, and permissions are implemented to regulate and restrict user actions, ensuring that individuals or systems can only interact with specific resources or perform actions for which they have explicit permission.
  
  E.g. When you are trying to change some directive policies in the coporative email account and you cannot. This an example of how you are authentificated but not authorized.

### Policies, permissions and roles

With this 2 simple concepts IAM is defined, but lets dive a little bit more in the part of policies roles and permissions.

- **Policies:** Azure Entra ID policies are rules and settings that help control and govern the behavior of users and devices in your organization. These policies can include password policies, conditional access policies, and Identity Protection policies, among others. Policies play a crucial role in maintaining security and compliance within an Azure environment.

- **Permissions:** Permissions in Azure Entra ID define the actions that a user, group, or application can perform on a resource. These actions could include read, write, delete, or other specific operations depending on the resource type.

- **Roles:** Roles in Azure Entra ID define a set of permissions that can be assigned to users, groups, or applications. Roles help in efficiently managing access to resources by grouping related permissions together. 

There is a set of what the so called general use roles in Azure and is what we are going to play with in the following steps.

| Built-in role                                                                                                                                                       | Description                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **General**                                                                                                                                                         |                                                                                                                                                                     |
| [Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor)                                                         | Grants full access to manage all resources, but does not allow you to assign roles in Azure RBAC, manage assignments in Azure Blueprints, or share image galleries. |
| [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner)                                                                     | Grants full access to manage all resources, including the ability to assign roles in Azure RBAC.                                                                    |
| [Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#reader)                                                                   | View all resources, but does not allow you to make any changes.                                                                                                     |
| [Role Based Access Control Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator) | Manage access to Azure resources by assigning roles using Azure RBAC. This role does not allow you to manage access using other ways, such as Azure Policy.         |
| [User Access Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator)                             | Lets you manage user access to Azure resources.                                                                                                                     |
