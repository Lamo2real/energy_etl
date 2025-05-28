

variable "data_lake_name" {
  description = "this value is set the CI/CD pipeline script for best practice and it is the name of the data lake hosted on Amazon S3"
  type = string
  sensitive = true
}