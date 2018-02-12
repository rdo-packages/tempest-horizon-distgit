%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
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
Version:    XXX
Release:    XXX
Summary:    Tempest Integration of Horizon
License:    ASL 2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:    https://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

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

Requires:   python2-pbr >= 2.0.0
Requires:   python2-babel >= 2.3.4
Requires:   python2-oslo-config >= 2:4.0.0
Requires:   python2-oslo-log >= 3.22.0
Requires:   python2-six >= 1.9.0
Requires:   python2-tempest >= 1:17.2.0

%description -n python2-%{service}-tests-tempest
%{common_desc}

%if 0%{?with_python3}
%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:   python3-pbr >= 2.0.0
Requires:   python3-babel >= 2.3.4
Requires:   python3-oslo-config >= 2:4.0.0
Requires:   python3-oslo-log >= 3.22.0
Requires:   python3-six >= 1.9.0
Requires:   python3-tempest >= 1:17.2.0

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
