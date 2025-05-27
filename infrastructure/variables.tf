

variable "infra_region" {
  default = "eu-central-1"
  description = "this is the region the entire infrastructure is hosted"
  type = string
  sensitive = true
}