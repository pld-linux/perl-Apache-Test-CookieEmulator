#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	Test-CookieEmulator
Summary:	Test::Apache::CookieEmulator - test tool for Cookies without httpd
#Summary(pl):	
Name:		perl-Apache-Test-CookieEmulator
Version:	0.04
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module assists authors of Apache::* modules write test suites that
would use B<Apache::Cookie> without actually having to run and query a
server to test the cookie methods. Loaded in the test script after the
author's target module is loaded, B<Test::Apache::CookieEmulator>

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_sitelib}/Apache/Test/*.pm
%{_mandir}/man3/*
