terraform {
  backend "s3" {
    bucket = "terraform-bucket-tb"
    key    = "Resources/lambda_event_based_triggering.tfstate"
    region = "us-east-1"
    # dynamodb_table = "terraform-state-locks"
  }
}
