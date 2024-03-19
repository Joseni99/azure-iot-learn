# Hands-on LAB: IoT Practice part 2

## Study Case

**Scenario:** A company aims to transmit IoT data, including temperature, humidity, and other sensor readings, through an IoT solution. The objective is to ensure reliable data transmission from IoT devices deployed in various locations to a centralized system for analysis and monitoring. Additionally, the company prioritizes data privacy and security, requiring the deployment of its IoT infrastructure on Microsoft Azure and use serverless services.

## Tasks:

1. **Setup Azure IoT Hub:**
   
   - Create an Azure IoT Hub instance in the Azure portal.
   - Configure IoT Hub with appropriate settings and security protocols.
   - Register IoT devices, such as Raspberry Pi, with IoT Hub and obtain connection credentials.

2. **Connect IoT Device to IoT Hub:**
   
   - Utilize Azure IoT SDK to enable IoT devices to communicate with IoT Hub.
   - Implement scripts on Raspberry Pi to collect sensor data and send it securely to IoT Hub.

3. **Setup Azure Database:** (DONE in Databases part)
   
   - Deploy an Azure Database service (SQL Database) to store processed IoT data.
   - Design the database schema to accommodate IoT data requirements.

4. **Implement Stream Analytics:**
   
   - Establish an Azure Stream Analytics job in the Azure portal.
   - Configure IoT Hub as the input source and choose the appropriate Azure Database as the output sink.
   - Develop Stream Analytics queries to process incoming sensor data in real-time and store it in the Azure database.

5. **Visualize Data with Grafana:**
   
   - Deploy Grafana within the Azure environment.
   - Connect Grafana to the Azure Database as a data source.
   - Design dashboards in Grafana to visualize IoT data trends, including temperature variations, humidity levels, and other sensor readings.

### 1. Setup Azure IoT Hub

1. Search for IoT Hub and click on create IoT Hub.

<p align="center">
<img src="../img/iohub%20(2).png" title="" alt="iohub (2).png" width="669">
</p>

2. Set the resource group, name and region freely just select the Tier as Free to avoid charges.

<p align="center">
<img title="" src="../img/iohub%20(3).png" alt="iohub (3).png" width="526">
</p>

3. Review and Create.

<p align="center">
<img title="" src="../img/iohub%20(4).png" alt="iohub (4).png" width="406">
</p>

4. Wait for the deployment to finish and go to the resource.

<p align="center">
<img src="../img/iohub%20(5).png" title="" alt="iohub (5).png" width="678">
</p>

5. Click on create a new device to add our Raspberry Pi.

<p align="center">
<img title="" src="../img/iohub%20(6).png" alt="iohub (6).png" width="524">
</p>

6. Give the device a name and the following configuration.

<p align="center">
<img title="" src="../img/iohub%20(7).png" alt="iohub (7).png" width="344">
</p>

7. Access the device and copy the Primary connection string.

<p align="center">
<img src="../img/iohub%20(8).png" title="" alt="iohub (8).png" width="675">
</p>

8. Open cloudshell and run the following commands to see if there is any messages reaching the IoT Hub. 
   
   Note: Use the correct hub name, your IoT Hub name.
   
   ```
   az extension add --name azure-iot
   az iot hub monitor-events --hub-name eu-iothub
   ```

<p align="center">
<img src="../img/iohub%20(9).png" title="" alt="iohub (9).png" width="524">
</p>

### 2. Connect IoT Devices to IoT Hub:

1. Now go to our Raspberry Pi and execute the following command in order to send an receive data from IoT Hub:
   
   Note: Replace the connection string by your connection string and do not forget the quotation marks and do not close it until you do not want more data from the raspberry, minize it.
   
   ```
   python azure-iot-learn/iothub.py --connection-string "HostName=eu-iothub.azure-devices.net;DeviceId=raspi;SharedAccessKey=cffO2I/5jEWbAAAA/ed29AAj+5AIoTLX5rpQ"=
   ```

2. Once we are seeing messages in our Cloud Shell, lets try to send messages to our Raspberry. This option is available as Message to Device in the same window where we got the connection string.

<p align="center">
<img src="../img/iohub%20(10).png" title="" alt="iohub (10).png" width="667">
</p>

```
{
  "msg": "Hello"
}
```

We should be seeing messages coming in the Cloud Shell and messages in the PiHat display. 

### 3. Implement Stream Analytics:

1. Lets move all the data that IoT Hub is receiving to the SQL database we have created in the Database lab.
   
   Click on Create a new Stream Analytics Job.

<p align="center">
<img src="../img/iohub%20(11).png" title="" alt="iohub (11).png" width="685">
</p>

2. Lets create our first ETL, apply the following configuration for the job.

<p align="center">
<img src="../img/iohub%20(12).png" title="" alt="iohub (12).png" width="479">
</p>

3. Wait for the deployment to complete and go to the resoruce.

<p align="center">
<img src="../img/iohub%20(13).png" title="" alt="iohub (13).png" width="478">
</p>

4. Go to the job Input and select Add input from IoT Hub.

<p align="center">
<img src="../img/iohub%20(14).png" title="" alt="iohub (14).png" width="476">
</p>

5. It should be getting automatically the parameters because we only have one IoT Hub, check it and click save.

<p align="center">
<img src="../img/iohub%20(15).png" title="" alt="iohub (14).png" width="200">
</p>

6. Now lets add an ouput and select SQL.

<p align="center">
<img title="" src="../img/iohub%20(16).png" alt="iohub (16).png" width="439">
</p>

7. Select the SQL database created and use SQL authentication with the credentials we have set up in the last practice.
   
   Click on Load existing tables.

<p align="center">
<img title="" src="../img/iohub%20(17).png" alt="iohub (17).png" width="218">
</p>

8. It will fail and prompt to Allow IP address, click on it to allow this resource to access our database.

<p align="center">
<img title="" src="../img/iohub%20(18).png" alt="iohub (18).png" width="303">
</p>

9. Create a new table and call it raspiiot and save the configuration.

<p align="center">
<img title="" src="../img/iohub%20(19).png" alt="iohub (19).png" width="211">
</p>

10. Lets test and check our ETL:
    
    - Click on Test Query and check everything is OK.
      
      ![iohub (20).png](../img/iohub%20(20).png)
    
    - Go to SQL Table Schema (preview) tab.
    
    - Log-in with the credentials. It will say the table is not created, click on create table.
      
      ![iohub (22).png](../img/iohub%20(22).png)
    
    - All the variables should be linked automatically like this:
      
      ![iohub (23).png](../img/iohub%20(23).png)

11. After all configurations, click on start job with the following options:
    
    Note: Remember to stop this service when you are not using it, it will generate consumption.

<p align="center">
<img src="../img/iohub%20(21).png" title="" alt="iohub (21).png" width="404">
</p>

12. Now use the Azure Data Studio or the Query tab from the Azure SQL website to check if the data is reaching the database.

<p align="center">
<img src="../img/iohub%20(24).png" title="" alt="iohub (24).png" width="710">
</p>

<p align="center">
<img src="../img/iohub%20(25).png" title="" alt="iohub (25).png" width="672">
</p>

### 5. Visualize Data with Grafana

1. Now the last part of our job, lets show some graphics about our data. For this we will create a Grafana Workspace.
   
   Grafana is an open source interactive data-visualization platform, developed by [Grafana Labs](https://www.grafana.com/), which allows users to see their data via charts and graphs that are unified into one dashboard (or multiple dashboards!) for easier interpretation and understanding.
   
   In this case again feel free to name it and deploy it wherever you want, but set the pricing plan to standard and the version in 9.

<p align="center">
<img src="../img/iohub%20(26).png" title="" alt="iohub (26).png" width="694">
</p>

2. Should be something like this:

<p align="center">
<img title="" src="../img/iohub%20(27).png" alt="iohub (27).png" width="344">
</p>

3. Wait for the deployment to finish and go to the resource.

<p align="center">
<img src="../img/iohub%20(28).png" title="" alt="iohub (28).png" width="671">
</p>

4. Search the endpoint and Log-in, should be something like this:
   
   ```
   https://Grafana2024-bqhsa4xxdtfrenax.wcde.grafana.azure.com
   ```

5. Inside de Grafana, set up a data source in Administration.
   
   Complete the MS SQL Connection tab with your own database endpoints and credentials and leave the other options as it is.

<p align="center">
<img title="" src="../img/iohub%20(30).png" alt="iohub (30).png" width="630">
</p>

6. Click on Save and test and check the connection with the database.

<p align="center">
<img title="" src="../img/iohub%20(31).png" alt="iohub (31).png" width="499">
</p>

7. Create a new panel as a time series, select the database and past the following query:
   
   ```
   SELECT
     humidity,
     temperature,
     EventProcessedUtcTime
   FROM
     dbo.raspiiot
   ```

![iohub (33).png](../img/iohub%20(33).png)

8. Click on apply and observe the graphs, again you can exhale some warm air to the Raspberry hat to modify the humidity and temperature values.

<p align="center">
<img src="../img/iohub%20(32).png" title="" alt="iohub (32).png" width="704">
</p>

9. Feel free to change any settings and view options.
