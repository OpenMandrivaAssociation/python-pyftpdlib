%define module pyftpdlib
%bcond tests 1

Name:		python-pyftpdlib
Version:	2.2.0
Release:	1
Summary:	Python FTP server library
Group:		System/Libraries
License:	MIT
URL:		https://github.com/giampaolo/pyftpdlib
Source0:	%{URL}/archive/release-%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	help2man
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pyopenssl)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	tomcli
%if %{with tests}
BuildRequires:	python-test
BuildRequires:	python%{pyver}dist(psutil)
BuildRequires:	python%{pyver}dist(pyasyncore)
BuildRequires:	python%{pyver}dist(pyasynchat)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-xdist)
%endif
# For FTPS Support
Recommends:	python%{pyver}dist(pyopenssl)
# To keep track of FTP server memory usage
Recommends:	python%{pyver}dist(psutil)

%description
Python FTP server library provides a high-level portable interface to easily
write asynchronous FTP servers with Python. pyftpdlib is currently the most
complete RFC-959 FTP server implementation available for Python programming
language.

%prep -a
# We dont package pytest-instafail
tomcli set pyproject.toml lists delitem 'project.optional-dependencies.test' 'pytest-instafail\b.*'
# also remove it from pytest options, and reduce verbosity
sed -r -i 's/(--instafail|-p instafail|--verbose)//' pyproject.toml
# fix interpreter in tests
sed -i '1i #!%{__python}' tests/*.py

%install -a
# make mandir
mkdir -p %{buildroot}%{_mandir}/man1
# generate ftpbench manpage
help2man --no-info --version-string 'ftpbench %{version}' \
  -o %{buildroot}%{_mandir}/man1/ftpbench.1 \
  --no-discard-stderr %{buildroot}%{_bindir}/ftpbench

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}"
skiptests+="not test_mlst"
skiptests+=" and not test_nlst"
skiptests+=" and not test_stat"
# false positive timing/sync issue? AssertionError: 225 No transfer to abort.
skiptests+=" and not test_on_incomplete_file_received"
# required for test_use_gmt_times tests to pass.
export TZ=GMT+1
pytest --ignore build -k "$skiptests" -W ignore::DeprecationWarning
%endif

%files
%doc CREDITS HISTORY.rst README.rst
%{_bindir}/ftpbench
%{_mandir}/man1/ftpbench.1*
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
