Name:          qrtr
Version:       0.0.3
Release:       1
Summary:       Userspace reference for net/qrtr in the Linux kernel
URL:           https://github.com/andersson/qrtr
Source0:       %{name}-%{version}.tar.gz
License:       BSD-3-Clause
BuildRequires: kernel-headers

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
make %{?_smp_mflags}

%install
make prefix=/usr install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_libdir}/systemd/system/multi-user.target.wants
ln -s ../qrtr-ns.service %{buildroot}/%{_libdir}/systemd/system/multi-user.target.wants/qrtr-ns.service

%clean
make clean

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/libqrtr.so.*
%{_libdir}/systemd/system/multi-user.target.wants/qrtr-ns.service
%{_libdir}/systemd/system/qrtr-ns.service

%files devel
%defattr(644, root, root, -)
%{_libdir}/libqrtr.so
%{_includedir}/*.h
