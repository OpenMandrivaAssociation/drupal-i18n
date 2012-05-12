%define modname		i18n
%define drupal_version	7
%define module_version	1.5
%define version		%{drupal_version}.x.%{module_version}
%define tarname		%{modname}-%{drupal_version}.x-%{module_version}

Name:		drupal-%{modname}
Summary:	Internationalization module for Drupal
Version:	%{version}
Release:	1
License:	GPLv2+
Group:		Networking/WWW
URL:		https://drupal.org/project/%{modname}
Source0:	http://ftp.drupal.org/files/projects/%{tarname}.tar.gz
BuildArch:	noarch
Requires:	drupal >= %{drupal_version}
Requires:	drupal < %{lua: print(rpm.expand("%{drupal_version}")+1)}
Requires:	drupal-variable

%description
This is a collection of modules to extend Drupal core multilingual capabilities
and be able to build real life multilingual sites. Some features:

* Taxonomy translation (both, per language terms and translatable terms)
* Multilingual variables
* Multilingual blocks (control visibility per language and translate title
  and content)
* Language selection (when you switch the site language you'll see only
  the content for that language)

%prep
%setup -q -n %{modname}

%build

%install
%__install -d -m 0755 %{buildroot}%{_var}/www/drupal/modules/
cp -a . %{buildroot}%{_var}/www/drupal/modules/%{modname}
rm -f %{buildroot}%{_var}/www/drupal/modules/%{modname}/*.txt

%files
%{_var}/www/drupal/modules/%{modname}
%doc README.txt
