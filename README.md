# RubyMine RPM

This RPM spec file enables to build binary RPM packages of the RubyMine IDE.

The RPM name consists of RubyMine-YYYY.X - So you can parallel install
for example RubyMine 2017.3 and 2018.1. 

The install dir is */opt/jetbrains/RubyMine/YYYY.x/*

A /usr/bin/RubyMine-YYYY.x shortcut is added to start. Maybe a nice desktop
file would be handy too.

A RubyMine-latest meta package could be created to always install
the latest when installing from a repo.


## Build the package


Prerequisites to build the package:


```
dnf install rpm-build rpmdevtools
mkdir SOURCES
spectool -s -C SOURCES rubymine.spec
```

Build the binary RPM:

```
rpmbuild --define "_topdir $(pwd)"  -bb rubymine.spec
```
