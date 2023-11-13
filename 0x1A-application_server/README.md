<!-- repo image -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/Abubacer/README-Template/blob/master/images/banner.png" alt="IMG" 
  </a>

<h1 align="center"></h1>
<div align="left">
<br />

# 0x1A. Application server

## Background Context

For this project, we are expected to look at these concepts:

- [Web server](https://www.youtube.com/watch?v=AZg4uJkEa-4)
- [Server](https://intranet.alxswe.com/concepts/67)
- [Web stack debugging](https://intranet.alxswe.com/concepts/68)

![alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231113%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231113T142747Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3df83534a4a2d3d1966c7799ee68f13d696bcf851e7ada69a8201f2f03d2f138)

Our web infrastructure is already serving web pages via Nginx that we installed in our first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server.

In this project we will add this piece to our infrastructure, plug it to our Nginx and make is serve our Airbnb clone project.

## Requirements

- A ```README.md``` file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using ```python3```
- All config files must have comments
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- All Bash script files must be executable
- The Bash script must pass ```Shellcheck``` (version 0.3.75~ubuntu16.04.1 via apt-get) without any error
- The first line of all Bash scripts should be exactly ```#!/usr/bin/env bash```
- The second line of all Bash scripts should be a comment explaining what it the script doing
