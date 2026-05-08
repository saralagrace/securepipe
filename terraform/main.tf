# On configure Azure comme provider
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# On crée un groupe de ressources (le dossier qui contient tout)
resource "azurerm_resource_group" "securepipe" {
  name     = var.resource_group_name
  location = var.location
}

# On crée un registry Docker (ACR) pour stocker nos images
resource "azurerm_container_registry" "securepipe" {
  name                = "securepipeacr"
  resource_group_name = azurerm_resource_group.securepipe.name
  location            = azurerm_resource_group.securepipe.location
  sku                 = "Basic"
  admin_enabled       = true
}

# On crée le cluster Kubernetes (AKS)
resource "azurerm_kubernetes_cluster" "securepipe" {
  name                = "securepipe-aks"
  location            = azurerm_resource_group.securepipe.location
  resource_group_name = azurerm_resource_group.securepipe.name
  dns_prefix          = "securepipe"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_B2s"
  }

  identity {
    type = "SystemAssigned"
  }
}