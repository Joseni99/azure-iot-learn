# Identity and Access Management

### Understanding Azure Entra ID

Azure Active Directory or now the Azure Entra ID (AEI) is a cloud-based identity and access management service that enables access resources. Example resources include Microsoft 365, the Azure portal, and thousands of other SaaS applications. The capabilties related to Entra ID are extensive, ranging from permission delegation to user and domain management, encompassing various business aplications aspects. However, in this practice, our primary focus will be on access control through RBAC (Role-Based Access Control), where we will provide a detailed explanation of RBAC. 

First we need to differentiate between authentication and authorization, these are fundamental concepts in the realm of security, each serving a distinct purpose in safeguarding information and resources, complementing the identity and the access management parts.

### Authentification and Authorization

**Authentication:** Authentication is the initial step in the security process and it is closely related to Identity, designed to confirm the legitimacy of a user, system, or entity. Various methods are employed for authentication, including traditional approaches such as passwords, or the more robust multi-factor authentication systems. The aim is to establish a reliable mechanism to validate and confirm the identity of individuals or entities seeking access.

E.g. When you sucessfully login in an account, such as an email. This is a successful authetification example.

**Authorization:** Authorization comes into play once authentication has successfully verified the identity of a user or system. While authentication confirms who the user is, authorization dictates what that authenticated user is allowed to do within the system (Access Management). This entails defining access rights, permissions, and privileges based on the user's role or specific attributes. Access control policies, roles, and permissions are implemented to regulate and restrict user actions, ensuring that individuals or systems can only interact with specific resources or perform actions for which they have explicit permission.

E.g. When you are trying to change some directive policies in the coporative email account and you cannot. This an example of how you are authentificated but not authorized.

### Policies, permissions and roles

With this 2 simple concepts IAM is defined, but lets dive a little bit more in the part of policies roles and permissions.

**Policies:**

Azure Entra ID policies are rules and settings that help control and govern the behavior of users and devices in your organization. These policies can include password policies, conditional access policies, and Identity Protection policies, among others. Policies play a crucial role in maintaining security and compliance within an Azure environment.

**Permissions:**

Permissions in Azure Entra ID define the actions that a user, group, or application can perform on a resource. These actions could include read, write, delete, or other specific operations depending on the resource type.

**Roles:**

Roles in Azure Entra ID define a set of permissions that can be assigned to users, groups, or applications. Roles help in efficiently managing access to resources by grouping related permissions together. 

There is a set of what the so called general use roles in Azure and is what we are going to play with in the following steps.

| Built-in role                                                                                                                                                       | Description                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **General**                                                                                                                                                         |                                                                                                                                                                     |
| [Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor)                                                         | Grants full access to manage all resources, but does not allow you to assign roles in Azure RBAC, manage assignments in Azure Blueprints, or share image galleries. |
| [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner)                                                                     | Grants full access to manage all resources, including the ability to assign roles in Azure RBAC.                                                                    |
| [Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#reader)                                                                   | View all resources, but does not allow you to make any changes.                                                                                                     |
| [Role Based Access Control Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator) | Manage access to Azure resources by assigning roles using Azure RBAC. This role does not allow you to manage access using other ways, such as Azure Policy.         |
| [User Access Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator)                             | Lets you manage user access to Azure resources.                                                                                                                     |

### Hands on the practice!

What we are going to do in this practice is to cover the fundamentals about what we have learned. The summary of this practice is that we will test Azure RBAC by creating a user with only viewing permissions, while retaining ownership in our original account. We will compare the actions each user can perform and observe the outcomes when lacking sufficient permissions. Additionally, this part of the practice introduces the integration of Azure Storage Blobs with CloudShell. Although the details will be covered extensively in the following chapters, it's noteworthy that Azure Blobs is a system for storing unstructured data, providing a foundation for our current exploration.

###### Corporative file storage

A company needs to store unstructured data, such as photos, texts, executables, and more, in the cloud. Specifically, as this will be part of the backend solution, and access to these files will only occur through API requests for various workloads, the idea of using services like OneDrive, Google Drive, and others has been discarded because there is no need of a user interface and pricing is key. The company also aims to create a user who can occasionally access these files to verify some files, but simultaneously, this user should not have the ability to delete files due to compliance concerns.

How we can do this?

##### 

Hands on the lab!!!

1- First login into your Azure portal.

```
https://portal.azure.com/
```

2- We need to create a blob storage to save the clients data. As we learnt, resources should be in resources groups so we are going to create that first.

Search "Resource groups".

<img src="img\4%20(5).png" title="" alt="4 (5).png" width="590">

3- Inside of resource groups click on +Create

Select the subscription and call the resource group EU-resource-group, and the region in West Europe, here what we are doing is go give it a name and selecting the location of our resources.

<img src="img\4%20(6).png" title="" alt="4 (6).png" width="595">

4- Once the resource group is in place, let's proceed to establish a storage account. Remember to select the previously created resource group. Ensure the storage account name is distinct throughout entire Azure and make a note of it. Opt for standard performance and choose locally redundant storage to maintain cost-effectiveness.

<img src="img\4%20(15).png" title="" alt="4 (15).png" width="612">

5- Click on review and create and wait for the deployment.

<img src="img\4%20(17).png" title="" alt="4 (17).png" width="613">

6- Click on go to resource and open container tab.

<img src="img\4%20(18).png" title="" alt="4 (18).png" width="613">

7- Create a new container called "practice1" and click create.

<img src="img\4%20(19).png" title="" alt="4 (19).png" width="297">

8- Now head to Cloud Shell and type the next commands:

Download a test image in Cloud Shell to store it in our container.

```
wget -O kitty.png https://en.wikipedia.org/wiki/Hello_Kitty#/media/File:Hello_kitty_character_portrait.png
```

Configure the variables of our container. Please change the storage account to yours.

```
AZURE_STORAGE_ACCOUNT=yourstorageccountname
AZURE_CONTAINER_NAME=practice1
FILE_NAME=kitty.png
```

Upload the file using AZURE's API call.

```
az storage blob upload --file kitty.png --account-name $AZURE_STORAGE_ACCOUNT --container-name $AZURE_CONTAINER_NAME --name kitty.png
```

9- The result should be the file uploaded in our container.

You can download it to check it if you want.

<img src="img\4%20(20).png" title="" alt="4 (20).png" width="644">

10- Once finished the previous steps we are going to create a user that will have read-only permissions to access the resource group.

Search "Users" and click or you can go to Azure Entra ID and select the "Users" tab and click +New user.

<img src="img\4%20(1).png" title="" alt="4 (1).png" width="646">

10a- Call the user principal name user01, generate a password or set one youself, and write both down. We are going to use it later.

Click on Review + create -> Create

<img title="" src="img\4%20(2).png" alt="4 (2).png" width="642">

10b- Lets go back to reseource groups and this time we are going to select the resource group we have created and open the tab Access control (IAM) and click add role assignment.

<img src="img\4%20(8).png" title="" alt="4 (8).png" width="641">

11- Select Reader role.

<img title="" src="img\4%20(9).png" alt="4 (9).png" width="641">

12- In members tab add the user we created called user01.

<img title="" src="img\4%20(10).png" alt="4 (10).png" width="640">

13- Open a private tab and login with the user we have created

```
https://portal.azure.com/
```

13a- Change the password and skip the Action Required window.

<img title="" src="img\4%20(22).png" alt="4 (22).png" width="349">

14- Now it is time to try if we can reach or kitty.png, remember is in a container of a storage account

Spoiler, we cannot access the file due because we only can read and not list. 

<img src="img\4%20(24).png" title="" alt="4 (24).png" width="646">

15- To fix this issue let's add another role assginment to user01 from our main account (the one which is not in private navigation), in this case will be Storage Blob Data Reader.

<img src="img\4%20(26).png" title="" alt="4 (26).png" width="646">

16- Try again to access and this time also try to delete the image.

<img title="" src="img\4%20(28).png" alt="4 (28).png" width="645">

<img src="img\4%20(29).png" title="" alt="4 (29).png" width="435">

This is a perfect example of how an authenticated user lacks permissions to delete the file, showcasing how Azure RBAC (Role-Based Access Control) operates effectively.

17- In order to finish, close the private navigation and delete the container to avoid extra cost.

<img src="img\4%20(31).png" title="" alt="4 (31).png" width="642">
