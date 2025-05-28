

resource "aws_s3_bucket" "data_lake" {
  bucket = var.data_lake_name
}

resource "aws_s3_bucket_public_access_block" "data_lake_pab" {
    bucket = aws_s3_bucket.data_lake.id

    block_public_acls       = true
    block_public_policy     = true
    ignore_public_acls      = true
    restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data_lake_encryption" {
  bucket = aws_s3_bucket.data_lake.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}