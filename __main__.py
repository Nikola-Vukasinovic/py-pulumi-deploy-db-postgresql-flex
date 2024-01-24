"""An Azure RM Python Pulumi program"""

import pulumi
import pulumi_azure as azure

# Create an Azure Resource Group
example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")

# Create an Azure resource (Storage Account)
flexible_server = azure.postgresql.FlexibleServer("exampleFlexibleServer",
    resource_group_name=example_resource_group.name,
    location=example_resource_group.location,
    version="12",
    administrator_login="psqladmin",
    administrator_password="H@Sh1CoR3!",
    public_network_access_enabled = True, 
    zone="2",
    storage_mb=32768,
    sku_name="Standard_B1ms",
)

pulumi.export("flexible_server", flexible_server)
