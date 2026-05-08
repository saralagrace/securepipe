output "resource_group_name" {
  value = azurerm_resource_group.securepipe.name
}

output "aks_cluster_name" {
  value = azurerm_kubernetes_cluster.securepipe.name
}

output "acr_login_server" {
  value = azurerm_container_registry.securepipe.login_server
}