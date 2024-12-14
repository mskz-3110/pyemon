# pyemon
Python auxiliary tools

## Concept
Make your python work easier

## What is possible
1. Initialization work required to create your own package
2. Installing the package
3. Testing the package
4. Building the package
5. Uploading the package

## Reason for development
- I want to easily create my own packages

## Versions

|Version|Summary|
|:--|:--|
|0.1.0|Release pyemon|

## Installation
### [pyemon](https://pypi.org/project/pyemon/)
`pip install pyemon`

## CLI
### package.init
Initialization work required to create your own package

`pyemon package.init`
```
[With value]
  -u|--user-name    {USERNAME}    # User name
  -e|--email        {EMAIL}       # Email
  -d|--description  {DESCRIPTION} # Description
  -p|--project-name               # Project name
```

### package.install
Installing the package

`pyemon package.install`
```
[No value]
  -p|--pip   # PIP
  -d|--dev   # Development
  -t|--test  # TestPYPI
```

### package.test
Testing the package

`pyemon package.test`

### package.build
Building the package

`pyemon package.build`

### package.upload
Uploading the package

`pyemon package.upload`
```
[No value]
  -p|--pypi  # PYPI
```
