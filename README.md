# py-pulumi-deploy-db-postgresql-flex

Deploy PostgreSQL in Azure DB - flexible server with Pulumi

## Prerequisites

Working with Python version 3.7 or later.

Pulumi >=3.0.0, <=4.0.0.

pulumi-azure-native >=2.0.0, <=3.0.0.

## Installation of Pulumi

Install Pulumi

```
pip install pulumi
```

New azure-python project

```
pulumi new azure-python
```

Last step just spin it up with

```
pulumi up
```

When done with the resource it can be deleted with

```
pulumi destroy
```

## Multiple stacks

Pulumi supports multiple stacks (dev, stage, prod etc.)

You can see stacks with

```
pulumi stack ls
```

For more information plese see [stacks](https://www.pulumi.com/docs/concepts/stack/)

## Pulumi Authentication

In order to enable Pulumi to interact with you're Azure subscription there are multiple options to register you're py-pulumi app with Azure.

For fast setup you can use **Azure CLI** but preffered way is to use authentication with **Service Principal.**

### **Azure CLI**

How to install Azure CLI please follow [link](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).

On you're terminal just use

```
az login
```

When logged in you need to configure pulumi to use azure cli with:

```
pulumi config set cloud:useAzureCli true
```

### Service Principal

There are multiple resources on this topic so you can follow this to find out more about Service Principal authentication of the apps [link](https://learn.microsoft.com/en-us/cli/azure/azure-cli-sp-tutorial-1?tabs=bash)

Create new application

1. In the left navigation pane, click on "Azure Active Directory."
2. Under "App registrations," click on "New registration."
3. Provide a name for your application, select the appropriate account type, and enter a redirect URI if required. Click "Register."
4. Note down the "Application (client) ID" and "Directory (tenant) ID" from the overview page. These will be needed for configuring Pulumi.

Add client secret

1. In the left navigation pane, click on "Certificates & Secrets."
2. Under "Client secrets," click on "New client secret." Enter a description, choose an expiry period, and click "Add."
3. Note down the value of the client secret immediately. This will be needed for configuring Pulumi.

Adjust permissions

1. In the left navigation pane, click on "API permissions."
2. Ensure that your application has the necessary permissions to manage Azure resources. If needed, click on "Add a permission" and grant the required permissions.

### Configure Pulumi with Azure Credentials

```
pulumi config set azure:clientId <Application (client) ID>
pulumi config set azure:clientSecret <Client Secret>
pulumi config set azure:tenantId <Directory (tenant) ID>
pulumi config set azure:subscriptionId <Your Azure Subscription ID>
```

On the end of the configuration confirm settings with

```
pulumi up
```

## **Pulumi Secrets**

Another great aspect of Pulumi is built-in secret manger. You can store and retrieve secrets with:

```
pulumi config set myApiKey <your-secret-api-key>
```

In you're program to retrieve the secret you can do:

```python
import pulumi

config = pulumi.Config()

# Access the secret
api_key = config.require_secret("myApiKey")

# Use the secret in your infrastructure definition
# (Replace this with the actual resource where the secret is needed)
my_resource = SomeResource(name="example", api_key=api_key)
```

## Set service resource info

There are couple parameters that can be changed using Pulumi config or default will be used:

```
location = config.get("location") or "West Europe"
res_group = config.get("resource_group") or "test_group"
vm_size = config.get("vm_size") or "Standard_D2_v2"
node_count = config.get("node_count") or 2
env = config.get("environment") or "Development"
```

To set each of the config params use:

```
pulumi config set location <location_name>
```

In case you wan't to use already existing resource group please advise [link](https://www.pulumi.com/ai/answers/vL7zWqGtZqQHwJBLd4MnUC/accessing-existing-azure-resource-group). It is recommended to use new resource group or use GET function to fetch already existing resource group.

## Results

On end of pulumi up command depending on the time but it can take up to 10 minutes the resources are ready to use.

Notice that on end of the pulumi create/deploy process there are **export** commands that will enable you to access information from resource creation.

This is important in order to setup you're **kubectl** config.

To see pulumi output use:

```
pulumi stack output <output-name>
```
