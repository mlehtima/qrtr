Name:          qrtr
Version:       1.0
Release:       1
Summary:       Userspace reference for net/qrtr in the Linux kernel
URL:           https://github.com/andersson/qrtr
Source0:       %{name}-%{version}.tar.gz
License:       BSD-3-Clause
BuildRequires: kernel-headers
BuildRequires: systemd

%description
Userspace reference for net/qrtr in the Linux kernel

%package devel
Summary:       Devel package for %{name}
License:       BSD-3-Clause
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
Userspace reference for net/qrtr in the Linux kernel
This package contains static libraries and header files need for development.

%prep
%autosetup -p1 -n %{name}-%{version}/qrtr

%build
%make_build

%install
make prefix=%{_prefix} libdir=%{_libdir} install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_unitdir}/multi-user.target.wants
ln -s ../qrtr-ns.service %{buildroot}/%{_unitdir}/multi-user.target.wants/qrtr-ns.service

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE
%{_bindir}/*
%{_libdir}/libqrtr.so.*
%{_unitdir}/multi-user.target.wants/qrtr-ns.service
%{_unitdir}/qrtr-ns.service

%files devel
%defattr(644, root, root, -)
%{_libdir}/libqrtr.so
%{_includedir}/*.h
