Name: libocrdma
Version: 1.0.3
Release: 1%{?dist}
Summary: Userspace Library for Emulex ROCEE Device.
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: https://www.openfabrics.org/
Source: https://www.openfabrics.org/downloads/libocrdma/%{name}-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: libibverbs-devel
ExcludeArch: s390 s390x
Provides: libibverbs-driver.%{_arch}

%description
libocrdma provides a device-specific userspace driver for Emulex One
Command RoCE Adapters for use with the libibverbs library.

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
# %doc AUTHORS COPYING ChangeLog README
%config %{_sysconfdir}/libibverbs.d/ocrdma.driver

%files static
%defattr(-,root,root,-)
%{_libdir}/libocrdma*.a

%changelog
* Thu Jul 24 2014 Doug Ledford <dledford@redhat.com> - 1.0.3-1
- Update to later upstream source
- Related: bz1080183

* Wed Jun 04 2014 Doug Ledford <dledford@redhat.com> - 1.0.2-2
- Bump and rebuild for pkgwrangler review
- Related: bz1080183

* Mon May 30 2014 Doug Ledford <dledford@redhat.com> - 1.0.2-1
- Initial import into rhel6
- Resolves: bz1080183
