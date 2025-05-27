

terraform {
    backend "s3" {}
    required_version = "=1.11.1"
    required_providers {
      aws = {
        source = "hashicorp/aws"
        version = "= 5.85.0"
      }
    }
}

provider "aws" {
  region = var.infra_region
}

