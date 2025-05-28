

variable "infra_region" {
  default = "eu-central-1"
  description = "this is the region the entire infrastructure is hosted"
  type = string
  sensitive = true
}



############################### STORAGE ###############################
variable "data_lake" {
  description = "this is the bucket where the data lake is hosted"
  type = string
  sensitive = true
}
#######################################################################

