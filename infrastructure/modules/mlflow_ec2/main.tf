resource "aws_instance" "mlflow_ec2" {
    ami = var.ami_id
    instance_type = var.instance_type
    vpc_security_group_ids = [ var.vpc_security_group_ids ]
    key_name = var.key_name
    iam_instance_profile = aws_iam_instance_profile.ec2_profile.name


    user_data = <<-EOF
    #!/bin/bash
    sudo yum -y update
    pip3 install boto3 mlflow
    echo 'export MODEL_BUCKET="${var.bucket_name}"' >> /home/ec2-user/.bashrc
    source /home/ec2-user/.bashrc
    mlflow server --backend-store-uri sqlite:///backend.db --default-artifact-root s3://$MODEL_BUCKET/mlflow/ -h 0.0.0.0 -p 5000
    EOF
}

output "ec2_arn" {
    value = aws_instance.mlflow_ec2.arn
}

output "ec2_public_dns" {
    value = aws_instance.mlflow_ec2.public_dns
}

output "ec2_public_ip" {
    value = aws_instance.mlflow_ec2.public_ip
}
