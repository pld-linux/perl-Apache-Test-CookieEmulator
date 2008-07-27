#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Test-CookieEmulator
Summary:	Test::Apache::CookieEmulator - test tool for cookies without httpd
Summary(pl.UTF-8):	Test::Apache::CookieEmulator - narzędzie testowe do ciasteczek bez httpd
Name:		perl-Apache-Test-CookieEmulator
Version:	0.05
Release:	4
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d78fe181f0874d0bc55cc50607a39f03
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module assists authors of Apache::* modules write test suites
that would use Apache::Cookie without actually having to run and query
a server to test the cookie methods.

%description -l pl.UTF-8
Ten moduł pomaga autorom modułów Apache::* pisać własne zestawy testów
używające Apache::Cookie bez potrzeby posiadania uruchomionego serwera
i odpytywania go, aby przetestować działanie ciasteczek.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%dir %{perl_vendorlib}/Apache/Test
%{perl_vendorlib}/Apache/Test/*.pm
%{_mandir}/man3/*
