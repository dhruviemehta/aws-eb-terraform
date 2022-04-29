resource "aws_elastic_beanstalk_application" "application" {
  name        = "flask-weather-app"
}
resource "aws_elastic_beanstalk_environment" "environment" {
  name                = "flask-weather-app-environment"
  application         = aws_elastic_beanstalk_application.application.name
  solution_stack_name = "64bit Amazon Linux 2 v3.3.13 running Python 3.8"
  setting {
        namespace = "aws:autoscaling:launchconfiguration"
        name      = "IamInstanceProfile"
        value     = "aws-elasticbeanstalk-ec2-role"
      }
}