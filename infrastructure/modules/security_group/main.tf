# create security group for the ec2 instance
resource "aws_security_group" "ec2_security_group" {
  name        = "mlflow_ec2 security group"
  description = "allow access on ports 5000 and 22"

  ingress {
    description      = "http access"
    from_port        = 5000
    to_port          = 5000
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  ingress {
    description      = "ssh access"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = -1
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags   = {
    Name = "mlflow_ec2 security group"
  }
}

output "security_group_id" {
    value = aws_security_group.ec2_security_group.id
}
