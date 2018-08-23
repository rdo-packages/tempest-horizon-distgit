%{!?upstream_version: %global upstream_version %{commit}}
%global commit 6490739059135e05b7fee75ee083701b4c8aa097
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%global service horizon
%global plugin tempest-horizon
%global module tempest_horizon

%if 0%{?fedora}
%global with_python3 1
%endif

%global common_desc \
This package contains Tempest tests to cover the Horizon project. \
Additionally it provides a plugin to automatically load these tests \
into tempest.

Name:       python-%{service}-tests-tempest
Version:    0.0.1
Release:    0.3%{?alphatag}%{?dist}
Summary:    Tempest Integration of Horizon
License:    ASL 2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:    http://github.com/openstack/%{plugin}/archive/%{commit}.tar.gz#/%{plugin}-%{shortcommit}.tar.gz

BuildArch:  noarch
BuildRequires:  git
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python2-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python2-%{service}-tests-tempest}
BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools

Requires:   python2-pbr >= 3.1.1
Requires:   python2-babel >= 2.3.4
Requires:   python2-oslo-config >= 2:5.2.0
Requires:   python2-oslo-log >= 3.36.0
Requires:   python2-six >= 1.10.0
Requires:   python2-tempest >= 1:18.0.0

%description -n python2-%{service}-tests-tempest
%{common_desc}

%if 0%{?with_python3}
%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:   python3-pbr >= 3.1.1
Requires:   python3-babel >= 2.3.4
Requires:   python3-oslo-config >= 2:5.2.0
Requires:   python3-oslo-log >= 3.36.0
Requires:   python3-six >= 1.10.0
Requires:   python3-tempest >= 1:18.0.0

%description -n python3-%{service}-tests-tempest
%{common_desc}
%endif

%prep
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

%files -n python2-%{service}-tests-tempest
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{module}
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{service}-tests-tempest
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/*.egg-info
%endif

%changelog
* Thu Aug 23 2018 Chandan Kumar <chkumar@redhat.com> 0.0.1-0.3.64907390git
- Update to pre-release 0.0.1 (6490739059135e05b7fee75ee083701b4c8aa097)
