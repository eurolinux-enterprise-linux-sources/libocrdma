Name: libocrdma
Version: 1.0.8
Release: 1%{?dist}
Summary: Userspace Library for Emulex OneConnect RDMA/RoCE Device
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: https://www.openfabrics.org/
Source: https://www.openfabrics.org/downloads/libocrdma/%{name}-%{version}.tar.gz
BuildRequires: libibverbs-devel
Requires: rdma
ExcludeArch: s390 s390x
Provides: libibverbs-driver.%{_arch}

%description
libocrdma provides a device-specific userspace driver for Emulex OneConnect
RDMA/RoCE Adapters for use with the libibverbs library.

%package static
Summary: Static version of the libocrdma driver
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description static
Static version of libocrdma that may be linked directly to an
application, which may be useful for debugging.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%files
%defattr(-,root,root,-)
%{_libdir}/libocrdma*.so
%license COPYING
%doc AUTHORS README
%config %{_sysconfdir}/libibverbs.d/ocrdma.driver

%files static
%defattr(-,root,root,-)
%{_libdir}/libocrdma*.a

%changelog
* Wed Apr 13 2016 Jarod Wilson <jarod@redhat.com> - 1.0.8-1
- Update to upstream release v1.0.8 for RoCE v2 support
- Restore AUTHORS, COPYING and README installation
- Resolves: bz1276743

* Fri Jan 23 2015 Doug Ledford <dledford@redhat.com> - 1.0.5-1
- Update to latest release (fix return error codes to match libibverbs spec)
- Resolves: bz1183636

* Tue Dec 23 2014 Doug Ledford <dledford@redhat.com> - 1.0.4-2
- Add requires on rdma package
- Related: bz1164618

* Mon Nov 10 2014 Doug Ledford <dledford@redhat.com> - 1.0.4-1
- Update to latest upstream release
- Related: bz1080183

* Thu Jul 24 2014 Doug Ledford <dledford@redhat.com> - 1.0.3-1
- Update to later upstream source
- Related: bz1080183

* Wed Jun 04 2014 Doug Ledford <dledford@redhat.com> - 1.0.2-2
- Bump and rebuild for pkgwrangler review
- Related: bz1080183

* Mon May 26 2014 Doug Ledford <dledford@redhat.com> - 1.0.2-1
- Initial import into rhel6
- Resolves: bz1080183
