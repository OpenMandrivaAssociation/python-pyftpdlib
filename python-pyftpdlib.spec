%define upstream_name pyftpdlib

Name:		python-%{upstream_name}
Version:	1.5.4
Release:	%mkrel 3
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

%package -n python3-%{upstream_name}
Summary:	Python FTP server library
BuildRequires:	python3

%description -n python3-%{upstream_name}
Python FTP server library provides a high-level portable interface to easily
write asynchronous FTP servers with Python. pyftpdlib is currently the most
complete RFC-959 FTP server implementation available for Python programming
language.

%prep
%setup -q -n %{upstream_name}-release-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{upstream_name}
%doc CREDITS HISTORY.rst LICENSE README.rst
%{python3_sitelib}/%{upstream_name}
%{python3_sitelib}/%{upstream_name}-%{version}-py%{python3_version}.egg-info
%{_bindir}/ftpbench
