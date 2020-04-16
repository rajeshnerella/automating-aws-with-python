# Automating AWS with Python

Repository for the A Cloud Guru course *Automating AWS with python*

## 01-webotron

Webotron is a script that will sync a local directory toan s3 bucket, and optionally configure Route 53 and cloudfront as well.

### Features

webotron currently has the following options:

- List buckets
- list contents of a bucket
- Create and setup bucket
- Sync directory tree to bucket
- Set AWS profile with --profile=<profileName>
- Configure route 53 domain