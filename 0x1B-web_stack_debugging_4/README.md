<!-- repo image -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/Abubacer/README-Template/blob/master/images/banner.png" alt="IMG" 
  </a>

<h1 align="center"></h1>
<div align="left">
<br />

# 0x1B-web_stack_debugging_4

## Background Context

For this project, we are expected to look at these concepts:

- [Network basics](https://intranet.alxswe.com/concepts/33)
- [Web server](https://intranet.alxswe.com/concepts/17)
- [Web stack debugging](https://intranet.alxswe.com/concepts/68)

In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let’s fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends! 

## Requirements

- All files will be interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Puppet manifests must run without error
- Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Puppet manifests files must end with the extension .pp
- Files will be checked with Puppet v3.4

## Installing puppet-lint

```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```
