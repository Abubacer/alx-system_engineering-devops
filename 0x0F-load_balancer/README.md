<!-- repo image -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/Abubacer/README-Template/blob/master/images/banner.png" alt="IMG" 
  </a>

<h1 align="center"></h1>
<div align="left">
<br />

# 0x0F. Load balancer

## Background Context

For this project, we are expected to look at these concepts:

- [Load balancer](https://intranet.alxswe.com/concepts/46)
- [Web stack debugging](https://intranet.alxswe.com/concepts/68)

In this project, we have been given 2 additional servers:

- gc-[STUDENT_ID]-web-02-XXXXXXXXXX
- gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

Let’s improve our web stack so that there is [redundancy](https://intranet.alxswe.com/rltoken/xnAaJdhmAxx7PoH3l6EwDg) for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, we will need to write Bash scripts to automate our work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Learning Objectives

At the end of this project, we are expected to be able to learn:

- What is the main role of a load-balancer and HAproxy
- What is a HTTP header
- What are the main Debian/Ubuntu HAProxy packages

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- All Bash script files must be executable
- The Bash script must pass ```Shellcheck``` (version 0.3.7) without any error
- The first line of all Bash scripts should be exactly ```#!/usr/bin/env bash```
- The second line of all Bash scripts should be a comment explaining what is the script doing
