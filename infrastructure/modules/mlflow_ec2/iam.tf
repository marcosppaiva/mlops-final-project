resource "aws_iam_policy" "ec2_policy" {
  name = "ec2_policy"
  path = "/"
  policy = jsonencode({
    Version: "2012-10-17"
    Statement: [
      {
        Action: [
          "s3:*"
        ]
        Effect: "Allow"
        Resource: "*"
    },
  ]
})
}

resource "aws_iam_role" "ec2_s3_access_role" {
  name = "s3-role"
  assume_role_policy = jsonencode({
    Version: "2012-10-17"
    Statement: [
        {
        Action: "sts:AssumeRole",
        Principal: {
            Service: "ec2.amazonaws.com"
        }
        Effect: "Allow"
        Sid: ""
        },
    ]
    })

}

resource "aws_iam_policy_attachment" "ec2_role_policy_attachment" {
    name = "Policy Attachment"
    policy_arn = aws_iam_policy.ec2_policy.arn
    roles = [aws_iam_role.ec2_s3_access_role.name]
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "ec2_profile"
  role = aws_iam_role.ec2_s3_access_role.name
}
