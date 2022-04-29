terraform {
  backend "s3" {
    bucket = "terraform-state-demo-temp"
    key    = "core/terraform.tfstate"
    region = "ap-south-1"
  }
}