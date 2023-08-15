terraform {
  required_version = ">= 1.0"
  # backend "s3" {
  #   bucket = "tf-state-final-project-mlops"
  #   key = "mlops-final.tfstate"
  #   region = "eu-west-3"
  #   encrypt = true
  # }
    backend "local" {}
}

provider "aws" {
    region = var.aws_region
}

data "aws_caller_identity" "current_identity" {}

locals {
  account_id = data.aws_caller_identity.current_identity
}

module "s3_bucket" {
  source = "./modules/s3"
  bucket_name = var.bucket_name
}

module "security_group_ec2_mlflow" {
  source = "./modules/security_group"

}

module "mlflow_instance" {
  source = "./modules/mlflow_ec2"
  ami_id = var.ami_id
  key_name = var.key_name
  instance_type = var.instance_type
  vpc_security_group_ids = module.security_group_ec2_mlflow.security_group_id
  bucket_name = var.bucket_name
}


output "public_ip_dns_ec2" {
  value = module.mlflow_instance.ec2_public_dns

}

output "public_ip_ec2" {
  value = module.mlflow_instance.ec2_public_ip

}
