resource "aws_s3_bucket" "s3_bucket" {
  bucket = var.bucket_name
}

resource "aws_s3_object" "object" {
  bucket = aws_s3_bucket.s3_bucket.id
  key    = "data/"
}

output "bucket" {
  value = aws_s3_bucket.s3_bucket.bucket
}
