# Hands-on LAB: IAM and Blob Storage

## Study Case

What we are going to do in this practice is to cover the fundamentals about what we have learned. The summary of this practice is that we will test Azure RBAC by creating a user with only viewing permissions, while retaining ownership in our original account. We will compare the actions each user can perform and observe the outcomes when lacking sufficient permissions. Additionally, this part of the practice introduces the integration of Azure Storage Blobs with CloudShell. Although the details will be covered extensively in the following chapters, it's noteworthy that Azure Blobs is a system for storing unstructured data, providing a foundation for our current exploration.

###### Corporative file storage

A company needs to store unstructured data, such as photos, texts, executables, and more, in the cloud. Specifically, as this will be part of the backend solution, and access to these files will only occur through API requests for various workloads, the idea of using services like OneDrive, Google Drive, and others has been discarded because there is no need of a user interface and pricing is key. The company also aims to create a user who can occasionally access these files to verify some files, but simultaneously, this user should not have the ability to delete files due to compliance concerns.

How we can do this?

## Steps

1- First login into your Azure portal.

```
https://portal.azure.com/
```

2- We need to create a blob storage to save the clients data. As we learnt, resources should be in resources groups so we are going to create that first.

Search "Resource groups".

<img src="img\4%20(5).png" title="" alt="4 (5).png" width="590">

3- Inside of resource groups click on +Create

Select the subscription and call the resource group EU-resource-group, and the region in West Europe, here what we are doing is go give it a name and selecting the location of our resources metadata, not the resources themselves. 

The resource group stores metadata about the resources. Therefore, when you specify a location for the resource group, you are specifying where that metadata is stored. **For compliance reasons**, you may need to ensure that your data is stored in a particular region.

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

<img title="" src="img\4%20(29).png" alt="4 (29).png" width="317">

This is a perfect example of how an authenticated user lacks permissions to delete the file, showcasing how Azure RBAC (Role-Based Access Control) operates effectively.

17- In order to finish, close the private navigation and delete the container to avoid extra cost.

<img src="img\4%20(31).png" title="" alt="4 (31).png" width="642">
