#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Touch
Version  : 0.11
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/File-Touch-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/File-Touch-0.11.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-touch-perl/libfile-touch-perl_0.11-1.debian.tar.xz
Summary  : 'update file access and modification times, optionally creating files if needed'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Touch-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution File-Touch,
version 0.11:
update file access and modification times, optionally creating files if needed

%package dev
Summary: dev components for the perl-File-Touch package.
Group: Development
Provides: perl-File-Touch-devel = %{version}-%{release}

%description dev
dev components for the perl-File-Touch package.


%package license
Summary: license components for the perl-File-Touch package.
Group: Default

%description license
license components for the perl-File-Touch package.


%prep
%setup -q -n File-Touch-0.11
cd ..
%setup -q -T -D -n File-Touch-0.11 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-Touch-0.11/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Touch
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-File-Touch/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-File-Touch/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/File/Touch.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Touch.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Touch/LICENSE
/usr/share/package-licenses/perl-File-Touch/deblicense_copyright
