<!-- repo image -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/Abubacer/README-Template/blob/master/images/banner.png" alt="IMG" 
  </a>

<h1 align="center"></h1>
<div align="left">
<br />

# 0x17. Web stack debugging #3

## Background Context

For this project, we are expected to look at these concepts:

- [Network basics](https://intranet.alxswe.com/concepts/33)
- [Web server](https://intranet.alxswe.com/concepts/17)
- [Web stack debugging](https://intranet.alxswe.com/concepts/68)

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… It actually powers 26% of the web, so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack you are debugging today is a Wordpress website running on a LAMP stack.

## Learning Objectives

At the end of this project, we are expected to be able to learn:

- How to use ```strace```
- How ```strace``` can attach to a current running process

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
