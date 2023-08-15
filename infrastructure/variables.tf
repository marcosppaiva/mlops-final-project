variable "aws_region" {
  description = "AWS regio to create resources"
  default = "eu-west-3"
}

variable "project_id" {
  description = "project_id"
  default = "mlops_final"
}

variable "bucket_name" {
  description = "s3_bucket"
}

variable "ami_id" {
  description = "General service AMI ID"
}

variable "key_name" {
  description = "SSH Key pair to use that already exists in AWS"
}

variable "instance_type" {
    description = "EC2 Instance size/type"
}
