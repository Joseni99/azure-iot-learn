# Hands-on LAB: VNetworks and VMachines:

## Study Case

**Scenario:** A company is planning to deploy a website on Azure and wishes to ensure its availability from a different region. The objective is to deploy the web server  and use Azure networking features such as network peering and NSGs to establish connectivity and perform a ping test to verify the website's functionality, all using Azure Virtual Machines.

The idea is to deploy a default apache web server in an european region, and later a  VM that can realize a healthcheck in another region that could be US.

**Tasks:**

**PART 1:**

1. **Azure Resource Deployment:**
   
   - Set up the necessary networking components, including virtual networks and subnets.
   - Deploy an apache web server on Azure in a specified region.
   - Modify the NSGs so the port 80 can serve the website an ICMP protocol is allowed for the healthcheck in another region.

**PART 2:**

1. **Network Peering:**
   
   - Establish network peering between the regions to enable communication.

2. **Ping Test:**
   
   - From a virtual machine in one region, perform a ping test to the deployed web page in the other region.
   - Ensure that the web page responds appropriately to validate its availability.

## Part 1: VNetworks and VMachines

To establish a virtual machine (VM), it is essential to link it with a virtual network (VN). This connection is crucial as it facilitates both incoming and outgoing access to our system. Without this association, the analogy can be drawn to constructing a house without doors or windows – a non sense. Additionally, it is important that both the virtual machine and virtual network exist within the same region to enable seamless association.

1. Lets create our first virtual network for our webserver VM, select the EU-resource-group that we created previously or create a new resource group.
   
   Name your virtual network EU-virtual-network and select the region as Europe and Germany West Central

<p align="center">
<img src="../img/5%20(12).png" title="" alt="5 (12).png" width="632">
</p>

2. Go to the IP addresses, there is a default subnet created with a range of IPs, in this case is enough for us but in other cases you might have to first design your network architecture before trying to deploy de virtual network.

<p align="center">
<img src="../img/5%20(3).png" title="" alt="5 (3).png" width="635">
</p>

3. Click on Review + create verify and wait for the deployment to finish.

<p align="center">
<img src="../img/5%20(4).png" title="" alt="5 (4).png" width="638">
</p>

4. Open Cloud Shell, this time and lets create a Virtual Network through command line, this one will be the US region one.

```
az network vnet create \
  --resource-group EU-resource-group \
  --name US-virtual-network \
  --location centralus \
  --address-prefix 10.1.0.0/16 \
  --subnet-name default \
  --subnet-prefix 10.1.0.0/24
```

    Some explanation here, we modified the subnets IPs because later we are going to peer this two networks so there cannot be overlapping IPs interfering with each other, if we forget this step, later Azure will not let us peer the networks.

    The successful execution shall deliver a response like this:

<p align="center">
<img src="../img/5%20(5).png" title="" alt="5 (5).png" width="639">
</p>

5. Lets deploy our first VM, find in Azure VM an click on Create a virtual machine hosted by Azure.

<p align="center">
<img src="../img/5%20(6).png" alt="5 (6).png" width="640">
</p>

6. Establish the basic configuration of the machine:
   
   - Resource group: The created previously
   
   - Name: eu-vm1.
   
   - Region: Europe Germany West Central.
   
   - Availability Zone: You can choose any of the 3 zones, sometimes the instance is not available in the availability zone due to resources limitation in the education suscription, choose the zone freely.
   
   - Image: We are going to work on Ubuntu, so choose Ubuntu 20.04.

<p align="center">
<img src="../img/5%20(13).png" title="" alt="5 (13).png" width="641">
</p>

- Size: Standard B1s, 1 vcpu and 1GiB, we do not need powerful machines in this practice, this size will be more than enought.

- SSH: Generate a new key pair and save it.

- Others: Keep it default.
  
  <p align="center">
  <img src="../img/5%20(14).png" title="" alt="5 (14).png" width="641">
  </p>
7. Lets establish the disks configuration of our machine:
   
   - Disk Type: Select a standard SSD tier in order to reduce costs .
   
   - Delete with VM: This option will delete the disk when we remove the VM in order to avoid unwanted costs.
     
     <p align="center">
     <img src="../img/5%20(16).png" alt="5 (16).png" width="637">
     </p>

8. Last step, the network configuration:
- Virtual network: Select the EU-virtual-network that we create before

- Subnet: Default

- Delete public IP: This option will delete the public IP when we remove the VM in order to avoid unwanted costs.
  
  <p align="center">
  <img src="../img/5%20(15).png" title="" alt="5 (15).png" width="638">
  </p>
9. Click on Review+Create, and wait for the validation.
   
   <p align="center">
   <img src="../img/5%20(17).png" title="" alt="5 (17).png" width="640">
   </p>

10. Wait for the the deployment to complete and after that go the resource.
    
    <p align="center">
    <img src="../img/5%20(19).png" title="" alt="5 (19).png" width="642">
    </p>

11. Click on Connect in order to SSH our VM.
    
    <p align="center">
    <img src="../img/5%20(20).png" title="" alt="5 (20).png" width="642">
    </p>

12. Select SSH using Azure CLI and complete the prompt with Configure+connect.
    
    <p align="center">
    <img title="" src="../img/5%20(21).png" alt="5 (21).png" width="315">
    </p>

<p align="center">
<img title="" src="../img/5%20(22).png" alt="5 (22).png" width="480">
</p>

13. Now let's intall the apache web server in the Ubuntu server:

Update the repositories so we can download packages

```
sudo apt update
```

Install the apache webserver

```
sudo apt install apache2 -y
```

Check if apache is running

```
sudo systemctl status apache2
```

If everything is correct we should be seen something like this:
```
● apache2.service - The Apache HTTP Server
     Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2020-04-23 22:36:30 UTC; 20h ago
       Docs: https://httpd.apache.org/docs/2.4/
   Main PID: 29435 (apache2)
      Tasks: 55 (limit: 1137)
     Memory: 8.0M
     CGroup: /system.slice/apache2.service
             ├─29435 /usr/sbin/apache2 -k start
             ├─29437 /usr/sbin/apache2 -k start
             └─29438 /usr/sbin/apache2 -k start

```

Ctrl+C to exit

14. Now go back to the VM and get its public IP address an try to connect via browser.
    
    <p align="center">
    <img src="../img/5%20(23).png" title="" alt="5 (23).png" width="619">
    </p>

15. Ooops, seems somthing is not working:
    
    <p align="center">
    <img src="../img/5%20(24).png" title="" alt="5 (24).png" width="590">
    </p>

16. This is completely normal, rembember that we only opened port 22 in the configuration of the machine so there is no way our web server is going to serve the webpage via port 80.
    
    Let's go to the VM networking tab, here we click "Add a new inbound security role"
    
    <p align="center">
    <img title="" src="../img/5%20(25).png" alt="5 (25).png" width="619">
    </p>

17. Open the port 80 to any IP in order to server the content to any client.
    
    <p align="center">
    <img title="" src="../img/5%20(26).png" alt="5 (26).png" width="351">
    </p>

18. Ta-da!!! Our Apache web server is working and serving a default webpage.
    
    <p align="center">
    <img src="../img/5%20(27).png" title="" alt="5 (27).png" width="632">
    </p>

## Part 2: Network peering and health-check

We have finished the first part, we have deployed our own webpage but now what we have to do is to deploy another VM in another region in order to check if our machine is working.

1. Before deploying another machine, lets interconnect both virtual networks using peering functions in virtual networks tab.
   
   <p align="center">
   <img title="" src="../img/5%20(30).png" alt="5 (30).png" width="658">
   </p>

2. Apply the following configuration:
   
   <p align="center">
   <img title="" src="../img/5%20(31).png" alt="5 (31).png" width="533">
   </p>

3. Repeat the previous steps (6-10) to create another VM but this time in US, same size, same disks, change the name to us-vm1, and of course the virtual network shall be the US one.

4. Once the machine is deployed go to both machines and edit NSGs in the networking tab, this time allow the ICMP protocol, this will be the healthcheck of our service
   
   <p align="center">
   <img src="../img/5%20(32).png" title="" alt="5 (32).png" width="644">
   </p>

5. SSH into the US machine and try to ping the EU one, you can do it in both ways, with the internal private IPs or the external public IPs. Remember you can get this data from the networking tab of each machine.
   
   <p align="center">
   <img src="../img/5%20(33).png" title="" alt="5 (33).png" width="474">
   </p>

6. If you executed everything correctly you will see something like this, and around 110ms between US and EU regions.

<p align="center">
<img src="../img/5%20(34).png" title="" alt="5 (34).png" width="425">
</p>

7. This is the farewell of this practice, remember to delete both machines when you finish to avoid extra charge.

<p align="center">
<img title="" src="../img/5%20(36).png" alt="5 (36).png" width="691">
</p>
