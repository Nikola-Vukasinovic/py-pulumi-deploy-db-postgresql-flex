"""An Azure RM Python Pulumi program"""

import pulumi
import pulumi_azure as azure

# Create an Azure Resource Group
example_resource_group = azure.core.ResourceGroup("example-resource-group", location="West Europe")

# Create an Azure resource (Storage Account)
flexible_server = azure.postgresql.FlexibleServer("example-fs",
    resource_group_name=example_resource_group.name,
    location=example_resource_group.location,
    version="12",
    administrator_login="psqladmin",
    administrator_password="H@Sh1CoR3!",
    zone="2",
    storage_mb=32768,
    sku_name="B_Standard_B1ms",
)

pulumi.export("flexible_server", flexible_server)
