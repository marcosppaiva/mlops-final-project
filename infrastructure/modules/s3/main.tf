resource "aws_s3_bucket" "s3_bucket" {
  bucket = var.bucket_name
  force_destroy = true
}

resource "aws_s3_object" "object_1" {
  bucket = aws_s3_bucket.s3_bucket.id
  key    = "data/processed/"
}

resource "aws_s3_object" "object_2" {
  bucket = aws_s3_bucket.s3_bucket.id
  key    = "data/raw/"
}


output "bucket" {
  value = aws_s3_bucket.s3_bucket.bucket
}
