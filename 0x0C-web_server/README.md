<!-- repo image -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/Abubacer/README-Template/blob/master/images/banner.png" alt="IMG" 
  </a>

<h1 align="center"></h1>
<div align="left">
<br />

# 0x0C. Web server

## Background Context

For this project, we are expected to look at these concepts:

[Web server](https://www.youtube.com/watch?v=AZg4uJkEa-4)
[What is a Child Process?](https://intranet.alxswe.com/concepts/110)

In this project, some of the tasks will be graded on 2 aspects:

   - Is our web-01 server configured according to requirements
   - Does our answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if we need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, we can use emacs on our server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But our answer file would contain:

```
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
```

As we can tell, we are not using emacs to perform the task in our answer file. This exercise is aiming at training us on automating our work. If we can automate tasks that we do manually, we can then automate ourselves out of repetitive tasks and focus our energy on something more interesting. For an SRE, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute our script as the root user, we do not need to use the sudo command.

A good Software Engineer is a [lazy Software Engineer](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb).

Tips: to test the answer Bash script, feel free to reproduce the checker environment:

    - We start a Ubuntu 16.04 sandbox
    - We run our script on it
    - We see how it behaves

## Learning Objectives

At the end of this project, we are expected to be able to learn:

- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests
- What DNS stands for
- What is DNS main role
- What are the DNS Record Types ```A```, ```CNAME```, ```TXT```, ```MX```

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- All Bash script files must be executable
- The Bash script must pass ```Shellcheck``` (version 0.3.7) without any error
- The first line of all Bash scripts should be exactly ```#!/usr/bin/env bash```
- The second line of all Bash scripts should be a comment explaining what is the script doing
- The use of ```systemctl``` for restarting a process is not allowed
