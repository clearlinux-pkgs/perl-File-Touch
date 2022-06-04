#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Touch
Version  : 0.12
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/File-Touch-0.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/File-Touch-0.12.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-touch-perl/libfile-touch-perl_0.11-1.debian.tar.xz
Summary  : 'update file access and modification times, optionally creating files if needed'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Touch-license = %{version}-%{release}
Requires: perl-File-Touch-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution File-Touch,
version 0.12:
update file access and modification times, optionally creating files if needed

%package dev
Summary: dev components for the perl-File-Touch package.
Group: Development
Provides: perl-File-Touch-devel = %{version}-%{release}
Requires: perl-File-Touch = %{version}-%{release}

%description dev
dev components for the perl-File-Touch package.


%package license
Summary: license components for the perl-File-Touch package.
Group: Default

%description license
license components for the perl-File-Touch package.


%package perl
Summary: perl components for the perl-File-Touch package.
Group: Default
Requires: perl-File-Touch = %{version}-%{release}

%description perl
perl components for the perl-File-Touch package.


%prep
%setup -q -n File-Touch-0.12
cd %{_builddir}
tar xf %{_sourcedir}/libfile-touch-perl_0.11-1.debian.tar.xz
cd %{_builddir}/File-Touch-0.12
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-Touch-0.12/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Touch
cp %{_builddir}/File-Touch-0.12/LICENSE %{buildroot}/usr/share/package-licenses/perl-File-Touch/da4b651334951322707e858f051a633fc12de5ed
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-Touch/3baac3cbe3e5e9d4d8d6cc75b6c8aa6be5636151
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Touch.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Touch/3baac3cbe3e5e9d4d8d6cc75b6c8aa6be5636151
/usr/share/package-licenses/perl-File-Touch/da4b651334951322707e858f051a633fc12de5ed

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
