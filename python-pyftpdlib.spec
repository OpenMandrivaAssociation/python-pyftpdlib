%define upstream_name pyftpdlib

Name:		python-%{upstream_name}
Version:	1.5.5
Release:	1
Summary:	Python FTP server library
Group:		System/Libraries
License:	MIT
URL:		https://github.com/giampaolo/pyftpdlib
Source0:	https://github.com/giampaolo/pyftpdlib/archive/pyftpdlib-release-%{version}.tar.gz
BuildArch:	noarch

%description
Python FTP server library provides a high-level portable interface to easily
write asynchronous FTP servers with Python. pyftpdlib is currently the most
complete RFC-959 FTP server implementation available for Python programming
language.

%prep
%setup -q -n %{upstream_name}-release-%{version}

%build
%py_build

%install
%py_install

%files
%doc CREDITS HISTORY.rst LICENSE README.rst
%{python_sitelib}/%{upstream_name}
%{python_sitelib}/%{upstream_name}-%{version}-py%{python_version}.egg-info
%{_bindir}/ftpbench
