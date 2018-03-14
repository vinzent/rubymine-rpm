%define debug_package %{nil}
#%define __jar_repack %{nil}
%global __provides_exclude ^(lib\.so|libunpack\.so).*$
%global __requires_exclude ^(lib\.so|libunpack\.so).*$

%global product_name RubyMine
%global product_release 2017.3
%global product_patchlevel 3
%global product_installroot /opt/jetbrains/%{product_name}/%{product_release}
%global product_startscript %{product_installroot}/bin/rubymine.sh

Name:           %{product_name}-%{product_release}
Version:        %{product_release}.%{product_patchlevel}
Release:        1%{?dist}
Summary:        Jetbrains %{product_name} %{product_release}

License:        Proprietary
URL:            https://www.jetbrains.com
Source0:        https://download.jetbrains.com/ruby/%{product_name}-%{product_release}.%{product_patchlevel}.tar.gz

#BuildRequires:  
#Requires:       

%description
Jetbrains %{product_name} %{product_release}

%prep
%setup -n %{product_name}-%{product_release}.%{product_patchlevel} -q
echo "Prep (post): $(pwd)"

# only 64bit, no arm!
rm -f ./bin/fsnotifier ./bin/fsnotifier-arm


%build
echo "Build: $(pwd)"


%install
rm -rf $RPM_BUILD_ROOT
echo "Install: $(pwd)"

install -d --mode 0755 $RPM_BUILD_ROOT%{product_installroot}
install -d --mode 0755 $RPM_BUILD_ROOT%{_bindir}

cp -Ra ./ $RPM_BUILD_ROOT%{product_installroot}/
ln --symbolic --relative %{product_installroot}/bin/rubymine.sh $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%{product_installroot}
%{_bindir}/%{name}



%changelog
* Wed Mar 14 2018 Thomas Mueller <thomas@chaschperli.ch>
- 
