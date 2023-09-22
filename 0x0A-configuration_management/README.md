<!-- repo image -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/Abubacer/README-Template/blob/master/images/banner.png" alt="IMG" 
  </a>

<h1 align="center"></h1>
<div align="left">
<br />

# 0x0A. Configuration management

## Background Context

As a broader subject, configuration management (CM) refers to the process of systematically handling changes to a system in a way that it maintains integrity over time. Even though this process was not originated in the IT industry, the term is broadly used to refer to server configuration management.

### Benefits of Configuration Management for Servers

Although the use of configuration management typically requires more initial planning and effort than manual system administration, all but the simplest of server infrastructures will be improved by the benefits that it provides. To name a few:
- Quick Provisioning of New Servers

Whenever a new server needs to be deployed, a configuration management tool can automate most, if not all, of the provisioning process for you. Automation makes provisioning much quicker and more efficient because it allows tedious tasks to be performed faster and more accurately than any human could. Even with proper and thorough documentation, manually deploying a web server, for instance, could take hours compared to a few minutes with configuration management/automation.
Quick Recovery from Critical Events

With quick provisioning comes another benefit: quick recovery from critical events. When a server goes offline due to unknown circumstances, it might take several hours to properly audit the system and find out what really happened. In scenarios like this, deploying a replacement server is usually the safest way to get your services back online while a detailed inspection is done on the affected server. With configuration management and automation, this can be done in a quick and reliable way.

- No More Snowflake Servers

At first glance, manual system administration may seem to be an easy way to deploy and quickly fix servers, but it often comes with a price. With time, it may become extremely difficult to know exactly what is installed on a server and which changes were made, when the process is not automated. Manual hotfixes, configuration tweaks, and software updates can turn servers into unique snowflakes, hard to manage and even harder to replicate. By using a configuration management tool, the procedure necessary for bringing up a new server or updating an existing one will be all documented in the provisioning scripts.

### Version Control for the Server Environment

Once you have your server setup translated into a set of provisioning scripts, you will have the ability to apply to your server environment many of the tools and workflows you normally use for software source code.

Version control tools, such as Git, can be used to keep track of changes made to the provisioning and to maintain separate branches for legacy versions of the scripts. You can also use version control to implement a code review policy for the provisioning scripts, where any changes should be submitted as a pull request and approved by a project lead before being accepted. This practice will add extra consistency to your infrastructure setup.

- Replicated Environments

Configuration management makes it trivial to replicate environments with the exact same software and configurations. This enables you to effectively build a multistage ecosystem, with production, development, and testing servers. You can even use local virtual machines for development, built with the same provisioning scripts. This practice will minimize problems caused by environment discrepancies that frequently occur when applications are deployed to production or shared between co-workers with different machine setups (different operating system, software versions and/or configurations).

## Learning Objectives

At the end of this project, we are expected to be able to learn:

- What is Configuration Management
- What is Puppet
- What is Puppet manifests
- How to use Puppet’s Declarative Language: Modeling Instead of Scripting
- What is Puppet resource type
- How to use Puppet lint

## Requirements

- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- Puppet manifests must pass ```puppet-lint``` version 2.1.1 without any errors
- All puppet manifests must run without error
- All puppet manifests first line must be a comment explaining what the Puppet manifest is about
- All puppet manifests files must end with the extension ```.pp```

## Install puppet

On Ubuntu 20.04 VM, Puppet 5.5 is already preinstalled.

```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

## Install puppet-lint

```
gem install puppet-lint
```
