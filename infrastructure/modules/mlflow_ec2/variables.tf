variable "instance_type" {
    description = "EC2 Instance size/type"
}

variable "ami_id" {
    description = "AMI ID"
}

variable "key_name" {
    description = "SSH Key pair to use that already exists in AWS"
}

variable "bucket_name" {
    description = "model bucket"
}

variable "vpc_security_group_ids" {
    description = "vpc security group id"
}
